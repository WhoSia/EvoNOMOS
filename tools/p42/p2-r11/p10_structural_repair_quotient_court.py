#!/usr/bin/env python3
"""P42 R11-P10 finite source/rights repair-quotient court (standard Python only).

Mathematical object is a classical cost-labelled transition system, NOT a
sound abstraction of arbitrary Go source. Native original-client receipts
are checked separately. This file tests finite logical obligations and
deliberate failing abstractions; nothing in it creates a new SOLID law.
"""
from collections import defaultdict
from dataclasses import dataclass
from itertools import product
import argparse
import json
from pathlib import Path


@dataclass(frozen=True)
class State:
    flush: int
    right_to_edit: int
    irrelevant_tag: int


STATES = tuple(State(*parts) for parts in product((0, 1), repeat=3))


def enabled_steps(s):
    # Actions/rights are primitive facts, not inferred from successful repairs.
    if s.right_to_edit and not s.flush:
        yield ("add_optional_Flush", (1, 1), State(1, s.right_to_edit, s.irrelevant_tag))
    if s.right_to_edit and s.flush:
        yield ("remove_optional_Flush", (1, 1), State(0, s.right_to_edit, s.irrelevant_tag))


def old_clients_good(s):
    # All source states share old HTTP 200/body, independently of Flush.
    return True


def goal(s, demand):
    if demand == "needs_Flush":
        return bool(s.flush)
    if demand == "must_not_expose_Flush":
        return not s.flush
    raise ValueError(demand)


def pareto(costs):
    return sorted({tuple(c) for c in costs if not any(
        all(y <= x for x, y in zip(c, other)) and
        any(y < x for x, y in zip(c, other))
        for other in costs)}, key=lambda x: x)


def frontier(start, demand):
    # Nonnegative edit costs: Pareto-minimal paths need no state cycles.
    found = []
    def visit(state, cost, visited):
        if not old_clients_good(state):
            return
        if goal(state, demand):
            found.append(cost)
        for name, stepcost, nxt in enabled_steps(state):
            if nxt not in visited:
                visit(nxt, tuple(a+b for a,b in zip(cost, stepcost)), visited | {nxt})
    visit(start, (0,0), {start})
    return pareto(found)


def is_cost_labelled_bisimulation(quotient):
    blocks = defaultdict(list)
    for s in STATES:
        blocks[quotient(s)].append(s)
    for fiber in blocks.values():
        for s,t in product(fiber,repeat=2):
            if old_clients_good(s) != old_clients_good(t):
                return False
            for demand in ("needs_Flush", "must_not_expose_Flush"):
                if goal(s,demand) != goal(t,demand):
                    return False
            # Exact action label, edit+review cost and successor equivalence.
            left = {(name,cost,quotient(nxt)) for name,cost,nxt in enabled_steps(s)}
            right = {(name,cost,quotient(nxt)) for name,cost,nxt in enabled_steps(t)}
            if left != right:
                return False
    return True


def check_five_fragments():
    # SRP: two disjoint responsibility changes commute; other observer intact.
    for a,b in product((0,1),repeat=2):
        e1=lambda x:(1,x[1])
        e2=lambda x:(x[0],1)
        assert e1(e2((a,b))) == e2(e1((a,b)))
        assert e1((a,b))[1] == b and e2((a,b))[0] == a
    # OCP: source core is fixed and a new independently specified demand
    # is fulfilled by an authorized extension-only edit.
    core,extension,authorized=42,0,True
    assert authorized and extension==0
    nxt=(core,1)
    assert nxt[0]==core and nxt[1]==1
    # LSP: a source-level subtype declaration does not guarantee refinement.
    # Only trace containment under stated client contexts suffices.
    original_trace_set={("OK",)}
    substitution_good={("OK",)}
    substitution_bad={("OK",),("PANIC",)}
    assert substitution_good.issubset(original_trace_set)
    assert not substitution_bad.issubset(original_trace_set)
    # ISP: a client only observing capability1 is frame-insensitive to
    # source changes strictly on capability2, under independence premises.
    for cap1,cap2 in product((0,1),repeat=2):
        assert (cap1,cap2)[0] == (cap1,1-cap2)[0]
    # DIP: dependency only through a stable port cannot observe provider ID;
    # all provider variants must meet the same *source-checked* port traces.
    for provider in ("concrete_A","concrete_B"):
        port_output={"concrete_A":"contract_42","concrete_B":"contract_42"}[provider]
        assert port_output=="contract_42"
    return True


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--gin-log")
    parser.add_argument("--echo-log")
    parser.add_argument("--out",default="out/p42-r11-p10/p10-repair-quotient-court.json")
    a=parser.parse_args()
    q_http=lambda s:("200","old")
    q_without_rights=lambda s:("200","old",s.flush)
    q_complete=lambda s:("200","old",s.flush,s.right_to_edit)
    # Hidden irrelevant_tag is genuinely quotiented by complete certificate.
    assert not is_cost_labelled_bisimulation(q_http)
    assert not is_cost_labelled_bisimulation(q_without_rights)
    assert is_cost_labelled_bisimulation(q_complete)
    for s,t in product(STATES,repeat=2):
        if q_complete(s)==q_complete(t):
            for d in ("needs_Flush","must_not_expose_Flush"):
                assert frontier(s,d)==frontier(t,d)
    # Actual obstruction: old-HTTP-equivalent starts have different repair
    # frontiers for an independent new optional-capability demand.
    has=State(1,1,0)
    missing=State(0,1,0)
    forbidden=State(0,0,0)
    assert q_http(has)==q_http(missing)==q_http(forbidden)
    assert frontier(has,"needs_Flush")==[(0,0)]
    assert frontier(missing,"needs_Flush")==[(1,1)]
    assert frontier(forbidden,"needs_Flush")==[]
    assert check_five_fragments()
    # Every capability mask can be distinguished by an old client asserting
    # exactly one of k optional interfaces. Thus a fixed dynamic method-set
    # type cannot represent all realized 2**k signatures without loss.
    signatures={k:len(set(product((0,1),repeat=k))) for k in range(1,5)}
    assert signatures=={1:2,2:4,3:8,4:16}
    native={}
    if bool(a.gin_log)!=bool(a.echo_log):
        parser.error("supply both native logs or neither")
    if a.gin_log:
        gin=Path(a.gin_log).read_text()
        echo=Path(a.echo_log).read_text()
        assert "GIN_P10_NATIVE: oldGET=200/old, noFlush=NO_PANIC, flushSupported=NO_PANIC" in gin
        assert "ECHO_P10_NATIVE: oldGET=200/old, noFlush=PANIC, flushSupported=NO_PANIC" in echo
        assert "--- PASS:" in gin and "--- PASS:" in echo
        native={"gin":"PASS","echo":"PASS","comparative_clients":"source-conditioned demand reversal"}
    output={
        "verdict":"P10_BOUNDED_CLASSICAL_REPAIR_QUOTIENT_AND_CONDITIONAL_FIVE_FRAGMENTS_PASS",
        "full_context_repair_quotient":True,
        "http_only_quotient":False,
        "capability_without_edit_rights":False,
        "frontiers":{"has_capability":frontier(has,"needs_Flush"),
                     "may_edit_to_gain":frontier(missing,"needs_Flush"),
                     "no_edit_right":frontier(forbidden,"needs_Flush")},
        "finite_conditional_solid_fragments":check_five_fragments(),
        "minimal_distinct_method_set_signatures":signatures,
        "native":native,
        "novel_universal_law":"NOT_ESTABLISHED",
        "limits":"Full source/rights extraction, genuine maintenance costs and equal-information competitor novelty not proved",
        "stage":"P42 RUNNING; R11-P10-P0; P43 HOLD; LAW-R2 NOT_AUTHORIZED"
    }
    destination=Path(a.out)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(output["verdict"])
    print(json.dumps(output["frontiers"],sort_keys=True))
    print("CLASSICAL_NOVELTY_NOT_CLAIMED")


if __name__=="__main__":
    main()
