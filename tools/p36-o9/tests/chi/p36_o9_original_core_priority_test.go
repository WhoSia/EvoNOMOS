package chi

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

func p36O9RouteTag(tag string)http.HandlerFunc {
 return func(w http.ResponseWriter,r *http.Request){
  w.Header().Set("X-P36-O9-Winner",tag)
  w.WriteHeader(http.StatusOK)
 }
}
func p36O9Build(paramFirst bool)http.Handler{
 r:=NewRouter()
 if paramFirst {
  r.Get("/members/{id}",p36O9RouteTag("PARAM"))
  r.Get("/members/me",p36O9RouteTag("STATIC"))
 } else {
  r.Get("/members/me",p36O9RouteTag("STATIC"))
  r.Get("/members/{id}",p36O9RouteTag("PARAM"))
 }
 return r
}
func p36O9Get(h http.Handler,path string)(int,string){
 r:=httptest.NewRequest(http.MethodGet,path,nil)
 w:=httptest.NewRecorder()
 h.ServeHTTP(w,r)
 return w.Code,w.Header().Get("X-P36-O9-Winner")
}
func TestP36O9BaselineDisjointPath(t *testing.T){
 for _,first:=range []bool{true,false}{
  h:=p36O9Build(first)
  code,tag:=p36O9Get(h,"/members/42")
  if code!=200||tag!="PARAM"{t.Fatalf("P36_O9_Q0_FAILURE first=%t tag=%s code=%d",first,tag,code)}
  code,tag=p36O9Get(h,"/outside")
  if code!=404||tag!=""{t.Fatalf("P36_O9_Q0_FAILURE missing first=%t tag=%s code=%d",first,tag,code)}
 }
}
func TestP36O9D19SpecificityRegardlessOfOrder(t *testing.T){
 for _,paramFirst:=range []bool{true,false} {
  h:=p36O9Build(paramFirst)
  for i:=0;i<64;i++{
   code,tag:=p36O9Get(h,"/members/me")
   if code!=200||tag!="STATIC"{t.Fatalf("P36_O9_D19_SPECIFICITY_MISMATCH paramFirst=%t trial=%d tag=%s code=%d want=STATIC",paramFirst,i,tag,code)}
  }
 }
}
func TestP36O9D20ChronologyRegardlessOfSpecificity(t *testing.T){
 for _,paramFirst:=range []bool{true,false}{
  h:=p36O9Build(paramFirst)
  want:="STATIC"
  if paramFirst{want="PARAM"}
  for i:=0;i<64;i++{
   code,tag:=p36O9Get(h,"/members/me")
   if code!=200||tag!=want{t.Fatalf("P36_O9_D20_CHRONOLOGY_MISMATCH paramFirst=%t trial=%d tag=%s code=%d want=%s",paramFirst,i,tag,code,want)}
  }
 }
}
