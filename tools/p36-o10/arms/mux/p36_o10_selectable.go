// P36-O10 research-authored ADDITIVE original-module Gorilla source repair.
// Not part of independently evolved upstream Gorilla. Preserves original API.
// Scope: exactly two frozen GET patterns and two policy values.
package mux

import (
 "fmt"
 "net/http"
)

type p36O10Rule struct { pattern,label string }

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
 if p.built{return fmt.Errorf("P36-O10 already published")}
 if pattern!="/members/me"&&pattern!="/members/{id}"{
  return fmt.Errorf("P36-O10 unsupported path %q",pattern)
 }
 if label==""{return fmt.Errorf("P36-O10 empty label")}
 for _,r:=range p.rules{if r.pattern==pattern{return fmt.Errorf("P36-O10 duplicate path %q",pattern)}}
 p.rules=append(p.rules,p36O10Rule{pattern:pattern,label:label})
 return nil
}
func(p *P36O10SelectableRouter)Handler()http.Handler{
 p.built=true
 ordered:=append([]p36O10Rule(nil),p.rules...)
 if p.policy=="specificity"&&len(ordered)==2&&ordered[0].pattern!="/members/me"{
  ordered[0],ordered[1]=ordered[1],ordered[0]
 }
 // Original Gorilla mux.Router scans the registered list in order.
 // New wrapper changes REGISTRATION POLICY, not core matching source.
 router:=NewRouter()
 for _,entry:=range ordered{
  tag:=entry.label
  router.HandleFunc(entry.pattern,func(w http.ResponseWriter,r *http.Request){
   w.Header().Set("X-P36-O10-Winner",tag)
   w.WriteHeader(http.StatusOK)
  }).Methods(http.MethodGet)
 }
 return router
}
