package p37c1_test

import (
 "bytes"
 "encoding/json"
 "errors"
 "net/http"
 "net/http/httptest"
 "reflect"
 "sync"
 "testing"

 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/archive"
 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/ingress"
)
func consume(t *testing.T,a *archive.Store,raw []byte,forward bool)[]byte{
 t.Helper()
 handler:=ingress.New(a,forward)
 post:=httptest.NewRecorder()
 handler.ServeHTTP(post,httptest.NewRequest(http.MethodPost,"/events",bytes.NewReader(raw)))
 if post.Code!=204{t.Fatalf("POST actual=%d body=%s",post.Code,post.Body.String())}
 get:=httptest.NewRecorder()
 handler.ServeHTTP(get,httptest.NewRequest(http.MethodGet,"/state",nil))
 if get.Code!=200{t.Fatalf("GET actual=%d",get.Code)}
 var x struct{ID int `json:"id"`;Revision int `json:"revision"`}
 if err:=json.Unmarshal(get.Body.Bytes(),&x);err!=nil{t.Fatal(err)}
 if x.ID!=7{t.Fatalf("current state id %d",x.ID)}
 return append([]byte(nil),get.Body.Bytes()...)
}
func TestP37C1SameLegacyObservationAcrossFourWorlds(t *testing.T){
 plain:=[]byte(`{"id":7}`)
 escaped:=[]byte(`{"i\u0064":7}`)
 var baseline []byte
 for _,forward:=range []bool{false,true}{
  for _,doc:=range [][]byte{plain,escaped}{
   a:=archive.New()
   got:=consume(t,a,doc,forward)
   if baseline==nil{baseline=got}
   if !bytes.Equal(got,baseline){t.Fatalf("Q0 observable world changed: %s vs %s",got,baseline)}
   id,rev:=a.State()
   if id!=7||rev!=1{t.Fatalf("state id %d revision %d",id,rev)}
  }
 }
}
func TestP37C1OwnerBRepairCanRecoverWhenIngressRetainedRaw(t *testing.T){
 cases:=[]struct{payload,want string}{
  {`{"id":7}`,`"id"`},
  {`{"i\u0064":7}`,`"i\u0064"`},
 }
 for _,tc:=range cases{
  a:=archive.New()
  consume(t,a,[]byte(tc.payload),true)
  got,err:=a.OriginalKeyAt(0)
  if err!=nil||got!=tc.want{t.Fatalf("Q23 historical raw key got=%q want=%q err=%v",got,tc.want,err)}
 }
}
func TestP37C1OwnerBLossyHistoricalWorldsIndistinguishable(t *testing.T){
 a:=archive.New();b:=archive.New()
 consume(t,a,[]byte(`{"id":7}`),false)
 consume(t,b,[]byte(`{"i\u0064":7}`),false)
 ea,_:=a.EventAt(0);eb,_:=b.EventAt(0)
 if !reflect.DeepEqual(ea,eb){t.Fatalf("lossy histories retained distinguishing data: %#v %#v",ea,eb)}
 if _,err:=a.OriginalKeyAt(0);!errors.Is(err,archive.ErrNoOriginal){t.Fatalf("unexpected raw recovery from collapsed plain history: %v",err)}
 if _,err:=b.OriginalKeyAt(0);!errors.Is(err,archive.ErrNoOriginal){t.Fatalf("unexpected raw recovery from collapsed escaped history: %v",err)}
}
func TestP37C1IngressPolicyChangeProtectsFutureNotHistory(t *testing.T){
 a:=archive.New()
 consume(t,a,[]byte(`{"id":7}`),false)
 consume(t,a,[]byte(`{"i\u0064":7}`),true)
 if _,err:=a.OriginalKeyAt(0);!errors.Is(err,archive.ErrNoOriginal){t.Fatalf("historical recovery without replay: %v",err)}
 got,err:=a.OriginalKeyAt(1)
 if err!=nil||got!=`"i\u0064"`{t.Fatalf("new event provenance lost %q %v",got,err)}
 id,rev:=a.State()
 if id!=7||rev!=2{t.Fatalf("state=%d,%d",id,rev)}
}
func TestP37C1ConcurrentReadersPreserveLegacyContract(t *testing.T){
 a:=archive.New();consume(t,a,[]byte(`{"i\u0064":7}`),true)
 h:=ingress.New(a,true)
 var wg sync.WaitGroup
 errs:=make(chan string,16)
 for i:=0;i<16;i++ {wg.Add(1);go func(){defer wg.Done();for j:=0;j<32;j++{
  response:=httptest.NewRecorder()
  h.ServeHTTP(response,httptest.NewRequest(http.MethodGet,"/state",nil))
  if response.Code!=200{errs<-"wrong code";return}
  lex,err:=a.OriginalKeyAt(0)
  if err!=nil||lex!=`"i\u0064"`{errs<-"wrong lexeme";return}
 }}()}
 wg.Wait();close(errs)
 for s:=range errs{t.Error(s)}
}
