#!/usr/bin/env python3
"""R7: exhaustive finite hypergraph transversal court for explicitly declared
source edits. Real Go compiler outcomes were separately verified in R6.
This is NOT source evidence that adapters compile, nor a novel TCS theorem.
"""
import itertools,json,hashlib,sys
from pathlib import Path

def transversals(obligations, atoms, coverage):
    target=set(obligations)
    solutions=[]
    for size in range(len(atoms)+1):
        for selection in itertools.combinations(atoms,size):
            if target <= set().union(*(set(coverage[a]) for a in selection)):
                S=set(selection)
                if not any(set(old)<=S for old in solutions):
                    solutions.append(list(selection))
    return solutions

def canonical(solutions):
    return sorted([tuple(sorted(x)) for x in solutions])

def audit(case):
    U=set(case["obligations"])
    atoms=case["repair_atoms"]
    cover=case["coverage"]
    assert len(U)==len(case["obligations"])
    assert len(atoms)==len(set(atoms))
    assert set(cover)==set(atoms)
    assert all(set(v)<=U for v in cover.values())
    sols=transversals(case["obligations"],atoms,cover)
    assert canonical(sols)==canonical(case["expected_global_minimal"]),case["id"]
    restriction=transversals(case["obligations"],case["restricted_atoms"],cover)
    assert restriction
    k=min(map(len,restriction))
    assert k==case["expected_restricted_minimum"]
    for witness in sols:
        for removed in witness:
            subset=set(witness)-{removed}
            assert not U <= set().union(*(set(cover[a]) for a in subset))
    return {"case":case["id"],"obligations":case["obligations"],
      "all_inclusion_minimal_repair_sets":sols,
      "minimum_global_atom_count":min(map(len,sols)),
      "restricted_minimum":k,
      "only_declared_repair_grammar_certified":True}

def main():
    if len(sys.argv)!=3:raise SystemExit("usage audit_transversals.py manifest.json receipt.json")
    path,out=map(Path,sys.argv[1:])
    data=json.loads(path.read_text())
    assert data["protocol"]=="EVONOMOS_P42_P2_R7_TYPED_OBLIGATION_CUTSET_COURT_V1"
    assert data["status"]=="DECLARED_MODEL_BEFORE_R7_CI"
    assert {c["id"] for c in data["cases"]}=={"chi-implementor","grpc-old-bufferpool","grpc-old-codec"}
    assert data["scope"]["novel_universal_law"] is False
    checks=[audit(c) for c in data["cases"]]
    d={x["case"]:x for x in checks}
    assert d["chi-implementor"]["restricted_minimum"]==1
    assert d["grpc-old-bufferpool"]["restricted_minimum"]==2
    assert d["grpc-old-bufferpool"]["minimum_global_atom_count"]==1
    assert d["grpc-old-codec"]["restricted_minimum"]==0
    rec={"status":"P42_R7_EXHAUSTIVE_TYPED_OBLIGATION_HYPERGRAPH_CLASSICAL_TRANSVERSAL_PASS",
      "frozen_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
      "actual_original_Go_compiler_testing_done_here":False,
      "preexisting_original_R6_compiler_run":38209926838,
      "finite_instances":3,"minimality_all_subset_falsifiers_pass":True,
      "source_realizability_of_all_hypothetical_adapters_proven":False,
      "global_repair_minimum_independent_of_grammar":False,
      "new_TCS_or_OO_law":False,"LAW_R2":False,"results":checks}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
    print(rec["status"])
if __name__=="__main__":main()
