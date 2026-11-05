# F20 B — Gin original source patch audit (AFTER prepatch seal)

Original https://github.com/gin-gonic/gin/commit/ea53388e6ee4a6a0a1647b390c56eeed780e7e56, parent 9d11234efec1e5517b2887a6e7dfbc9c017bc52c, authored 2024-10-26T00:28:59Z. Files `tree.go`, `tree_test.go`, plus `.github/workflows/gin.yml`. This source commit includes an unrelated linter-version update; don't infer all changed files are needed for the bug fix.

A boundary decrement in catch-all wildcard parsing can yield index <0. The patch adds an explicit i<0 condition before dereferencing path[i], so invalid wildcard routes emit the intended descriptive panic rather than an unrelated index error. Original new TestWildcardInvalidSlash covers valid /foo/bar and invalid /foo/x*zy, /foo/b*r, checking panic string prefix.

Our posthoc native test `TestF20WildcardErrorType` constructs a fresh private route tree, invokes invalid `/foo/b*r`, recovers panic and checks its message begins `no / before catch-all in path`. Parent should fail its assertion with a different panic; post should pass. Returning a panic is the API semantics under invalid input, not 'safe no-panic'. Full production middleware behavior is not tested.
