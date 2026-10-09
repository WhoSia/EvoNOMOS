package middleware

import (
  "bytes"
  "net/http"
  "net/http/httptest"
  "testing"
)

// P35-P4 acceptance oracle; frozen before any arm implementation.
// Compare the same public HTTP behavior for unchanged, independently parsed,
// and shared-parser treatments at upstream go-chi/chi@v5.1.0.
func TestP35P4CanonicalContentPolicy(t *testing.T) {
 cases:=[]struct{
  name string
  value string
  body bool
  only string
  want int
 }{
  {"quoted_charset", `application/json; charset="UTF-8"`,true,"both",200},
  {"reordered_params", `application/json; note="alpha;beta"; charset="Utf-8"`,true,"both",200},
  {"casefold_and_spacing", `Application/JSON ; ChArSeT = "utf-8"`,true,"both",200},
  {"unquoted_normal",`application/json; charset=utf-8`,true,"both",200},
  {"unrelated_quoted_semicolon",`application/json; x="a;b"; charset=utf-8`,true,"both",200},
  {"different_charset",`application/json; charset=iso-8859-1`,true,"both",415},
  {"different_type",`text/plain; charset=utf-8`,true,"both",415},
  {"malformed_quoted_charset",`application/json; charset="UTF-8`,true,"both",415},
  {"malformed_unrelated_param",`application/json; a="b`,true,"type",415},
  {"duplicate_charset",`application/json; charset=utf-8; charset=latin-1`,true,"both",415},
  {"charset_missing_not_allowed",`application/json; foo=bar`,true,"both",415},
  {"charset_missing_allowed",`application/json; foo=bar`,true,"optional",200},
  {"bodyless_bypass_type",``,false,"type",200},
  {"missing_type_with_body",``,true,"type",415},
  {"charset_only_quoted",`text/plain; charset="utf-8"`,true,"charset",200},
  {"charset_only_malformed",`text/plain; charset="utf-8`,true,"charset",415},
 }
 for _,tt:=range cases {
  t.Run(tt.name,func(t *testing.T){
   requestBody:=[]byte("hello")
   if !tt.body {requestBody=nil}
   request:=httptest.NewRequest(http.MethodPost,"http://example.test/",bytes.NewReader(requestBody))
   if tt.value!="" {request.Header.Set("Content-Type",tt.value)}
   handler:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.WriteHeader(http.StatusOK)})
   useType:=tt.only=="both"||tt.only=="type"||tt.only=="optional"
   useCharset:=tt.only=="both"||tt.only=="charset"||tt.only=="optional"
   if useCharset {
    if tt.only=="optional"{handler=asHandler(ContentCharset("UTF-8","")(handler))}else{handler=asHandler(ContentCharset("UTF-8")(handler))}
   }
   if useType {handler=asHandler(AllowContentType("application/json")(handler))}
   recorder:=httptest.NewRecorder()
   handler.ServeHTTP(recorder,request)
   if recorder.Code!=tt.want {t.Errorf("P35P4_POLICY_FAILURE %s status=%d want=%d value=%q",tt.name,recorder.Code,tt.want,tt.value)}
  })
 }
}
func asHandler(h http.Handler) http.HandlerFunc {
 return func(w http.ResponseWriter,r *http.Request){h.ServeHTTP(w,r)}
}
