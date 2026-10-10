package p40p4

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "strings"
 "testing"

 "github.com/go-chi/chi/v5"
)

const originalSourceCommit = "167e1e3bd039d060696b99c8da4e876ae04f42c1"

func mountRoot(name string) chi.Router {
 r := chi.NewRouter()
 r.Get("/", func(w http.ResponseWriter, req *http.Request) { fmt.Fprint(w, name) })
 r.Get("/item", func(w http.ResponseWriter, req *http.Request) { fmt.Fprint(w, name+":item") })
 return r
}
func originalParent() chi.Router {
 r:=chi.NewRouter()
 r.Get("/old", func(w http.ResponseWriter, req *http.Request){fmt.Fprint(w,"unchanged")})
 return r
}
func request(t *testing.T,h http.Handler,p,want string){
 t.Helper()
 w:=httptest.NewRecorder()
 req:=httptest.NewRequest(http.MethodGet,p,nil)
 h.ServeHTTP(w,req)
 if w.Code!=200 || strings.TrimSpace(w.Body.String())!=want {
  t.Fatalf("GET %s got (%d,%q) want (200,%q)",p,w.Code,w.Body.String(),want)
 }
}
func TestOriginalChiDistinctMountsPreserveOldAndOwnPaths(t *testing.T){
 r:=originalParent()
 r.Mount("/service/a",mountRoot("A"))
 r.Mount("/service/b",mountRoot("B"))
 request(t,r,"/old","unchanged")
 request(t,r,"/service/a/item","A:item")
 request(t,r,"/service/b/item","B:item")
 t.Log("P40_P4_ORIGINAL_CHI_SEPARATE_MOUNTS_PASS")
}
func TestOriginalChiMinimalDuplicateMountObstruction(t *testing.T){
 paths:=[]string{"/service/a","/service/b","/service/c"}
 successes,conflicts:=0,0
 for _,a:=range paths{
  for _,b:=range paths{
   singleA:=originalParent()
   singleA.Mount(a,mountRoot("A"))
   request(t,singleA,"/old","unchanged")
   request(t,singleA,a+"/item","A:item")
   singleB:=originalParent()
   singleB.Mount(b,mountRoot("B"))
   request(t,singleB,"/old","unchanged")
   request(t,singleB,b+"/item","B:item")
   together:=originalParent()
   together.Mount(a,mountRoot("A"))
   var recovered any
   func(){
    defer func(){recovered=recover()}()
    together.Mount(b,mountRoot("B"))
   }()
   if a==b{
    if recovered==nil || !strings.Contains(fmt.Sprint(recovered),"attempting to Mount() a handler on an existing path") {
      t.Fatalf("expected original chi duplicate mount panic for %s; got %#v",a,recovered)
    }
    conflicts++
   }else{
    if recovered!=nil{t.Fatalf("distinct namespaces unexpectedly conflict: %v",recovered)}
    request(t,together,"/old","unchanged")
    request(t,together,a+"/item","A:item")
    request(t,together,b+"/item","B:item")
    successes++
   }
  }
 }
 if successes!=6||conflicts!=3{t.Fatalf("joint counts success=%d conflicts=%d",successes,conflicts)}
 t.Logf("P40_P4_ORIGINAL_CHI_3X3_LOCAL_GLOBAL_BOUNDARY_PASS distinct=%d duplicate_minimal=%d",successes,conflicts)
}
func TestOriginalChiMiddlewareOrderGuard(t *testing.T){
 r:=originalParent()
 r.Mount("/service/a",mountRoot("A"))
 request(t,r,"/old","unchanged")
 var recovered any
 func(){
  defer func(){recovered=recover()}()
  r.Use(func(next http.Handler)http.Handler{return next})
 }()
 if recovered==nil||!strings.Contains(fmt.Sprint(recovered),"all middlewares must be defined before routes on a mux"){
  t.Fatalf("expected original mux middleware timing panic; got %#v",recovered)
 }
 r2:=chi.NewRouter()
 r2.Use(func(next http.Handler)http.Handler{return next})
 r2.Get("/old",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"unchanged")})
 r2.Mount("/service/a",mountRoot("A"))
 request(t,r2,"/old","unchanged")
 request(t,r2,"/service/a/item","A:item")
 t.Log("P40_P4_ORIGINAL_CHI_MIDDLEWARE_ORDER_GUARD_PASS")
}
