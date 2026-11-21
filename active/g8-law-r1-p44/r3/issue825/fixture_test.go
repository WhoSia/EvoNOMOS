package issue825
import("io";"net/http";"net/http/httptest";"strings";"testing")
func measure(t *testing.T,kind string,preserve bool,supplied string)(string,string){
 t.Helper();s:=httptest.NewServer(Build(kind,preserve));defer s.Close()
 req,e:=http.NewRequest("GET",s.URL+"/id",nil);if e!=nil{t.Fatal(e)}
 if supplied!=""{req.Header.Set("X-Request-Id",supplied)}
 res,e:=s.Client().Do(req);if e!=nil{t.Fatal(e)};defer res.Body.Close()
 b,e:=io.ReadAll(res.Body);if e!=nil{t.Fatal(e)}
 if res.StatusCode!=200{t.Fatalf("status=%d",res.StatusCode)}
 return res.Header.Get("X-Outer-Observed"),strings.TrimSpace(string(b))
}
func TestUpstreamReport825ReproducedOnOriginalSource(t *testing.T){
 for _,kind:=range []string{"stdlib","chi"}{
  outer,inner:=measure(t,kind,false,"")
  if outer==""||inner==""||outer==inner{t.Fatalf("unexpected raw request ID kind=%s outer=%q inner=%q",kind,outer,inner)}
  t.Logf("EXTERNAL_825_RAW router=%s ids_nonempty=true same=%v",kind,outer==inner)
 }
}
func TestExplicitHeaderOldClientPreserved(t *testing.T){
 for _,kind:=range []string{"stdlib","chi"}{for _,preserve:=range []bool{false,true}{
  outer,inner:=measure(t,kind,preserve,"user-7")
  if outer!="user-7"||inner!="user-7"{t.Fatalf("kind=%s repair=%v got %q,%q",kind,preserve,outer,inner)}
 }}
}
func TestAppOnlyBridgeRestoresExternalContract(t *testing.T){
 for _,kind:=range []string{"stdlib","chi"}{
  outer,inner:=measure(t,kind,true,"")
  if outer==""||outer!=inner{t.Fatalf("kind=%s bridge mismatched %q,%q",kind,outer,inner)}
  t.Logf("EXTERNAL_825_BRIDGE router=%s nonempty=true same=%v",kind,outer==inner)
 }
}
