from itertools import product
from collections import defaultdict

def menu(a, o):
    return len({x ^ y for x, y in zip(a, o)})

groups = defaultdict(set)
for a in product(range(2), repeat=4):
    for o in product(range(2), repeat=4):
        groups[a, sum(o)].add(menu(a, o))
a = (0, 0, 1, 1)
x = (0, 0, 1, 1)
y = (0, 1, 0, 1)
assert sum(x) == sum(y)
assert (menu(a, x), menu(a, y)) == (1, 2)
assert len(groups) == 80
assert sum(len(v) > 1 for v in groups.values()) == 22
print('R98 incidence: PASS, 256 assignments, 80 classes, 22 ambiguous')
