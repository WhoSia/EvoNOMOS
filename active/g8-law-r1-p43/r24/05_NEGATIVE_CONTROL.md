# Negative control

The fixture deliberately makes an otherwise similar handler answer HEAD with 404 while the standard handler accepts HEAD. The paired oracle must report a mismatch.

This verifies sensitivity to a selected method divergence; it does not prove sensitivity to all possible contract divergences.

Positive control uses the same handler on both sides; zero mismatches are required on the finite probe list. Both controls passed locally.
