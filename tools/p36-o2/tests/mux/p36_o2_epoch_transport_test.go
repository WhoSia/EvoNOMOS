package mux

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "os"
    "sync"
    "testing"
)

func p35O6Middleware(label string) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("X-P35-O6", label)
            next.ServeHTTP(w, r)
        })
    }
}

func p35O6Dispatch(p *P35EpochRouter, value string) string {
    r:=httptest.NewRequest(http.MethodGet,"/",nil)
    if value!="" {r.Header.Set("X-P35-Epoch",value)}
    w:=httptest.NewRecorder()
    p.ServeHTTP(w,r)
    return w.Header().Get("X-P35-O6")
}

func p35O6Setup() *P35EpochRouter {
    p:=NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){
        if w.Header().Get("X-P35-O6")=="" {w.Header().Set("X-P35-O6","next")}
    }))
    for i:=0;i<32;i++ {
        p.Register("X-P35-Epoch",fmt.Sprintf("base-%02d",i),p35O6Middleware(fmt.Sprintf("base-%02d",i)))
    }
    return p
}

func TestP35O6ExactTraceCounts(t *testing.T) {
    arm:=os.Getenv("P35_O6_ARM")
    if arm!="EAGER" && arm!="LAZY" {t.Fatalf("P35_O6_ARM must be EAGER or LAZY, got %q",arm)}
    for _,tc:=range []struct{name string;interleaved bool}{
        {"burst",false},{"interleaved",true},
    }{
        t.Run(tc.name,func(t *testing.T){
            p:=p35O6Setup()
            if got:=p35O6Dispatch(p,"base-00");got!="base-00" {t.Fatalf("initial snapshot: %q",got)}
            baseRev,basePublished,baseBuild:=p.Stats()
            if baseRev!=32||basePublished!=32{t.Fatalf("baseline revisions %d/%d",baseRev,basePublished)}
            for i:=0;i<16;i++{
                name:=fmt.Sprintf("change-%02d",i)
                p.Register("X-P35-Epoch",name,p35O6Middleware(name))
                if tc.interleaved {
                    if got:=p35O6Dispatch(p,name);got!=name {t.Fatalf("prefix %d: got %q",i,got)}
                }
            }
            if !tc.interleaved{
                for i:=0;i<16;i++{
                    name:=fmt.Sprintf("change-%02d",i)
                    if got:=p35O6Dispatch(p,name);got!=name {t.Fatalf("burst %d: got %q",i,got)}
                }
            }
            rev,published,rebuilds:=p.Stats()
            want:=uint64(16)
            if arm=="LAZY"&&!tc.interleaved{want=1}
            if rebuilds-baseBuild!=want {t.Fatalf("P35_O6_REBUILD_SIGNATURE_FAIL arm=%s schedule=%s got=%d want=%d",arm,tc.name,rebuilds-baseBuild,want)}
            if rev!=48||published!=48 {t.Fatalf("final revisions %d/%d",rev,published)}
        })
    }
}

func TestP35O6RegistrationAndFallback(t *testing.T){
    p:=p35O6Setup()
    p.Register("X-P35-Epoch","same",p35O6Middleware("first"))
    p.Register("X-P35-Epoch","same",p35O6Middleware("second"))
    if got:=p35O6Dispatch(p,"same");got!="first"{t.Fatalf("registration priority %q",got)}
    p.RegisterAny("X-P35-Epoch",[]string{"none","special"},p35O6Middleware("any"))
    if got:=p35O6Dispatch(p,"special");got!="any"{t.Fatalf("any %q",got)}
    p.RegisterDefault(p35O6Middleware("fallback"))
    if got:=p35O6Dispatch(p,"unknown");got!="fallback"{t.Fatalf("default %q",got)}
    if got:=p35O6Dispatch(p,"base-01");got!="base-01"{t.Fatalf("baseline regression %q",got)}
}

func TestP35O6ConcurrentCompletedUpdatesVisible(t *testing.T){
    p:=p35O6Setup()
    var wg sync.WaitGroup
    for i:=0;i<64;i++ {
        wg.Add(2)
        go func(i int){
            defer wg.Done()
            name:=fmt.Sprintf("concurrent-%02d",i)
            p.Register("X-P35-Epoch",name,p35O6Middleware(name))
        }(i)
        go func(){
            defer wg.Done()
            if got:=p35O6Dispatch(p,"base-00");got!="base-00"{
                t.Errorf("stable dispatch %q",got)
            }
        }()
    }
    wg.Wait()
    for i:=0;i<64;i++ {
        name:=fmt.Sprintf("concurrent-%02d",i)
        if got:=p35O6Dispatch(p,name);got!=name {t.Fatalf("completed update invisible: %q want %q",got,name)}
    }
    rev,pub,_:=p.Stats()
    if rev!=96||pub!=96{t.Fatalf("after sync completed registration %d/%d",rev,pub)}
}

func BenchmarkP35O6Burst(b *testing.B){
    for k:=0;k<b.N;k++{
        p:=p35O6Setup()
        _=p35O6Dispatch(p,"base-00")
        for i:=0;i<16;i++{
            v:=fmt.Sprintf("change-%02d",i)
            p.Register("X-P35-Epoch",v,p35O6Middleware(v))
        }
        for i:=0;i<16;i++{_ = p35O6Dispatch(p,fmt.Sprintf("change-%02d",i))}
    }
}
func BenchmarkP35O6Interleaved(b *testing.B){
    for k:=0;k<b.N;k++{
        p:=p35O6Setup()
        _=p35O6Dispatch(p,"base-00")
        for i:=0;i<16;i++{
            v:=fmt.Sprintf("change-%02d",i)
            p.Register("X-P35-Epoch",v,p35O6Middleware(v))
            _=p35O6Dispatch(p,v)
        }
    }
}
