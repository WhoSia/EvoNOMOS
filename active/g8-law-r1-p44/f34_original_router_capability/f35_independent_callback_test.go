package originalrouters

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "strings"
    "sync"
    "testing"
)

// independentCallbackPicker is an application-owned competing selector.
// It does not call Pick, and its dispatch map contains functions rather
// than http.Handler values. The upstream routers remain unchanged.
// This does not eliminate http.Handler use inside the wrapped providers.
func independentCallbackPicker(callbacks map[RouterKind]func(http.ResponseWriter, *http.Request)) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        kind := RouterKind(strings.ToLower(r.Header.Get("X-Router")))
        callback, ok := callbacks[kind]
        if !ok {
            http.Error(w, "unknown router", http.StatusBadRequest)
            return
        }
        callback(w, r)
    }
}

func TestF35IndependentCallbackRivalAgainstPinnedOriginalRouters(t *testing.T) {
    chiHandler, err := Build(Chi, "v1")
    if err != nil { t.Fatal(err) }
    httpRouterHandler, err := Build(HTTPRouter, "v2")
    if err != nil { t.Fatal(err) }

    interfaceSelector := Pick(map[RouterKind]http.Handler{
        Chi: chiHandler, HTTPRouter: httpRouterHandler,
    })
    callbackSelector := independentCallbackPicker(map[RouterKind]func(http.ResponseWriter, *http.Request){
        Chi: chiHandler.ServeHTTP,
        HTTPRouter: httpRouterHandler.ServeHTTP,
    })
    testcases := []struct {
        header, path string
        wantStatus int
        wantBody string
    }{
        {"chi", "/legacy", 200, "old"},
        {"httprouter", "/legacy", 200, "old"},
        {"chi", "/item/a", 200, "v1:a"},
        {"httprouter", "/item/a", 200, "v2:a"},
        {"CHI", "/item/abc", 200, "v1:abc"},
        {"httprouter", "/item/abc", 200, "v2:abc"},
        {"missing", "/item/a", 400, "unknown router\n"},
        {"", "/legacy", 400, "unknown router\n"},
    }

    for _, tc := range testcases {
        t.Run(tc.header+tc.path, func(t *testing.T) {
            requestFor := func() *http.Request {
                request := httptest.NewRequest("GET", tc.path, nil)
                request.Header.Set("X-Router", tc.header)
                return request
            }
            left, right := httptest.NewRecorder(), httptest.NewRecorder()
            interfaceSelector.ServeHTTP(left, requestFor())
            callbackSelector.ServeHTTP(right, requestFor())
            if left.Code != right.Code || left.Body.String() != right.Body.String() {
                t.Fatalf("dispatch mismatch: interface %d/%q, callback %d/%q",
                    left.Code, left.Body.String(), right.Code, right.Body.String())
            }
            if right.Code != tc.wantStatus || right.Body.String() != tc.wantBody {
                t.Fatalf("unexpected output %d/%q, want %d/%q",
                    right.Code, right.Body.String(), tc.wantStatus, tc.wantBody)
            }
        })
    }

    // A faulty callback must be detected: comparing a selector to a
    // forwarding wrapper around itself would never test independent logic.
    faulty := independentCallbackPicker(map[RouterKind]func(http.ResponseWriter, *http.Request){
        Chi: func(w http.ResponseWriter, r *http.Request) { fmt.Fprint(w, "incorrect") },
        HTTPRouter: httpRouterHandler.ServeHTTP,
    })
    requestFor := func() *http.Request {
        req := httptest.NewRequest("GET", "/item/a", nil)
        req.Header.Set("X-Router", "chi")
        return req
    }
    good, bad := httptest.NewRecorder(), httptest.NewRecorder()
    interfaceSelector.ServeHTTP(good, requestFor())
    faulty.ServeHTTP(bad, requestFor())
    if good.Code == bad.Code && good.Body.String() == bad.Body.String() {
        t.Fatal("negative control did not distinguish a deliberately faulty callback")
    }

    // Immutable provider callbacks must not leak concurrent version state.
    var wg sync.WaitGroup
    for i := 0; i < 32; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            kind, want := "chi", "v1:concurrent"
            if i%2 == 1 {
                kind, want = "httprouter", "v2:concurrent"
            }
            req := httptest.NewRequest("GET", "/item/concurrent", nil)
            req.Header.Set("X-Router", kind)
            recorder := httptest.NewRecorder()
            callbackSelector.ServeHTTP(recorder, req)
            if recorder.Code != 200 || recorder.Body.String() != want {
                t.Errorf("concurrent %d: %d/%q instead of %q",
                    i, recorder.Code, recorder.Body.String(), want)
            }
        }(i)
    }
    wg.Wait()
}
