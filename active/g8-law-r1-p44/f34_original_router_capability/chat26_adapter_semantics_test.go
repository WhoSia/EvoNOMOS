package originalrouters

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "testing"

    "evonomos/f34-original-router-capability/f37arms/callbackarm"
    "evonomos/f34-original-router-capability/f37arms/handlerarm"
)

// Chat26 reproduces a standard Go adapter property, NOT a new F38 demand.
func TestChat26HandlerCallbackExtensionalRoundTrips(t *testing.T) {
    left := handlerarm.New("v1", "v2")
    right := callbackarm.New("v1", "v2")
    throughHandlerFunc := http.HandlerFunc(left.ServeHTTP)
    throughCallback := http.HandlerFunc(right)

    cases := []struct {
        provider, path, want string
        status int
    }{
        {"chi", "/legacy", "old", 200},
        {"httprouter", "/legacy", "old", 200},
        {"chi", "/item/a", "v1:a", 200},
        {"httprouter", "/item/a", "v2:a", 200},
        {"CHI", "/item/abc", "v1:abc", 200},
        {"HTTPROUTER", "/item/abc", "v2:abc", 200},
        {"", "/legacy", "unknown router\n", 400},
        {"other", "/legacy", "unknown router\n", 400},
    }
    for _, tc := range cases {
        tc := tc
        t.Run(fmt.Sprintf("%s:%s", tc.provider, tc.path), func(t *testing.T) {
            req := httptest.NewRequest("GET", tc.path, nil)
            req.Header.Set("X-Router", tc.provider)
            a := httptest.NewRecorder()
            b := httptest.NewRecorder()
            throughHandlerFunc.ServeHTTP(a, req)
            throughCallback.ServeHTTP(b, req)
            if a.Code != tc.status || a.Body.String() != tc.want {
                t.Fatalf("handler adapter: %d/%q, expected %d/%q", a.Code, a.Body.String(), tc.status, tc.want)
            }
            if b.Code != tc.status || b.Body.String() != tc.want {
                t.Fatalf("callback adapter: %d/%q, expected %d/%q", b.Code, b.Body.String(), tc.status, tc.want)
            }
        })
    }
}

type chat26Extra interface { Marker() string }

type chat26CustomHandler struct{}

func (chat26CustomHandler) Marker() string { return "identity" }
func (chat26CustomHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "same HTTP output")
}

func TestChat26HandlerFuncLosesExtraMethodSet(t *testing.T) {
    original := chat26CustomHandler{}
    var originalHandler http.Handler = original
    adapted := http.Handler(http.HandlerFunc(original.ServeHTTP))
    if _, ok := originalHandler.(chat26Extra); !ok {
        t.Fatal("original custom handler must expose Marker")
    }
    if _, ok := adapted.(chat26Extra); ok {
        t.Fatal("HandlerFunc wrapper must not expose original Marker")
    }
    request := httptest.NewRequest("GET", "/", nil)
    a, b := httptest.NewRecorder(), httptest.NewRecorder()
    originalHandler.ServeHTTP(a, request)
    adapted.ServeHTTP(b, request)
    if a.Code != b.Code || a.Body.String() != b.Body.String() {
        t.Fatal("expected equal HTTP response despite unequal method sets")
    }
}

type chat26NilPointerHandler struct{}
func (*chat26NilPointerHandler) ServeHTTP(http.ResponseWriter, *http.Request) {}

func TestChat26TypedNilIsNotNilHandlerInterface(t *testing.T) {
    var pointer *chat26NilPointerHandler
    var iface http.Handler = pointer
    if iface == nil {
        t.Fatal("typed nil pointer interface must be nonnil")
    }
    var f func(http.ResponseWriter, *http.Request)
    var functionIface http.Handler = http.HandlerFunc(f)
    if functionIface == nil {
        t.Fatal("HandlerFunc(nil function) interface must be nonnil")
    }
    // Neither is called: a panic would not prove anything about safe source repair.
}
