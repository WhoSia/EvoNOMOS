package middleware

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

func evo1247Tag(label string) func(http.Handler) http.Handler {
 return func(next http.Handler) http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
   w.Header().Set("X-Evo1247-Tag",label)
   next.ServeHTTP(w,r)
  })
 }
}
func evo1247Request(h http.Handler, header, value string) string {
 req:=httptest.NewRequest(http.MethodGet,"/route",nil)
 if value!="" {req.Header.Set(header,value)}
 rec:=httptest.NewRecorder()
 h.ServeHTTP(rec,req)
 return rec.Header().Get("X-Evo1247-Tag")
}
func evo1247Build(mode string, match string, any []string) http.Handler {
 registry:=RouteHeaders()
 switch mode {
 case "route":registry.Route("X-Tier",match,evo1247Tag("matched"))
 case "any":registry.RouteAny("X-Tier",any,evo1247Tag("matched"))
 default:panic("unknown test mode")
 }
 registry.RouteDefault(evo1247Tag("fallback"))
 return registry.Handler(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){}))
}
func TestEvo1247OriginalOldClientContract(t *testing.T) {
 cases:=[]struct{name,mode,pattern,headerValue string;any []string;want string}{
  {"lowercase-pattern-with-mixed-value","route","gold","Gold",nil,"matched"},
  {"lowercase-wildcard","route","g*","Gold",nil,"matched"},
  {"lowercase-suffix","route","*old","Gold",nil,"matched"},
  {"lowercase-any","any","","Gold",[]string{"silver","gold"},"matched"},
  {"unmatched-value-falls-back","route","silver","Gold",nil,"fallback"},
  {"missing-header-falls-back","route","gold","",nil,"fallback"},
 }
 for _,tc:=range cases{
  t.Run(tc.name,func(t *testing.T){
   got:=evo1247Request(evo1247Build(tc.mode,tc.pattern,tc.any),"X-Tier",tc.headerValue)
   if got!=tc.want{t.Fatalf("EVO1247_OLD_CONTRACT got=%q want=%q",got,tc.want)}
  })
 }
}
func TestEvo1247LaterIndependentDemand(t *testing.T){
 cases:=[]struct{name,mode,pattern,headerValue string;any []string}{
  {"issue-exact-Gold","route","Gold","Gold",nil},
  {"issue-route-any-Gold","any","","Gold",[]string{"Silver","Gold"}},
  {"research-wildcard-prefix-Go","route","Go*","Gold",nil},
  {"research-wildcard-suffix-OlD","route","*OlD","Gold",nil},
 }
 for _,tc:=range cases{
  t.Run(tc.name,func(t *testing.T){
   got:=evo1247Request(evo1247Build(tc.mode,tc.pattern,tc.any),"X-Tier",tc.headerValue)
   if got!="matched"{
    t.Errorf("EVO1247_NEW_CONTRACT_FAIL case=%q got=%q want=matched",tc.name,got)
   }
  })
 }
}
