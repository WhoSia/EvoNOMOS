package r24

import "testing"

func TestHEADWireBodyIsEmptyEvenWhenHandlerWrites(t *testing.T) {
 h := StandardMux()
 handler := Observe(h, "HEAD", "/items/alpha")
 wire, err := WireObserve(h, "HEAD", "/items/alpha")
 if err != nil {t.Fatal(err)}
 if handler.Status != 200 || wire.Status != 200 {t.Fatalf("handler=%+v wire=%+v", handler, wire)}
 if handler.Body == wire.Body {t.Fatalf("expected HEAD handler/wire distinction: handler=%q wire=%q", handler.Body, wire.Body)}
 if wire.Body != "" {t.Fatalf("HEAD wire has unexpected body %q", wire.Body)}
}

func TestWireMethodStatusesAndEncodedPath(t *testing.T) {
 h := StandardMux()
 cases := []struct {method, path string; status int; body string}{
  {"GET", "/items/alpha", 200, "alpha"},
  {"HEAD", "/items/alpha", 200, ""},
  {"POST", "/items/alpha", 405, "Method Not Allowed"},
  {"GET", "/items/a%2Fb", 200, "a/b"},
 }
 for _, tc := range cases {
  got, err := WireObserve(h, tc.method, tc.path)
  if err != nil {t.Fatal(err)}
  if got.Status != tc.status || got.Body != tc.body {t.Fatalf("%s %s got %+v want status %d body %q", tc.method, tc.path, got, tc.status, tc.body)}
 }
}
