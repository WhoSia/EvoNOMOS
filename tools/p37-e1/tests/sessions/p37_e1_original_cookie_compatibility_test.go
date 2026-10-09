package sessions

import (
 "bytes"
 "net/http"
 "net/http/httptest"
 "testing"
)

// This test is copied as ONE additional file into the exact original
// gorilla/sessions Go module. Its original production store.go uses original
// securecookie.EncodeMulti/DecodeMulti in a separately pinned local checkout.
func p37E1Keys() ([]byte,[]byte){
 return bytes.Repeat([]byte{'A'},32), bytes.Repeat([]byte{'B'},32)
}
func p37E1Issue(t *testing.T,store *CookieStore)*http.Cookie{
 t.Helper()
 req:=httptest.NewRequest(http.MethodGet,"http://example.test/session",nil)
 sess,err:=store.New(req,"p37_e1")
 if err!=nil{t.Fatal(err)}
 sess.Values["stage"]="kept"
 reply:=httptest.NewRecorder()
 if err=store.Save(req,reply,sess);err!=nil{t.Fatal(err)}
 cookies:=reply.Result().Cookies()
 if len(cookies)!=1{t.Fatalf("issued %d cookies, expected 1",len(cookies))}
 return cookies[0]
}
func p37E1Accept(t *testing.T,reader *CookieStore, cookie *http.Cookie)bool{
 t.Helper()
 req:=httptest.NewRequest(http.MethodGet,"http://example.test/session",nil)
 req.AddCookie(cookie)
 sess,err:=reader.New(req,"p37_e1")
 return err==nil&&!sess.IsNew&&sess.Values["stage"]=="kept"
}
func TestP37E1ExactOriginalCompatibilityMatrix(t *testing.T){
 oldKey,newKey:=p37E1Keys()
 w0:=NewCookieStore(oldKey)
 w1:=NewCookieStore(newKey)
 r0:=NewCookieStore(oldKey)
 r1:=NewCookieStore(newKey)
 // Securecookie.CodecsFromPairs interprets every (hashKey, blockKey) as
 // ONE codec, so nil block keys must separate the two hash key entries.
 dual:=NewCookieStore(newKey,nil,oldKey,nil)
 if len(dual.Codecs)!=2{t.Fatalf("expected two original codecs, got %d",len(dual.Codecs))}
 oldCookie:=p37E1Issue(t,w0)
 newCookie:=p37E1Issue(t,w1)
 cases:=[]struct{name string;current *http.Cookie;reader *CookieStore;wantLive,wantLegacy bool}{
  {"W0_R0_INITIAL",oldCookie,r0,true,true},
  {"W1_R0_A_FIRST_BLOCKED",newCookie,r0,false,true},
  {"W0_R1_B_FIRST_BLOCKED",oldCookie,r1,false,false},
  {"W0_RSTAR_EXPANDED",oldCookie,dual,true,true},
  {"W1_RSTAR_BRIDGED",newCookie,dual,true,true},
  {"W1_R1_AFTER_HISTORY_EXPIRES_ONLY",newCookie,r1,true,false},
 }
 for _,tc:=range cases{
  t.Run(tc.name,func(t *testing.T){
   live:=p37E1Accept(t,tc.reader,tc.current)
   legacy:=p37E1Accept(t,tc.reader,oldCookie)
   if live!=tc.wantLive||legacy!=tc.wantLegacy{
    t.Fatalf("compatibility actual=(live=%v,legacy=%v) expected=(%v,%v)",live,legacy,tc.wantLive,tc.wantLegacy)
   }
  })
 }
}
func TestP37E1OriginalSafeSequentialMigration(t *testing.T){
 oldKey,newKey:=p37E1Keys()
 oldOnly,dual:=NewCookieStore(oldKey),NewCookieStore(newKey,nil,oldKey,nil)
 newOnly:=NewCookieStore(newKey)
 oldCookie:=p37E1Issue(t,oldOnly)
 newCookie:=p37E1Issue(t,newOnly)
 // The invariant must hold at EACH checkpoint; these are real original
 // CookieStore instances and original securecookie module decoders.
 stages:=[]struct{name string;current *http.Cookie;reader *CookieStore}{
  {"initial",oldCookie,oldOnly},
  {"B_expand_first",oldCookie,dual},
  {"A_switch_after_B_expansion",newCookie,dual},
 }
 for _,step:=range stages {
  if !p37E1Accept(t,step.reader,step.current) {t.Errorf("%s live invariant",step.name)}
  if !p37E1Accept(t,step.reader,oldCookie) {t.Errorf("%s legacy invariant",step.name)}
 }
 // The final contraction is forbidden during the OLD cookie compatibility
 // obligation, even though it accepts all newly issued cookies.
 if !p37E1Accept(t,newOnly,newCookie){t.Fatal("new reader did not accept current")}
 if p37E1Accept(t,newOnly,oldCookie){t.Fatal("new reader improperly preserves old-key history")}
}
