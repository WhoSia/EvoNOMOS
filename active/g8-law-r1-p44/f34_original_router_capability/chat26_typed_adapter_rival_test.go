package originalrouters

import (
    "net/http"
    "net/http/httptest"
    "sync"
    "testing"

    "evonomos/f34-original-router-capability/f37arms/callbackarm"
    "evonomos/f34-original-router-capability/f37arms/handlerarm"
)

// Explicit typed adapter: an ordinary callback can retain extra method sets.
// It does not modify either app-owned source arm or its pinned upstream router.
type chat26TypedAdapter struct {
    run func(http.ResponseWriter, *http.Request)
    token string
}
func (a chat26TypedAdapter) ServeHTTP(w http.ResponseWriter, r *http.Request) { a.run(w,r) }
func (a chat26TypedAdapter) Marker() string { return a.token }

func TestChat26ClassicalTypedAdapterCounterRival(t *testing.T) {
    left := handlerarm.New("v1", "v2")
    right := callbackarm.New("v1", "v2")
    cases := []struct{
        name string
        call func(http.ResponseWriter,*http.Request)
    }{
        {"interface_arm",left.ServeHTTP},
        {"callback_arm",right},
    }
    requests := []struct{
        path, provider, body string
        code int
    }{
        {"/legacy","chi","old",200},
        {"/legacy","httprouter","old",200},
        {"/item/a","chi","v1:a",200},
        {"/item/a","httprouter","v2:a",200},
        {"/item/z","CHI","v1:z",200},
        {"/item/z","HTTPROUTER","v2:z",200},
        {"/legacy","","unknown router\n",400},
        {"/legacy","other","unknown router\n",400},
    }
    for _, arm:=range cases {
        t.Run(arm.name,func(t *testing.T){
            var full http.Handler=chat26TypedAdapter{run:arm.call,token:"owned-metadata"}
            var plain http.Handler=http.HandlerFunc(arm.call)
            labeled, ok:=full.(chat26Extra)
            if !ok || labeled.Marker()!="owned-metadata" {
                t.Fatal("typed callback adapter must expose its own marker")
            }
            if _,ok:=plain.(chat26Extra);ok {
                t.Fatal("plain HandlerFunc unexpectedly exposes marker")
            }
            for _,tc:=range requests {
                req:=httptest.NewRequest("GET",tc.path,nil)
                req.Header.Set("X-Router",tc.provider)
                a,b:=httptest.NewRecorder(),httptest.NewRecorder()
                full.ServeHTTP(a,req)
                plain.ServeHTTP(b,req)
                for _,response:=range []*httptest.ResponseRecorder{a,b} {
                    if response.Code!=tc.code || response.Body.String()!=tc.body {
                        t.Fatalf("%s %s got %d/%q expected %d/%q",
                            arm.name,tc.path,response.Code,response.Body.String(),tc.code,tc.body)
                    }
                }
            }
        })
    }
}

func TestChat26TypedAdapterConcurrentReadOnlyRequests(t *testing.T) {
    left:=handlerarm.New("first","second")
    right:=callbackarm.New("first","second")
    adapters:=[]http.Handler{
        chat26TypedAdapter{run:left.ServeHTTP,token:"interface"},
        chat26TypedAdapter{run:right,token:"callback"},
    }
    var wg sync.WaitGroup
    for _,h:=range adapters {
        for i:=0;i<32;i++ {
            wg.Add(1)
            go func(h http.Handler,i int) {
                defer wg.Done()
                req:=httptest.NewRequest("GET","/item/x",nil)
                expected:="first:x"
                provider:="chi"
                if i%2==1 { provider="httprouter"; expected="second:x" }
                req.Header.Set("X-Router",provider)
                response:=httptest.NewRecorder()
                h.ServeHTTP(response,req)
                if response.Code!=200 || response.Body.String()!=expected {
                    t.Errorf("parallel typed adapter %d: %d/%q expected %q",
                        i,response.Code,response.Body.String(),expected)
                }
            }(h,i)
        }
    }
    wg.Wait()
}
