"""P40-MATH-B finite synthetic continuation-congruence checker.
A model calibrated to P40-P4 chi middleware staging, NOT a new native Go run.
No formal verification of the general mathematical theorem is claimed.
"""
from itertools import product

ALPHABET = ("U", "M")
SINK = "invalid"
STATES = ("00", "U", "M", "UM", SINK)
NEXT = {("00", "U"): "U", ("00", "M"): "M", ("U", "M"): "UM"}


def step(state, edit):
    return NEXT.get((state, edit), SINK)


def output(state, regime):
    goal = int(state == "UM")
    if regime == "goal_only":
        return (goal,)
    if regime == "compile_plus_goal":
        return (int(state != SINK), goal)
    raise ValueError(regime)


def words(maxlen):
    for k in range(maxlen + 1):
        yield from product(ALPHABET, repeat=k)


def after(state, word):
    for edit in word:
        state = step(state, edit)
    return state


def suffix_equivalent(a, b, regime, maxlen=6):
    return all(output(after(a, word), regime) == output(after(b, word), regime)
               for word in words(maxlen))


def minimal_classes(regime):
    initial = {s: output(s, regime) for s in STATES}
    labels = sorted(set(initial.values()))
    classes = {s: labels.index(initial[s]) for s in STATES}
    while True:
        signatures = {s: (output(s, regime),
                          tuple(classes[step(s, e)] for e in ALPHABET))
                      for s in STATES}
        distinct = sorted(set(signatures.values()))
        new = {s: distinct.index(signatures[s]) for s in STATES}
        # Equality of induced partitions, not arbitrary class label numbers.
        stable = all((classes[s] == classes[t]) == (new[s] == new[t])
                     for s in STATES for t in STATES)
        classes = new
        if stable:
            break
    for s, t in product(STATES, repeat=2):
        same = classes[s] == classes[t]
        assert same == suffix_equivalent(s, t, regime)
        if same:
            assert all(classes[step(s, e)] == classes[step(t, e)]
                       for e in ALPHABET)
    groups = {}
    for s, c in classes.items():
        groups.setdefault(c, []).append(s)
    return sorted((tuple(g) for g in groups.values()), key=str)


def main():
    assert after("00", ("U", "M")) == "UM"
    assert after("00", ("M", "U")) == SINK
    assert after("00", ("M",)) == "M"
    assert after("00", ("U",)) == "U"
    goal = minimal_classes("goal_only")
    full = minimal_classes("compile_plus_goal")
    assert len(goal) == 4 and ("M", SINK) in goal, goal
    assert len(full) == 5, full

    # Two distinct permission histories can lead to the SAME source text.
    histories = {("same_source", "allow"), ("same_source", "deny")}
    assert len({src for src, _ in histories}) == 1
    assert len({permission == "allow" for _, permission in histories}) == 2
    print("P40_MATH_B_ORDERED_SOURCE_GUARD U,M=ACCEPT M,U=REJECT PASS")
    print("P40_MATH_B_GOAL_ONLY_MINIMAL_CONTINUATION_CLASSES=4 PASS", goal)
    print("P40_MATH_B_COMPILE_AND_GOAL_MINIMAL_CONTINUATION_CLASSES=5 PASS", full)
    print("P40_MATH_B_SOURCE_ONLY_NONMARKOV_HISTORY_WITNESS PASS")
    print("P40_MATH_B_FINITE_SYNTHETIC_COURT_PASS")


if __name__ == "__main__":
    main()
