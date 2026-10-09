"""P37 E4 independently evolved session algorithms: capability-indexed edit graph.

Original source API identities were inspected before modelling:
Gorilla CookieStore.New uses securecookie.DecodeMulti (client-state cookie);
SCS SessionManager.Load finds server-stored session under opaque token.
This is a bounded OWNER/INTERFACE model, not an enumeration of all source edits.
"""
from collections import deque
from itertools import product

G, S = "gorilla", "scs"
RG, RD, RS = "gorilla_only", "dual", "scs_only"
OLD, EXPIRED = True, False


def decode(reader, encoded_as, key_g, matching_store_s):
    if reader == RG:
        return bool(key_g) and encoded_as == G
    if reader == RS:
        return bool(matching_store_s) and encoded_as == S
    if reader == RD:
        return (bool(key_g) and encoded_as == G) or (bool(matching_store_s) and encoded_as == S)
    raise ValueError(reader)


def invariant(state, key_g, matching_store_s):
    issuer, reader, legacy_duty = state
    live = decode(reader, issuer, key_g, matching_store_s)
    legacy = (not legacy_duty) or decode(reader, G, key_g, matching_store_s)
    return live and legacy


def enabled(state, key_g, matching_store_s, bridge=True, duty_expiry=True):
    issuer, reader, duty = state
    actions = []
    if issuer == G:
        actions.append(("A_issuer_change", (S, reader, duty)))
    if reader == RG:
        actions.append(("B_direct_replace", (issuer, RS, duty)))
        if bridge:
            actions.append(("B_authorized_dual_reader", (issuer, RD, duty)))
    if reader == RD:
        actions.append(("B_remove_legacy_reader", (issuer, RS, duty)))
    if duty and duty_expiry:
        actions.append(("EXTERNAL_expire_legacy_obligation", (issuer, reader, EXPIRED)))
    return [(name, target) for name, target in actions if invariant(target, key_g, matching_store_s)]


def find(start, goal, key_g, matching_store_s, bridge=True, duty_expiry=True):
    if not invariant(start, key_g, matching_store_s):
        return None
    seen = {start}
    todo = deque([(start, [])])
    while todo:
        s, path = todo.popleft()
        if s == goal:
            return path
        for label, target in enabled(s, key_g, matching_store_s, bridge, duty_expiry):
            if target not in seen:
                seen.add(target)
                todo.append((target, path + [(label, target)]))
    return None


def run():
    start = (G, RG, OLD)
    target = (S, RS, EXPIRED)
    # Source-semantics-derived observable matrix under explicit capabilities.
    assert decode(RG, G, True, True) and not decode(RG, S, True, True)
    assert not decode(RS, G, True, True) and decode(RS, S, True, True)
    assert decode(RD, G, True, True) and decode(RD, S, True, True)
    assert not decode(RD, G, False, True) and decode(RD, S, False, True)
    assert decode(RD, G, True, False) and not decode(RD, S, True, False)
    assert find(start, target, True, True, bridge=False) is None
    assert find(start, target, True, True, duty_expiry=False) is None
    p = find(start, target, True, True)
    assert p is not None
    assert [x[0] for x in p] == [
        "B_authorized_dual_reader",
        "A_issuer_change",
        "EXTERNAL_expire_legacy_obligation",
        "B_remove_legacy_reader",
    ], p
    assert all(invariant(state, True, True) for _, state in p)
    # The old key or SCS store is an essential capability for THIS grammar,
    # not a proof about all possible migration architectures.
    for key_g, matching_store_s in product((False,True),repeat=2):
        reachable = find(start, target, key_g, matching_store_s) is not None
        assert reachable == (key_g and matching_store_s)
    # Current semantic observation is deliberately equal, while context
    # supplied only with a particular permitted decoder separates protocols.
    assert decode(RD,G,True,True) == decode(RD,S,True,True)
    assert decode(RG,G,True,True) != decode(RG,S,True,True)
    assert decode(RS,G,True,True) != decode(RS,S,True,True)
    print("P37_E4_CAPABILITY_MATRIX_ALL_FIVE_SOURCE_SIGNATURES_PASS")
    print("P37_E4_NO_DIRECT_OWNER_SEQUENTIAL_REPAIR_PASS")
    print("P37_E4_BRIDGE_FOUR_TRANSITIONS_WITH_EXPLICIT_LEGACY_EXPIRY_PASS")
    print("P37_E4_BOTH_OWNER_CAPABILITIES_NEEDED_FOR_THIS_GAMMA_PASS")
    print("P37_E4_PRESENT_EQUIVALENCE_NOT_FUTURE_CONTEXT_CONGRUENCE_PASS")
    print("P37_E4_PATH="+repr(p))
    print("CLASSICAL_CONTEXTUAL_AND_PRODUCT_GRAPH_THEORY_PREDICTS_ALL")
if __name__=="__main__":
    run()
