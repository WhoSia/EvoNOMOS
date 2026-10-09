package middleware
import (
 "net/http"
 "net/http/httptest"
 "testing"
)
func p35tag(s string)func(http.Handler)http.Handler{
 return func(next http.Handler)http.Handler{
  return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.Header().Set("X-P35-P7",s);next.ServeHTTP(w,r)})
 }
}
func p35request(h http.Handler, headers map[string]string)string{
 r:=httptest.NewRequest("GET","/",nil)
 for k,v:=range headers{r.Header.Set(k,v)}
 rec:=httptest.NewRecorder();h.ServeHTTP(rec,r)
 return rec.Header().Get("X-P35-P7")
}
func TestP35P7EmptyRouterExactlyOnce(t *testing.T){
 n:=0; next:=http.HandlerFunc(func(http.ResponseWriter,*http.Request){n++})
 h:=RouteHeaders().Handler(next)
 h.ServeHTTP(httptest.NewRecorder(),httptest.NewRequest("GET","/",nil))
 if n!=1{t.Fatalf("P35P7_D0_EMPTY_ROUTE_FAILURE exactly-once expected 1, got %d",n)}
}
func TestP35P7StableHeaderOrderAndFallback(t *testing.T){
 next:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){if w.Header().Get("X-P35-P7")=="" { w.Header().Set("X-P35-P7","next") }})
 r:=RouteHeaders().Route("X-B","b",p35tag("B")).Route("X-A","a",p35tag("A")).Route("X-A","a",p35tag("A-second")).RouteDefault(p35tag("fallback"))
 h:=r.Handler(next)
 for _,c:=range []struct{name string;headers map[string]string;want string}{
  {"lexical-deterministic",map[string]string{"X-A":"a","X-B":"b"},"A"},
  {"same-header-first",map[string]string{"X-A":"a"},"A"},
  {"only-b",map[string]string{"X-B":"b"},"B"},
  {"fallback",map[string]string{"X-Z":"z"},"fallback"},
 }{t.Run(c.name,func(t *testing.T){for i:=0;i<20;i++{if got:=p35request(h,c.headers);got!=c.want{t.Fatalf("P35P7_D0_ROUTE_FAILURE got %q want %q",got,c.want)}}})}
}
func TestP35P7RouteAny(t *testing.T){
 h:=RouteHeaders().RouteAny("X-Q",[]string{"q*","*z"},p35tag("match")).Handler(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){if w.Header().Get("X-P35-P7")=="" { w.Header().Set("X-P35-P7","none") }}))
 for _,v:=range []string{"q42","az"}{if got:=p35request(h,map[string]string{"X-Q":v});got!="match"{t.Fatalf("got %q",got)}}
 if got:=p35request(h,map[string]string{"X-Q":"no"});got!="none"{t.Fatal(got)}
}
func BenchmarkP35P7SteadyLookup(b *testing.B){
 r:=RouteHeaders()
 for i:=0;i<128;i++{name:= "X-P35-"+string(rune(1000+i));r.Route(name,"yes",p35tag("unused"))}
 r.Route("X-ZZZ","yes",p35tag("yes"))
 h:=r.Handler(http.HandlerFunc(func(http.ResponseWriter,*http.Request){}))
 req:=httptest.NewRequest("GET","/",nil);req.Header.Set("X-ZZZ","yes")
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{h.ServeHTTP(httptest.NewRecorder(),req)}
}
func BenchmarkP35P7ConstructOnce(b *testing.B){
 r:=RouteHeaders()
 for i:=0;i<128;i++{name:="X-P35-"+string(rune(1000+i));r.Route(name,"yes",p35tag("unused"))}
 req:=httptest.NewRequest("GET","/",nil)
 next:=http.HandlerFunc(func(http.ResponseWriter,*http.Request){})
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{r.Handler(next).ServeHTTP(httptest.NewRecorder(),req)}
}
