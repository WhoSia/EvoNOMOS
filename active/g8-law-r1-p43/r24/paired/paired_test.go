package paired
import("fmt";"io";"net/http";"net/http/httptest";"strings";"testing";"github.com/go-chi/chi/v5")
type Obs struct{Status int;Body,Allow,Location string}
func obs(h http.Handler,method,path string)(Obs,error){
 s:=httptest.NewServer(h);defer s.Close()
 c:=&http.Client{CheckRedirect:func(*http.Request,[]*http.Request)error{return http.ErrUseLastResponse}}
 r,e:=http.NewRequest(method,s.URL+path,nil);if e!=nil{return Obs{},e}
 res,e:=c.Do(r);if e!=nil{return Obs{},e};defer res.Body.Close()
 b,e:=io.ReadAll(res.Body);if e!=nil{return Obs{},e}
 return Obs{res.StatusCode,strings.TrimSpace(string(b)),res.Header.Get("Allow"),res.Header.Get("Location")},nil
}
func standard(stage int)http.Handler{
 m:=http.NewServeMux();m.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,r.PathValue("id"))})
 if stage>0{m.HandleFunc("GET /lookup/{id}",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"lookup:",r.PathValue("id"))})}
 if stage>1{m.HandleFunc("GET /lookup/{id}/meta",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"meta:",r.PathValue("id"))})}
 return m
}
func chiMux(stage int,head bool)http.Handler{
 m:=chi.NewRouter();handler:=func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,chi.URLParam(r,"id"))}
 m.Get("/items/{id}",handler);if head{m.Head("/items/{id}",handler)}
 if stage>0{m.Get("/lookup/{id}",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"lookup:",chi.URLParam(r,"id"))})}
 if stage>1{m.Get("/lookup/{id}/meta",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"meta:",chi.URLParam(r,"id"))})}
 return m
}
var baseline=[][2]string{{"GET","/items/alpha"},{"HEAD","/items/alpha"},{"GET","/items/123"},{"HEAD","/items/123"},{"GET","/items/"},{"GET","/items/alpha/"}}
var exploratory=[][2]string{{"POST","/items/alpha"},{"OPTIONS","/items/alpha"},{"GET","/items/a%2Fb"},{"GET","/items/%61lpha"},{"HEAD","/items/a%2Fb"},{"GET","/items/%2e%2e"}}
func equal(a,b Obs)bool{return a.Status==b.Status&&a.Body==b.Body&&a.Allow==b.Allow&&a.Location==b.Location}
func TestRawChiHEADCounterexample(t *testing.T){
 a,e:=obs(standard(0),"HEAD","/items/alpha");if e!=nil{t.Fatal(e)}
 b,e:=obs(chiMux(0,false),"HEAD","/items/alpha");if e!=nil{t.Fatal(e)}
 if a.Status!=200||b.Status==200{t.Fatalf("raw HEAD hypothesis failed std=%+v chi=%+v",a,b)}
 t.Logf("RAW_HEAD std=%+v chi=%+v",a,b)
 for _,p:=range exploratory{
  x,e:=obs(standard(0),p[0],p[1]);if e!=nil{t.Fatal(e)}
  y,e:=obs(chiMux(0,false),p[0],p[1]);if e!=nil{t.Fatal(e)}
  t.Logf("EXPLORATORY method=%s path=%s std=%+v chi=%+v equal=%v",p[0],p[1],x,y,equal(x,y))
 }
}
func TestDeclaredSixProbeMatchedBaseline(t *testing.T){
 for _,p:=range baseline{
  x,e:=obs(standard(0),p[0],p[1]);if e!=nil{t.Fatal(e)}
  y,e:=obs(chiMux(0,true),p[0],p[1]);if e!=nil{t.Fatal(e)}
  if !equal(x,y){t.Fatalf("unmatched method=%s path=%s std=%+v chi=%+v",p[0],p[1],x,y)}
 }
}
func TestStagewiseSafeSameRightsTie(t *testing.T){
 for stage:=0;stage<=2;stage++{
  a,b:=standard(stage),chiMux(stage,true)
  for _,p:=range baseline{
   x,e:=obs(a,p[0],p[1]);if e!=nil{t.Fatal(e)}
   y,e:=obs(b,p[0],p[1]);if e!=nil{t.Fatal(e)}
   if !equal(x,y){t.Fatalf("old-client violation stage=%d %s %s: %+v %+v",stage,p[0],p[1],x,y)}
  }
  goals:=[][2]string{}
  if stage>0{goals=append(goals,[2]string{"/lookup/alpha","lookup:alpha"})}
  if stage>1{goals=append(goals,[2]string{"/lookup/alpha/meta","meta:alpha"})}
  for _,p:=range goals{
   x,e:=obs(a,"GET",p[0]);if e!=nil{t.Fatal(e)}
   y,e:=obs(b,"GET",p[0]);if e!=nil{t.Fatal(e)}
   if x.Status!=200||y.Status!=200||x.Body!=p[1]||y.Body!=p[1]{t.Fatalf("new goal failed stage=%d std=%+v chi=%+v",stage,x,y)}
  }
  t.Logf("STAGE_SAFE stage=%d protected=%d new_goals=%d edit_units=%d both_structures=PASS",stage,len(baseline),len(goals),stage)
 }
}
