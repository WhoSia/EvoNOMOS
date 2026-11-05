// Package online models finite, staged, nonanticipating safe source repair.
// It is a mathematical reference model, not a Go source soundness checker.
package online

import "sort"

// Transition is a permission-labelled edge in a finite edit graph.
type Transition struct {
 To string
 Cost int
 Authorized bool
}

// World fixes one possible future demand after an initial commitment.
type World struct {
 Name string
 Goal map[string]bool
}

// Game freezes the first-stage commitment set before revealing the world.
type Game struct {
 Start string
 Stage1 map[string]bool
 Safe map[string]bool
 Edges map[string][]Transition
 Futures []World
}

func (g Game) successors(from string) []string {
 out:=[]string{}
 for _,e:=range g.Edges[from] {
  if e.Authorized && e.Cost>=0 && g.Safe[e.To] {out=append(out,e.To)}
 }
 sort.Strings(out)
 return out
}

// Reach computes existence of an authorized, all-prefix-safe path to a goal.
func (g Game) Reach(from string,goal map[string]bool) bool {
 if !g.Safe[from] {return false}
 seen:=map[string]bool{from:true}
 q:=[]string{from}
 for len(q)>0 {
  s:=q[0];q=q[1:]
  if goal[s] {return true}
  for _,to:=range g.successors(s){
   if !seen[to]{seen[to]=true;q=append(q,to)}
  }
 }
 return false
}

// Commitments are allowed stage-one endpoint states; the endpoint is fixed
// before any future-world identity is disclosed.
func (g Game) Commitments() []string {
 if !g.Safe[g.Start] {return nil}
 // Compute reachable states, then project to states fulfilling Stage1.
 seen:=map[string]bool{g.Start:true};q:=[]string{g.Start}
 out:=[]string{}
 for len(q)>0{
  s:=q[0];q=q[1:]
  if g.Stage1[s] {out=append(out,s)}
  for _,to:=range g.successors(s){
   if !seen[to]{seen[to]=true;q=append(q,to)}
  }
 }
 sort.Strings(out);return out
}

// OfflinePerFuture permits a different initial commitment for each future.
// It captures forall future exists path, not an actual nonanticipating policy.
func (g Game) OfflinePerFuture() map[string]bool {
 ans:=map[string]bool{}
 c:=g.Commitments()
 for _,w:=range g.Futures{
  for _,s:=range c{if g.Reach(s,w.Goal){ans[w.Name]=true;break}}
 }
 return ans
}

// OnlineWinning requires one stage-one commitment before future disclosure.
// Once revealed, paths can be chosen in a demand-dependent way.
func (g Game) OnlineWinning() (bool,string){
 for _,s:=range g.Commitments(){
  ok:=true
  for _,w:=range g.Futures{if !g.Reach(s,w.Goal){ok=false;break}}
  if ok{return true,s}
 }
 return false,""
}

// CandidateFutureFailures provides a concrete falsifier for each commitment.
func (g Game) CandidateFutureFailures() map[string][]string{
 out:=map[string][]string{}
 for _,s:=range g.Commitments(){
  for _,w:=range g.Futures{if !g.Reach(s,w.Goal){out[s]=append(out[s],w.Name)}}
 }
 return out
}
