package middleware

import "testing"

// Researcher-authored legacy semantics to expose direct exported Pattern consumers.
// This suite preserves *observed* historical behavior, NOT a documented upstream
// promise that Pattern must always be case sensitive.
func TestEvoP44DirectLegacyPatternContract(t *testing.T) {
 cases := []struct{name, pattern, input string; want bool}{
  {"exact-same-case", "Gold", "Gold", true},
  {"exact-mixed-case", "Gold", "gold", false},
  {"wildcard-prefix-same", "Go*", "Gold", true},
  {"wildcard-prefix-different", "Go*", "gold", false},
  {"wildcard-suffix-same", "*OlD", "xxOlD", true},
  {"wildcard-suffix-different", "*OlD", "xxold", false},
  {"literal-star-case", "A*B", "AxxB", true},
  {"literal-star-mixed", "A*B", "axxB", false},
 }
 for _,tc := range cases {
  t.Run(tc.name,func(t *testing.T){
   got := NewPattern(tc.pattern).Match(tc.input)
   if got != tc.want {
    t.Fatalf("EVO_P44_DIRECT_LEGACY_CONTRACT_FAILED pattern=%q input=%q got=%v want=%v",tc.pattern,tc.input,got,tc.want)
   }
  })
 }
}
