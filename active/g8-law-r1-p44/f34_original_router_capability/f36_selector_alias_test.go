package originalrouters

import (
    "net/http"
    "net/http/httptest"
    "strings"
    "testing"
)

// snapshotCallbackPicker has independent app-owned selection logic, like the
// F35 independent callback selector, but snapshots the input configuration.
// It does not invoke Pick or independentCallbackPicker.
func snapshotCallbackPicker(input map[RouterKind]func(http.ResponseWriter, *http.Request)) http.HandlerFunc {
    frozen := make(map[RouterKind]func(http.ResponseWriter, *http.Request), len(input))
    for kind, callback := range input {
        frozen[kind] = callback
    }
    return func(w http.ResponseWriter, r *http.Request) {
        kind := RouterKind(strings.ToLower(r.Header.Get("X-Router")))
        callback, ok := frozen[kind]
        if !ok {
            http.Error(w, "unknown router", http.StatusBadRequest)
            return
        }
        callback(w, r)
    }
}

func f36Request(h http.Handler, path, router string) (int, string) {
    req := httptest.NewRequest(http.MethodGet, path, nil)
    req.Header.Set("X-Router", router)
    recorder := httptest.NewRecorder()
    h.ServeHTTP(recorder, req)
    return recorder.Code, recorder.Body.String()
}

func f36Expect(t *testing.T, h http.Handler, path, router string, wantCode int, wantBody string) {
    t.Helper()
    status, body := f36Request(h, path, router)
    if status != wantCode || body != wantBody {
        t.Fatalf("%s %s: got %d/%q; want %d/%q",
            router, path, status, body, wantCode, wantBody)
    }
}

func TestF36SelectorMapAliasingAndSnapshotRival(t *testing.T) {
    v1, err := Build(Chi, "v1")
    if err != nil { t.Fatal(err) }
    v2, err := Build(Chi, "v2")
    if err != nil { t.Fatal(err) }

    t.Run("interface-selector-live-map", func(t *testing.T) {
        handlers := map[RouterKind]http.Handler{Chi: v1}
        selected := Pick(handlers)
        f36Expect(t, selected, "/item/x", "chi", 200, "v1:x")
        f36Expect(t, selected, "/legacy", "chi", 200, "old")
        handlers[Chi] = v2 // sequential, after selector construction
        f36Expect(t, selected, "/item/x", "chi", 200, "v2:x")
        f36Expect(t, selected, "/legacy", "chi", 200, "old")
        f36Expect(t, selected, "/item/x", "", 400, "unknown router\n")
    })

    t.Run("independent-callback-selector-live-map", func(t *testing.T) {
        callbacks := map[RouterKind]func(http.ResponseWriter, *http.Request){
            Chi: v1.ServeHTTP,
        }
        selected := independentCallbackPicker(callbacks)
        f36Expect(t, selected, "/item/x", "chi", 200, "v1:x")
        callbacks[Chi] = v2.ServeHTTP
        f36Expect(t, selected, "/item/x", "chi", 200, "v2:x")
        f36Expect(t, selected, "/legacy", "chi", 200, "old")
        f36Expect(t, selected, "/item/x", "unknown", 400, "unknown router\n")
    })

    t.Run("snapshot-rival-preserves-published-dispatch", func(t *testing.T) {
        callbacks := map[RouterKind]func(http.ResponseWriter, *http.Request){
            Chi: v1.ServeHTTP,
        }
        selected := snapshotCallbackPicker(callbacks)
        f36Expect(t, selected, "/item/x", "chi", 200, "v1:x")
        callbacks[Chi] = v2.ServeHTTP
        f36Expect(t, selected, "/item/x", "chi", 200, "v1:x")
        f36Expect(t, selected, "/legacy", "chi", 200, "old")
        f36Expect(t, selected, "/item/x", "", 400, "unknown router\n")

        // The old client's /legacy observation alone cannot distinguish the
        // v1/v2 providers; /item/x exposes the post-construction mutation.
        live := independentCallbackPicker(callbacks)
        f36Expect(t, live, "/item/x", "chi", 200, "v2:x")
        f36Expect(t, live, "/legacy", "chi", 200, "old")
    })
}
