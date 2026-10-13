package mux_test
import(
 "net/http"
 "net/http/httptest"
 "testing"
 "github.com/gorilla/mux"
)
func TestR11P8RealGorillaOriginalRetainedVars(t *testing.T) {
 r:=mux.NewRouter()
 var firstVars map[string]string
 var secondVars map[string]string
 count:=0
 r.HandleFunc("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  count++
  v:=mux.Vars(req)
  if v["id"]=="Ada"{firstVars=v}
  if v["id"]=="Bob"{secondVars=v}
  w.WriteHeader(200);w.Write([]byte("OLD"))
 }).Methods("GET")
 for _,name:=range []string{"Ada","Bob"}{
  rec:=httptest.NewRecorder()
  r.ServeHTTP(rec,httptest.NewRequest("GET","/users/"+name,nil))
  if rec.Code!=200 || rec.Body.String()!="OLD"{t.Fatalf("old contract %d %q",rec.Code,rec.Body.String())}
 }
 if count!=2||firstVars==nil||secondVars==nil||firstVars["id"]!="Ada"||secondVars["id"]!="Bob"{t.Fatalf("unexpected original Gorilla vars: %v %v",firstVars,secondVars)}
 t.Logf("R11_P8_NATIVE_GORILLA_INDEPENDENT_RETAINED_ROUTE_VARS_PASS after=%s",firstVars["id"])
}
