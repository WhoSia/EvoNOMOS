package chi_test
import (
  "net/http"
  "net/http/httptest"
  "runtime"
  "runtime/debug"
  "testing"
  "github.com/go-chi/chi/v5"
)
func TestR11P8OriginalMergedMaintainerContextClone(t *testing.T) {
 oldP:=runtime.GOMAXPROCS(1);defer runtime.GOMAXPROCS(oldP)
 oldGC:=debug.SetGCPercent(-1);defer debug.SetGCPercent(oldGC)
 r:=chi.NewRouter()
 var heldOriginal,heldClone *chi.Context
 firstValue,secondValue:="",""
 calls:=0
 r.Get("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  calls++
  v:=chi.URLParam(req,"id")
  if v=="Ada" {
   heldOriginal=chi.RouteContext(req.Context())
   heldClone=heldOriginal.Clone() // crucial: during request BEFORE handler returns
   firstValue=v
  }
  if v=="Bob"{secondValue=v}
  w.WriteHeader(200);w.Write([]byte("OLD"))
 })
 for _,name:=range []string{"Ada","Bob"} {
  recorder:=httptest.NewRecorder()
  r.ServeHTTP(recorder,httptest.NewRequest("GET","/users/"+name,nil))
  if recorder.Code!=200 || recorder.Body.String()!="OLD"{t.Fatalf("original retained old-client HTTP contract: %d %s",recorder.Code,recorder.Body.String())}
 }
 if calls!=2 || firstValue!="Ada" || secondValue!="Bob" || heldOriginal==nil || heldClone==nil {t.Fatalf("original route dispatch mismatch")}
 if heldClone==heldOriginal || heldClone.URLParam("id")!="Ada" {
  t.Fatalf("actual upstream Clone failed to retain first request: %q",heldClone.URLParam("id"))
 }
 t.Logf("R11_P8_ACTUAL_MERGED_UPSTREAM_CHI_CLONE_NATIVE_PASS original_after=%q clone_after=%q source_original=true",heldOriginal.URLParam("id"),heldClone.URLParam("id"))
}
