#!/usr/bin/env python3
"""P31 prospective state-aware structural policy world-contact calibration.

No state or action is selected from a future Y. Each one-step trajectory is an
independent disk-backed SQLite DB, and every SQL statement runs in a new CLI
process. Only the exact-source hosted workflow can grant canonical evidence.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import tempfile
import time

SOURCE_SHA = "f3d536d37825302e31ed0eddd811c689f38f85a3"
SOURCE_FOSSIL = "c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33"
HIGH_WATERS = (0, 3, 7, 11)
THRESHOLDS = (5, 9)
ACTIONS = ("NOOP", "RESERVE")
REPETITIONS = 3
FINAL_SQL = "INSERT INTO events(note) VALUES('next') RETURNING id;"

def query(executable, database, statement):
    cp = subprocess.run(
        [str(executable), "-json", str(database), statement],
        capture_output=True, text=True, check=False, timeout=40
    )
    if cp.returncode:
        raise RuntimeError(
            f"sqlite3 cli failure: rc={cp.returncode}, statement={statement!r}, "
            f"stderr={cp.stderr[:500]}"
        )
    raw = cp.stdout.strip()
    return json.loads(raw) if raw else []

def snapshot(executable, database):
    return {
        "schema": query(executable, database,
                        "SELECT type,name,tbl_name,sql FROM sqlite_schema ORDER BY type,name;"),
        "rows": query(executable, database, "SELECT id,note FROM events ORDER BY id;"),
        "count": query(executable, database, "SELECT count(*) AS n FROM events;"),
        "journal": query(executable, database, "PRAGMA journal_mode;"),
        "foreign_keys": query(executable, database, "PRAGMA foreign_keys;"),
        "read_uncommitted": query(executable, database, "PRAGMA read_uncommitted;")
    }

def sequence(executable, database):
    return query(executable, database,
                 "SELECT name,seq FROM sqlite_sequence WHERE name='events' ORDER BY rowid;")

def trajectory(executable, root, iteration, initial_h, minimum, action):
    db = root / f"r{iteration}_h{initial_h}_m{minimum}_{action}.db"
    query(executable, db,
          "CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT NOT NULL);")
    query(executable, db,
          "BEGIN; INSERT INTO events(id,note) VALUES"
          f"({initial_h},'seed'); DELETE FROM events WHERE id={initial_h}; COMMIT;")
    before = snapshot(executable, db)
    seq_before = sequence(executable, db)
    if seq_before != [{"name": "events", "seq": initial_h}]:
        raise RuntimeError(
            f"Seeding unexpectedly changed allocator context: {db.name}, {seq_before}")
    if before["rows"] or before["count"] != [{"n":0}]:
        raise RuntimeError(f"Initial public state mismatch: {db.name}")
    pre_bytes = db.stat().st_size
    treatment = "NO_EXTRA_WRITE"
    transaction_count = 0
    mutation_count = 0
    action_elapsed_ns = 0
    if action == "RESERVE":
        sentinel = minimum - 1
        treatment = "BEGIN; INSERT_EXPLICIT_SENTINEL; DELETE_SENTINEL; COMMIT;"
        start = time.perf_counter_ns()
        query(executable, db,
              "BEGIN; INSERT INTO events(id,note) VALUES"
              f"({sentinel},'reservation'); "
              f"DELETE FROM events WHERE id={sentinel}; COMMIT;")
        action_elapsed_ns = time.perf_counter_ns() - start
        transaction_count = 1
        mutation_count = 2
    elif action != "NOOP":
        raise RuntimeError(f"Unexpected treatment: {action}")
    seq_after = sequence(executable, db)
    after = snapshot(executable, db)
    post_bytes = db.stat().st_size
    # No future outcome is observed before checking that treatment preserved
    # the public table state and delivery was directly witnessed.
    if before != after or after["rows"] != []:
        raise RuntimeError(f"Structural action failed public-state preservation: {db.name}")
    expected_seq = max(initial_h, minimum-1) if action == "RESERVE" else initial_h
    if seq_after != [{"name": "events", "seq": expected_seq}]:
        raise RuntimeError(f"Treatment-delivery gate failed before Y: {db.name}, {seq_after}")
    future = query(executable, db, FINAL_SQL)
    return {
        "round": iteration,
        "initial_h": initial_h,
        "minimum_id": minimum,
        "action": action,
        "source_schema": "events(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)",
        "snapshot_before": before,
        "seq_before": seq_before,
        "treatment": treatment,
        "extra_write_transactions": transaction_count,
        "extra_mutation_statements": mutation_count,
        "seq_after": seq_after,
        "snapshot_after": after,
        "delivery_verified_before_future": True,
        "future_sql": FINAL_SQL,
        "future": future,
        "file_bytes_before": pre_bytes,
        "file_bytes_after": post_bytes,
        "file_size_delta": post_bytes - pre_bytes,
        "action_elapsed_ns": action_elapsed_ns,
        "independent_file_database": True,
        "fresh_sqlite_process_per_statement": True
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sqlite-bin", required=True)
    args = parser.parse_args()
    cli = pathlib.Path(args.sqlite_bin).resolve()
    if not cli.is_file():
        raise RuntimeError("Pinned sqlite3 executable missing")
    version = query(cli, ":memory:", "SELECT sqlite_version() AS version;")
    if version != [{"version": "3.46.1"}]:
        raise RuntimeError(f"Wrong SQLite runtime version: {version}")
    with tempfile.TemporaryDirectory(prefix="p31_sqlite_decision_") as name:
        workspace = pathlib.Path(name)
        outcomes = [
            trajectory(cli, workspace, iteration, h, minimum, action)
            for iteration in range(REPETITIONS)
            for minimum in THRESHOLDS
            for h in HIGH_WATERS
            for action in ACTIONS
        ]
    result = {
        "stage": "G8 LAW-R1-P31",
        "candidate": "SQLite Allocation-Threshold State-Aware Structural Policy",
        "expected_source_sha": SOURCE_SHA,
        "expected_fossil_uuid": SOURCE_FOSSIL,
        "runtime_version": version[0]["version"],
        "source_executable_sha256": hashlib.sha256(cli.read_bytes()).hexdigest(),
        "population": {
            "rounds": REPETITIONS,
            "high_water_values": list(HIGH_WATERS),
            "thresholds": list(THRESHOLDS),
            "structural_actions": list(ACTIONS),
            "trajectories": len(outcomes)
        },
        "rows": outcomes,
        "authorities": {
            "state_aware_policy_predeclared": True,
            "source_pinned_in_hosted_workflow": True,
            "mechanism_transport_established": False,
            "real_maintenance_demand": False,
            "law_r2_authorized": False,
            "p31_closed": False
        }
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
