package middleware

import (
  "fmt"
  "net/http"
  "net/http/httptest"
  "testing"
)

type p36O6Entry struct { tag string; enabled bool }
type p36O6Reference struct {
  ordered []p36O6Entry
  pendingFIFO []int
}
func (m *p36O6Reference)register(tag string) {
  m.ordered=append(m.ordered,p36O6Entry{tag:tag,enabled:true})
}
func (m *p36O6Reference)disable()bool{
  for i:=range m.ordered{
    if m.ordered[i].enabled {
      m.ordered[i].enabled=false
      m.pendingFIFO=append(m.pendingFIFO,i)
      return true
    }
  }
  return false
}
func (m *p36O6Reference)enable()bool{
  if len(m.pendingFIFO)==0{return false}
  index:=m.pendingFIFO[0]
  m.pendingFIFO=m.pendingFIFO[1:]
  m.ordered[index].enabled=true
  return true
}
func (m *p36O6Reference)first()string{
  for _,entry:=range m.ordered{
    if entry.enabled {return entry.tag}
  }
  return "fallback"
}
func p36O6Middleware(label string)func(http.Handler)http.Handler{
  return func(next http.Handler)http.Handler{
    return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
      w.Header().Set("X-P36-O6-Result",label)
      next.ServeHTTP(w,r)
    })
  }
}
func p36O6Dispatch(p *P35EpochRouter)string{
  r:=httptest.NewRequest(http.MethodGet,"/",nil)
  r.Header.Set("X-P36-O6","test")
  w:=httptest.NewRecorder()
  p.ServeHTTP(w,r)
  return w.Header().Get("X-P36-O6-Result")
}
func p36O6CheckWord(t *testing.T,word string){
  t.Helper()
  p:=NewP35EpochRouter(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
    if w.Header().Get("X-P36-O6-Result")=="" {w.Header().Set("X-P36-O6-Result","fallback")}
  }))
  model:=&p36O6Reference{}
  for _,tag:=range []string{"A","B","C"}{
    model.register(tag)
    p.Register("X-P36-O6","test",p36O6Middleware(tag))
  }
  rev:=uint64(3)
  if got:=p36O6Dispatch(p);got!=model.first(){
    t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE word=%q prefix=initial got=%q want=%q",word,got,model.first())
  }
  for i,action:=range []byte(word){
    before:=rev
    switch action {
    case 'R':
      tag:=fmt.Sprintf("N%d",i)
      p.Register("X-P36-O6","test",p36O6Middleware(tag))
      model.register(tag)
      rev++
    case 'D':
      want:=model.disable()
      got:=p.DisableRoute("X-P36-O6","test")
      if got!=want{t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE word=%q prefix=%q Disable actual=%v ref=%v",word,word[:i+1],got,want)}
      if want{rev++}
    case 'E':
      want:=model.enable()
      got:=p.EnableRoute("X-P36-O6","test")
      if got!=want{t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE word=%q prefix=%q Enable actual=%v ref=%v",word,word[:i+1],got,want)}
      if want{rev++}
    default: t.Fatalf("invalid action %q",action)
    }
    actualRev,published,_:=p.Stats()
    if actualRev!=rev||published!=rev{
      t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE word=%q prefix=%q revision was %d expected %d actual %d published %d",word,word[:i+1],before,rev,actualRev,published)
    }
    if got,want:=p36O6Dispatch(p),model.first();got!=want {
      t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE word=%q prefix=%q HTTP actual=%q reference=%q",word,word[:i+1],got,want)
    }
  }
}

// All 1+3+9+27+81+243+729=1093 sequences of length at most 6,
// enumerated shortest first. Independently model all intermediate prefixes.
func TestP36O6ExhaustiveFiniteMaintenanceWords(t *testing.T){
  const maxDepth=6
  alphabet:=[]byte{'R','D','E'}
  seen:=0
  var enumerate func([]byte,int)
  enumerate=func(prefix []byte,remaining int){
    if remaining==0 {
      p36O6CheckWord(t,string(prefix))
      seen++
      return
    }
    for _,action:=range alphabet{
      next:=append(append([]byte(nil),prefix...),action)
      enumerate(next,remaining-1)
    }
  }
  for depth:=0;depth<=maxDepth;depth++ {
    enumerate(nil,depth)
  }
  if seen!=1093{t.Fatalf("P36_O6_TRACE_MODEL_DIVERGENCE enumeration count=%d",seen)}
  t.Logf("P36_O6_ORIGINAL_GO_FINITE_1093_WORDS_ALL_PREFIXES_PASS")
}
