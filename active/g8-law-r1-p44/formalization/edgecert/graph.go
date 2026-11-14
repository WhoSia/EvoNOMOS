// Package edgecert checks a finite source-edit graph abstraction. The caller
// must separately justify that the concrete graph covers every permitted
// actual source edit and all protected client observations.
package edgecert

import (
    "errors"
    "math"
)

var (
    ErrMissingState = errors.New("safe concrete state has no abstract image")
    ErrStageMismatch = errors.New("abstract image changes demand-disclosure stage")
    ErrGoalOmission = errors.New("concrete demand goal not represented as abstract goal")
    ErrMissingTransition = errors.New("permitted safe concrete edit has no cost-nonincreasing abstract match")
    ErrNegativeCost = errors.New("negative edit cost")
    ErrInvalidSource = errors.New("start state missing or violates protected contract")
    ErrInvalidWitness = errors.New("concrete witness has unauthorized or unsafe edit")
)

type State struct { Stage int; Safe bool; Goal bool }
type Edge struct { From, To, Right string; Cost int; Authorized bool }
type Graph struct { Start string; States map[string]State; Edges []Edge }
type Certificate struct { Image map[string]string }

// Verify checks a sufficient edge-local condition for mapping every finite
// concrete safe edit path into an abstract path with no higher cost.
// This checks a supplied graph; it is not a proof of source graph completeness.
func Verify(concrete, abstract Graph, cert Certificate) error {
    start,ok:=concrete.States[concrete.Start]
    if !ok || !start.Safe {return ErrInvalidSource}
    for _,g:=range []Graph{concrete,abstract}{
        for _,e:=range g.Edges {
            if e.Cost<0{return ErrNegativeCost}
            if _,ok:=g.States[e.From];!ok{return ErrInvalidSource}
            if _,ok:=g.States[e.To];!ok{return ErrInvalidSource}
        }
    }
    if cert.Image[concrete.Start]!=abstract.Start {return ErrMissingState}
    for id,s:=range concrete.States {
        if !s.Safe{continue}
        image,ok:=cert.Image[id]
        if !ok{return ErrMissingState}
        a,ok:=abstract.States[image]
        if !ok || !a.Safe{return ErrMissingState}
        if s.Stage!=a.Stage{return ErrStageMismatch}
        if s.Goal&&!a.Goal{return ErrGoalOmission}
    }
    for _,e:=range concrete.Edges {
        src,dst:=concrete.States[e.From],concrete.States[e.To]
        // Stage transitions require separate demand-disclosure semantics and
        // cannot silently be counted as a same-stage source edit.
        if !e.Authorized || !src.Safe || !dst.Safe || src.Stage!=dst.Stage {continue}
        f,t:=cert.Image[e.From],cert.Image[e.To]
        match:=false
        for _,a:=range abstract.Edges {
            if a.Authorized && a.From==f && a.To==t && a.Right==e.Right && a.Cost<=e.Cost {
                match=true;break
            }
        }
        if !match{return ErrMissingTransition}
    }
    return nil
}

// Shortest computes the exact authorized safe edit cost for a finite graph.
// It is an independent classical reference oracle, not part of the certificate.
func Shortest(g Graph) (int,error) {
    start,ok:=g.States[g.Start]
    if !ok||!start.Safe{return 0,ErrInvalidSource}
    d:=map[string]int{g.Start:0}
    used:=map[string]bool{}
    for {
        u:="";du:=math.MaxInt
        for id,v:=range d {if !used[id] && v<du{u,du=id,v}}
        if u==""{break}
        if g.States[u].Goal{return du,nil}
        used[u]=true
        for _,e:=range g.Edges {
            if e.Cost<0{return 0,ErrNegativeCost}
            if !e.Authorized||e.From!=u{continue}
            dest,ok:=g.States[e.To]
            if !ok{return 0,ErrInvalidSource}
            if !dest.Safe||dest.Stage!=g.States[u].Stage{continue}
            if e.Cost>math.MaxInt-du{continue}
            if w,ok:=d[e.To];!ok||du+e.Cost<w{d[e.To]=du+e.Cost}
        }
    }
    return math.MaxInt,nil
}

// CheckWitness validates the named source path in the supplied finite graph.
// This remains conditional on the authenticity and completeness of that graph.
func CheckWitness(g Graph, states []string)(int,error){
    if len(states)==0||states[0]!=g.Start{return 0,ErrInvalidWitness}
    st,ok:=g.States[g.Start];if !ok||!st.Safe{return 0,ErrInvalidWitness}
    total:=0
    for i:=1;i<len(states);i++{
        src,dst:=g.States[states[i-1]],g.States[states[i]]
        if !dst.Safe||src.Stage!=dst.Stage{return 0,ErrInvalidWitness}
        best:=math.MaxInt
        for _,e:=range g.Edges {
            if e.From==states[i-1]&&e.To==states[i]&&e.Authorized {
                if e.Cost<0{return 0,ErrInvalidWitness}
                if e.Cost<best{best=e.Cost}
            }
        }
        if best==math.MaxInt||best>math.MaxInt-total{return 0,ErrInvalidWitness}
        total+=best
    }
    if !g.States[states[len(states)-1]].Goal{return 0,ErrInvalidWitness}
    return total,nil
}
