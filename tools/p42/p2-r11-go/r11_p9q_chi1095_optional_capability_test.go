package middleware

import (
    "net/http"
    "net/http/httptest"
    "os"
    "strings"
    "testing"

    "github.com/go-chi/chi/v5"
)

// Source-conditioned after PR text reveal; independent native probe of
// real source snapshots, NOT prospective unknown-PR prediction.
func TestR11P9QChi1095AllowHeaderVsExistingFlusher(t *testing.T) {
    phase := os.Getenv("R11P9Q_SOURCE_PHASE")
    if phase != "original" && phase != "proposal" {
        t.Fatalf("R11P9Q_SOURCE_PHASE must be original or proposal, got %q", phase)
    }
    router := chi.NewRouter()
    router.Use(GetHead)
    router.Get("/only-get", func(w http.ResponseWriter, r *http.Request) {
        _, hasFlusher := w.(http.Flusher)
        if hasFlusher {
            w.Header().Set("X-EvoNOMOS-Has-Flusher", "true")
        } else {
            w.Header().Set("X-EvoNOMOS-Has-Flusher", "false")
        }
        w.WriteHeader(http.StatusOK)
        _, _ = w.Write([]byte("preserved-body"))
    })

    // Input ResponseRecorder implements Flush. If the ordinary GET handler
    // no longer receives it, the GetHead middleware erased a client capability.
    recorder := httptest.NewRecorder()
    if _, ok := interface{}(recorder).(http.Flusher); !ok {
        t.Fatal("precondition violated: original ResponseRecorder lacks Flusher")
    }
    router.ServeHTTP(recorder, httptest.NewRequest(http.MethodGet, "/only-get", nil))
    if recorder.Code != http.StatusOK || recorder.Body.String() != "preserved-body" {
        t.Fatalf("GET old HTTP output not preserved: code=%d body=%q", recorder.Code, recorder.Body.String())
    }
    actualFlusher := recorder.Header().Get("X-EvoNOMOS-Has-Flusher")
    expectedFlusher := "true"
    if phase == "proposal" {
        expectedFlusher = "false"
    }
    if actualFlusher != expectedFlusher {
        t.Fatalf("source=%s old-client Flusher=%q want=%q", phase, actualFlusher, expectedFlusher)
    }

    // The proposed PR's explicit contract. Do not infer anything about
    // maintainer acceptance from a successful source test.
    methodNotAllowed := httptest.NewRecorder()
    router.ServeHTTP(methodNotAllowed, httptest.NewRequest(http.MethodPost, "/only-get", nil))
    if methodNotAllowed.Code != http.StatusMethodNotAllowed {
        t.Fatalf("POST status=%d want 405", methodNotAllowed.Code)
    }
    allow := strings.Join(methodNotAllowed.Header().Values("Allow"), ",")
    entries := strings.Split(allow, ",")
    contains := func(target string) bool {
        for _, v := range entries {
            if strings.TrimSpace(v) == target {
                return true
            }
        }
        return false
    }
    if !contains(http.MethodGet) {
        t.Fatalf("source=%s Allow missing GET: %q", phase, allow)
    }
    expectHead := phase == "proposal"
    if contains(http.MethodHead) != expectHead {
        t.Fatalf("source=%s Allow includes HEAD=%t want=%t: %q", phase, contains(http.MethodHead), expectHead, allow)
    }
    t.Logf("P42_R11_P9Q_REAL_CHI_1095 phase=%s GET200 body=preserved-body old_flusher=%s POST405 Allow=%q", phase, actualFlusher, allow)
}
