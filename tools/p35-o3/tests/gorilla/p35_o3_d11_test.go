package mux

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

func p35O3GMatch(regex bool, expression string, physical []string) bool {
 r:=NewRouter()
 route:=r.NewRoute()
 if regex {route.HeadersRegexp("X-EvoNOMOS-Mode",expression)} else {route.Headers("X-EvoNOMOS-Mode",expression)}
 route.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){w.WriteHeader(http.StatusNoContent)})
 req:=httptest.NewRequest(http.MethodGet,"/",nil)
 for _,v:=range physical{req.Header.Add("X-EvoNOMOS-Mode",v)}
 rec:=httptest.NewRecorder();r.ServeHTTP(rec,req)
 return rec.Code==http.StatusNoContent
}
func TestP35O3D11GorillaHeadersAndRegex(t *testing.T){
 tests:=[]struct{name string;value string;raw []string;expected bool}{
  {"quoted-comma", "pi,ng",[]string{`"pi,ng"`},true},
  {"plain-quoted","ping",[]string{`"ping"`},true},
  {"escaped-double-quote",`pi"ng`,[]string{`"pi""ng"`},true},
  {"second-token","pi,ng",[]string{`other, "pi,ng"`},true},
  {"repeated-fields","pi,ng",[]string{"other",`"pi,ng"`},true},
  {"unquoted-compatibility","ping",[]string{"ping"},true},
  {"unquoted-comma-added","ping",[]string{"other, ping"},true},
  {"malformed-no-partial-match","ping",[]string{`"ping`},false},
  {"malformed-field-valid-second","ping",[]string{`"broken,ping`,"ping"},true},
  {"nonmatch","ping",[]string{`"other"`},false},
 }
 for _,tt:=range tests{
  t.Run(tt.name,func(t *testing.T){
   for _,regex:=range []bool{false,true}{
    pattern:=tt.value
    if regex {pattern="^"+tt.value+"$"}
    got:=p35O3GMatch(regex,pattern,tt.raw)
    if got!=tt.expected{t.Errorf("P35_O3_D11_CONTRACT_FAILURE regex=%t got=%t want=%t fields=%q",regex,got,tt.expected,tt.raw)}
   }
  })
 }
}
