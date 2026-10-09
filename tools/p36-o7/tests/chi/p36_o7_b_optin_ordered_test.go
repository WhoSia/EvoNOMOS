package middleware

import ("net/http";"net/http/httptest";"testing")

func p36O7BWrap(label string)func(http.Handler)http.Handler{
 return func(next http.Handler)http.Handler {
  return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request) {
   w.Header().Set("X-P36-O7-Winner",label)
   next.ServeHTTP(w,r)
  })
 }
}
func p36O7BRequest(alpha,beta bool)*http.Request {
 r:=httptest.NewRequest(http.MethodGet,"/",nil)
 if alpha{r.Header.Set("X-P36-O7-Alpha","on")}
 if beta{r.Header.Set("X-P36-O7-Beta","on")}
 return r
}
func p36O7BObserved(h http.Handler,r *http.Request)string{
 w:=httptest.NewRecorder();h.ServeHTTP(w,r);return w.Header().Get("X-P36-O7-Winner")
}
func p36O7BNext()http.Handler{
 return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if w.Header().Get("X-P36-O7-Winner")==""{w.Header().Set("X-P36-O7-Winner","next")}
 })
}
func p36O7BHandler(first string)http.Handler{
 o:=P36O7NewOrderedHeaderRouter()
 if first=="A"{
  o.Route("X-P36-O7-Alpha","on",p36O7BWrap("A"))
  o.Route("X-P36-O7-Beta","on",p36O7BWrap("B"))
 }else{
  o.Route("X-P36-O7-Beta","on",p36O7BWrap("B"))
  o.Route("X-P36-O7-Alpha","on",p36O7BWrap("A"))
 }
 o.RouteDefault(p36O7BWrap("default"))
 return o.Handler(p36O7BNext())
}
func TestP36O7BOptInChronologicalHeaders(t *testing.T){
 for _,first:=range []string{"A","B"}{
  h:=p36O7BHandler(first)
  for _,one:=range []struct{alpha,beta bool;want string}{
    {true,false,"A"},{false,true,"B"},{true,true,first},{false,false,"default"},
  }{
   for i:=0;i<128;i++{
    if got:=p36O7BObserved(h,p36O7BRequest(one.alpha,one.beta));got!=one.want{
     t.Fatalf("P36_O7_B_CHRONOLOGICAL_REPAIR_FAILED first=%s a=%v b=%v got=%s want=%s iteration=%d",first,one.alpha,one.beta,got,one.want,i)
    }
   }
  }
 }
}
func TestP36O7BExistingChiPatternPriority(t *testing.T){
 o:=P36O7NewOrderedHeaderRouter()
 o.RouteAny("X-P36-O7-Alpha",[]string{"o*","never"},p36O7BWrap("first"))
 o.Route("X-P36-O7-Alpha","on",p36O7BWrap("second"))
 o.RouteDefault(p36O7BWrap("default"))
 h:=o.Handler(p36O7BNext())
 if got:=p36O7BObserved(h,p36O7BRequest(true,false));got!="first"{t.Fatalf("RouteAny priority got=%s",got)}
 if got:=p36O7BObserved(h,p36O7BRequest(false,false));got!="default"{t.Fatalf("default got=%s",got)}
}
func TestP36O7BLegacyHeaderRouterUnmodified(t *testing.T){
 legacy:=RouteHeaders()
 legacy.Route("X-P36-O7-Alpha","on",p36O7BWrap("old-map"))
 if _,ok:=legacy["x-p36-o7-alpha"];!ok{t.Fatal("legacy public map shape changed")}
 got:=p36O7BObserved(legacy.Handler(p36O7BNext()),p36O7BRequest(true,false))
 if got!="old-map"{t.Fatalf("legacy route changed got=%s",got)}
}
func BenchmarkP36O7BOriginalChiUniqueHeader(b *testing.B){
 hr:=RouteHeaders().Route("X-P36-O7-Alpha","on",p36O7BWrap("A"))
 h:=hr.Handler(p36O7BNext())
 r:=p36O7BRequest(true,false)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{w:=httptest.NewRecorder();h.ServeHTTP(w,r)}
}
func BenchmarkP36O7BOptInChronologicalUniqueHeader(b *testing.B){
 h:=P36O7NewOrderedHeaderRouter().Route("X-P36-O7-Alpha","on",p36O7BWrap("A")).Handler(p36O7BNext())
 r:=p36O7BRequest(true,false)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{w:=httptest.NewRecorder();h.ServeHTTP(w,r)}
}
func BenchmarkP36O7BOptInChronologicalOverlap(b *testing.B){
 h:=p36O7BHandler("A")
 r:=p36O7BRequest(true,true)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{w:=httptest.NewRecorder();h.ServeHTTP(w,r)}
}
