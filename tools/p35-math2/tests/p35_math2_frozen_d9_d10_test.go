package middleware

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

// D9 and D10 were frozen before either treatment source. Both architectures
// and both repair styles must satisfy this EXACT architecture-neutral oracle.
type p35M2HeaderField struct { Name string; Values []string }
func p35M2Check(t *testing.T,router HeaderRouter,fields []p35M2HeaderField,want string){
 t.Helper()
 next:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if w.Header().Get("X-P35-P7")=="" {w.Header().Set("X-P35-P7","next")}
 })
 h:=router.Handler(next)
 for repetition:=0;repetition<3;repetition++{
  req:=httptest.NewRequest("GET","/",nil)
  for _,f:=range fields {for _,v:=range f.Values {req.Header.Add(f.Name,v)}}
  rec:=httptest.NewRecorder()
  h.ServeHTTP(rec,req)
  if got:=rec.Header().Get("X-P35-P7");got!=want{
   t.Fatalf("P35_MATH2_ORACLE_FAILURE got=%q want=%q fields=%+v",got,want,fields)
  }
 }
}

func TestP35Math2D9RepeatedPhysicalHeaderFields(t *testing.T){
 cases:=[]struct{
  name string; route HeaderRouter; fields []p35M2HeaderField; want string
 }{
  {"second-physical-field-literal",
   RouteHeaders().Route("X-A","ping",p35tag("literal")),
   []p35M2HeaderField{{"X-A",[]string{"miss","ping"}}},"literal"},
  {"first-registered-wildcard-vs-later-literal",
   RouteHeaders().Route("X-A","p*",p35tag("first")).Route("X-A","ping",p35tag("second")),
   []p35M2HeaderField{{"X-A",[]string{"ping","pong"}}},"first"},
  {"cross-header-exact-beats-wildcard",
   RouteHeaders().Route("X-A","p*",p35tag("wild")).Route("X-B","ping",p35tag("exact")),
   []p35M2HeaderField{{"X-A",[]string{"miss","pong"}},{"X-B",[]string{"ping"}}},"exact"},
  {"route-any-on-later-physical-value",
   RouteHeaders().RouteAny("X-B",[]string{"z*","ping"},p35tag("any")),
   []p35M2HeaderField{{"X-B",[]string{"miss","ping"}}},"any"},
  {"empty-first-physical-value-is-not-rejection",
   RouteHeaders().Route("X-A","ping",p35tag("match")),
   []p35M2HeaderField{{"X-A",[]string{"","ping"}}},"match"},
  {"default-if-none-matches",
   RouteHeaders().Route("X-A","p*",p35tag("wild")).RouteDefault(p35tag("default")),
   []p35M2HeaderField{{"X-A",[]string{"miss","none"}}},"default"},
 }
 for _,tc:=range cases{t.Run(tc.name,func(t *testing.T){p35M2Check(t,tc.route,tc.fields,tc.want)})}
}

func TestP35Math2D10CommaDelimitedTokens(t *testing.T){
 cases:=[]struct{
  name string; route HeaderRouter; fields []p35M2HeaderField; want string
 }{
  {"second-comma-token-matches",
   RouteHeaders().Route("X-A","ping",p35tag("literal")),
   []p35M2HeaderField{{"X-A",[]string{"miss,ping"}}},"literal"},
  {"trim-whitespace-comma-token",
   RouteHeaders().Route("X-A","ping",p35tag("trimmed")),
   []p35M2HeaderField{{"X-A",[]string{" none , ping , pong "}}},"trimmed"},
  {"within-header-first-registered-wins",
   RouteHeaders().Route("X-A","p*",p35tag("first")).Route("X-A","ping",p35tag("later")),
   []p35M2HeaderField{{"X-A",[]string{"other, ping"}}},"first"},
  {"cross-header-literal-from-comma-beats-wildcard",
   RouteHeaders().Route("X-A","p*",p35tag("wild")).Route("X-B","ping",p35tag("exact")),
   []p35M2HeaderField{{"X-A",[]string{"pong"}},{"X-B",[]string{"miss, ping"}}},"exact"},
  {"mixed-physical-and-comma-fields",
   RouteHeaders().Route("X-B","ping",p35tag("mixed")),
   []p35M2HeaderField{{"X-B",[]string{"miss, none","foo, ping"}}},"mixed"},
  {"route-any-exact-in-comma-list",
   RouteHeaders().Route("X-A","p*",p35tag("wild")).RouteAny("X-B",[]string{"p*","ping"},p35tag("any")),
   []p35M2HeaderField{{"X-A",[]string{"pong"}},{"X-B",[]string{"miss, ping"}}},"any"},
  {"no-nonempty-matched-token-fallback",
   RouteHeaders().Route("X-A","ping",p35tag("route")).RouteDefault(p35tag("fallback")),
   []p35M2HeaderField{{"X-A",[]string{" , ,, "}}},"fallback"},
 }
 for _,tc:=range cases{t.Run(tc.name,func(t *testing.T){p35M2Check(t,tc.route,tc.fields,tc.want)})}
}
