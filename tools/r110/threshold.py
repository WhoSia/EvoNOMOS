"""Restricted shared-backing model: first buffer live, later copies released.
All requests pooled and positive-sized, samples after each copy, failure sticky.
"""
from itertools import product


def execution(high, word):
    attached, failed = True, False
    for size, differs in word:
        if size > high:
            high, attached = size, False
        elif attached and differs:
            failed = True
    return failed


def threshold(word):
    largest = 0
    for size, differs in word:
        largest = max(largest, size)
        if differs:
            return largest
    return None


def check():
    count = 0
    for m in (3, 5):
        alphabet = list(product(range(1, m+1), (False, True)))
        signatures = set()
        for length in range(5):
            for word in product(alphabet, repeat=length):
                q = threshold(word)
                sig = tuple(execution(h, word) for h in range(1, m+1))
                assert sig == tuple(q is not None and h >= q for h in range(1, m+1))
                signatures.add(sig)
                count += m
        # A distinct threshold between each adjacent pair is necessary and sufficient.
        useful = [s for s in signatures if any(s) and not all(s)]
        assert len(useful) == m-1
        for i in range(m-1):
            assert sum(s[i] != s[i+1] for s in useful) == 1
        assert len({tuple(s[i] for s in useful) for i in range(m)}) == m
        print(f'levels={m} distinct_signatures={len(signatures)} minimum_nonadaptive_reset_probes={len(useful)}')
    print(f'word_state_checks={count}')


if __name__ == '__main__':
    check()
