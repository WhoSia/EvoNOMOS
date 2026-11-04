# Prefix-safety countermodel

Consider symbolic configurations s, u and g. Initial s and final g satisfy old clients; intermediate u does not.

Transitions: s -> u (cost 1), u -> g (cost 1), s -> g (cost 4). All edits authorized under the broad permission set.

A final-state-only shortest-path calculation reports cost 2. A pathwise protected-contract calculation must reject both edges through u and returns cost 4.

Removing permission for the direct edit leaves no admissible safe repair although the final desired source g remains syntactically expressible.

This countermodel was encoded in Go and tested locally (PASS). It establishes a definitional distinction, not an empirical fact about arbitrary Go revisions. Historical P42 source evidence must not be reclassified as this newly constructed model.
