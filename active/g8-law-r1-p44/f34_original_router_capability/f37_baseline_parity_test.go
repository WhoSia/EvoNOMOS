package originalrouters

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "sync"
    "testing"

    "evonomos/f34-original-router-capability/f37arms/callbackarm"
    "evonomos/f34-original-router-capability/f37arms/handlerarm"
)

// The external oracle below was sealed in F37-R1 before either application
// arm was written. It checks each arm against expected results, not merely
// against the other arm. Both packages were implemented separately.
func f37Probe(call func(http.ResponseWriter, *http.Request), method, path, router string) (int, string) {
    request := httptest.NewRequest(method, path, nil)
    request.Header.Set("X-Router", router)
    response := httptest.NewRecorder()
    call(response, request)
    return response.Code, response.Body.String()
}

func TestF37IndependentArmsMeetFrozenInitialOracle(t *testing.T) {
    left := handlerarm.New("v1", "v2")
    right := callbackarm.New("v1", "v2")
    cases := []struct {
        name, method, path, router, body string
        status int
        checkBody bool
    }{
        {"chi-legacy", "GET", "/legacy", "chi", "old", 200, true},
        {"httprouter-legacy", "GET", "/legacy", "httprouter", "old", 200, true},
        {"chi-item-a", "GET", "/item/a", "chi", "v1:a", 200, true},
        {"httprouter-item-a", "GET", "/item/a", "httprouter", "v2:a", 200, true},
        {"chi-item-abc-uppercase", "GET", "/item/abc", "CHI", "v1:abc", 200, true},
        {"httprouter-item-abc-uppercase", "GET", "/item/abc", "HTTPROUTER", "v2:abc", 200, true},
        {"chi-missing-path", "GET", "/missing", "chi", "", 404, false},
        {"httprouter-missing-path", "GET", "/missing", "httprouter", "", 404, false},
        {"missing-router-header", "GET", "/legacy", "", "unknown router\n", 400, true},
        {"unsupported-router-header", "GET", "/legacy", "unsupported", "unknown router\n", 400, true},
    }

    for _, tc := range cases {
        tc := tc
        t.Run(tc.name, func(t *testing.T) {
            leftCode, leftBody := f37Probe(left.ServeHTTP, tc.method, tc.path, tc.router)
            rightCode, rightBody := f37Probe(right, tc.method, tc.path, tc.router)
            if leftCode != tc.status || (tc.checkBody && leftBody != tc.body) {
                t.Fatalf("handler arm: %d/%q expected %d/%q", leftCode, leftBody, tc.status, tc.body)
            }
            if rightCode != tc.status || (tc.checkBody && rightBody != tc.body) {
                t.Fatalf("callback arm: %d/%q expected %d/%q", rightCode, rightBody, tc.status, tc.body)
            }
            if leftCode != rightCode || leftBody != rightBody {
                t.Fatalf("arms disagree: handler %d/%q callback %d/%q",
                    leftCode, leftBody, rightCode, rightBody)
            }
        })
    }

    // Instance isolation was part of the preseal: independent constructors
    // cannot silently alter the already-constructed first app.
    altLeft := handlerarm.New("v3", "v4")
    altRight := callbackarm.New("v3", "v4")
    for _, arm := range []struct {
        name string
        call func(http.ResponseWriter, *http.Request)
    }{
        {"handler-old-instance", left.ServeHTTP},
        {"callback-old-instance", right},
        {"handler-alt-instance", altLeft.ServeHTTP},
        {"callback-alt-instance", altRight},
    } {
        want := "v1:z"
        if arm.name == "handler-alt-instance" || arm.name == "callback-alt-instance" {
            want = "v3:z"
        }
        code, body := f37Probe(arm.call, "GET", "/item/z", "chi")
        if code != 200 || body != want {
            t.Errorf("%s: got %d/%q expected %s", arm.name, code, body, want)
        }
    }

    // Sensitivity control: this deliberately faulty *test wrapper* is not a
    // variant of either source arm. It must be distinguishable by the
    // old-client observation; otherwise the oracle cannot catch regressions.
    broken := func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/legacy" {
            fmt.Fprint(w, "broken")
            return
        }
        right(w, r)
    }
    code, body := f37Probe(broken, "GET", "/legacy", "chi")
    if code == 200 && body == "old" {
        t.Fatal("old-client negative control incorrectly passed")
    }
}

func TestF37IndependentArmsConcurrentReadOnlyProviders(t *testing.T) {
    left := handlerarm.New("v1", "v2")
    right := callbackarm.New("v1", "v2")
    arms := []struct {
        name string
        call func(http.ResponseWriter, *http.Request)
    }{
        {"handler", left.ServeHTTP},
        {"callback", right},
    }
    var wg sync.WaitGroup
    for _, arm := range arms {
        arm := arm
        for i := 0; i < 32; i++ {
            wg.Add(1)
            go func(i int) {
                defer wg.Done()
                kind, want := "chi", "v1:parallel"
                if i%2 == 1 {
                    kind, want = "httprouter", "v2:parallel"
                }
                status, body := f37Probe(arm.call, "GET", "/item/parallel", kind)
                if status != 200 || body != want {
                    t.Errorf("%s request %d returned %d/%q, expected %s", arm.name, i, status, body, want)
                }
            }(i)
        }
    }
    wg.Wait()
}
