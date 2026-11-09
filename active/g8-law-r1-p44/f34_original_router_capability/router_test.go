package originalrouters

import (
 "net/http"
 "net/http/httptest"
 "sync"
 "testing"
)

func probe(h http.Handler,method,path string) (int,string) {
 req:=httptest.NewRequest(method,path,nil)
 rr:=httptest.NewRecorder()
 h.ServeHTTP(rr,req)
 return rr.Code,rr.Body.String()
}
func TestBothOriginalRoutersPreserveOldClient(t *testing.T) {
 for _,kind:=range []RouterKind{Chi,HTTPRouter} {
  h,e:=Build(kind,"v1");if e!=nil{t.Fatal(e)}
  status,body:=probe(h,"GET","/legacy")
  if status!=200||body!="old" {t.Fatalf("%s old: %d %q",kind,status,body)}
  status,body=probe(h,"GET","/item/a")
  if status!=200||body!="v1:a" {t.Fatalf("%s new: %d %q",kind,status,body)}
 }
}
func TestIndependentVersionsCoexist(t *testing.T) {
 for _,kind:=range []RouterKind{Chi,HTTPRouter}{
  v1,e:=Build(kind,"v1");if e!=nil{t.Fatal(e)}
  v2,e:=Build(kind,"v2");if e!=nil{t.Fatal(e)}
  if _,body:=probe(v1,"GET","/item/a");body!="v1:a" {t.Fatal(kind,body)}
  if _,body:=probe(v2,"GET","/item/a");body!="v2:a" {t.Fatal(kind,body)}
  if _,body:=probe(v1,"GET","/item/b");body!="v1:b" {t.Fatal(kind,body)}
 }
}
func TestRouterSwitchByRequestAgainstOriginalLibraries(t *testing.T){
 a,e:=Build(Chi,"v1");if e!=nil{t.Fatal(e)}
 b,e:=Build(HTTPRouter,"v2");if e!=nil{t.Fatal(e)}
 choose:=Pick(map[RouterKind]http.Handler{Chi:a,HTTPRouter:b})
 for _,tc:=range []struct{header,want string}{
  {"chi","v1:a"},{"httprouter","v2:a"},
 }{
  req:=httptest.NewRequest("GET","/item/a",nil);req.Header.Set("X-Router",tc.header)
  rec:=httptest.NewRecorder();choose(rec,req)
  if rec.Code!=200||rec.Body.String()!=tc.want{t.Fatalf("%s: %d/%q",tc.header,rec.Code,rec.Body.String())}
 }
}
func TestCallbackRivalMatchesInterfaceSelection(t *testing.T){
 a,_:=Build(Chi,"v1");b,_:=Build(HTTPRouter,"v2")
 handlers:=map[RouterKind]http.Handler{Chi:a,HTTPRouter:b}
 iface:=Pick(handlers)
 // A plain injected function is not less capable than this interface boundary.
 callback:=func(w http.ResponseWriter,r *http.Request) {iface(w,r)}
 for _,kind:=range []string{"chi","httprouter"} {
  req:=httptest.NewRequest("GET","/item/abc",nil);req.Header.Set("X-Router",kind)
  a1,b1:=httptest.NewRecorder(),httptest.NewRecorder()
  iface.ServeHTTP(a1,req)
  callback(b1,req)
  if a1.Code!=b1.Code||a1.Body.String()!=b1.Body.String(){t.Fatalf("callback mismatch: %s",kind)}
 }
}
func TestConcurrentOriginalRoutersIndependent(t *testing.T){
 a,_:=Build(Chi,"v1");b,_:=Build(HTTPRouter,"v2")
 var wg sync.WaitGroup
 for i:=0;i<32;i++{wg.Add(1);go func(i int){defer wg.Done()
  h,want:=a,"v1:z";if i%2==1{h=b;want="v2:z"}
  status,body:=probe(h,"GET","/item/z")
  if status!=200||body!=want{t.Errorf("case %d: %d %q",i,status,body)}
 }(i)}
 wg.Wait()
}
func TestUnknownRouterRefused(t *testing.T){
 h,_:=Build(Chi,"v1")
 chooser:=Pick(map[RouterKind]http.Handler{Chi:h})
 req:=httptest.NewRequest("GET","/legacy",nil)
 req.Header.Set("X-Router","unsupported")
 rr:=httptest.NewRecorder();chooser.ServeHTTP(rr,req)
 if rr.Code!=http.StatusBadRequest{t.Fatalf("not refused: %d",rr.Code)}
}
