// P36-O10 research-authored ADDITIVE original-module Chi source repair.
// Not part of independently evolved upstream Chi. Preserves every original API.
// Scope: exactly two frozen GET patterns and two policy values.
package chi

import (
 "fmt"
 "net/http"
)

type p36O10Rule struct { pattern, label string }

type P36O10SelectableRouter struct {
 policy string
 rules []p36O10Rule
 built bool
}

func P36O10NewSelectableRouter(policy string)(*P36O10SelectableRouter,error){
 if policy!="specificity"&&policy!="chronology"{
  return nil,fmt.Errorf("P36-O10 unsupported policy %q",policy)
 }
 return &P36O10SelectableRouter{policy:policy},nil
}

func(p *P36O10SelectableRouter)Register(pattern,label string)error{
 if p.built {return fmt.Errorf("P36-O10 already published")}
 if pattern!="/members/me"&&pattern!="/members/{id}" {
  return fmt.Errorf("P36-O10 unsupported path %q",pattern)
 }
 if label==""{return fmt.Errorf("P36-O10 empty label")}
 for _,r:=range p.rules{if r.pattern==pattern{return fmt.Errorf("P36-O10 duplicate path %q",pattern)}}
 p.rules=append(p.rules,p36O10Rule{pattern:pattern,label:label})
 return nil
}
func(p *P36O10SelectableRouter)Handler()http.Handler{
 p.built=true
 // Sorting is a frozen policy-selection *construction* step.
 // The core Chi radix-tree still chooses static first within a single Mux,
 // so chronological policy deliberately uses separate real Chi mini-Muxes.
 ordered:=append([]p36O10Rule(nil),p.rules...)
 if p.policy=="specificity"&&len(ordered)==2&&ordered[0].pattern!="/members/me" {
  ordered[0],ordered[1]=ordered[1],ordered[0]
 }
 core:=make([]*Mux,0,len(ordered))
 for _,r:=range ordered{
  router:=NewRouter()
  tag:=r.label
  router.Get(r.pattern,func(w http.ResponseWriter,req *http.Request){
   w.Header().Set("X-P36-O10-Winner",tag)
   w.WriteHeader(http.StatusOK)
  })
  core=append(core,router)
 }
 return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  for _,router:=range core{
   // Original core Chi Mux.Match determines path grammar, not a fake matcher.
   ctx:=NewRouteContext()
   if router.Match(ctx,r.Method,r.URL.Path){
    router.ServeHTTP(w,r)
    return
   }
  }
  http.NotFound(w,r)
 })
}
