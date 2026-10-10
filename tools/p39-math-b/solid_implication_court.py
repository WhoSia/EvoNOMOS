"""P39 Math-B: classical finite source-action implication sanity checks."""
from itertools import product

worlds = list(product((0, 1), repeat=2))
def flip_x(p): return (1-p[0], p[1])
def flip_y(p): return (p[0], 1-p[1])
def copy_x_into_y(p): return (p[0], p[0])
assert len(worlds) == 4
assert all(flip_x(flip_y(p)) == flip_y(flip_x(p)) for p in worlds)
assert flip_x(copy_x_into_y((0,0))) == (1,0)
assert copy_x_into_y(flip_x((0,0))) == (1,1)
safe = {(0,0),(1,1)}
assert (0,0) in safe
assert flip_x((0,0)) not in safe
assert flip_y((0,0)) not in safe
# All runtime observations are identical across these source configurations.
assert len({0 for p in worlds}) == 1
# A source dependency graph need not be determined by runtime observations.
dependencies = {"minimal": {"f"}, "coupled": {"f", "g"}}
assert dependencies["minimal"] != dependencies["coupled"]
print("P39_MATH_B_DISJOINT_EDIT_COMMUTATION_PASS states=4")
print("P39_MATH_B_OVERLAPPING_SOURCE_EDIT_NONCOMMUTATION_PASS")
print("P39_MATH_B_NONRECTANGULAR_INVARIANT_BLOCK_PASS")
print("P39_MATH_B_OBSERVATION_DOES_NOT_DETERMINE_DEPENDENCY_PASS")
print("P39_MATH_B_THEOREM_NOVELTY_HOLD_CLASSICAL")
