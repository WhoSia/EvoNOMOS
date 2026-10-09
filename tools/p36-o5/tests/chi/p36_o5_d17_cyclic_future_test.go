package middleware

import (
  "net/http"
  "net/http/httptest"
  "testing"
)

func p36O5Tag(label string) func(http.Handler) http.Handler {
  return func(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request) {
      w.Header().Set("X-P36-O5", label)
      next.ServeHTTP(w,r)
    })
  }
}
func p36O5Observed(p *P35EpochRouter)string{
  r:=httptest.NewRequest(http.MethodGet,"/",nil)
  r.Header.Set("X-P36-O5-Match","stable")
  w:=httptest.NewRecorder()
  p.ServeHTTP(w,r)
  return w.Header().Get("X-P36-O5")
}

// New independently predeclared D17 future demand; frozen separately
// from prior D14, D15 and D16 oracles.
func TestP36O5D17CyclicDisableRestorePriority(t *testing.T){
  for _,interleaveNewRegistration:=range []bool{false,true}{
    name:="no_new_registration"
    if interleaveNewRegistration{name="new_registration_during_disable"}
    t.Run(name,func(t *testing.T){
      p:=NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
        if w.Header().Get("X-P36-O5")==""{w.Header().Set("X-P36-O5","fallback")}
      }))
      for _,label:=range []string{"A","B","C"} {
        p.Register("X-P36-O5-Match","stable",p36O5Tag(label))
      }
      revision,_,_:=p.Stats()
      check:=func(action string, ok bool, want string) {
        t.Helper()
        if !ok {t.Fatalf("%s returned false",action)}
        newer,published,_:=p.Stats()
        if newer!=revision+1 || published!=newer {
          t.Fatalf("incorrect immediate publication %s: old=%d new=%d pub=%d",action,revision,newer,published)
        }
        revision=newer
        if got:=p36O5Observed(p);got!=want {
          t.Fatalf("P36_O5_D17_CYCLIC_PRIORITY_FAILURE action=%s got=%q want=%q",action,got,want)
        }
      }
      if got:=p36O5Observed(p);got!="A"{t.Fatalf("initial priority %q",got)}
      check("disable_A",p.DisableRoute("X-P36-O5-Match","stable"),"B")
      check("disable_B",p.DisableRoute("X-P36-O5-Match","stable"),"C")
      if interleaveNewRegistration {
        p.Register("X-P36-O5-Match","stable",p36O5Tag("D"))
        newer,published,_:=p.Stats()
        if newer!=revision+1||published!=newer{t.Fatal("intervening registration not published")}
        revision=newer
        if got:=p36O5Observed(p);got!="C"{t.Fatalf("later registration displaced C: %q",got)}
      }
      check("restore_A",p.EnableRoute("X-P36-O5-Match","stable"),"A")
      check("disable_A_again",p.DisableRoute("X-P36-O5-Match","stable"),"C")
      // The earliest still disabled handler is B, and C is a later
      // registration. A local index rebase after the first restore can
      // insert B AFTER C here, violating original priority.
      check("restore_B",p.EnableRoute("X-P36-O5-Match","stable"),"B")
      check("restore_A_again",p.EnableRoute("X-P36-O5-Match","stable"),"A")
      if p.EnableRoute("X-P36-O5-Match","missing"){t.Fatal("unexpected restore")}
      unchanged,_,_:=p.Stats()
      if unchanged!=revision{t.Fatal("missing route changed revision")}
    })
  }
}
