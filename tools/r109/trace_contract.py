"""Finite deterministic overwrite traces; not a general alias/contract solver."""
from itertools import product


def preserves(initial, writes, obligations):
    """Obligations are (time, coordinate, expected value), time 0 is initial."""
    states = [dict(initial)]
    for key, value in writes:
        states.append({**states[-1], key: value})
    return all(states[t][k] == v for t, k, v in obligations)


def last_writer(initial, writes, obligations):
    return all(next((x for q, x in reversed(writes[:t]) if q == k), initial[k]) == v
               for t, k, v in obligations)


def overlap_warning(writes, obligations):
    return any(any(q == k for q, _ in writes[:t]) for t, k, _ in obligations)


def main():
    cases = violations = false_alarms = restored = 0
    for a, b, c in product((1, 2), repeat=3):
        initial = {'x': a}
        writes = [('x', b), ('x', c)]
        for mask in (1, 2, 3):
            obs = [(t, 'x', a) for t in (1, 2) if mask & (1 << (t-1))]
            ok = preserves(initial, writes, obs)
            assert ok == last_writer(initial, writes, obs)
            assert overlap_warning(writes, obs)
            cases += 1
            violations += not ok
            false_alarms += ok
            restored += mask == 2 and b != a and c == a
    assert (cases, violations, false_alarms, restored) == (24, 14, 10, 2)
    # A write to the other coordinate is irrelevant to this observation.
    assert preserves({'x': 1, 'y': 1}, [('y', 2)], [(1, 'x', 1)])
    # Same trace can satisfy one observation policy but fail a stronger one.
    assert preserves({'x': 1}, [('x', 2), ('x', 1)], [(2, 'x', 1)])
    assert not preserves({'x': 1}, [('x', 2), ('x', 1)], [(1, 'x', 1), (2, 'x', 1)])
    print(f'{cases=}, {violations=}, {false_alarms=}, {restored=}')


if __name__ == '__main__':
    main()
