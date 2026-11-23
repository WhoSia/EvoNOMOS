package middleware

import (
    "net/http"
    "net/http/httptest"
    "strconv"
    "testing"
)

// Post-primary exploratory validation of an observed cost crossover.
// Not preregistered prior to the R81 steady/construction microbenchmarks.
func BenchmarkR81Lifecycle(b *testing.B) {
    for _, requests := range []int{1, 2, 3, 16} {
        b.Run("requests_"+strconv.Itoa(requests), func(b *testing.B) {
            registry := r81Registry()
            next := http.HandlerFunc(func(http.ResponseWriter, *http.Request) {})
            req := httptest.NewRequest("GET", "/", nil)
            req.Header.Set("X-ZZZ", "ping")
            b.ReportAllocs()
            b.ResetTimer()
            for i := 0; i < b.N; i++ {
                handler := registry.Handler(next)
                r81HandlerSink = handler
                for j := 0; j < requests; j++ {
                    recorder := httptest.NewRecorder()
                    handler.ServeHTTP(recorder, req)
                    if recorder.Header().Get("X-P35-P7") != "exact" {
                        b.Fatal("wrong routing behavior")
                    }
                }
            }
        })
    }
}
