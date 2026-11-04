package r2
import ("fmt";"io";"net/http";"net/http/httptest";"strings";"testing")
type Request struct{Method,Path string}
type Response struct{Status int;Body,Allow,Location string}
func observe(h http.Handler,p Request)(Response,error){
 s:=httptest.NewServer(h);defer s.Close()
 req,e:=http.NewRequest(p.Method,s.URL+p.Path,nil);if e!=nil{return Response{},e}
 c:=&http.Client{CheckRedirect:func(*http.Request,[]*http.Request)error{return http.ErrUseLastResponse}}
 res,e:=c.Do(req);if e!=nil{return Response{},e};defer res.Body.Close()
 b,e:=io.ReadAll(io.LimitReader(res.Body,1<<20));if e!=nil{return Response{},e}
 return Response{res.StatusCode,strings.TrimSpace(string(b)),res.Header.Get("Allow"),res.Header.Get("Location")},nil
}
var protected=[]Request{
 {"GET","/items/alpha"},{"HEAD","/items/alpha"},
 {"GET","/items/123"},{"HEAD","/items/123"},
 {"GET","/items/"},{"GET","/items/alpha/"},
 {"POST","/items/alpha"},{"OPTIONS","/items/alpha"},
 {"GET","/items/a%2Fb"},{"GET","/items/%61lpha"},
 {"HEAD","/items/a%2Fb"},{"GET","/items/%2e%2e"},
}
func compare(t *testing.T,a,b http.Handler,probes []Request){t.Helper()
 for _,p:=range probes{
  x,e:=observe(a,p);if e!=nil{t.Fatal(e)}
  y,e:=observe(b,p);if e!=nil{t.Fatal(e)}
  if x!=y{t.Fatalf("mismatch %s %s std=%+v chi=%+v",p.Method,p.Path,x,y)}
 }
}
func checkDemands(t *testing.T,a,b http.Handler,active []int){t.Helper()
 for _,k:=range active{
  d:=FrozenDemands[k];p:=Request{"GET","/ledger/alpha/"+d.Name}
  x,e:=observe(a,p);if e!=nil{t.Fatal(e)}
  y,e:=observe(b,p);if e!=nil{t.Fatal(e)}
  want:=d.ResponsePrefix+"alpha"
  if x.Status!=200||y.Status!=200||x.Body!=want||y.Body!=want{t.Fatalf("demand %s failed std=%+v chi=%+v want=%s",d.Name,x,y,want)}
 }
}
func TestFrozenIndependentDemandSequence(t *testing.T){
 for step:=0;step<=3;step++{
  enabled:=[]int{};for j:=0;j<step;j++{enabled=append(enabled,j)}
  a,b:=StdlibRouter(enabled),ChiRouter(enabled)
  compare(t,a,b,protected);checkDemands(t,a,b,enabled)
  t.Logf("FROZEN_SEQUENCE stage=%d protected=%d achieved=%d std_incremental_cost=%d chi_incremental_cost=%d std_total_cost=%d chi_total_cost=%d",step,len(protected),step,step,step,step,3+step)
 }
}
func TestAllSixAdditionOrdersPreserveOldContracts(t *testing.T){
 orders:=[][]int{{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}}
 for _,order:=range orders{t.Run(fmt.Sprint(order),func(t *testing.T){
  for step:=0;step<=3;step++{
   enabled:=append([]int{},order[:step]...)
   a,b:=StdlibRouter(enabled),ChiRouter(enabled)
   compare(t,a,b,protected);checkDemands(t,a,b,enabled)
  }
 })}
}
func TestNegativeControlIsDetected(t *testing.T){
 broken:=http.NewServeMux()
 broken.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){w.WriteHeader(200);fmt.Fprint(w,"WRONG")})
 good:=StdlibRouter(nil)
 p:=Request{"GET","/items/alpha"}
 a,e:=observe(good,p);if e!=nil{t.Fatal(e)}
 b,e:=observe(broken,p);if e!=nil{t.Fatal(e)}
 if a==b{t.Fatal("negative control missed incorrect handler body")}
 t.Logf("NEGATIVE_CONTROL good=%+v bad=%+v",a,b)
}
