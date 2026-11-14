// Package online models finite, staged, nonanticipating safe source repair.
// This is a mathematical reference, NOT a general Go source checker.
package online

import "sort"

type Transition struct{ To string; Cost int; Authorized bool }
type World struct{ Name string; Goal map[string]bool }
type Game struct{
 Start string
 // Stage1 is the previously accepted contract; it must remain protected.
 Stage1 map[string]bool
 // Checkpoint enumerates permitted first-stage release endpoints.
 Checkpoint map[string]bool
 Safe map[string]bool
 Edges map[string][]Transition
 Futures []World
}
func(g Game)successors(from string,protectStage1 bool)[]string{
 out:=[]string{}
 for _,e:=range g.Edges[from]{
  if e.Authorized&&e.Cost>=0&&g.Safe[e.To]&&(!protectStage1||g.Stage1[e.To]){out=append(out,e.To)}
 }
 sort.Strings(out);return out
}
func(g Game)Reach(from string,goal map[string]bool,protectStage1 bool)bool{
 if !g.Safe[from] || protectStage1&&!g.Stage1[from]{return false}
 seen:=map[string]bool{from:true};q:=[]string{from}
 for len(q)>0{
  s:=q[0];q=q[1:]
  if goal[s]{return true}
  for _,to:=range g.successors(s,protectStage1){if !seen[to]{seen[to]=true;q=append(q,to)}}
 }
 return false
}
func(g Game)Commitments()[]string{
 if !g.Safe[g.Start]{return nil}
 seen:=map[string]bool{g.Start:true};q:=[]string{g.Start};out:=[]string{}
 for len(q)>0{
  s:=q[0];q=q[1:]
  if g.Checkpoint[s]&&g.Stage1[s]{out=append(out,s)}
  for _,to:=range g.successors(s,false){if !seen[to]{seen[to]=true;q=append(q,to)}}
 }
 sort.Strings(out);return out
}
func(g Game)OfflinePerFuture()map[string]bool{
 out:=map[string]bool{}
 for _,w:=range g.Futures{for _,s:=range g.Commitments(){
  if g.Reach(s,w.Goal,true){out[w.Name]=true;break}
 }}
 return out
}
func(g Game)OnlineWinning()(bool,string){
 for _,s:=range g.Commitments(){
  ok:=true
  for _,w:=range g.Futures{if !g.Reach(s,w.Goal,true){ok=false;break}}
  if ok{return true,s}
 }
 return false,""
}
func(g Game)CandidateFutureFailures()map[string][]string{
 out:=map[string][]string{}
 for _,s:=range g.Commitments(){for _,w:=range g.Futures{
  if !g.Reach(s,w.Goal,true){out[s]=append(out[s],w.Name)}
 }}
 return out
}
