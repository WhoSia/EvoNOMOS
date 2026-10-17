package middleware

import (
    "net/http"
    "net/http/httptest"
    "strings"
    "testing"

    "github.com/go-chi/chi/v5"
)

// Embedding only the http.ResponseWriter interface deliberately hides
// the optional Flush method of its underlying httptest.ResponseRecorder.
type evonomosR11P9QBasicOnlyWriter struct{ http.ResponseWriter }

func TestR11P9QChi1095ConditionalRepairSupportsBothOriginalClientClasses(t *testing.T) {
    for _, tc := range []struct { name string; inputFlusher bool }{
        {"old-client-requires-Flusher", true},
        {"old-client-requires-no-Flusher", false},
    } {
        t.Run(tc.name, func(t *testing.T) {
            router := chi.NewRouter()
            router.Use(GetHead)
            router.Get("/only-get", func(w http.ResponseWriter, r *http.Request) {
                _, got := w.(http.Flusher)
                marker := "false"
                if got { marker = "true" }
                w.Header().Set("X-EvoNOMOS-Flusher", marker)
                w.WriteHeader(http.StatusOK)
                _, _ = w.Write([]byte("preserved-body"))
            })
            output := httptest.NewRecorder()
            var source http.ResponseWriter = output
            if !tc.inputFlusher {
                source = &evonomosR11P9QBasicOnlyWriter{ResponseWriter: output}
            }
            _, originalHas := source.(http.Flusher)
            if originalHas != tc.inputFlusher {
                t.Fatal("negative/positive input capability precondition failed")
            }
            router.ServeHTTP(source, httptest.NewRequest(http.MethodGet, "/only-get", nil))
            observed := output.Header().Get("X-EvoNOMOS-Flusher") == "true"
            if observed != tc.inputFlusher || output.Code != 200 || output.Body.String() != "preserved-body" {
                t.Fatalf("old capability/output not preserved: input=%t output=%t status=%d body=%q", tc.inputFlusher, observed, output.Code, output.Body.String())
            }
            out405 := httptest.NewRecorder()
            router.ServeHTTP(out405, httptest.NewRequest(http.MethodPost, "/only-get", nil))
            if out405.Code != http.StatusMethodNotAllowed {
                t.Fatalf("POST status %d !=405", out405.Code)
            }
            allow := strings.Join(out405.Header().Values("Allow"), ",")
            foundGet, foundHead := false, false
            for _, s := range strings.Split(allow, ",") {
                switch strings.TrimSpace(s) {
                case "GET": foundGet=true
                case "HEAD": foundHead=true
                }
            }
            if !foundGet || !foundHead {
                t.Fatalf("conditional repair did not retain proposed Allow: %q", allow)
            }
            t.Logf("REPAIRED_CHI_1095 sourceFlusher=%t observedFlusher=%t GET200 POST405 Allow=%s", tc.inputFlusher, observed, allow)
        })
    }
}
