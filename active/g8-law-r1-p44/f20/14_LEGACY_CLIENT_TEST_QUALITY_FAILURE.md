# F20 B — distinguish tests, contract semantics and historical false confidence

Chi's original prepatch `TestMuxFind` has at least two faulty comparator directions in its assertions; the published fix changes `==` to `!=` for positive search match and `==` to `!=` for negative wrong-method check, alongside genuine code change and more nested coverage. Therefore a passing original upstream test at baseline is not an exhaustive safety proof. A posthoc test must be registered as new retrospective oracle.

Httprouter tests ordinary OPTIONS operation and makes no guaranteed coverage claim for disabled HandleOPTIONS; one targeted flag check changes the protected output observation.

Gin's original post patch adds a new panic-message test and unrelated lint workflow update. A green baseline test does not imply no change in panic quality for invalid wildcard cases.

Three client-observer types must be treated distinctly: (chi) router pattern string under method/path, (httprouter) allowed methods under config and request method/path, (gin) error message under invalid registration. A generic 'HTTP works' boolean is under-specified. Do not apply F17 alias structure findings to these without source-level evidence.
