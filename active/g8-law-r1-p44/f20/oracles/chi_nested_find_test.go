package chi
import ("net/http";"testing")
// Historical retrospective oracle, designed AFTER reading commit #954.
// This test is NOT a genuinely prospective sealed prediction.
func TestF20NestedRoutePattern(t *testing.T) {
 r:=NewRouter()
 r.Route("/api",func(r Router){
  r.Route("/groups",func(r Router){
   r.Route("/v2",func(r Router){
    r.Post("/{id}",func(w http.ResponseWriter,req *http.Request){w.WriteHeader(http.StatusNoContent)})
   })
  })
 })
 ctx:=NewRouteContext()
 got:=r.Find(ctx,"POST","/api/groups/v2/17")
 want:="/api/groups/v2/{id}"
 t.Logf("F20_CHI nested=%q expected=%q",got,want)
 if got!=want {t.Fatalf("nested Find contract: %q != %q",got,want)}
}
