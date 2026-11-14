package chi_test

// This is a research-owned external customer-contract fixture copied into an
// ephemeral original go-chi/chi checkout. It does not edit upstream sources.
import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "strings"
 "testing"

 "github.com/go-chi/chi/v5"
)

func evoIssue1188Router() http.Handler {
 r:=chi.NewRouter()
 handler:=func(w http.ResponseWriter, req *http.Request) {
  fmt.Fprint(w,chi.URLParam(req,"name"))
 }
 r.Get("/re/{name:[^.]+}.json",handler)
 r.Get("/bare/{name:[^.]+}",handler)
 r.Get("/plain/{name}.json",handler)
 return r
}
func evoIssue1188Get(r http.Handler,path string)(int,string) {
 rec:=httptest.NewRecorder()
 r.ServeHTTP(rec,httptest.NewRequest(http.MethodGet,path,nil))
 return rec.Code,strings.TrimSpace(rec.Body.String())
}
func TestEvoIssue1188OldClients(t *testing.T) {
 r:=evoIssue1188Router()
 cases:=[]struct{path,body string}{
  {"/re/a.json","a"},
  {"/re/b.json","b"},
  {"/bare/a","a"},
  {"/plain/a.json","a"},
 }
 for _,tc:=range cases{
  t.Run(tc.path,func(t *testing.T){
   status,body:=evoIssue1188Get(r,tc.path)
   if status!=http.StatusOK||body!=tc.body{
    t.Fatalf("old contract %q: got HTTP %d body %q, want 200 %q",tc.path,status,body,tc.body)
   }
  })
 }
}
func TestEvoIssue1188NewCustomerContract(t *testing.T) {
 r:=evoIssue1188Router()
 for _,path:=range []string{"/re/a/b.json","/bare/a/b","/plain/a/b.json"}{
  t.Run(path,func(t *testing.T){
   status,body:=evoIssue1188Get(r,path)
   if status!=http.StatusNotFound{
    t.Errorf("ISSUE1188_BROKEN_SEGMENT_CONTRACT path=%q status=%d body=%q want=404",path,status,body)
   }
  })
 }
}
