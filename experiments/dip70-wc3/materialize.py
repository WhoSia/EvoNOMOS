#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

TARGET = Path("scripts/video_intel.py")
HELPER = Path("scripts/index_update_policy.py")

OLD_FORCE = '''    # Drop existing table if force rebuild
    if force and LANCEDB_TABLE in db.list_tables().tables:
        db.drop_table(LANCEDB_TABLE)
        log.info("Dropped existing table '%s' for rebuild", LANCEDB_TABLE)
'''

OLD_WRITE = '''    # Create or overwrite table
    table = db.create_table(LANCEDB_TABLE, data=all_records, mode="overwrite")

    # Create indices for efficient search
    if len(all_records) >= 256:
        table.create_index(metric="cosine", vector_column_name="vector")
    table.create_fts_index("text")
    table.create_fts_index("title")
'''

OLD_HYBRID = '''    if channel_filter:
        where_clauses.append(f"channel = '{channel_filter}'")
'''

QUOTE_HELPER = '''\n\ndef _lancedb_quote_literal(value: str) -> str:
    """Return one LanceDB/SQL single-quoted literal."""
    return "'" + value.replace("'", "''") + "'"
'''

DIRECT_FORCE_PHASE1 = '''    table_exists = LANCEDB_TABLE in db.list_tables().tables
    if channel_filter and not table_exists:
        raise RuntimeError("Scoped index requires an existing full index; run index without --channel first.")
    if force and not channel_filter and table_exists:
        db.drop_table(LANCEDB_TABLE)
        log.info("Dropped existing table '%s' for rebuild", LANCEDB_TABLE)
'''

DIRECT_WRITE_PHASE0 = '''    # DIRECT: scoped/full mutation policy remains inline in build_search_index.
    if channel_filter:
        table = db.open_table(LANCEDB_TABLE)
        table.delete(f"channel = '{channel_filter}'")
        table.add(all_records)
        table.optimize()
    else:
        table = db.create_table(LANCEDB_TABLE, data=all_records, mode="overwrite")
        if len(all_records) >= 256:
            table.create_index(metric="cosine", vector_column_name="vector")
        table.create_fts_index("text")
        table.create_fts_index("title")
'''

DIRECT_WRITE_PHASE1 = '''    # DIRECT: scoped/full mutation policy remains inline in build_search_index.
    if channel_filter:
        table = db.open_table(LANCEDB_TABLE)
        table.delete(f"channel = {_lancedb_quote_literal(channel_filter)}")
        table.add(all_records)
        table.optimize()
    else:
        table = db.create_table(LANCEDB_TABLE, data=all_records, mode="overwrite")
        if len(all_records) >= 256:
            table.create_index(metric="cosine", vector_column_name="vector")
        table.create_fts_index("text")
        table.create_fts_index("title")
'''

DIRECT_HYBRID_PHASE1 = '''    if channel_filter:
        where_clauses.append(f"channel = {_lancedb_quote_literal(channel_filter)}")
'''

INVERT_FORCE = '''    from index_update_policy import IndexUpdatePolicy

    index_update = IndexUpdatePolicy(db, LANCEDB_TABLE, channel_filter, force)
    index_update.pre_embed()
'''

INVERT_WRITE = '''    # INVERT: mutation lifecycle is owned by index_update_policy.py.
    table = index_update.commit(all_records)
    if not channel_filter:
        if len(all_records) >= 256:
            table.create_index(metric="cosine", vector_column_name="vector")
        table.create_fts_index("text")
        table.create_fts_index("title")
'''

INVERT_HYBRID_PHASE1 = '''    if channel_filter:
        from index_update_policy import quote_lancedb_literal

        where_clauses.append(f"channel = {quote_lancedb_literal(channel_filter)}")
'''

HELPER_PHASE0 = '''"""Scoped/full LanceDB mutation policy for video-intel index writes."""


class IndexUpdatePolicy:
    def __init__(self, db, table_name: str, channel_filter: str | None, force: bool):
        self.db = db
        self.table_name = table_name
        self.channel_filter = channel_filter
        self.force = force

    def pre_embed(self) -> None:
        if self.force and self.table_name in self.db.list_tables().tables:
            self.db.drop_table(self.table_name)

    def commit(self, records):
        if self.channel_filter:
            table = self.db.open_table(self.table_name)
            table.delete(f"channel = '{self.channel_filter}'")
            table.add(records)
            table.optimize()
            return table
        return self.db.create_table(self.table_name, data=records, mode="overwrite")
'''

HELPER_PHASE1 = '''"""Scoped/full LanceDB mutation policy for video-intel index writes."""


def quote_lancedb_literal(value: str) -> str:
    """Return one LanceDB/SQL single-quoted literal."""
    return "'" + value.replace("'", "''") + "'"


class IndexUpdatePolicy:
    def __init__(self, db, table_name: str, channel_filter: str | None, force: bool):
        self.db = db
        self.table_name = table_name
        self.channel_filter = channel_filter
        self.force = force

    def pre_embed(self) -> None:
        table_exists = self.table_name in self.db.list_tables().tables
        if self.channel_filter and not table_exists:
            raise RuntimeError("Scoped index requires an existing full index; run index without --channel first.")
        if self.force and not self.channel_filter and table_exists:
            self.db.drop_table(self.table_name)

    def commit(self, records):
        if self.channel_filter:
            table = self.db.open_table(self.table_name)
            table.delete(f"channel = {quote_lancedb_literal(self.channel_filter)}")
            table.add(records)
            table.optimize()
            return table
        return self.db.create_table(self.table_name, data=records, mode="overwrite")
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"MATERIALIZE_HOLD:{label}:expected_once:found_{count}")
    return text.replace(old, new, 1)


def direct(base: str, phase: int) -> str:
    text = base
    if phase == 0:
        text = replace_once(text, OLD_WRITE, DIRECT_WRITE_PHASE0, "direct_phase0_write")
        return text
    text = replace_once(text, OLD_FORCE, DIRECT_FORCE_PHASE1, "direct_phase1_force")
    text = replace_once(text, OLD_WRITE, DIRECT_WRITE_PHASE1, "direct_phase1_write")
    marker = "\n\ndef build_search_index(\n"
    text = replace_once(text, marker, QUOTE_HELPER + marker, "direct_phase1_quote_helper")
    text = replace_once(text, OLD_HYBRID, DIRECT_HYBRID_PHASE1, "direct_phase1_hybrid")
    return text


def invert(base: str, phase: int) -> tuple[str, str]:
    text = replace_once(base, OLD_FORCE, INVERT_FORCE, f"invert_phase{phase}_force")
    text = replace_once(text, OLD_WRITE, INVERT_WRITE, f"invert_phase{phase}_write")
    helper = HELPER_PHASE0
    if phase == 1:
        text = replace_once(text, OLD_HYBRID, INVERT_HYBRID_PHASE1, "invert_phase1_hybrid")
        helper = HELPER_PHASE1
    return text, helper


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_snapshot(base_dir: Path, out_dir: Path, policy: str, phase: int) -> dict:
    src = (base_dir / TARGET).read_text(encoding="utf-8")
    dest_root = out_dir / policy / f"phase{phase}"
    (dest_root / TARGET.parent).mkdir(parents=True, exist_ok=True)
    changed = []
    if policy == "DIRECT":
        (dest_root / TARGET).write_text(direct(src, phase), encoding="utf-8")
        changed = [str(TARGET)]
    else:
        target, helper = invert(src, phase)
        (dest_root / TARGET).write_text(target, encoding="utf-8")
        (dest_root / HELPER).write_text(helper, encoding="utf-8")
        changed = [str(TARGET), str(HELPER)]
    return {
        "policy": policy,
        "phase": phase,
        "changed_production_paths": changed,
        "sha256": {p: sha256(dest_root / p) for p in changed},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    base_dir = Path(args.base_dir).resolve()
    out_dir = Path(args.out).resolve()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    receipts = [
        write_snapshot(base_dir, out_dir, policy, phase)
        for policy in ("DIRECT", "INVERT")
        for phase in (0, 1)
    ]
    (out_dir / "materialization.json").write_text(
        json.dumps({"status": "MATERIALIZED_PREOUTCOME", "snapshots": receipts}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "MATERIALIZED_PREOUTCOME", "snapshots": receipts}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
