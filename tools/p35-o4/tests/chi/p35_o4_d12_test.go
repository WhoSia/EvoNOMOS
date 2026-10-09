package middleware

import "testing"

// Prospective D12 opt-in feature; never change the old D11 Route behavior.
func TestP35O4D12QuotedOnlyFutureDemand(t *testing.T) {
	quoted := RouteHeaders().RouteQuoted("X-EvoNOMOS-Mode", "ping", p35tag("quoted"))
	cases := []struct {
		name string
		vals []string
		want string
	}{
		{"quoted-match", []string{`"ping"`}, "quoted"},
		{"bare-no-match", []string{"ping"}, "next"},
		{"mixed-unquoted-then-quoted", []string{`ping, "ping"`}, "quoted"},
		{"independent-physical-field", []string{"ping", `"ping"`}, "quoted"},
		{"malformed-first-field", []string{`"ping`, `"ping"`}, "quoted"},
		{"malformed-only", []string{`"ping`}, "next"},
		{"quoted-other-token", []string{`"other"`}, "next"},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			if got := p35O3D11Got(quoted, tc.vals); got != tc.want {
				t.Fatalf("P35_O4_D12_CONTRACT_FAILURE got=%q want=%q fields=%q", got, tc.want, tc.vals)
			}
		})
	}
	legacy := RouteHeaders().Route("X-EvoNOMOS-Mode", "ping", p35tag("legacy"))
	for _, val := range []string{"ping", `"ping"`} {
		if got := p35O3D11Got(legacy, []string{val}); got != "legacy" {
			t.Fatalf("P35_O4_D12_LEGACY_REGRESSION got=%q field=%q", got, val)
		}
	}
}
