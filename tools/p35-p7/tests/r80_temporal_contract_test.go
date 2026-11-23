package middleware

import (
	"net/http"
	"os"
	"testing"
)

// R80 verifies temporal contract behavior under *sequential* registration.
// Set R80_EXPECT=after for LIVE, downstream for SNAPSHOT. No concurrent
// mutation is performed or asserted safe; source SHA/arm selection is external.
func TestR80TemporalAfterConstruction(t *testing.T) {
	want := os.Getenv("R80_EXPECT")
	if want == "" {
		t.Skip("R80_EXPECT=after (LIVE) or R80_EXPECT=downstream (SNAPSHOT)")
	}
	if want != "after" && want != "downstream" {
		t.Fatalf("invalid R80_EXPECT=%q", want)
	}
	r := RouteHeaders().Route("X-Temporal", "before", p35tag("before"))
	next := http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		if w.Header().Get("X-P35-P7") == "" {
			w.Header().Set("X-P35-P7", "downstream")
		}
	})
	h := r.Handler(next)
	if got := p35request(h, map[string]string{"X-Temporal": "before"}); got != "before" {
		t.Fatalf("pre-mutation: got %q, want before", got)
	}
	r.Route("X-Temporal", "after", p35tag("after"))
	got := p35request(h, map[string]string{"X-Temporal": "after"})
	t.Logf("post-construction handler observation: %q", got)
	if got != want {
		t.Fatalf("sequential temporal contract: got %q, want %q", got, want)
	}
}
