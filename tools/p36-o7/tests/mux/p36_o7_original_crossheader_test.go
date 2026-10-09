package mux

import ("net/http";"net/http/httptest";"testing")

func p36O7Request(both bool,only string)*http.Request{
 r:=httptest.NewRequest(http.MethodGet,"/",nil)
 if both||only=="A"{r.Header.Set("X-P36-O7-Alpha","on")}
 if both||only=="B"{r.Header.Set("X-P36-O7-Beta","on")}
 return r
}
func p36O7Build(earliest string)http.Handler {
 router:=NewRouter()
 router.NotFoundHandler=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.Header().Set("X-P36-O7-Winner","fallback")})
 a:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.Header().Set("X-P36-O7-Winner","A")})
 b:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){w.Header().Set("X-P36-O7-Winner","B")})
 if earliest=="A"{
  router.Headers("X-P36-O7-Alpha","on").Handler(a)
  router.Headers("X-P36-O7-Beta","on").Handler(b)
 } else {
  router.Headers("X-P36-O7-Beta","on").Handler(b)
  router.Headers("X-P36-O7-Alpha","on").Handler(a)
 }
 return router
}
func p36O7Got(handler http.Handler,req *http.Request)string{
 w:=httptest.NewRecorder();handler.ServeHTTP(w,req);return w.Header().Get("X-P36-O7-Winner")
}
func TestP36O7BaselineUniqueHeaderRoutes(t *testing.T){
 for _,first:=range []string{"A","B"}{
  h:=p36O7Build(first)
  for _,only:=range []string{"A","B"} {
   if got:=p36O7Got(h,p36O7Request(false,only));got!=only{t.Fatalf("P36_O7_Q0_BASELINE_MISMATCH first=%s only=%s got=%s",first,only,got)}
  }
 }
}
func TestP36O7D18ChronologicalPriority(t *testing.T){
 for _,first:=range []string{"A","B"}{
  h:=p36O7Build(first)
  for i:=0;i<128;i++{
   if got:=p36O7Got(h,p36O7Request(true,""));got!=first {
    t.Fatalf("P36_O7_D18_ORIGINAL_SOURCE_PRIORITY_MISMATCH first=%s request=%d got=%s",first,i,got)
   }
  }
 }
}
