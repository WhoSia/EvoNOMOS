package middleware

import (
  "bytes"
  "net/http"
  "net/http/httptest"
  "strings"
  "testing"
)

// Original real chi source receives this second-demand test only after
// P35-P4 D4 alternatives have passed the earlier frozen oracle.
func TestP35P4BHeaderLengthBudget(t *testing.T) {
 const capBytes=128
 prefix:=`application/json; note="`
 suffix:=`"; charset="UTF-8"`
 if len(prefix)+len(suffix)>=capBytes {t.Fatal("test fixture design error")}
 exact:=prefix+strings.Repeat("a",capBytes-len(prefix)-len(suffix))+suffix
 over:=prefix+strings.Repeat("a",capBytes-len(prefix)-len(suffix)+1)+suffix
 if len(exact)!=128||len(over)!=129 {t.Fatal("boundary fixture error")}
 cases:=[]struct{name,header,mode string;body bool;want int}{
 {"exact_128_combined",exact,"both",true,200},
 {"over_129_combined",over,"both",true,415},
 {"over_129_charset",over,"charset",true,415},
 {"over_129_type",over,"type",true,415},
 {"short_valid",`application/json; charset="UTF-8"`,"both",true,200},
 {"bodyless_type_bypass",over,"type",false,200},
 }
 for _,c:=range cases {
  t.Run(c.name,func(t *testing.T){
   var body []byte
   if c.body {body=[]byte("x")}
   r:=httptest.NewRequest(http.MethodPost,"http://example.test/",bytes.NewReader(body))
   r.Header.Set("Content-Type",c.header)
   var handler http.Handler=http.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){w.WriteHeader(http.StatusOK)})
   if c.mode=="both"||c.mode=="charset"{handler=ContentCharset("UTF-8")(handler)}
   if c.mode=="both"||c.mode=="type"{handler=AllowContentType("application/json")(handler)}
   rec:=httptest.NewRecorder();handler.ServeHTTP(rec,r)
   if rec.Code!=c.want{t.Errorf("P35P4B_LENGTH_BUDGET_FAILURE %s status=%d want=%d inputlen=%d",c.name,rec.Code,c.want,len(c.header))}
  })
 }
}
