package middleware

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

// Frozen D11 source-independent acceptance. Synthetic header ONLY:
// CSV-style quoting of research field, not a claim about generic HTTP syntax.
func p35O3D11Got(reg HeaderRouter, vals []string) string {
 next:=http.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){if w.Header().Get("X-P35-P7")==""{w.Header().Set("X-P35-P7","next")}})
 req:=httptest.NewRequest(http.MethodGet,"/",nil)
 for _,v:=range vals{req.Header.Add("X-EvoNOMOS-Mode",v)}
 rec:=httptest.NewRecorder()
 reg.Handler(next).ServeHTTP(rec,req)
 return rec.Header().Get("X-P35-P7")
}
func TestP35O3D11QuotedResearchHeader(t *testing.T){
 tests:=[]struct{name string;reg HeaderRouter;values []string;want string}{
  {"quoted-comma-exact",RouteHeaders().Route("X-EvoNOMOS-Mode","pi,ng",p35tag("comma")),[]string{`"pi,ng"`},"comma"},
  {"quoted-single-token",RouteHeaders().Route("X-EvoNOMOS-Mode","ping",p35tag("single")),[]string{`"ping"`},"single"},
  {"double-quote-escape",RouteHeaders().Route("X-EvoNOMOS-Mode",`pi"ng`,p35tag("escaped")),[]string{`"pi""ng"`},"escaped"},
  {"quoted-comma-second-token",RouteHeaders().Route("X-EvoNOMOS-Mode","pi,ng",p35tag("second")),[]string{`miss, "pi,ng"`},"second"},
  {"repeated-physical-fields",RouteHeaders().Route("X-EvoNOMOS-Mode","pi,ng",p35tag("repeat")),[]string{"none",`"pi,ng"`},"repeat"},
  {"existing-unquoted-d10",RouteHeaders().Route("X-EvoNOMOS-Mode","ping",p35tag("legacy")),[]string{"none, ping"},"legacy"},
  {"missing-quote-must-not-partially-match",RouteHeaders().Route("X-EvoNOMOS-Mode","ping",p35tag("should-not")),[]string{`"ping`},"next"},
  {"malformed-first-field-valid-second",RouteHeaders().Route("X-EvoNOMOS-Mode","ping",p35tag("valid")),[]string{`"broken,ping`,"ping"},"valid"},
  {"route-any-double-quote",RouteHeaders().RouteAny("X-EvoNOMOS-Mode",[]string{"nomatch",`pi"ng`},p35tag("any")),[]string{`"pi""ng"`},"any"},
  {"quoted-wildcard-matches-one-token",RouteHeaders().Route("X-EvoNOMOS-Mode","pi*",p35tag("wild")),[]string{`"pi,ng"`},"wild"},
  {"unmatched-no-route",RouteHeaders().Route("X-EvoNOMOS-Mode","ping",p35tag("no")),[]string{`"none"`},"next"},
 }
 for _,tc:=range tests{
  t.Run(tc.name,func(t *testing.T){for i:=0;i<2;i++{
   if got:=p35O3D11Got(tc.reg,tc.values);got!=tc.want{t.Fatalf("P35_O3_D11_CONTRACT_FAILURE got=%q want=%q values=%q",got,tc.want,tc.values)}
  }})
 }
}
