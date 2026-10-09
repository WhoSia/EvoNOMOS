package middleware

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "testing"
)

func p36O3Tag(s string)func(http.Handler)http.Handler{
 return func(next http.Handler)http.Handler{
  return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
   w.Header().Set("X-P36-O3",s);next.ServeHTTP(w,r)
  })
 }
}
func p36O3Got(p *P35EpochRouter,v string)string{
 r:=httptest.NewRequest(http.MethodGet,"/",nil)
 r.Header.Set("X-P35-O3",v)
 w:=httptest.NewRecorder()
 p.ServeHTTP(w,r)
 return w.Header().Get("X-P36-O3")
}
func p36O3Case(label string)*P35EpochRouter{
 p:=NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){
  if w.Header().Get("X-P36-O3")=="" {w.Header().Set("X-P36-O3","next")}
 }))
 p.Register("X-P35-O3","target",p36O3Tag(label))
 p.Register("X-P35-O3","target",p36O3Tag("secondary"))
 p.Register("X-P35-O3","other",p36O3Tag("other"))
 return p
}
func TestP36O3D14Disable(t *testing.T){
 for _,label:=range []string{"alpha","beta"} {
  t.Run(label,func(t *testing.T){
   p:=p36O3Case(label)
   if got:=p36O3Got(p,"target");got!=label{t.Fatalf("old priority got %q want %q",got,label)}
   rev0,_,_:=p.Stats()
   if p.DisableRoute("X-P35-O3","missing"){t.Fatal("unexpected missing disable")}
   rev1,_,_:=p.Stats()
   if rev1!=rev0{t.Fatalf("missing changed revision %d->%d",rev0,rev1)}
   if !p.DisableRoute("X-P35-O3","target"){t.Fatal("wanted disable true")}
   rev2,pub,_:=p.Stats()
   if rev2!=rev0+1||pub!=rev2{t.Fatalf("not published %d,%d",rev2,pub)}
   if got:=p36O3Got(p,"target");got!="secondary"{t.Fatalf("old deleted route still matches got %q",got)}
   if got:=p36O3Got(p,"other");got!="other"{t.Fatalf("other route altered %q",got)}
   if got:=p36O3Got(p,"absent");got!="next"{t.Fatalf("fallback changed %q",got)}
  })
 }
}
func TestP36O3D14ConcurrentStable(t *testing.T){
 p:=p36O3Case("alpha")
 done:=make(chan struct{})
 go func(){defer close(done);for i:=0;i<32;i++{
  p.Register("X-P35-O3",fmt.Sprintf("parallel-%02d",i),p36O3Tag("parallel"))
 }}()
 for i:=0;i<32;i++ {
  if got:=p36O3Got(p,"other");got!="other"{t.Fatalf("stable other got %q",got)}
 }
 <-done
 if !p.DisableRoute("X-P35-O3","target"){t.Fatal("disable lost")}
 if got:=p36O3Got(p,"target");got!="secondary"{t.Fatalf("post completed %q",got)}
}
