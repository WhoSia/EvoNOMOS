package chi

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "testing"
 "github.com/go-chi/chi/v5"
)

// EXPLORATORY AFTER prereg: logically independent old-client frame obligation.
// Explicitly excluded from the 16 locked admission forecasts.
func TestP40P4OldClientHeaderFrameIndependentOfSourceAdmission(t *testing.T){
 fresh:=func(addHeader bool) chi.Router{
  parent:=chi.NewRouter()
  if addHeader{
   // Registered before any route; this is legal native source staging.
   parent.Use(func(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
     w.Header().Set("X-P40-Frame","altered")
     next.ServeHTTP(w,r)
    })
   })
  }
  parent.Get("/old",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"unchanged")})
  child:=chi.NewRouter()
  child.Get("/item",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"new")})
  parent.Mount("/pros/frame",child)
  return parent
 }
 read:=func(p chi.Router,path string)*httptest.ResponseRecorder{
  out:=httptest.NewRecorder()
  p.ServeHTTP(out,httptest.NewRequest(http.MethodGet,path,nil))
  return out
 }
 clean:=fresh(false)
 changed:=fresh(true)
 for _, p:=range []chi.Router{clean,changed}{
  old:=read(p,"/old")
  newClient:=read(p,"/pros/frame/item")
  if old.Code!=200 || old.Body.String()!="unchanged" || newClient.Code!=200 || newClient.Body.String()!="new"{
   t.Fatalf("all source edits must be accepted and old/new bodies preserved")
  }
 }
 if read(clean,"/old").Header().Get("X-P40-Frame")!=""{
  t.Fatal("control violates declared old client header")
 }
 if read(changed,"/old").Header().Get("X-P40-Frame")!="altered"{
  t.Fatal("expected old client header change from legal middleware")
 }
 t.Log("P40_P4_OLD_CLIENT_FRAME_INDEPENDENT_OF_ADMISSION_GUARDS_ORIGINAL_CHI_PASS")
}
