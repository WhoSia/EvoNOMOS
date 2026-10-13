package chi_test
import(
 "net/http"
 "net/http/httptest"
 "runtime"
 "runtime/debug"
 "testing"
 "github.com/go-chi/chi/v5"
)
func TestR11P8RealChiOldSourceContextLifetime(t *testing.T) {
 oldP:=runtime.GOMAXPROCS(1); defer runtime.GOMAXPROCS(oldP)
 oldGC:=debug.SetGCPercent(-1);defer debug.SetGCPercent(oldGC)
 r:=chi.NewRouter()
 var captured *chi.Context
 var firstValue,secondValue string
 var second *chi.Context
 count:=0
 r.Get("/users/{id}",func(w http.ResponseWriter, req *http.Request){
  count++
  ctx:=chi.RouteContext(req.Context())
  got:=chi.URLParam(req,"id")
  if got=="Ada"{captured=ctx;firstValue=got}
  if got=="Bob"{second=ctx;secondValue=got}
  w.WriteHeader(200);w.Write([]byte("OLD"))
 })
 for _,name:=range []string{"Ada","Bob"} {
  rec:=httptest.NewRecorder()
  r.ServeHTTP(rec,httptest.NewRequest("GET","/users/"+name,nil))
  if rec.Code!=200||rec.Body.String()!="OLD"{t.Fatalf("old source contract: %v %q",rec.Code,rec.Body.String())}
 }
 if count!=2||firstValue!="Ada"||secondValue!="Bob"||captured==nil||second==nil{t.Fatal("incorrect original Chi source routing baseline")}
 reuse:=captured==second
 retained:=captured.URLParam("id")
 if reuse && retained!="Bob"{t.Fatalf("pooled reused source context should now carry second route: %q",retained)}
 if !reuse && retained!="Ada"{t.Fatalf("unreused source context unexpectedly modified: %q",retained)}
 stableClientSnapshot:=firstValue
 if stableClientSnapshot!="Ada"{t.Fatal("source-observation consumer snapshot failed")}
 t.Logf("R11_P8_NATIVE_CHI_CONTEXT_LIFETIME_RISK_WITNESS_PASS alias=%v first=Ada after=%q copied_snapshot=%q",reuse,retained,stableClientSnapshot)
}
