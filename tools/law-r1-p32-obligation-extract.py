#!/usr/bin/env python3
"""P32 bounded typed-obligation extractor for pinned P3 Uptime Kuma snapshots.

This is a source-anchored syntax recognizer, NOT a complete JavaScript AST
analyzer. It does not read lifecycle results or infer causal laws.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import re
import shutil
import tempfile
from pathlib import Path

UPSTREAM = "398482d590daaac0d44e288c9be3bc6f6667f8b8"
ARMS = {"DISPERSED": "dispersed", "DUAL": "dual"}
PROVIDERS = {
    "phase0": ["IssueTracker"],
    "phase1": ["NetGSM", "Mutlucell", "Verimor", "IletiMerkezi"],
}
KINDS = ("backend_import", "backend_instance", "frontend_import", "frontend_form", "ui_category")
DIRECTIONS = {"backend_import":"consumer_imports_provider", "backend_instance":"registry_constructs_provider", "frontend_import":"consumer_imports_form", "frontend_form":"registry_maps_form", "ui_category":"catalog_exposes_provider"}


class ExtractionError(ValueError):
    pass


def file_patterns(arm: str, provider: str) -> list[tuple[str, str, str]]:
    p = re.escape(provider)
    if arm == "DISPERSED":
        return [
            ("backend_import", "server/notification.js",
             rf'const {p} = require\("\./notification-providers/[^"]+"\);'),
            ("backend_instance", "server/notification.js", rf'\bnew {p}\(\)'),
            ("frontend_import", "src/components/notifications/index.js",
             rf'import {p} from "\./{p}\.vue";'),
            ("frontend_form", "src/components/notifications/index.js", rf'^\s*{p}: {p},'),
            ("ui_category", "src/components/NotificationDialog.vue", rf'^\s*{p}: "[^"]+",'),
        ]
    if arm == "DUAL":
        return [
            ("backend_import", "server/notification-providers/law-r1-p2-membership-registry.js",
             rf'const {p} = require\("\./[^"]+"\);'),
            ("backend_instance", "server/notification-providers/law-r1-p2-membership-registry.js",
             rf'\bnew {p}\(\)'),
            ("frontend_import", "src/components/notifications/law-r1-p2-membership-registry.js",
             rf'import {p} from "\./{p}\.vue";'),
            ("frontend_form", "src/components/notifications/law-r1-p2-membership-registry.js",
             rf'^\s*{p}: {p},'),
            ("ui_category", "src/components/notifications/law-r1-p2-membership-registry.js",
             rf'\b{p}: "[^"]+"'),
        ]
    raise ExtractionError(f"unknown architecture {arm}")


def locate(root: Path, arm: str, provider: str, phase: str) -> list[dict]:
    rows = []
    for kind, rel, pattern in file_patterns(arm, provider):
        path = root / rel
        if not path.is_file():
            raise ExtractionError(f"missing source {rel}")
        data = path.read_bytes()
        content = data.decode("utf-8")
        matches = list(re.finditer(pattern, content, re.MULTILINE))
        if len(matches) != 1:
            raise ExtractionError(f"ambiguous/missing {arm}/{phase}/{provider}/{kind}: {len(matches)}")
        match = matches[0]
        ln = content.count("\n", 0, match.start()) + 1
        rows.append({
            "phase": phase, "arm": arm, "provider": provider,
            "obligation_type": kind, "owner": rel,
            "direction": DIRECTIONS[kind], "source_vertex": f"module:{rel}",
            "target_vertex": f"provider:{provider}", "edge_type": kind,
            "demand": "#7316" if phase == "phase0" else "#7559",
            "source_line": ln, "source_sha256": hashlib.sha256(data).hexdigest(),
            "evidence": content.splitlines()[ln - 1].strip(),
        })
    return rows


def extract(snapshots: Path) -> dict:
    entries = []
    summaries = {}
    for phase, providers in PROVIDERS.items():
        for arm, slug in ARMS.items():
            root = snapshots / slug / phase
            if not root.is_dir():
                raise ExtractionError(f"missing phase tree: {root}")
            rows = []
            for provider in providers:
                rows += locate(root, arm, provider, phase)
            entries += rows
            # Logical classes and physical files must remain distinct coordinates.
            owners = sorted({r["owner"] for r in rows})
            by_kind = {kind: sorted({r["owner"] for r in rows if r["obligation_type"] == kind})
                       for kind in KINDS}
            summaries[f"{phase}:{arm}"] = {
                "providers": providers,
                "obligation_instances": len(rows),
                "obligation_types": len(by_kind),
                "physical_owner_files": len(owners),
                "owners": owners,
                "semantic_membership_edit_sites_from_frozen_design": 5 if arm == "DISPERSED" else 2,
                "type_to_owner": by_kind,
            }
    if len(entries) != 50:
        raise ExtractionError(f"unexpected obligation count {len(entries)}")
    return {
        "schema": "evonomos-p32-bounded-obligations-v1",
        "source_birth": UPSTREAM,
        "source_origin": "P2/P3 pinned real source materializer, bounded historical treatments",
        "method": "source-anchored line-and-SHA lexical signatures, not general AST/semantic verification",
        "outcome_blind": True,
        "historical_result_used_as_feature": False,
        "observations": entries,
        "typed_edges": [{"source": e["source_vertex"], "target": e["target_vertex"], "edge_type": e["edge_type"], "demand": e["demand"], "owner": e["owner"], "source_line": e["source_line"]} for e in entries],
        "direction_warning": "These arrows encode declarations, not demonstrated causal change propagation.",
        "summaries": summaries,
        "rival_judgment": {
            "B0": "The pre-existing site-count baseline already predicts 5 versus 2 under provider additions.",
            "B1": "No independent historical/semantic co-change rival was fitted or beaten.",
            "B2": "Parnas/DRSpaces and existing interface segregation can explain boundary relocation.",
            "H": "Ownership and typed roles are observable, but no incremental prospective discriminator exists.",
            "verdict": "NO_NEW_DISCRIMINATOR_ON_HISTORICAL_DEMANDS",
        },
        "scientific_authority": "METHOD_ONLY__P32_OPEN__LAW_R2_NOT_AUTHORIZED",
    }


def fixture(root: Path):
    contents = {
        "server/notification.js": 'const { commandExists } = require("./util-server");\n'
                                  'function registry() {\n        const list = [\n        ];\n}\n',
        "src/components/notifications/index.js": 'import Alerta from "./Alerta.vue";\n'
            'const NotificationFormList = {\n};\n',
        "src/components/NotificationDialog.vue": '<script>\nfunction category() {\n'
            '            let other = {\n                GoogleSheets: "Google Sheets",\n            };\n'
            '            let smsServices = {\n            };\n'
            '            // Sort by notification name alphabetically\n}\n</script>\n',
    }
    for rel, data in contents.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(data, encoding="utf-8")


def run_self_test(materializer: Path) -> dict:
    spec = importlib.util.spec_from_file_location("p32_p2", materializer)
    if spec is None or spec.loader is None:
        raise ExtractionError("cannot import the frozen materializer")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        birth = root / "birth"
        fixture(birth)
        for arm, slug in ARMS.items():
            for phase in PROVIDERS:
                target = root / slug / phase
                shutil.copytree(birth, target)
                mod.PROVIDERS = [x for x in mod.PROVIDERS if x[0] in PROVIDERS[phase]] if phase == "phase0" else [
                    ("IssueTracker", "issue_tracker"), ("NetGSM", "sms"),
                    ("Mutlucell", "sms"), ("Verimor", "sms"), ("IletiMerkezi", "sms")]
                # phase1 must include full materialization because P3 compares phase0->phase1.
                if arm == "DISPERSED":
                    mod.apply_dispersed(target)
                else:
                    mod.apply_dual(target)
                if phase == "phase0":
                    # Exact P3 fix removes future provider category declarations.
                    for rel in (["src/components/NotificationDialog.vue"] if arm == "DISPERSED"
                                else ["src/components/notifications/law-r1-p2-membership-registry.js"]):
                        p = target / rel
                        p.write_text("\n".join(
                            line for line in p.read_text().splitlines()
                            if not any(x in line for x in PROVIDERS["phase1"])
                        ) + "\n")
        actual = extract(root)
        assert len(actual["observations"]) == 50
        assert len(actual["typed_edges"]) == 50
        assert len(set(e["direction"] for e in actual["observations"])) == 5
        assert actual["summaries"]["phase0:DISPERSED"]["physical_owner_files"] == 3
        assert actual["summaries"]["phase1:DUAL"]["physical_owner_files"] == 2
        # Destructive mutation: one removed registration invalidates the grammar.
        victim = root / "dual/phase0/src/components/notifications/law-r1-p2-membership-registry.js"
        original = victim.read_text()
        victim.write_text(original.replace('IssueTracker: "Issue Tracker"', 'IssueTrackerMissing: "Issue Tracker"'))
        rejected = False
        try:
            extract(root)
        except ExtractionError:
            rejected = True
        assert rejected, "missing obligation was accepted"
    return {"fixture_extraction": "PASS", "source_trace_rows": 50,
            "destructive_mutation_rejection": "PASS",
            "fixture_is_synthetic": True, "fresh_world_effect": False}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshots", type=Path)
    ap.add_argument("--materializer", type=Path, default=Path("tools/law-r1-p2-materialize.py"))
    ap.add_argument("--out", type=Path)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        result = run_self_test(args.materializer)
    else:
        if args.snapshots is None:
            ap.error("--snapshots is required unless --self-test")
        result = extract(args.snapshots)
    txt = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(txt)
    else:
        print(txt)


if __name__ == "__main__":
    main()
