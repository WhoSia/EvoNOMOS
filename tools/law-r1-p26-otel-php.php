<?php
declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

use Mockery;
use OpenTelemetry\API\Trace\SpanContext;
use OpenTelemetry\API\Trace\SpanContextValidator;
use OpenTelemetry\API\Trace\TraceFlags;
use OpenTelemetry\SDK\Common\Future\CancellationInterface;
use OpenTelemetry\SDK\Common\Future\CompletedFuture;
use OpenTelemetry\SDK\Common\Future\FutureInterface;
use OpenTelemetry\SDK\Trace\ReadableSpanInterface;
use OpenTelemetry\SDK\Trace\SpanDataInterface;
use OpenTelemetry\SDK\Trace\SpanExporterInterface;
use OpenTelemetry\SDK\Trace\SpanProcessor\SimpleSpanProcessor;

final class P26Exporter implements SpanExporterInterface
{
    public int $exports = 0;
    public bool $shutdownState = false;

    public function export(iterable $batch, ?CancellationInterface $cancellation = null): FutureInterface
    {
        foreach ($batch as $_) {
            $this->exports++;
        }
        return new CompletedFuture(true);
    }

    public function shutdown(?CancellationInterface $cancellation = null): bool
    {
        $this->shutdownState = true;
        return true;
    }

    public function forceFlush(?CancellationInterface $cancellation = null): bool
    {
        return true;
    }
}

function makeSpan(bool $sampled): array
{
    $ctx = $sampled
        ? SpanContext::create(
            SpanContextValidator::INVALID_TRACE,
            SpanContextValidator::INVALID_SPAN,
            TraceFlags::SAMPLED
        )
        : SpanContext::getInvalid();

    $span = Mockery::mock(ReadableSpanInterface::class);
    $span->shouldReceive('getContext')->zeroOrMoreTimes()->andReturn($ctx);
    $span->shouldReceive('toSpanData')->zeroOrMoreTimes()->andReturn(Mockery::mock(SpanDataInterface::class));
    return [$span, $ctx];
}

function gate(P26Exporter $exp): int
{
    return $exp->shutdownState ? 0 : 1;
}

function runGroup(int $g): array
{
    $exp = new P26Exporter();
    $p = new SimpleSpanProcessor($exp);
    if ($g === 0) {
        $p->shutdown();
    }

    $sequence = [
        ['baseline', true],
        ['drop', false],
        ['restore', true],
    ];
    $rows = [];
    foreach ($sequence as [$name, $sampled]) {
        [$span, $ctx] = makeSpan($sampled);
        $q = $ctx->isSampled() ? 1 : 0;
        $beforeGate = gate($exp);
        $beforeExports = $exp->exports;
        $p->onEnd($span);
        $y = $exp->exports > $beforeExports ? 1 : 0;
        $afterGate = gate($exp);
        $rows[] = [
            'mechanism' => 'OTEL_PHP_SIMPLE_SPAN_PROCESSOR',
            'intervention' => $name,
            'q' => $q,
            'g' => $g,
            'y' => $y,
            'gate_before' => $beforeGate,
            'gate_after' => $afterGate,
        ];
    }
    if ($g === 1) {
        $p->shutdown();
    }
    return $rows;
}

$rows = array_merge(runGroup(0), runGroup(1));
$want = [
    'baseline/0' => 0,
    'baseline/1' => 1,
    'drop/0' => 0,
    'drop/1' => 0,
    'restore/0' => 0,
    'restore/1' => 1,
];
$pass = true;
foreach ($rows as $r) {
    $key = $r['intervention'] . '/' . $r['g'];
    if ($want[$key] !== $r['y'] || $r['gate_before'] !== $r['g'] || $r['gate_after'] !== $r['g']) {
        $pass = false;
    }
    if ($r['intervention'] === 'drop' && $r['q'] !== 0) {
        $pass = false;
    }
    if (($r['intervention'] === 'baseline' || $r['intervention'] === 'restore') && $r['q'] !== 1) {
        $pass = false;
    }
}

$out = [
    'stage' => 'EvoNOMOS Generation VIII LAW-R1-P26',
    'mechanism' => 'OTEL_PHP_SIMPLE_SPAN_PROCESSOR',
    'status' => $pass ? 'PASS' : 'FAIL',
    'rows' => $rows,
];

$path = getenv('P26_OUT_PHP') ?: 'p26-otel-php.json';
file_put_contents($path, json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . PHP_EOL);
Mockery::close();

fwrite(STDOUT, 'P26_PHP=' . ($pass ? 'PASS' : 'FAIL') . PHP_EOL);
if (!$pass) {
    exit(2);
}
