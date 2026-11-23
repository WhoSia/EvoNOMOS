package originalrouters

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/go-chi/chi/v5"
)

// Reproduces only the *remaining* method-precedence complaint in issue #1035.
// Its original author withdrew the separate regex-subpath allegation.
// This is a NONBLIND pinned historical source check, not F38.
func chat26Chi1035Routes(guard bool) http.Handler {
    router:=chi.NewRouter()
    router.Get("/users/me",func(w http.ResponseWriter,r *http.Request){
        fmt.Fprint(w,"current-user")
    })
    router.Put("/users/{id}",func(w http.ResponseWriter,r *http.Request){
        fmt.Fprint(w,"updated:"+chi.URLParam(r,"id"))
    })
    if guard {
        // App-owned explicit static endpoint, not a new upstream StrictRouting API.
        router.Put("/users/me",func(w http.ResponseWriter,r *http.Request){
            w.WriteHeader(http.StatusMethodNotAllowed)
        })
    }
    return router
}

func chat26Chi1035Response(h http.Handler,method,path string)(int,string) {
    req:=httptest.NewRequest(method,path,nil)
    out:=httptest.NewRecorder()
    h.ServeHTTP(out,req)
    return out.Code,out.Body.String()
}

func TestChat26Chi1035AuthorScopedMethodPrecedenceAndStaticGuard(t *testing.T) {
    original:=chat26Chi1035Routes(false)
    guarded:=chat26Chi1035Routes(true)
    code,body:=chat26Chi1035Response(original,http.MethodPut,"/users/me")
    t.Logf("#1035 original Chi v5.1.0 PUT /users/me: %d %q",code,body)
    if code!=http.StatusOK || body!="updated:me" {
        t.Fatalf("reported parameter fallthrough not reproduced: %d %q",code,body)
    }
    cases:=[]struct{method,path string;status int;body string}{
        {http.MethodGet,"/users/me",http.StatusOK,"current-user"},
        {http.MethodPut,"/users/123",http.StatusOK,"updated:123"},
        {http.MethodPut,"/users/me",http.StatusMethodNotAllowed,""},
    }
    for _,tc:=range cases {
        gotCode,gotBody:=chat26Chi1035Response(guarded,tc.method,tc.path)
        if gotCode!=tc.status || gotBody!=tc.body {
            t.Fatalf("guarded %s %s = %d/%q wanted %d/%q",
                tc.method,tc.path,gotCode,gotBody,tc.status,tc.body)
        }
    }
    // We do not run any test of the withdrawn nested-regex allegation.
    // The added explicit PUT route is not proof of global precedence semantics.
}
