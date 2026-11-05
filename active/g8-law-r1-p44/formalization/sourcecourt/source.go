// Package sourcecourt interprets a rigorously closed Go syntax fragment.
// It does not claim soundness or completeness for arbitrary Go programs.
package sourcecourt

import (
 "bytes"
 "errors"
 "fmt"
 "go/ast"
 "go/format"
 "go/parser"
 "go/token"
 "strconv"
 "sort"
)

var ErrOutsideGrammar=errors.New("source is outside the declared two-function grammar")
var ErrUnauthorized=errors.New("edit is not in the declared right/domain")
type Program struct { Legacy string; Future string }
type Policy struct { Allowed []string }

func literal(fn *ast.FuncDecl)(string,error){
 if fn.Recv!=nil || fn.Type.TypeParams!=nil && len(fn.Type.TypeParams.List)!=0 || fn.Type.Params==nil || len(fn.Type.Params.List)!=0 || fn.Type.Results==nil || len(fn.Type.Results.List)!=1 || fn.Body==nil || len(fn.Body.List)!=1 {return "",ErrOutsideGrammar}
 result:=fn.Type.Results.List[0]
 if len(result.Names)!=0{return "",ErrOutsideGrammar}
 id,ok:=result.Type.(*ast.Ident)
 if !ok||id.Name!="string"{return "",ErrOutsideGrammar}
 ret,ok:=fn.Body.List[0].(*ast.ReturnStmt)
 if !ok||len(ret.Results)!=1{return "",ErrOutsideGrammar}
 str,ok:=ret.Results[0].(*ast.BasicLit)
 if !ok||str.Kind!=token.STRING{return "",ErrOutsideGrammar}
 v,e:=strconv.Unquote(str.Value)
 if e!=nil{return "",ErrOutsideGrammar}
 return v,nil
}

// Parse enforces exactly two zero-argument pure constant-string functions.
// No import, variable, extra declaration, side-effect, alias or hidden call.
func Parse(source string)(Program,error){
 fset:=token.NewFileSet()
 file,e:=parser.ParseFile(fset,"fixture.go",source,parser.AllErrors)
 if e!=nil||file.Name.Name!="fixture"||len(file.Decls)!=2{return Program{},ErrOutsideGrammar}
 vals:=map[string]string{}
 for _,d:=range file.Decls{
  fn,ok:=d.(*ast.FuncDecl)
  if !ok || (fn.Name.Name!="Legacy"&&fn.Name.Name!="Future"){return Program{},ErrOutsideGrammar}
  if _,exists:=vals[fn.Name.Name];exists{return Program{},ErrOutsideGrammar}
  v,e:=literal(fn);if e!=nil{return Program{},e}
  vals[fn.Name.Name]=v
 }
 if len(vals)!=2{return Program{},ErrOutsideGrammar}
 return Program{Legacy:vals["Legacy"],Future:vals["Future"]},nil
}

func (p Policy) domain()(map[string]bool,error){
 if len(p.Allowed)==0{return nil,ErrUnauthorized}
 d:=map[string]bool{}
 for _,v:=range p.Allowed{
  if d[v]{return nil,ErrUnauthorized}
  d[v]=true
 }
 return d,nil
}

// PatchFuture is the ONLY authorized edit constructor in this closed grammar.
// It edits the BasicLit in function Future, preserves the Legacy AST and
// reparses the generated complete source to confirm it remains in-grammar.
func PatchFuture(src string,p Policy,next string)(string,error){
 original,e:=Parse(src);if e!=nil{return "",e}
 d,e:=p.domain();if e!=nil||!d[original.Future]||!d[next]{return "",ErrUnauthorized}
 fs:=token.NewFileSet();file,e:=parser.ParseFile(fs,"fixture.go",src,parser.AllErrors)
 if e!=nil{return "",ErrOutsideGrammar}
 for _,decl:=range file.Decls{
  fn:=decl.(*ast.FuncDecl)
  if fn.Name.Name=="Future"{
   stmt:=fn.Body.List[0].(*ast.ReturnStmt)
   stmt.Results[0].(*ast.BasicLit).Value=strconv.Quote(next)
  }
 }
 var out bytes.Buffer
 if e:=format.Node(&out,fs,file);e!=nil{return "",e}
 resulting,e:=Parse(out.String())
 if e!=nil||resulting.Legacy!=original.Legacy||resulting.Future!=next{return "",ErrOutsideGrammar}
 return out.String(),nil
}

type Edge struct{ From,To string; Cost int; Right string }
type Graph struct{ States map[string]string; Edges []Edge; Legacy string }

// Enumerate constructs the complete directed non-identity edit graph,
// RELATIVE TO the specified closed policy: any value may be replaced by
// any other exactly once for synthetic unit edit cost.
func Enumerate(src string,p Policy)(Graph,error){
 initial,e:=Parse(src);if e!=nil{return Graph{},e}
 d,e:=p.domain();if e!=nil||!d[initial.Future]{return Graph{},ErrUnauthorized}
 states:=map[string]string{}
 values:=append([]string(nil),p.Allowed...)
 sort.Strings(values)
 for _,v:=range values{
  patched,e:=PatchFuture(src,p,v);if e!=nil{return Graph{},e}
  state,e:=Parse(patched);if e!=nil||state.Legacy!=initial.Legacy||state.Future!=v{return Graph{},ErrOutsideGrammar}
  states[v]=patched
 }
 edges:=[]Edge{}
 for _,a:=range values{
  for _,b:=range values{
   if a==b{continue}
   changed,e:=PatchFuture(states[a],p,b);if e!=nil{return Graph{},e}
   result,e:=Parse(changed);if e!=nil||result.Future!=b{return Graph{},fmt.Errorf("missing legal edit %q->%q",a,b)}
   edges=append(edges,Edge{From:a,To:b,Cost:1,Right:"app:Future-literal"})
  }
 }
 return Graph{States:states,Edges:edges,Legacy:initial.Legacy},nil
}

// Observe is the entire declared bounded observational semantics here:
// there are no inputs or nondeterministic schedules in the source grammar.
func Observe(src string)(Program,error){return Parse(src)}

// ExactDistance is an equal-information classical shortest-path reference.
func ExactDistance(g Graph,start,goal string)(int,error){
 if _,ok:=g.States[start];!ok{return -1,ErrOutsideGrammar}
 if _,ok:=g.States[goal];!ok{return -1,ErrOutsideGrammar}
 if start==goal{return 0,nil}
 seen:=map[string]bool{start:true};queue:=[]string{start};depth:=map[string]int{start:0}
 for len(queue)>0{
  s:=queue[0];queue=queue[1:]
  for _,e:=range g.Edges{
   if e.From!=s || e.Cost!=1 || e.Right!="app:Future-literal"{continue}
   if seen[e.To]{continue}
   if e.To==goal{return depth[s]+1,nil}
   seen[e.To]=true;depth[e.To]=depth[s]+1;queue=append(queue,e.To)
  }
 }
 return -1,nil
}
