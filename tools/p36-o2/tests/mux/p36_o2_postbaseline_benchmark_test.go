package mux

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "testing"
)

// P36 post-treatment measurement correction: not prospective/blind.
// The P35 original microbenchmark timed 32 base registrations as well as
// 16 changes + 16 dispatches, confounding initial EAGER compilation with
// steady maintenance. Setup and first publication are excluded here.
// Same exact original Chi package and unchanged EAGER/LAZY P35 source.
func BenchmarkP36PostBaselineBurst(b *testing.B) {
    p36MeasureMaintenance(b, false)
}
func BenchmarkP36PostBaselineInterleaved(b *testing.B) {
    p36MeasureMaintenance(b, true)
}
func p36MeasureMaintenance(b *testing.B, interleaved bool) {
    b.ReportAllocs()
    for k := 0; k < b.N; k++ {
        b.StopTimer()
        p := NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {}))
        for i := 0; i < 32; i++ {
            base := fmt.Sprintf("base-%02d", i)
            p.Register("X-P35-Epoch", base, p36BenchmarkTag(base))
        }
        p36BenchmarkDispatch(p, "base-00")
        _, _, startBuild := p.Stats()
        b.StartTimer()

        for i := 0; i < 16; i++ {
            key := fmt.Sprintf("change-%02d", i)
            p.Register("X-P35-Epoch", key, p36BenchmarkTag(key))
            if interleaved {
                p36BenchmarkDispatch(p, key)
            }
        }
        if !interleaved {
            for i := 0; i < 16; i++ {
                p36BenchmarkDispatch(p, fmt.Sprintf("change-%02d", i))
            }
        }
        b.StopTimer()
        rev, pub, endBuild := p.Stats()
        if rev != 48 || pub != 48 {
            b.Fatalf("P36_O1_REVISION_FAIL rev=%d published=%d", rev, pub)
        }
        if endBuild < startBuild {
            b.Fatal("P36_O1_REBUILD_COUNTER_REVERSED")
        }
        b.StartTimer()
    }
}
func p36BenchmarkTag(label string) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("X-P36-Tag", label)
            next.ServeHTTP(w, r)
        })
    }
}
func p36BenchmarkDispatch(p *P35EpochRouter, value string) {
    req := httptest.NewRequest("GET", "/", nil)
    req.Header.Set("X-P35-Epoch", value)
    rec := httptest.NewRecorder()
    p.ServeHTTP(rec, req)
}
