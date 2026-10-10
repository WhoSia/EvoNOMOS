"""P39 MATH-D exact classical residual-state complexity court.

Synthetic finite language: a_i,b_i are one-shot source edits; q_i is a
future owner-certification edit, accepted only after ALL base edits if
a_i preceded b_i. All histories then have identical fully patched source.
No native Go or evidence of actual owner policy is claimed.
"""
from itertools import permutations
from collections import deque, defaultdict
from math import factorial

ACCEPT = -1
DEAD = -2


def step(state, letter, k):
    if state in (ACCEPT, DEAD):
        return DEAD
    kind, i = letter
    if kind in ("a", "b"):
        val = state[i]
        if kind == "a" and val == 0:
            result = 1
        elif kind == "b" and val == 0:
            result = 2
        elif kind == "b" and val == 1:
            result = 3
        elif kind == "a" and val == 2:
            result = 4
        else:
            return DEAD
        out = list(state)
        out[i] = result
        return tuple(out)
    if all(v in (3, 4) for v in state) and state[i] == 3:
        return ACCEPT
    return DEAD


def build(k):
    alphabet = [(tag, i) for i in range(k) for tag in ("a", "b", "q")]
    initial = (0,) * k
    seen = {initial}
    pending = deque([initial])
    while pending:
        state = pending.popleft()
        for label in alphabet:
            nxt = step(state, label, k)
            if nxt not in seen:
                seen.add(nxt)
                pending.append(nxt)
    return alphabet, seen, initial


def minimize_independently(k, alphabet, states):
    """DFA partition refinement (not a predicted 5**k formula)."""
    classes = {s: int(s == ACCEPT) for s in states}
    rounds = 0
    while True:
        sig = {
            s: (
                int(s == ACCEPT),
                tuple(classes[step(s, c, k)] for c in alphabet)
            ) for s in states
        }
        sig_ids = {x: i for i, x in enumerate(sorted(set(sig.values())))}
        new = {s: sig_ids[sig[s]] for s in states}
        old_parts = {frozenset(s for s in states if classes[s] == j)
                     for j in set(classes.values())}
        new_parts = {frozenset(s for s in states if new[s] == j)
                     for j in set(new.values())}
        rounds += 1
        if old_parts == new_parts:
            return new, rounds
        classes = new


def main():
    for k in range(1, 5):
        alphabet, states, initial = build(k)
        assert len(states) == 5**k + 2
        classes, iterations = minimize_independently(k, alphabet, states)
        predicted = 5**k - 2**k + 2
        assert len(set(classes.values())) == predicted

        dead_profiles = [
            s for s in states if isinstance(s, tuple)
            and all(v in (2, 4) for v in s)
        ]
        assert len(dead_profiles) == 2**k
        assert len({classes[s] for s in dead_profiles + [DEAD]}) == 1

        full = [
            s for s in states if isinstance(s, tuple)
            and all(v in (3, 4) for v in s)
        ]
        assert len(full) == 2**k
        assert len({classes[s] for s in full}) == 2**k

        for ii, x in enumerate(full):
            for y in full[ii + 1:]:
                assert any(
                    (step(x, ("q", j), k) == ACCEPT)
                    != (step(y, ("q", j), k) == ACCEPT)
                    for j in range(k)
                )

        # Exhaustive ORIGINAL synthetic edit orders, not source code runs.
        counts = defaultdict(int)
        letters = [("a", i) for i in range(k)]
        letters += [("b", i) for i in range(k)]
        for order in permutations(letters):
            state = initial
            for letter in order:
                state = step(state, letter, k)
            assert state in full
            profile = tuple(int(v == 3) for v in state)
            counts[profile] += 1

        assert len(counts) == 2**k
        assert set(counts.values()) == {factorial(2 * k) // 2**k}
        print(
            f"P39_MATH_D_EXACT_MIN_DFA k={k} "
            f"patch_histories={factorial(2*k)} "
            f"same_source_profiles={2**k} "
            f"minimal_total_dfa={predicted} "
            f"refinement_rounds={iterations} PASS"
        )

    # Unbounded monitor: prefixes inc^m and inc^n are separated
    # by continuation dec^m approve; thus infinite residual classes.
    for m in range(10):
        for n in range(10):
            balance = n
            valid = True
            for _ in range(m):
                balance -= 1
                if balance < 0:
                    valid = False
            accept = valid and balance == 0
            assert accept == (m == n)

    print("P39_MATH_D_UNBOUNDED_OBLIGATION_COUNTER_DISTINGUISHERS_PASS pairs=100")
    print("P39_MATH_D_2POWERK_FIBER_HISTORY_MEMORY_SHARP_CLASSICAL")
    print("P39_MATH_D_TRACE_DIAMOND_FAIL_SOURCE_COMMUTATION_ONLY")
    print("P39_MATH_D_NO_ORIGINAL_GO_NO_NOVEL_MATH_CLAIM")


if __name__ == "__main__":
    main()
