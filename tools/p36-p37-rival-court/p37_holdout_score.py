#!/usr/bin/env python3
"""P37 prospective H_G vs strong-classical B* holdout court.

This is a deterministic SCORING PROGRAM, not an observed law and not a
model that computes either prediction. Prediction files must be frozen
before repair outcomes. A CSV supplied by an evaluator contains only
episodes unseen by the models during fitting.

Columns: repo_id, episode_id, domain, split, outcome, p_classical, p_geometry
All tests/sources can remain outside the Python runtime.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path

COLUMNS = ("repo_id", "episode_id", "domain", "split", "outcome", "p_classical", "p_geometry")
MIN_EPISODES = 20
MIN_REPOS = 6
MIN_DOMAINS = 3
MIN_REPOS_PER_DOMAIN = 2
MARGIN_NATS_PER_EPISODE = 0.05
BOOTSTRAP_RESAMPLES = 2000
SEED = 37


def safe_logloss(y: int, p: float) -> float:
    """Proper binary log score. p must be strictly within (0,1)."""
    if y not in (0, 1) or not (0.0 < p < 1.0):
        raise ValueError("outcome and probability outside strict valid range")
    return -(y * math.log(p) + (1 - y) * math.log1p(-p))


def load_holdout(path: Path) -> list[dict[str, object]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or tuple(reader.fieldnames) != COLUMNS:
            raise ValueError(f"exact schema expected: {COLUMNS!r}")
        out: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()
        for line, row in enumerate(reader, start=2):
            if any(row[k] is None or not row[k].strip() for k in COLUMNS):
                raise ValueError(f"line {line}: missing field")
            if row["split"] != "holdout":
                raise ValueError(f"line {line}: training or other split forbidden in holdout court")
            key = (row["repo_id"], row["episode_id"])
            if key in seen:
                raise ValueError(f"line {line}: duplicate episode {key}")
            seen.add(key)
            if row["outcome"] not in ("0", "1"):
                raise ValueError(f"line {line}: outcome must be 0 or 1")
            try:
                pc, pg = float(row["p_classical"]), float(row["p_geometry"])
            except ValueError as err:
                raise ValueError(f"line {line}: malformed prediction") from err
            if not (math.isfinite(pc) and math.isfinite(pg) and 0 < pc < 1 and 0 < pg < 1):
                raise ValueError(f"line {line}: predictions must be finite and in (0,1)")
            y = int(row["outcome"])
            out.append({
                "repo_id": row["repo_id"],
                "domain": row["domain"],
                "episode_id": row["episode_id"],
                "delta": safe_logloss(y, pc) - safe_logloss(y, pg),
            })
    return out


def judge(path: Path) -> dict[str, object]:
    rows = load_holdout(path)
    grouped: dict[str, list[float]] = defaultdict(list)
    domains: dict[str, set[str]] = defaultdict(set)
    repo_domain: dict[str, str] = {}
    for row in rows:
        repo = str(row["repo_id"])
        domain = str(row["domain"])
        if repo in repo_domain and repo_domain[repo] != domain:
            raise ValueError("one repository cannot span multiple domains")
        repo_domain[repo] = domain
        grouped[repo].append(float(row["delta"]))
        domains[domain].add(repo)
    if len(rows) < MIN_EPISODES:
        raise ValueError(f"too few holdout episodes: {len(rows)} < {MIN_EPISODES}")
    if len(grouped) < MIN_REPOS:
        raise ValueError(f"too few independent repos: {len(grouped)} < {MIN_REPOS}")
    if len(domains) < MIN_DOMAINS:
        raise ValueError(f"too few domains: {len(domains)} < {MIN_DOMAINS}")
    if any(len(repos) < MIN_REPOS_PER_DOMAIN for repos in domains.values()):
        raise ValueError("each represented domain must have at least two independent repos")

    # Equal weight per repository prevents a large project's many changes
    # from dominating the primary source-independent holdout score.
    per_repo = [sum(scores) / len(scores) for repo, scores in sorted(grouped.items())]
    mean_delta = sum(per_repo) / len(per_repo)
    rng = random.Random(SEED)
    boot = []
    for _ in range(BOOTSTRAP_RESAMPLES):
        group_sample = [per_repo[rng.randrange(len(per_repo))] for _ in per_repo]
        boot.append(sum(group_sample) / len(group_sample))
    boot.sort()
    low = boot[int(0.025 * BOOTSTRAP_RESAMPLES)]
    high = boot[int(0.975 * BOOTSTRAP_RESAMPLES)]
    # Experimental feature-prediction success, not a new universal law.
    passes = mean_delta >= MARGIN_NATS_PER_EPISODE and low > 0
    return {
        "court": "P37_NAME_PROPOSED_ONLY_STRONG_RIVAL_HOLDOUT_V1",
        "n_episodes": len(rows),
        "n_repositories": len(grouped),
        "n_domains": len(domains),
        "mean_repo_balanced_logloss_gain_nats": round(mean_delta, 9),
        "cluster_bootstrap_95pct_interval_nats": [round(low, 9), round(high, 9)],
        "minimum_gain_nats": MARGIN_NATS_PER_EPISODE,
        "bootstrap_seed": SEED,
        "bootstrap_repetitions": BOOTSTRAP_RESAMPLES,
        "prediction_feature_test": "PASS_INCREMENTAL_GAIN" if passes else "HOLD_NO_GAIN",
        "scientific_law_status": "DIP49_IDENTIFICATION_HOLD",
        "law_r2": "NOT_AUTHORIZED",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("holdout_csv", type=Path)
    args = ap.parse_args()
    print(json.dumps(judge(args.holdout_csv), ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
