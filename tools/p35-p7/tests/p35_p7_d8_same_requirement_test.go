package middleware
import("net/http";"testing")
func TestP35P7D8IdenticalNewDemand(t *testing.T){
 next:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){if w.Header().Get("X-P35-P7")==""{w.Header().Set("X-P35-P7","next")}})
 testCases:=[]struct{name string;registry HeaderRouter;headers map[string]string;want string}{
  {"later-exact-over-earlier-wildcard",RouteHeaders().Route("X-A","p*",p35tag("wild")).Route("X-B","ping",p35tag("exact")),map[string]string{"X-A":"ping","X-B":"ping"},"exact"},
  {"two-wildcards-lexical",RouteHeaders().Route("X-A","p*",p35tag("wildA")).Route("X-B","p*",p35tag("wildB")),map[string]string{"X-A":"ping","X-B":"ping"},"wildA"},
  {"within-one-header-registration-order",RouteHeaders().Route("X-A","p*",p35tag("firstWild")).Route("X-A","ping",p35tag("laterExact")),map[string]string{"X-A":"ping"},"firstWild"},
  {"route-any-exact-pattern-matches",RouteHeaders().Route("X-A","p*",p35tag("wild")).RouteAny("X-B",[]string{"p*","ping"},p35tag("anyExact")),map[string]string{"X-A":"ping","X-B":"ping"},"anyExact"},
  {"fallback-without-match",RouteHeaders().Route("X-A","p*",p35tag("wild")).RouteDefault(p35tag("fallback")),map[string]string{"X-A":"nope"},"fallback"},
 }
 for _,tc:=range testCases{
  t.Run(tc.name,func(t *testing.T){h:=tc.registry.Handler(next);for i:=0;i<5;i++{got:=p35request(h,tc.headers);if got!=tc.want{t.Fatalf("P35P7_D8_SPECIFICITY_FAILURE got=%q want=%q",got,tc.want)}}})
 }
}
