// Closed source fragment: exactly Legacy() string and Future(flag bool) string.
// Source edit rights cover only either return-string literal in Future.
package branchcourt
import("bytes";"errors";"go/ast";"go/format";"go/parser";"go/token";"strconv";"sort")
var ErrGrammar=errors.New("outside bounded Go source grammar")
var ErrRight=errors.New("outside permitted source edit right")
type State struct{T,F string}
type Observation struct{Legacy,OnTrue,OnFalse string}
type Policy struct{Allowed []string}
type Edge struct{From,To State;Changed string;Cost int}
type Graph struct{Sources map[State]string;Edges []Edge;Legacy string}
func ret(stmt ast.Stmt)(string,error){
 r,ok:=stmt.(*ast.ReturnStmt);if !ok||len(r.Results)!=1{return "",ErrGrammar}
 l,ok:=r.Results[0].(*ast.BasicLit);if !ok||l.Kind!=token.STRING{return "",ErrGrammar}
 s,e:=strconv.Unquote(l.Value);if e!=nil{return "",ErrGrammar};return s,nil
}
func parsed(src string)(*token.FileSet,*ast.File,Observation,error){
 fs:=token.NewFileSet()
 f,e:=parser.ParseFile(fs,"fixture.go",src,parser.AllErrors|parser.ParseComments)
 if e!=nil||f.Name.Name!="fixture"||len(f.Decls)!=2||len(f.Comments)!=0{return nil,nil,Observation{},ErrGrammar}
 seen:=map[string]bool{};out:=Observation{}
 for _,dec:=range f.Decls{
  fn,ok:=dec.(*ast.FuncDecl);if !ok||seen[fn.Name.Name]||fn.Recv!=nil||fn.Body==nil{return nil,nil,Observation{},ErrGrammar}
  if fn.Type.TypeParams!=nil&&len(fn.Type.TypeParams.List)!=0{return nil,nil,Observation{},ErrGrammar}
  if fn.Type.Results==nil||len(fn.Type.Results.List)!=1{return nil,nil,Observation{},ErrGrammar}
  rs:=fn.Type.Results.List[0]; typ,ok:=rs.Type.(*ast.Ident)
  if !ok||typ.Name!="string"||len(rs.Names)!=0||fn.Type.Params==nil{return nil,nil,Observation{},ErrGrammar}
  seen[fn.Name.Name]=true
  switch fn.Name.Name{
  case "Legacy":
   if len(fn.Type.Params.List)!=0||len(fn.Body.List)!=1{return nil,nil,Observation{},ErrGrammar}
   out.Legacy,e=ret(fn.Body.List[0]);if e!=nil{return nil,nil,Observation{},e}
  case "Future":
   if len(fn.Type.Params.List)!=1||len(fn.Body.List)!=2{return nil,nil,Observation{},ErrGrammar}
   param:=fn.Type.Params.List[0]; p,ok:=param.Type.(*ast.Ident)
   if !ok||p.Name!="bool"||len(param.Names)!=1||param.Names[0].Name!="flag"{return nil,nil,Observation{},ErrGrammar}
   cond,ok:=fn.Body.List[0].(*ast.IfStmt)
   if !ok||cond.Init!=nil||cond.Else!=nil||len(cond.Body.List)!=1{return nil,nil,Observation{},ErrGrammar}
   id,ok:=cond.Cond.(*ast.Ident)
   if !ok||id.Name!="flag"{return nil,nil,Observation{},ErrGrammar}
   out.OnTrue,e=ret(cond.Body.List[0]);if e!=nil{return nil,nil,Observation{},e}
   out.OnFalse,e=ret(fn.Body.List[1]);if e!=nil{return nil,nil,Observation{},e}
  default:return nil,nil,Observation{},ErrGrammar
  }
 }
 if !seen["Legacy"]||!seen["Future"]{return nil,nil,Observation{},ErrGrammar}
 return fs,f,out,nil
}
func Parse(src string)(Observation,error){_,_,o,e:=parsed(src);return o,e}
func(p Policy)domain()(map[string]bool,error){
 if len(p.Allowed)==0{return nil,ErrRight}
 d:=map[string]bool{}
 for _,v:=range p.Allowed{if d[v]{return nil,ErrRight};d[v]=true}
 return d,nil
}
func Rewrite(src string,p Policy,next State)(string,error){
 fs,f,old,e:=parsed(src);if e!=nil{return "",e}
 d,e:=p.domain()
 if e!=nil||!d[old.OnTrue]||!d[old.OnFalse]||!d[next.T]||!d[next.F]{return "",ErrRight}
 for _,dec:=range f.Decls{
  fn:=dec.(*ast.FuncDecl);if fn.Name.Name!="Future"{continue}
  a:=fn.Body.List[0].(*ast.IfStmt).Body.List[0].(*ast.ReturnStmt).Results[0].(*ast.BasicLit)
  b:=fn.Body.List[1].(*ast.ReturnStmt).Results[0].(*ast.BasicLit)
  a.Value=strconv.Quote(next.T);b.Value=strconv.Quote(next.F)
 }
 var buf bytes.Buffer
 if e:=format.Node(&buf,fs,f);e!=nil{return "",e}
 now,e:=Parse(buf.String())
 if e!=nil||now.Legacy!=old.Legacy||now.OnTrue!=next.T||now.OnFalse!=next.F{return "",ErrGrammar}
 return buf.String(),nil
}
func Enumerate(src string,p Policy)(Graph,error){
 original,e:=Parse(src);if e!=nil{return Graph{},e}
 d,e:=p.domain()
 if e!=nil||!d[original.OnTrue]||!d[original.OnFalse]{return Graph{},ErrRight}
 vals:=append([]string(nil),p.Allowed...);sort.Strings(vals)
 g:=Graph{Sources:map[State]string{},Legacy:original.Legacy}
 for _,t:=range vals{for _,f:=range vals{
  s:=State{t,f};output,e:=Rewrite(src,p,s);if e!=nil{return Graph{},e};g.Sources[s]=output
 }}
 for from:=range g.Sources{for _,v:=range vals{
  if from.T!=v{g.Edges=append(g.Edges,Edge{from,State{v,from.F},"true",1})}
  if from.F!=v{g.Edges=append(g.Edges,Edge{from,State{from.T,v},"false",1})}
 }}
 return g,nil
}
func Observe(src string,flag bool)(string,string,error){
 o,e:=Parse(src);if e!=nil{return "","",e}
 if flag{return o.Legacy,o.OnTrue,nil}
 return o.Legacy,o.OnFalse,nil
}
func ExactDistance(g Graph,a,b State)(int,error){
 if _,ok:=g.Sources[a];!ok{return -1,ErrGrammar}
 if _,ok:=g.Sources[b];!ok{return -1,ErrGrammar}
 if a==b{return 0,nil}
 depth:=map[State]int{a:0};q:=[]State{a}
 for len(q)>0{s:=q[0];q=q[1:]
  for _,e:=range g.Edges{
   if e.From!=s{continue}
   if _,ok:=depth[e.To];ok{continue}
   d:=depth[s]+1
   if e.To==b{return d,nil}
   depth[e.To]=d;q=append(q,e.To)
  }
 }
 return -1,nil
}
