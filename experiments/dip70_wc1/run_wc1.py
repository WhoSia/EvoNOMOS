#!/usr/bin/env python3
import argparse
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

SUBSTRATE_REPO = "https://github.com/yashumani/open-source-reviewer-app.git"
BASE_SHA = "60caaccb7514e28c633c3aa3bd179e9ae8d5b154"
CONSUMER_LOCI = ("src/analyzer.js",)

INITIAL_RULES = (
    ("postgresql", "PostgreSQL", "database", (
        ("image", r"(?:image:\\s*[^#\\n]*(?:postgres(?:ql)?)(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\bpostgres(?:ql)?\\b)"),
        ("environment", r"\\bPOSTGRES_(?:DB|USER|PASSWORD|HOST_AUTH_METHOD)\\b"),
    )),
    ("mysql-mariadb", "MySQL/MariaDB", "database", (
        ("image", r"(?:image:\\s*[^#\\n]*(?:mysql|mariadb)(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\b(?:mysqld|mariadbd)\\b)"),
        ("environment", r"\\b(?:MYSQL|MARIADB)_(?:DATABASE|USER|PASSWORD|ROOT_PASSWORD)\\b"),
    )),
    ("redis", "Redis", "data service", (
        ("image", r"(?:image:\\s*[^#\\n]*redis(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\bredis-server\\b)"),
        ("environment", r"\\bREDIS_(?:URL|HOST|PORT|PASSWORD)\\b"),
    )),
    ("rabbitmq", "RabbitMQ", "queue", (
        ("image", r"(?:image:\\s*[^#\\n]*rabbitmq(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\brabbitmq-server\\b)"),
        ("environment", r"\\bRABBITMQ_(?:DEFAULT_USER|DEFAULT_PASS|DEFAULT_VHOST|NODENAME)\\b"),
    )),
    ("kafka-compatible", "Kafka-compatible", "broker", (
        ("image", r"(?:image:\\s*[^#\\n]*(?:confluentinc/cp-kafka|bitnami/kafka|apache/kafka|redpandadata/redpanda)(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*(?:kafka-server-start|redpanda\\s+start))"),
        ("environment", r"\\b(?:KAFKA_(?:NODE_ID|PROCESS_ROLES|CONTROLLER_QUORUM_VOTERS)|KAFKA_CFG_[A-Z0-9_]+|REDPANDA_[A-Z0-9_]+)\\b"),
    )),
)

FOLLOWUP_RULES = INITIAL_RULES + (
    ("mongodb", "MongoDB", "database", (
        ("image", r"(?:image:\\s*[^#\\n]*(?:mongo|mongodb)(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\b(?:mongod|mongos)\\b)"),
        ("environment", r"\\bMONGO_INITDB_(?:DATABASE|ROOT_USERNAME|ROOT_PASSWORD)\\b"),
    )),
    ("nats-compatible", "NATS-compatible", "broker", (
        ("image", r"(?:image:\\s*[^#\\n]*(?:nats)(?::|@|\\s|$))"),
        ("command", r"(?:command:\\s*[^#\\n]*\\bnats-server\\b)"),
        ("environment", r"\\bNATS_(?:SERVER_NAME|CLUSTER_NAME|PORT|HTTP_PORT)\\b"),
    )),
)


def sh(cmd, cwd=None, check=False, timeout=300):
    p = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
    if check and p.returncode:
        raise RuntimeError(f"CMD_FAIL:{' '.join(cmd)}\n{p.stdout[-4000:]}")
    return p


def clone_base(dst: Path):
    sh(["git", "clone", "--quiet", "--no-checkout", SUBSTRATE_REPO, str(dst)], check=True, timeout=180)
    sh(["git", "checkout", "--quiet", BASE_SHA], cwd=dst, check=True)
    got = sh(["git", "rev-parse", "HEAD"], cwd=dst, check=True).stdout.strip()
    if got != BASE_SHA:
        raise RuntimeError(f"BASE_SHA_MISMATCH:{got}")


def regex_literal(source: str):
    return f"/{source}/i"


def rules_js(rules):
    chunks = []
    for rid, name, kind, signals in rules:
        sigs = ",\n      ".join(
            f'{{ signal: {json.dumps(signal)}, pattern: {regex_literal(pattern)} }}'
            for signal, pattern in signals
        )
        chunks.append(
            "  {\n"
            f"    id: {json.dumps(rid)},\n"
            f"    name: {json.dumps(name)},\n"
            f"    kind: {json.dumps(kind)},\n"
            "    signals: [\n"
            f"      {sigs}\n"
            "    ],\n"
            "  }"
        )
    return ",\n".join(chunks)


def detector_block(rules, exported=False, import_unique=False):
    prefix = 'import { unique } from "./schema.js";\n\n' if import_unique else ""
    export_kw = "export " if exported else ""
    return prefix + f'''// Compose service evidence detection.
const COMPOSE_SERVICE_PATH = /(^|\\/)(docker-)?compose(?:\\.[^/]+)?\\.ya?ml$/i;
const COMPOSE_SERVICE_RULES = Object.freeze([
{rules_js(rules)}
]);

function collectComposeAnchorBlocks(text) {{
  const lines = String(text ?? "").split(/\\r?\\n/);
  const anchors = new Map();
  for (let i = 0; i < lines.length; i += 1) {{
    const match = lines[i].match(/^(\\s*)(?:x-[A-Za-z0-9_.-]+|[A-Za-z0-9_.-]+):\\s*&([A-Za-z0-9_.-]+)\\s*(?:#.*)?$/);
    if (!match) continue;
    const baseIndent = match[1].length;
    const block = [];
    for (let j = i + 1; j < lines.length; j += 1) {{
      const line = lines[j];
      if (!line.trim() || line.trimStart().startsWith("#")) {{ block.push(line); continue; }}
      const indent = line.match(/^\\s*/)[0].length;
      if (indent <= baseIndent) break;
      block.push(line);
    }}
    anchors.set(match[2], block.join("\\n"));
  }}
  return anchors;
}}

function composeServiceBlocks(text) {{
  const raw = String(text ?? "");
  const lines = raw.split(/\\r?\\n/);
  const anchors = collectComposeAnchorBlocks(raw);
  let servicesIndent = null;
  let serviceIndent = null;
  let active = null;
  const blocks = [];
  const finish = () => {{
    if (!active) return;
    const original = active.lines.join("\\n");
    const merged = [];
    for (const match of original.matchAll(/<<:\\s*\\*([A-Za-z0-9_.-]+)/g)) {{
      if (anchors.has(match[1])) merged.push(anchors.get(match[1]));
    }}
    blocks.push({{ name: active.name, original, resolved: [original, ...merged].join("\\n") }});
    active = null;
  }};

  for (const line of lines) {{
    if (servicesIndent === null) {{
      const root = line.match(/^(\\s*)services:\\s*(?:#.*)?$/);
      if (root) servicesIndent = root[1].length;
      continue;
    }}
    if (!line.trim() || line.trimStart().startsWith("#")) {{ if (active) active.lines.push(line); continue; }}
    const indent = line.match(/^\\s*/)[0].length;
    if (indent <= servicesIndent) {{ finish(); break; }}
    const service = line.match(/^(\\s+)([A-Za-z0-9_.-]+):\\s*(?:#.*)?$/);
    if (serviceIndent === null && service && indent > servicesIndent) serviceIndent = indent;
    if (service && indent === serviceIndent) {{
      finish();
      active = {{ name: service[2], lines: [line] }};
    }} else if (active) {{
      active.lines.push(line);
    }}
  }}
  finish();
  return blocks;
}}

{export_kw}function detectComposeServices(corpus = []) {{
  const found = [];
  const seen = new Set();
  for (const item of corpus) {{
    if (!COMPOSE_SERVICE_PATH.test(item.path)) continue;
    for (const block of composeServiceBlocks(item.content)) {{
      for (const rule of COMPOSE_SERVICE_RULES) {{
        const signals = unique(rule.signals.filter((entry) => entry.pattern.test(block.resolved)).map((entry) => entry.signal));
        if (!signals.length) continue;
        const key = `${{item.path}}|${{block.name}}|${{rule.id}}`;
        if (seen.has(key)) continue;
        seen.add(key);
        found.push({{
          id: rule.id,
          name: rule.name,
          kind: rule.kind,
          service: block.name,
          path: item.path,
          signals,
          uncertain: /\\$\\{{[^}}]+\\}}/.test(block.resolved),
          runtimeUseProven: false,
        }});
      }}
    }}
  }}
  return found;
}}
// End Compose service evidence detection.
'''


def integrate_analyzer(text: str, detector_local=None, add_import=False):
    if add_import:
        marker = 'import { buildArtifactInventory, countExtensions, inventorySummary } from "./inventory.js";\n'
        replacement = marker + 'import { detectComposeServices } from "./compose-services.js";\n'
        if marker not in text:
            raise RuntimeError("ANALYZER_IMPORT_MARKER_MISSING")
        text = text.replace(marker, replacement, 1)
    if detector_local is not None:
        marker = "export function analyzeRepository(snapshot, rawContext = {}) {"
        if marker not in text:
            raise RuntimeError("ANALYZER_FUNCTION_MARKER_MISSING")
        text = text.replace(marker, detector_local + "\n" + marker, 1)

    old = '''  const databases = technologies.filter((item) => item.category === "database" || item.category === "data service").map((item) => item.name);
  const deployment = unique([
'''
    new = '''  const composeServices = detectComposeServices(corpus);
  const databases = unique([
    ...technologies.filter((item) => item.category === "database" || item.category === "data service").map((item) => item.name),
    ...composeServices.filter((item) => item.kind === "database" || item.kind === "data service").map((item) => item.name),
  ]);
  const deployment = unique([
'''
    if old not in text:
        raise RuntimeError("ANALYZER_DATABASE_MARKER_MISSING")
    text = text.replace(old, new, 1)
    old_ops = '''    databases,
    deployment,
'''
    new_ops = '''    databases,
    composeServices,
    deployment,
'''
    if old_ops not in text:
        raise RuntimeError("ANALYZER_OPERATIONS_MARKER_MISSING")
    return text.replace(old_ops, new_ops, 1)


def tests_js(followup=False):
    extra = '''

test("follow-up detects MongoDB and NATS-compatible services", () => {
  const ops = analyzeCompose(`services:\n  docstore:\n    image: mongo:8\n  events:\n    command: nats-server --js`);
  assert.equal(one(ops, "MongoDB").service, "docstore");
  assert.equal(one(ops, "NATS-compatible").service, "events");
  assert.ok(ops.databases.includes("MongoDB"));
});
''' if followup else ""
    return '''import test from "node:test";
import assert from "node:assert/strict";
import { analyzeRepository } from "../src/analyzer.js";
import { contexts, makeSnapshot } from "./fixtures.js";

function analyzeCompose(compose) {
  const files = {
    "README.md": "# Fixture",
    "LICENSE": "Apache-2.0",
    "package.json": "{}",
    "compose.yml": compose,
    "tests/smoke.test.js": "test",
    ".github/workflows/ci.yml": "name: ci\\non: [push]\\njobs: {}",
  };
  return analyzeRepository(makeSnapshot({ files }), contexts.selfHost).operations;
}

function one(ops, name) {
  const matches = ops.composeServices.filter((item) => item.name === name);
  assert.equal(matches.length, 1, `expected one ${name} result, got ${matches.length}`);
  return matches[0];
}

test("custom service names are classified from image or command evidence", () => {
  const ops = analyzeCompose(`services:\n  datahouse:\n    image: postgres:16\n  sqlbox:\n    image: mariadb:11\n  cachebox:\n    command: redis-server --appendonly yes\n  queuebox:\n    image: rabbitmq:3-management\n  streambox:\n    image: redpandadata/redpanda:v24.1.1`);
  assert.equal(one(ops, "PostgreSQL").service, "datahouse");
  assert.equal(one(ops, "MySQL/MariaDB").service, "sqlbox");
  assert.equal(one(ops, "Redis").service, "cachebox");
  assert.equal(one(ops, "RabbitMQ").service, "queuebox");
  assert.equal(one(ops, "Kafka-compatible").service, "streambox");
  assert.ok(ops.databases.includes("PostgreSQL"));
  assert.ok(ops.databases.includes("MySQL/MariaDB"));
  assert.ok(ops.databases.includes("Redis"));
});

test("duplicate service signals deduplicate while retaining signal provenance", () => {
  const ops = analyzeCompose(`services:\n  custom:\n    image: postgres:16\n    environment:\n      POSTGRES_DB: app`);
  const pg = one(ops, "PostgreSQL");
  assert.deepEqual(pg.signals.sort(), ["environment", "image"]);
  assert.equal(pg.path, "compose.yml");
  assert.equal(pg.runtimeUseProven, false);
});

test("simple YAML service anchors are resolved for static evidence", () => {
  const ops = analyzeCompose(`x-db: &db\n  image: postgres:16\nservices:\n  custom-name:\n    <<: *db\n    profiles: [prod]`);
  const pg = one(ops, "PostgreSQL");
  assert.equal(pg.service, "custom-name");
});

test("templated evidence remains explicitly uncertain", () => {
  const ops = analyzeCompose(`services:\n  custom-name:\n    image: ${DB_IMAGE}\n    environment:\n      POSTGRES_DB: ${DB_NAME}`);
  assert.equal(one(ops, "PostgreSQL").uncertain, true);
});

test("unrelated Compose services are not classified as data infrastructure", () => {
  const ops = analyzeCompose(`services:\n  app:\n    image: nginx:alpine\n    command: nginx -g 'daemon off;'`);
  assert.deepEqual(ops.composeServices, []);
});
''' + extra


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def apply_initial(root: Path, policy: str):
    analyzer_path = root / "src/analyzer.js"
    analyzer = analyzer_path.read_text()
    if policy == "DIRECT":
        analyzer = integrate_analyzer(analyzer, detector_local=detector_block(INITIAL_RULES), add_import=False)
    elif policy == "INVERT":
        write_text(root / "src/compose-services.js", detector_block(INITIAL_RULES, exported=True, import_unique=True))
        analyzer = integrate_analyzer(analyzer, detector_local=None, add_import=True)
    else:
        raise RuntimeError("UNKNOWN_POLICY")
    analyzer_path.write_text(analyzer)
    write_text(root / "tests/compose-service-detection.test.js", tests_js(False))
    certify_policy(root, policy)


def apply_followup(root: Path, policy: str):
    if policy == "DIRECT":
        p = root / "src/analyzer.js"
        text = p.read_text()
        old = detector_block(INITIAL_RULES)
        new = detector_block(FOLLOWUP_RULES)
        if text.count(old) != 1:
            raise RuntimeError(f"DIRECT_DETECTOR_REPLACEMENT_COUNT:{text.count(old)}")
        p.write_text(text.replace(old, new, 1))
    elif policy == "INVERT":
        p = root / "src/compose-services.js"
        old = detector_block(INITIAL_RULES, exported=True, import_unique=True)
        if p.read_text() != old:
            raise RuntimeError("INVERT_PROVIDER_BYTES_DRIFT_BEFORE_FOLLOWUP")
        p.write_text(detector_block(FOLLOWUP_RULES, exported=True, import_unique=True))
    else:
        raise RuntimeError("UNKNOWN_POLICY")
    write_text(root / "tests/compose-service-detection.test.js", tests_js(True))
    certify_policy(root, policy)


def certify_policy(root: Path, policy: str):
    analyzer = (root / "src/analyzer.js").read_text()
    provider = root / "src/compose-services.js"
    if policy == "DIRECT":
        if provider.exists():
            raise RuntimeError("DIRECT_FORBIDDEN_PROVIDER_FILE")
        if analyzer.count("function detectComposeServices(") != 1:
            raise RuntimeError("DIRECT_DETECTOR_NOT_LOCAL")
        if 'from "./compose-services.js"' in analyzer:
            raise RuntimeError("DIRECT_FORBIDDEN_PROVIDER_IMPORT")
    else:
        if not provider.exists():
            raise RuntimeError("INVERT_PROVIDER_MISSING")
        if 'import { detectComposeServices } from "./compose-services.js";' not in analyzer:
            raise RuntimeError("INVERT_PROVIDER_IMPORT_MISSING")
        if analyzer.count("function detectComposeServices(") != 0:
            raise RuntimeError("INVERT_DETECTOR_LEAKED_INTO_CONSUMER")


def production_snapshot(root: Path):
    out = {}
    src = root / "src"
    for path in sorted(src.rglob("*")):
        if path.is_file():
            out[path.relative_to(root).as_posix()] = path.read_text()
    return out


def line_churn(before: str, after: str):
    churn = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=before.splitlines(), b=after.splitlines()).get_opcodes():
        if tag == "replace": churn += (i2 - i1) + (j2 - j1)
        elif tag == "delete": churn += i2 - i1
        elif tag == "insert": churn += j2 - j1
    return churn


def delta_metrics(before, after):
    paths = sorted(set(before) | set(after))
    changed = [p for p in paths if before.get(p, "") != after.get(p, "")]
    return changed, sum(line_churn(before.get(p, ""), after.get(p, "")) for p in changed)


def snapshot_hash(snapshot):
    h = hashlib.sha256()
    for path in sorted(snapshot):
        h.update(path.encode()); h.update(b"\0"); h.update(snapshot[path].encode()); h.update(b"\0")
    return h.hexdigest()


def run_oracle(root: Path, phase: str):
    p = sh(["npm", "run", "validate"], cwd=root, timeout=600)
    return {
        "phase": phase,
        "returncode": p.returncode,
        "pass": p.returncode == 0,
        "tail": p.stdout[-6000:],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy", choices=["DIRECT", "INVERT"], required=True)
    ap.add_argument("--route", choices=["node22", "node24"], required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "stage": "DIP-70-WC1",
        "policy": args.policy,
        "route": args.route,
        "base_sha": BASE_SHA,
        "status": "HOLD",
        "first_failure_stage": None,
    }
    work = Path(tempfile.mkdtemp(prefix="evonomos_dip70_wc1_"))
    try:
        root = work / "repo"
        clone_base(root)
        node_version = sh(["node", "--version"], check=True).stdout.strip()
        rec["node_version"] = node_version
        wanted = 22 if args.route == "node22" else 24
        got = int(re.match(r"v(\\d+)", node_version).group(1))
        if got != wanted:
            raise RuntimeError(f"ROUTE_NODE_MAJOR_MISMATCH:{got}!={wanted}")

        base_snap = production_snapshot(root)
        rec["base_production_hash"] = snapshot_hash(base_snap)
        baseline = run_oracle(root, "BASELINE")
        rec["baseline_oracle"] = baseline
        if not baseline["pass"]:
            rec["first_failure_stage"] = "BASELINE_ORACLE"
            return

        apply_initial(root, args.policy)
        initial_snap = production_snapshot(root)
        changed0, c0 = delta_metrics(base_snap, initial_snap)
        rec["initial_production_hash"] = snapshot_hash(initial_snap)
        rec["initial_changed_files"] = changed0
        rec["F0"] = len(changed0)
        rec["C0"] = c0
        initial = run_oracle(root, "INITIAL")
        rec["initial_oracle"] = initial
        if not initial["pass"]:
            rec["first_failure_stage"] = "INITIAL_ORACLE"
            return

        apply_followup(root, args.policy)
        follow_snap = production_snapshot(root)
        changed1, c1 = delta_metrics(initial_snap, follow_snap)
        rec["followup_production_hash"] = snapshot_hash(follow_snap)
        rec["followup_changed_files"] = changed1
        rec["F1"] = len(changed1)
        rec["C1"] = c1
        provider_exclusion = set() if args.policy == "DIRECT" else {"src/compose-services.js"}
        rec["P1"] = sum(
            1 for p in CONSUMER_LOCI
            if p in changed1 and p not in provider_exclusion
        )
        follow = run_oracle(root, "FOLLOWUP")
        rec["followup_oracle"] = follow
        if not follow["pass"]:
            rec["first_failure_stage"] = "FOLLOWUP_ORACLE"
            return

        rec["V"] = [rec["F0"], rec["C0"], rec["F1"], rec["C1"], rec["P1"]]
        rec["status"] = "PASS"
    except subprocess.TimeoutExpired as e:
        rec["first_failure_stage"] = "INFRA_TIMEOUT"
        rec["error"] = str(e)
    except Exception as e:
        rec["first_failure_stage"] = rec.get("first_failure_stage") or "REALIZATION_OR_INFRA"
        rec["error"] = str(e)[:5000]
    finally:
        out.write_text(json.dumps(rec, ensure_ascii=False, indent=2))
        print("EVONOMOS_DIP70_WC1_RESULT", json.dumps({k: rec.get(k) for k in ("policy", "route", "status", "first_failure_stage", "V")}, separators=(",", ":")), flush=True)
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
