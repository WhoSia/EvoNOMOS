package chi

import (
 "net/http"
 "net/http/httptest"
 "strings"
 "testing"
)

// Retrospective source-intervention contract for real chi commit 4b14b832.
// Not a blinded predictor: selected after examining the historical patch.
func TestP35P6Historical405AllowContract(t *testing.T) {
 router:=NewRouter()
 router.Get("/known",func(w http.ResponseWriter,r *http.Request){w.WriteHeader(http.StatusOK)})
 req:=httptest.NewRequest(http.MethodPost,"http://example.test/known",nil)
 resp:=httptest.NewRecorder()
 router.ServeHTTP(resp,req)
 if resp.Code!=http.StatusMethodNotAllowed {t.Fatalf("got HTTP %d, want 405",resp.Code)}
 allowed:=resp.Header().Values("Allow")
 found:=false
 for _,entry:=range allowed{
  for _,part:=range strings.Split(entry,","){if strings.TrimSpace(part)==http.MethodGet{found=true}}
 }
 if !found{t.Fatalf("405 response must advertise GET in Allow header, got %v",allowed)}
 t.Log("P35_P6_REAL_405_ALLOW_HEADER_CONTRACT_PASS")
}
