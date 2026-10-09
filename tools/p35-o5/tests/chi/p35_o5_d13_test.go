package middleware

import "testing"

// O5/D13 clarification: ASCII space/tab after closing quote is allowed.
// Selected AFTER an exploratory local encoding/csv edge-case probe;
// native results are not blind law identification.
func TestP35O5D13TrailingWhitespace(t *testing.T) {
	cases := []struct {
		name string
		fields []string
		want string
	}{
		{"quoted-trailing-space", []string{`"pi,ng"   `}, "hit"},
		{"quoted-tab-before-comma", []string{"other, \"pi,ng\"\t, miss"}, "hit"},
		{"quoted-leading-and-trailing", []string{`  "pi,ng"   `}, "hit"},
		{"malformed-postquote-content", []string{`"pi,ng"x`}, "next"},
		{"malformed-field-isolated", []string{`"pi,ng"x`, `"pi,ng"  `}, "hit"},
		{"existing-quoted-D11", []string{`"pi,ng"`}, "hit"},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			reg := RouteHeaders().Route("X-EvoNOMOS-Mode", "pi,ng", p35tag("hit"))
			if got := p35O3D11Got(reg, tc.fields); got != tc.want {
				t.Fatalf("P35_O5_D13_CONTRACT_FAILURE got=%q want=%q fields=%q", got, tc.want, tc.fields)
			}
		})
	}
}
