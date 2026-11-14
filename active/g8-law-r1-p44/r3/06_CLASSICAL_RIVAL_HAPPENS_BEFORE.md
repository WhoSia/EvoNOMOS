# Strong conventional rival: alias plus happens-before

Event graph fixed by barrier:
C_A = middleware Capture of first GET A;
W_B = POST B commits mutation v2;
R_A = handler A reads captured View;
C_C = later GET C captures v2.

Order C_A < W_B < R_A < C_C.
- LiveAlias stores a pointer p to mutable Shared. Therefore R_A performs a fresh synchronized read after W_B and returns v2.
- FrozenValue copies v1 at C_A into a request-local string. Therefore R_A returns v1 even after W_B.
- Both return v2 for C_C and both pass O0.

Conventional alias/happens-before analysis predicts this before executing original source. The Go AST source reader independently confirms a pointer field, a snapshot assignment, context injection, mutex and original middleware call; AST syntax alone does NOT certify full read/write semantics.

EAC only packages observer/rights/provenance and a safe repair-path gate here. No novel performance gain or law promotion allowed.
