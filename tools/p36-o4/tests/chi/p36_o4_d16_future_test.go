package middleware

import (
  "net/http"
  "net/http/httptest"
  "testing"
)

func p36O4Tag(tag string) func(http.Handler) http.Handler {
  return func(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
      w.Header().Set("X-P36-O4", tag)
      next.ServeHTTP(w, r)
    })
  }
}

func p36O4Dispatch(p *P35EpochRouter) string {
  r:=httptest.NewRequest(http.MethodGet,"/",nil)
  r.Header.Set("X-P36-O4-Match","stable")
  w:=httptest.NewRecorder()
  p.ServeHTTP(w,r)
  return w.Header().Get("X-P36-O4")
}

// D16 is a genuinely new, separately frozen *future* demand.
// Must never be slipped into the earlier D14/D15 acceptance court.
func TestP36O4D16OriginalPriorityAfterMultipleDisableRestore(t *testing.T){
  for _,withInterveningInsert:=range []bool{false,true}{
    label:="no_intervening_registration"
    if withInterveningInsert{label="intervening_registration"}
    t.Run(label,func(t *testing.T){
      p:=NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
        if w.Header().Get("X-P36-O4")==""{w.Header().Set("X-P36-O4","fallback")}
      }))
      for _,tag:=range []string{"A","B","C"} {
        p.Register("X-P36-O4-Match","stable",p36O4Tag(tag))
      }
      if got:=p36O4Dispatch(p);got!="A"{t.Fatalf("precondition first priority got %s",got)}
      rev,_,_:=p.Stats()
      mustStep:=func(opName string, performed bool, wanted string){
        t.Helper()
        if !performed{t.Fatalf("%s false: expected successful transition",opName)}
        next,published,_:=p.Stats()
        if next!=rev+1||published!=next{t.Fatalf("%s invalid publication rev %d -> %d published %d",opName,rev,next,published)}
        rev=next
        if got:=p36O4Dispatch(p);got!=wanted{t.Fatalf("P36_O4_D16_ORDER_FAILURE step=%s got=%q want=%q",opName,got,wanted)}
      }
      mustStep("disable_A",p.DisableRoute("X-P36-O4-Match","stable"),"B")
      mustStep("disable_B",p.DisableRoute("X-P36-O4-Match","stable"),"C")
      if withInterveningInsert {
        p.Register("X-P36-O4-Match","stable",p36O4Tag("D"))
        next,published,_:=p.Stats()
        if next!=rev+1||published!=next{t.Fatalf("new register publication rev %d -> %d published %d",rev,next,published)}
        rev=next
        if got:=p36O4Dispatch(p);got!="C"{t.Fatalf("new later registration displaced C: %s",got)}
      }
      mustStep("restore_A",p.EnableRoute("X-P36-O4-Match","stable"),"A")
      mustStep("restore_B",p.EnableRoute("X-P36-O4-Match","stable"),"A")
      mustStep("disable_A_again",p.DisableRoute("X-P36-O4-Match","stable"),"B")
      if p.EnableRoute("X-P36-O4-Match","missing"){t.Fatal("missing enable must fail")}
      after,_,_:=p.Stats()
      if after!=rev{t.Fatalf("missing enable changed revision %d->%d",rev,after)}
    })
  }
}
