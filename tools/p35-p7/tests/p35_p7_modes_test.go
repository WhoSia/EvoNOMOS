package middleware
import ("net/http";"net/http/httptest";"testing")
func TestP35P7ConditionalMode(t *testing.T){
 next:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.Header().Set("X-P35-P7","next")})
 registry:=RouteHeaders()
 old:=registry.Handler(next)
 registry.Route("X-After","y",p35tag("late"))
 req:=httptest.NewRequest("GET","/",nil);req.Header.Set("X-After","y")
 rec:=httptest.NewRecorder();old.ServeHTTP(rec,req)
 got:=rec.Header().Get("X-P35-P7")
 // Different hypotheses are evaluated separately; the verdict for each
 // environment is in the CI receipt, not used to gate either arm out of D0.
 if got=="late"{t.Log("P35P7_D_LIVE_PASS__D_FROZEN_FAIL")}else if got=="next"{t.Log("P35P7_D_FROZEN_PASS__D_LIVE_FAIL")}else{t.Fatalf("P35P7_MODE_UNEXPECTED_RESPONSE=%q",got)}
}
