package httprouter
import("net/http";"strings";"testing")
// Retrospective historical fix oracle. Preserve separate prior behavior.
func TestF20AllowedOptionsDisabled(t *testing.T){
 r:=New()
 r.GET("/probe",func(w http.ResponseWriter,req *http.Request,p Params){})
 r.HandleOPTIONS=false
 got:=r.allowed("/probe",http.MethodPost)
 t.Logf("F20_HTTPROUTER allow_when_options_disabled=%q",got)
 if strings.Contains(got,http.MethodOptions){t.Fatalf("unexpected OPTIONS in Allow when disabled: %q",got)}
 if !strings.Contains(got,http.MethodGet){t.Fatalf("lost existing GET method: %q",got)}
}
