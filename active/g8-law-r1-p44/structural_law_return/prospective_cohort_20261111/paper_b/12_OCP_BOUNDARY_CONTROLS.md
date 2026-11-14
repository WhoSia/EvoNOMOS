# OCP controls with fixed reference patches

The checked-in fixture was rerun under Python 3.12.14. Four reference patches pass their 14 functional checks. Holding source and reference patch constant and changing only the protected paths flips the verdict twice. Holding the empty protected boundary constant and changing the demand never flips the verdict in this fixture. The empty-boundary cases are negative controls: demand variation need not change a verdict. All-path protection yields the demand-dependent reversal in both layouts.

This checks whether the specified patches touch protected files. It does not establish impossibility of a different patch, a human or model effect, or absence of context from any ASE item. For the real audit, a proposed question must state both demand and protection boundary, or require justified inference or abstention. Compare the scenario, actual serialized request, and judge label. The user-confirmed archive location is still unresolved. LAW-R2 HOLD.
