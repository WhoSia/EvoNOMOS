package middleware

import (
    "net/http"
    "net/http/httptest"
    "strconv"
    "testing"
)

// R81: same D8-compliant behavior, two distinct workloads.
// Only d8/live and d8/snapshot are compared. Not a study of human effort.
func r81Registry() HeaderRouter {
    r := RouteHeaders()
    for i := 0; i < 128; i++ {
        r.Route("X-R81-"+strconv.Itoa(i), "yes", p35tag("unused"))
    }
    r.Route("X-ZZZ", "ping", p35tag("exact"))
    return r
}

func BenchmarkR81SteadyLookup(b *testing.B) {
    r := r81Registry()
    next := http.HandlerFunc(func(http.ResponseWriter, *http.Request) {})
    h := r.Handler(next)
    req := httptest.NewRequest("GET", "/", nil)
    req.Header.Set("X-ZZZ", "ping")
    b.ReportAllocs()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        recorder := httptest.NewRecorder()
        h.ServeHTTP(recorder, req)
        if recorder.Header().Get("X-P35-P7") != "exact" {
            b.Fatalf("wrong result for common request")
        }
    }
}

func BenchmarkR81ConstructHandler(b *testing.B) {
    r := r81Registry()
    next := http.HandlerFunc(func(http.ResponseWriter, *http.Request) {})
    b.ReportAllocs()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        h := r.Handler(next)
        if h == nil {
            b.Fatal("nil constructed handler")
        }
    }
}
