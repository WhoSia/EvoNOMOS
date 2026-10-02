package trace_test

import (
	"context"
	"encoding/json"
	"os"
	"testing"

	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	"go.opentelemetry.io/otel/sdk/trace/tracetest"
	oteltrace "go.opentelemetry.io/otel/trace"
)

type countExporter struct {
	exports  int
	shutdown bool
}

func (e *countExporter) ExportSpans(_ context.Context, spans []sdktrace.ReadOnlySpan) error {
	e.exports += len(spans)
	return nil
}

func (e *countExporter) Shutdown(context.Context) error {
	e.shutdown = true
	return nil
}

func makeSpan(sampled bool) sdktrace.ReadOnlySpan {
	var tid oteltrace.TraceID
	var sid oteltrace.SpanID
	tid[15] = 1
	sid[7] = 1
	flags := oteltrace.TraceFlags(0).WithSampled(sampled)
	sc := oteltrace.NewSpanContext(oteltrace.SpanContextConfig{
		TraceID: tid,
		SpanID: sid,
		TraceFlags: flags,
	})
	return tracetest.SpanStub{Name: "p26", SpanContext: sc}.Snapshot()
}

func gate(exp *countExporter) int {
	if exp.shutdown {
		return 0
	}
	return 1
}

func runGroup(t *testing.T, g int) []map[string]any {
	t.Helper()
	ctx := context.Background()
	exp := &countExporter{}
	p := sdktrace.NewSimpleSpanProcessor(exp)
	if g == 0 {
		if err := p.Shutdown(ctx); err != nil {
			t.Fatal(err)
		}
	}

	sequence := []struct{
		name string
		sampled bool
	}{
		{"baseline", true},
		{"drop", false},
		{"restore", true},
	}

	rows := make([]map[string]any,0,len(sequence))
	for _, step := range sequence {
		s := makeSpan(step.sampled)
		q := 0
		if s.SpanContext().IsSampled() {
			q = 1
		}
		beforeGate := gate(exp)
		beforeExports := exp.exports
		p.OnEnd(s)
		y := 0
		if exp.exports > beforeExports {
			y = 1
		}
		afterGate := gate(exp)
		rows = append(rows,map[string]any{
			"mechanism":"OTEL_GO_SIMPLE_SPAN_PROCESSOR",
			"intervention":step.name,
			"q":q,
			"g":g,
			"y":y,
			"gate_before":beforeGate,
			"gate_after":afterGate,
		})
	}

	if g == 1 {
		if err := p.Shutdown(ctx); err != nil {
			t.Fatal(err)
		}
	}
	return rows
}

func TestP26Naturality(t *testing.T) {
	rows := append(runGroup(t,0), runGroup(t,1)...)
	want := map[string]int{
		"baseline/0":0,
		"baseline/1":1,
		"drop/0":0,
		"drop/1":0,
		"restore/0":0,
		"restore/1":1,
	}
	pass := true
	for _, r := range rows {
		name := r["intervention"].(string)
		g := r["g"].(int)
		q := r["q"].(int)
		y := r["y"].(int)
		key := name + "/" + string(rune('0'+g))
		if want[key] != y || r["gate_before"].(int) != g || r["gate_after"].(int) != g {
			pass = false
		}
		if name == "drop" && q != 0 {
			pass = false
		}
		if (name == "baseline" || name == "restore") && q != 1 {
			pass = false
		}
	}
	payload := map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P26",
		"mechanism":"OTEL_GO_SIMPLE_SPAN_PROCESSOR",
		"status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
		"rows":rows,
	}
	path := os.Getenv("P26_OUT_GO")
	if path == "" {
		path = "p26-otel-go.json"
	}
	f, err := os.Create(path)
	if err != nil { t.Fatal(err) }
	defer f.Close()
	enc := json.NewEncoder(f)
	enc.SetIndent("","  ")
	if err := enc.Encode(payload); err != nil { t.Fatal(err) }

	if !pass {
		t.Fatalf("P26 Go packet failed: %+v", rows)
	}
}
