package gin

import (
    "net/http"
    "net/http/httptest"
    "testing"
)

// The exact three-request old/new client alphabet was fixed BEFORE code
// at source preseal b1fda72566e5a93ae7ccc66b123a4357b1aac53a.
// This is authored application fixture code; original Gin source is untouched.
func TestEvoNOMOSP11NativeSourceStageContract(t *testing.T) {
    SetMode(TestMode)
    r := New()
    r.GET("/old", func(c *Context) { c.String(http.StatusOK, "old") })
    evonomosP11Install(r)

    for _, item := range []struct {
        path string
        enabled bool
        body string
    }{
        {"/old", true, "old"},
        {"/a", evonomosP11HasA, "A"},
        {"/b", evonomosP11HasB, "B"},
    } {
        t.Run(evonomosP11Stage+item.path, func(t *testing.T) {
            recorder := httptest.NewRecorder()
            r.ServeHTTP(recorder, httptest.NewRequest(http.MethodGet, item.path, nil))
            status := http.StatusNotFound
            if item.enabled { status = http.StatusOK }
            if recorder.Code != status {
                t.Fatalf("stage=%s path=%s expected code=%d got=%d",
                    evonomosP11Stage,item.path,status,recorder.Code)
            }
            if item.enabled && recorder.Body.String() != item.body {
                t.Fatalf("stage=%s path=%s expected body=%q got=%q",
                    evonomosP11Stage,item.path,item.body,recorder.Body.String())
            }
            if recorder.Flushed {
                t.Fatalf("stage=%s path=%s unexpected real recorder.Flush event",
                    evonomosP11Stage,item.path)
            }
            t.Logf("P11_NATIVE stage=%s input=%s code=%d body=%q no_transport_flush=true",
                evonomosP11Stage,item.path,recorder.Code,recorder.Body.String())
        })
    }
}
