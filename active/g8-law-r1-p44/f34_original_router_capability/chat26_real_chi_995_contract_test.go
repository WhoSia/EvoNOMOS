package originalrouters

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/go-chi/chi/v5"
)

// This is a researcher-run NONBLIND reproduction of the external, independently
// authored go-chi/chi issue #995 (2025-05-02), NOT a new F38 source task.
// The issue author asked for singleton support OR explicit error; replacing
// singleton middleware with a fresh instance is ONLY an app-owned workaround.
type chat26Issue995Middleware struct { next http.Handler }
func (m *chat26Issue995Middleware) ServeHTTP(w http.ResponseWriter,r *http.Request) {
    m.next.ServeHTTP(w,r)
}

func chat26Issue995Router(singleton bool) http.Handler {
    mux:=chi.NewRouter()
    shared:=&chat26Issue995Middleware{}
    factory:=func(next http.Handler) http.Handler{
        if singleton { shared.next=next; return shared }
        return &chat26Issue995Middleware{next:next}
    }
    hello:=func(msg string) func(http.ResponseWriter,*http.Request){
        return func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"Hello "+msg+"!\n")}
    }
    mux.Group(func(top chi.Router){
        top.Use(factory)
        top.Get("/",hello("World"))
        top.Group(func(foo chi.Router){foo.Get("/foo",hello("Foo"))})
        top.Group(func(bar chi.Router){bar.Get("/bar",hello("Bar"))})
    })
    return mux
}

func chat26Issue995Observe(h http.Handler,path string) (int,string) {
    request:=httptest.NewRequest("GET",path,nil)
    result:=httptest.NewRecorder()
    h.ServeHTTP(result,request)
    return result.Code,result.Body.String()
}

func TestChat26ExternalChi995ReproductionAndAppOwnedWorkaround(t *testing.T) {
    old:=chat26Issue995Router(true)
    fresh:=chat26Issue995Router(false)
    samples:=[]struct{path,want string}{
        {"/","Hello World!\n"},
        {"/foo","Hello Foo!\n"},
        {"/bar","Hello Bar!\n"},
    }
    observedBroken:=0
    for _,tc:=range samples{
        gotCode,gotBody:=chat26Issue995Observe(old,tc.path)
        if gotCode!=200 || gotBody!=tc.want {observedBroken++}
        newCode,newBody:=chat26Issue995Observe(fresh,tc.path)
        if newCode!=200 || newBody!=tc.want {
            t.Fatalf("fresh-instance app workaround fails %s: %d %q expected 200 %q",
                tc.path,newCode,newBody,tc.want)
        }
        t.Logf("#995 Chi v5.1.0 path %q singleton=%d/%q fresh=%d/%q",
            tc.path,gotCode,gotBody,newCode,newBody)
    }
    if observedBroken==0 {
        t.Fatal("issue #995 singleton misrouting not reproduced on this pinned version")
    }
    // This test does NOT claim that the upstream singleton contract was fixed:
    // the constructor now creates a new object per invocation, contrary to the
    // original request to allow the singleton or reject it explicitly.
}
