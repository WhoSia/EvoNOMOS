package native
import("fmt";"io";"net/http";"net/http/httptest";"testing";"time";"evonomos/p44r3core")
func hit(c *http.Client,url,method,id string)(int,string,error){
 req,e:=http.NewRequest(method,url,nil);if e!=nil{return 0,"",e}
 req.Header.Set("X-Request-Id",id)
 res,e:=c.Do(req);if e!=nil{return 0,"",e};defer res.Body.Close()
 b,e:=io.ReadAll(res.Body);return res.StatusCode,string(b),e
}
func TestOriginalRouterSequentialOldContract(t *testing.T){
 for _,kind:=range []string{"stdlib","chi"}{for _,mode:=range []core.CaptureMode{core.LiveAlias,core.FrozenValue}{
  t.Run(fmt.Sprintf("%s-mode%d",kind,mode),func(t *testing.T){
   s:=core.NewShared("v1");srv:=httptest.NewServer(Build(kind,mode,s,nil));defer srv.Close();c:=srv.Client();c.Timeout=3*time.Second
   for _,p:=range []struct{path,method,id,want string}{
    {"/items/alpha","GET","req-A","v1|req-A"},
    {"/policy/alpha?label=v2","POST","req-B","updated:v2"},
    {"/items/alpha","GET","req-C","v2|req-C"},
   }{
    status,body,e:=hit(c,srv.URL+p.path,p.method,p.id)
    if e!=nil||status!=200||body!=p.want{t.Fatalf("%s status=%d body=%q err=%v want=%q",p.path,status,body,e,p.want)}
   }
  })
 }}
}
func TestOriginalRouterConcurrentAliasWitnessAndRepair(t *testing.T){
 for _,kind:=range []string{"stdlib","chi"}{for _,tc:=range []struct{mode core.CaptureMode;want string}{
  {core.LiveAlias,"v2|req-A"},{core.FrozenValue,"v1|req-A"},
 }{
  t.Run(fmt.Sprintf("%s-mode%d",kind,tc.mode),func(t *testing.T){
   s:=core.NewShared("v1");b:=core.NewBarrier();srv:=httptest.NewServer(Build(kind,tc.mode,s,b));defer srv.Close()
   c:=srv.Client();c.Timeout=4*time.Second
   type result struct{status int;body string;err error}
   ch:=make(chan result,1)
   go func(){status,body,e:=hit(c,srv.URL+"/items/alpha","GET","req-A");ch<-result{status,body,e}}()
   select{case <-b.Entered:case <-time.After(3*time.Second):close(b.Release);t.Fatal("capture did not begin")}
   status,body,e:=hit(c,srv.URL+"/policy/alpha?label=v2","POST","req-B")
   if e!=nil||status!=200||body!="updated:v2"{close(b.Release);t.Fatalf("update %d %q %v",status,body,e)}
   close(b.Release)
   var first result
   select{case first=<-ch:case <-time.After(3*time.Second):t.Fatal("GET did not complete")}
   if first.err!=nil||first.status!=200||first.body!=tc.want{t.Fatalf("mode=%d first=%+v want=%q",tc.mode,first,tc.want)}
   status,body,e=hit(c,srv.URL+"/items/alpha","GET","req-C")
   if e!=nil||status!=200||body!="v2|req-C"{t.Fatalf("subsequent GET %d %q %v",status,body,e)}
   t.Logf("SOURCE_WITNESS router=%s mode=%d before_update_get=%q after_update_get=%q",kind,tc.mode,first.body,body)
  })
 }}
}
