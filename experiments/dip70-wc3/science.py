#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

EXPECTED_BASE = "57fc8f74366170b55ec5473d764336c75a08f169"
TARGET = Path("scripts/video_intel.py")
HELPER = Path("scripts/index_update_policy.py")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aggregate_hash(items: dict[str, str]) -> str:
    h = hashlib.sha256()
    for key in sorted(items):
        h.update(key.encode())
        h.update(b"\0")
        h.update(items[key].encode())
        h.update(b"\n")
    return h.hexdigest()


def load_vi(work: Path, client):
    scripts = str(work / "scripts")
    if scripts in sys.path:
        sys.path.remove(scripts)
    sys.path.insert(0, scripts)
    for name in ("video_intel", "index_update_policy"):
        sys.modules.pop(name, None)
    spec = importlib.util.spec_from_file_location("video_intel", work / TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError("SCIENCE_HOLD:cannot_load_video_intel")
    module = importlib.util.module_from_spec(spec)
    sys.modules["video_intel"] = module
    spec.loader.exec_module(module)
    fake_voyage = SimpleNamespace(Client=lambda: client)
    module.require_voyageai = lambda: fake_voyage
    os.environ["VOYAGE_API_KEY"] = "DIP70_WC3_FAKE_VOYAGE_ONLY"
    return module


class FakeVoyageClient:
    def __init__(self):
        self.calls: list[dict] = []
        self.fail_next = False

    @staticmethod
    def _vector(text: str) -> list[float]:
        raw = hashlib.sha256(text.encode("utf-8")).digest()
        return [((raw[i] / 255.0) * 2.0) - 1.0 for i in range(16)]

    def reset(self) -> None:
        self.calls.clear()
        self.fail_next = False

    def embed(self, texts, *, model=None, input_type=None, **_kwargs):
        values = list(texts)
        self.calls.append({"texts": values, "model": model, "input_type": input_type})
        if self.fail_next:
            self.fail_next = False
            raise RuntimeError("DIP70_WC3_SYNTHETIC_EMBED_FAILURE")
        return SimpleNamespace(embeddings=[self._vector(text) for text in values])


def write_video(corpus: Path, channel: str, slug: str, marker: str, video_id: str) -> None:
    channel_dir = corpus / channel
    channel_dir.mkdir(parents=True, exist_ok=True)
    prefix = f"2026-08-31-{slug}"
    lines = [f"[00:0{i}] Speaker: {marker} line {i}" for i in range(5)]
    (channel_dir / f"{prefix}.transcript.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (channel_dir / f"{prefix}.meta.json").write_text(
        json.dumps({"title": marker, "published": "2026-08-31", "video_id": video_id}),
        encoding="utf-8",
    )


def rows(vi, db_dir: Path) -> list[dict]:
    db = vi.require_lancedb().connect(str(db_dir))
    table = db.open_table(vi.LANCEDB_TABLE)
    raw = table.to_arrow().to_pylist()
    cleaned = []
    for row in raw:
        cleaned.append({k: v for k, v in row.items() if k != "vector"})
    return sorted(cleaned, key=lambda r: (str(r.get("channel")), str(r.get("video_id")), str(r.get("text"))))


def channels_of(values: list[dict]) -> set[str]:
    return {str(row["channel"]) for row in values}


def setup_two_channel(vi, client: FakeVoyageClient, root: Path, *, a_channel: str = "alpha") -> tuple[Path, Path, dict]:
    corpus = root / "corpus"
    db_dir = root / "db"
    db_dir.mkdir(parents=True, exist_ok=True)
    write_video(corpus, a_channel, "a", "A ORIGINAL", "video-a")
    write_video(corpus, "beta", "b", "B STABLE", "video-b")
    config = {"vector_db_dir": str(db_dir)}
    client.reset()
    count = vi.build_search_index(corpus, config=config)
    if count != 2:
        raise RuntimeError(f"SCIENCE_HOLD:full_index_count:{count}")
    initial = rows(vi, db_dir)
    if channels_of(initial) != {a_channel, "beta"}:
        raise RuntimeError(f"SCIENCE_HOLD:full_index_channels:{channels_of(initial)}")
    return corpus, db_dir, config


def baseline_probe(base: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix="dip70-wc3-baseline-") as td:
        work = Path(td) / "repo"
        shutil.copytree(base, work, symlinks=True)
        client = FakeVoyageClient()
        vi = load_vi(work, client)
        corpus, db_dir, config = setup_two_channel(vi, client, Path(td) / "case")
        write_video(corpus, "alpha", "a", "A BASELINE SCOPED", "video-a")
        client.reset()
        vi.build_search_index(corpus, channel_filter="alpha", config=config)
        after = rows(vi, db_dir)
        if channels_of(after) != {"alpha"}:
            raise RuntimeError(f"SCIENCE_HOLD:BASELINE_NOT_DESTRUCTIVE:{channels_of(after)}")
        return {"status": "EXPECTED_DESTRUCTIVE_SCOPED_OVERWRITE_REPRODUCED", "remaining_channels": sorted(channels_of(after))}


def overlay(base: Path, snapshot: Path, work: Path) -> None:
    shutil.copytree(base, work, symlinks=True)
    for src in snapshot.rglob("*"):
        if src.is_file():
            rel = src.relative_to(snapshot)
            dst = work / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def core_oracle(work: Path) -> dict:
    client = FakeVoyageClient()
    vi = load_vi(work, client)
    with tempfile.TemporaryDirectory(prefix="dip70-wc3-core-") as td:
        root = Path(td)
        corpus, db_dir, config = setup_two_channel(vi, client, root)
        write_video(corpus, "alpha", "a", "A UPDATED", "video-a")
        client.reset()
        vi.build_search_index(corpus, channel_filter="alpha", config=config)
        after = rows(vi, db_dir)
        if channels_of(after) != {"alpha", "beta"}:
            raise RuntimeError(f"SCIENCE_HOLD:PHASE_CORE_PRESERVATION:{channels_of(after)}")
        alpha = [r for r in after if r["channel"] == "alpha"]
        beta = [r for r in after if r["channel"] == "beta"]
        if len(alpha) != 1 or "A UPDATED" not in alpha[0]["text"] or len(beta) != 1 or beta[0]["video_id"] != "video-b":
            raise RuntimeError("SCIENCE_HOLD:PHASE_CORE_CONTENT")
        embedded_texts = [text for call in client.calls for text in call["texts"]]
        if not embedded_texts or any("B STABLE" in text for text in embedded_texts) or any("A UPDATED" not in text for text in embedded_texts):
            raise RuntimeError(f"SCIENCE_HOLD:SCOPED_EMBED_SCOPE:{embedded_texts}")

        before_failure = rows(vi, db_dir)
        write_video(corpus, "alpha", "a", "A FAILURE ATTEMPT", "video-a")
        client.reset()
        client.fail_next = True
        failed = False
        try:
            vi.build_search_index(corpus, channel_filter="alpha", config=config)
        except RuntimeError as exc:
            if "DIP70_WC3_SYNTHETIC_EMBED_FAILURE" not in str(exc):
                raise
            failed = True
        if not failed:
            raise RuntimeError("SCIENCE_HOLD:EMBED_FAILURE_NOT_PROPAGATED")
        after_failure = rows(vi, db_dir)
        if after_failure != before_failure:
            raise RuntimeError("SCIENCE_HOLD:EMBED_FAILURE_MUTATED_INDEX")
        return {
            "preserved_channels": sorted(channels_of(after)),
            "scoped_embed_text_count": len(embedded_texts),
            "embed_failure_preserved_old_rows": True,
        }


def phase1_oracle(work: Path) -> dict:
    client = FakeVoyageClient()
    vi = load_vi(work, client)
    result: dict = {}

    with tempfile.TemporaryDirectory(prefix="dip70-wc3-missing-") as td:
        root = Path(td)
        corpus = root / "corpus"
        db_dir = root / "db"
        db_dir.mkdir(parents=True)
        write_video(corpus, "alpha", "a", "A MISSING TABLE", "video-a")
        config = {"vector_db_dir": str(db_dir)}
        client.reset()
        refused = False
        try:
            vi.build_search_index(corpus, channel_filter="alpha", config=config)
        except RuntimeError as exc:
            if "Scoped index requires an existing full index" not in str(exc):
                raise
            refused = True
        if not refused or client.calls:
            raise RuntimeError(f"SCIENCE_HOLD:MISSING_TABLE_ORDER:refused={refused}:calls={client.calls}")
        result["missing_table_refused_before_embed"] = True

    with tempfile.TemporaryDirectory(prefix="dip70-wc3-force-") as td:
        root = Path(td)
        corpus, db_dir, config = setup_two_channel(vi, client, root)
        write_video(corpus, "alpha", "a", "A FORCE SCOPED", "video-a")
        client.reset()
        vi.build_search_index(corpus, channel_filter="alpha", force=True, config=config)
        after = rows(vi, db_dir)
        if channels_of(after) != {"alpha", "beta"}:
            raise RuntimeError(f"SCIENCE_HOLD:FORCE_SCOPED_DESTRUCTIVE:{channels_of(after)}")
        result["force_scoped_preserved_other_channel"] = True

    with tempfile.TemporaryDirectory(prefix="dip70-wc3-quote-") as td:
        root = Path(td)
        target = "o'brien"
        corpus, db_dir, config = setup_two_channel(vi, client, root, a_channel=target)
        write_video(corpus, target, "a", "O BRIEN UPDATED", "video-a")
        client.reset()
        vi.build_search_index(corpus, channel_filter=target, config=config)
        after = rows(vi, db_dir)
        if channels_of(after) != {target, "beta"}:
            raise RuntimeError(f"SCIENCE_HOLD:QUOTE_SCOPED_CHANNELS:{channels_of(after)}")
        target_rows = [r for r in after if r["channel"] == target]
        if len(target_rows) != 1 or "O BRIEN UPDATED" not in target_rows[0]["text"]:
            raise RuntimeError("SCIENCE_HOLD:QUOTE_SCOPED_CONTENT")
        client.reset()
        hits = vi.hybrid_search(corpus, "UPDATED", channel_filter=target, config=config, expand=False, limit=5)
        if not hits or any(hit.get("channel") != target for hit in hits):
            raise RuntimeError(f"SCIENCE_HOLD:HYBRID_QUOTE_RUNTIME:{hits}")
        result["apostrophe_delete_preserved_scope"] = True
        result["hybrid_quote_runtime"] = True

    return result


def verify_treatment_hashes(snapshot: Path, policy: str, phase: int, rcert: dict) -> str:
    expected = rcert["policies"][policy][f"phase{phase}"]
    actual = {}
    for rel in expected["changed_production_paths"]:
        actual[rel] = sha256(snapshot / rel)
    if actual != expected["file_sha256"]:
        raise RuntimeError(f"SCIENCE_HOLD:TREATMENT_FILE_HASH:{policy}:phase{phase}")
    agg = aggregate_hash(actual)
    if agg != expected["treatment_sha256"]:
        raise RuntimeError(f"SCIENCE_HOLD:TREATMENT_AGG_HASH:{policy}:phase{phase}")
    return agg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-dir", required=True)
    ap.add_argument("--sealed-root", required=True)
    ap.add_argument("--policy", choices=["DIRECT", "INVERT"], required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    base = Path(args.base_dir).resolve()
    sealed = Path(args.sealed_root).resolve()
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    policy = args.policy

    receipt = {
        "status": "SCIENCE_HOLD",
        "policy": policy,
        "python": sys.version.split()[0],
        "lancedb": importlib.metadata.version("lancedb"),
        "exact_base": EXPECTED_BASE,
    }
    try:
        rcert = json.loads((sealed / "RCERT.json").read_text(encoding="utf-8"))
        if rcert.get("status") != "RCERT_PASS_PREOUTCOME" or rcert.get("scientific_oracle_opened") is not False:
            raise RuntimeError("SCIENCE_HOLD:RCERT_NOT_PASS_PREOUTCOME")
        actual_base = os.popen(f"git -C {base} rev-parse HEAD").read().strip()
        if actual_base != EXPECTED_BASE:
            raise RuntimeError(f"SCIENCE_HOLD:BASE_IDENTITY:{actual_base}")

        receipt["baseline"] = baseline_probe(base)
        phases = {}
        for phase in (0, 1):
            snapshot = sealed / "treatments" / policy / f"phase{phase}"
            treatment_hash = verify_treatment_hashes(snapshot, policy, phase, rcert)
            with tempfile.TemporaryDirectory(prefix=f"dip70-wc3-{policy.lower()}-p{phase}-") as td:
                work = Path(td) / "repo"
                overlay(base, snapshot, work)
                phase_receipt = {"treatment_sha256": treatment_hash, "core": core_oracle(work)}
                if phase == 1:
                    phase_receipt["followup"] = phase1_oracle(work)
                phases[f"phase{phase}"] = phase_receipt
        receipt["phases"] = phases
        receipt["V"] = rcert["policies"][policy]["measurement"]["V"]
        receipt["measurement"] = rcert["policies"][policy]["measurement"]
        receipt["status"] = "SCIENCE_PASS"
    except Exception as exc:
        receipt["error"] = str(exc)

    receipt_bytes = json.dumps(receipt, sort_keys=True, separators=(",", ":")).encode()
    receipt["receipt_sha256"] = hashlib.sha256(receipt_bytes).hexdigest()
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
