"""P40-P3 exact conditional architectural evolvability for three Go rivals.

All eight context flags are explicit premises, not observed maintainer rights.
Safe source states are independently established by Go P3 compiler checker.
BFS explores *actual edit grammar*; theorem is an independent Boolean formula.
"""
from collections import Counter, deque
from itertools import product

ARCHES = ("coupled", "direct", "versioned_adapter")


def safe(arch, legacy, t, x, f):
    if arch == "coupled" and t and (not x or legacy):
        return False
    if f and not (t and x):
        return False
    return True


def reachable(arch, context):
    publish, factory, mutable_fast, add_wrapper, legacy, nominal, t_first, atomic = context
    permitted_x = add_wrapper if arch == "versioned_adapter" else mutable_fast
    if not safe(arch, legacy, 0, 0, 0):
        return False
    discovered = {(0, 0, 0)}
    queue = deque(discovered)
    while queue:
        t, x, f = queue.popleft()
        if (t, x, f) == (1, 1, 1) and not (nominal and arch == "versioned_adapter"):
            return True
        options = []
        if not t and publish:
            options.append((1, x, f))
        if not x and permitted_x and (t or not t_first):
            options.append((t, 1, f))
        if not f and factory:
            options.append((t, x, 1))
        # An atomic source update is a DISTINCT permitted operation;
        # it still requires both affected edit owners' authorization.
        if not t and not x and not f and atomic and publish and permitted_x:
            options.append((1, 1, 0))
        for dst in options:
            if dst not in discovered and safe(arch, legacy, *dst):
                discovered.add(dst)
                queue.append(dst)
    return False


def theorem(arch, context):
    publish, factory, mutable_fast, add_wrapper, legacy, nominal, t_first, atomic = context
    common = bool(publish and factory)
    if arch == "coupled":
        return common and mutable_fast and not legacy and (not t_first or atomic)
    if arch == "direct":
        return common and mutable_fast
    return common and add_wrapper and not nominal


def main():
    profiles = Counter()
    for context in product((False, True), repeat=8):
        answers = []
        for arch in ARCHES:
            observed = reachable(arch, context)
            calculated = theorem(arch, context)
            assert observed == calculated, (arch, context, observed, calculated)
            answers.append(observed)
        profiles[tuple(answers)] += 1
    assert sum(profiles.values()) == 256
    assert dict(profiles) == {
        (False, False, False): 216,
        (False, False, True): 8,
        (False, True, False): 15,
        (False, True, True): 5,
        (True, True, False): 9,
        (True, True, True): 3,
    }, profiles
    for row in sorted(profiles):
        print("P40_P3_256_OWNER_CONTEXTS signature=" +
              str(tuple(int(v) for v in row)) + " count=" + str(profiles[row]))
    print("P40_P3_768_ARCHITECTURE_CONTEXT_BFS_FORMULA_AGREE PASS")
    witnesses = {
        "only_direct": ((1,1,1,0,1,0,0,0), (0,1,0)),
        "only_wrapper": ((1,1,0,1,1,0,0,0), (0,0,1)),
        "both_structural": ((1,1,1,1,1,0,0,0), (0,1,1)),
        "nominal_disqualifies_wrapper": ((1,1,1,1,1,1,0,0), (0,1,0)),
        "coupled_T_first_blocked": ((1,1,1,0,0,0,1,0), (0,1,0)),
        "coupled_T_first_atomic_restores": ((1,1,1,0,0,0,1,1), (1,1,0)),
        "legacy_blocks_even_atomic": ((1,1,1,0,1,0,1,1), (0,1,0)),
    }
    for name, (bits, expected) in witnesses.items():
        actual = tuple(int(reachable(a, tuple(bool(b) for b in bits))) for a in ARCHES)
        assert actual == expected, (name, actual, expected)
        print(f"P40_P3_REVERSAL_WITNESS {name} coupled_direct_wrapper={actual} PASS")
    print("P40_P3_PERMISSION_CUT_FORMULA_AND_CONTEXT_DEPENDENT_REVERSAL_PASS")


if __name__ == "__main__":
    main()
