// Package sourcealias recognizes an intentionally tiny, closed, typed Go AST
// fragment and derives heap alias/footprint facts from source rather than
// accepting a hand-entered Alias=true/false switch. It is NOT general Go analysis.
package sourcealias

import (
 "errors"
 "go/ast"
 "go/parser"
 "go/token"
 "go/types"
 "strconv"
)

var ErrOutsideGrammar=errors.New("source outside the explicitly closed alias grammar")
type Result struct{Shared bool; LegacyInitial,FutureInitial,FutureAfterWrite string; LegacyAfterWrite string}
func ident(e ast.Expr,name string)bool{x,ok:=e.(*ast.Ident);return ok&&x.Name==name}
func typeField(f *ast.Field,names []string,kind string)bool{
 if len(f.Names)!=len(names){return false}
 for i,n:=range names{if f.Names[i].Name!=n{return false}}
 if kind=="string"{return ident(f.Type,"string")}
 if kind=="Clients"{return ident(f.Type,"Clients")}
 if kind=="*Cell"{p,ok:=f.Type.(*ast.StarExpr);return ok&&ident(p.X,"Cell")}
 return false
}
func typeDecl(d ast.Decl,name string,fieldNames []string,fieldType string)bool{
 g,ok:=d.(*ast.GenDecl);if !ok||g.Tok!=token.TYPE||len(g.Specs)!=1{return false}
 t,ok:=g.Specs[0].(*ast.TypeSpec);if !ok||t.Name.Name!=name||t.Assign.IsValid()||t.TypeParams!=nil{return false}
 st,ok:=t.Type.(*ast.StructType);if !ok||st.Fields==nil||len(st.Fields.List)!=1{return false}
 return typeField(st.Fields.List[0],fieldNames,fieldType)
}
func fn(d ast.Decl,name string)(*ast.FuncDecl,bool){
 f,ok:=d.(*ast.FuncDecl)
 return f,ok&&f.Name.Name==name&&f.Recv==nil&&f.Body!=nil&&f.Type.TypeParams==nil
}
func literal(e ast.Expr,expected string)bool{
 b,ok:=e.(*ast.BasicLit);if !ok||b.Kind!=token.STRING{return false}
 s,err:=strconv.Unquote(b.Value);return err==nil&&s==expected
}
func alloc(stmt ast.Stmt)(string,bool){
 a,ok:=stmt.(*ast.AssignStmt);if !ok||a.Tok!=token.DEFINE||len(a.Lhs)!=1||len(a.Rhs)!=1{return "",false}
 name,ok:=a.Lhs[0].(*ast.Ident);if !ok{return "",false}
 u,ok:=a.Rhs[0].(*ast.UnaryExpr);if !ok||u.Op!=token.AND{return "",false}
 c,ok:=u.X.(*ast.CompositeLit);if !ok||!ident(c.Type,"Cell")||len(c.Elts)!=1{return "",false}
 kv,ok:=c.Elts[0].(*ast.KeyValueExpr);if !ok||!ident(kv.Key,"Value")||!literal(kv.Value,"stable"){return "",false}
 return name.Name,true
}
func build(d ast.Decl)(bool,bool){
 f,ok:=fn(d,"Build");if !ok||f.Type.Params==nil||len(f.Type.Params.List)!=0||f.Type.Results==nil||len(f.Type.Results.List)!=1||!typeField(f.Type.Results.List[0],nil,"Clients"){return false,false}
 if len(f.Body.List)!=2&&len(f.Body.List)!=3{return false,false}
 vars:=map[string]bool{}
 for _,s:=range f.Body.List[:len(f.Body.List)-1]{
  name,ok:=alloc(s);if !ok||vars[name]{return false,false};vars[name]=true
 }
 r,ok:=f.Body.List[len(f.Body.List)-1].(*ast.ReturnStmt);if !ok||len(r.Results)!=1{return false,false}
 c,ok:=r.Results[0].(*ast.CompositeLit);if !ok||!ident(c.Type,"Clients")||len(c.Elts)!=2{return false,false}
 refs:=map[string]string{}
 for _,v:=range c.Elts{
  kv,ok:=v.(*ast.KeyValueExpr);if !ok{return false,false}
  key,ok:=kv.Key.(*ast.Ident);if !ok||refs[key.Name]!=""{return false,false}
  val,ok:=kv.Value.(*ast.Ident);if !ok||!vars[val.Name]{return false,false}
  refs[key.Name]=val.Name
 }
 if refs["Legacy"]==""||refs["Future"]==""{return false,false}
 if len(vars)!=len(f.Body.List)-1{return false,false}
 // Forbid extra allocations not referenced by either client.
 if len(vars)==2&&refs["Legacy"]==refs["Future"]{return false,false}
 return refs["Legacy"]==refs["Future"],true
}
func write(d ast.Decl)bool{
 f,ok:=fn(d,"Write");if !ok||f.Type.Params==nil||len(f.Type.Params.List)!=1||f.Type.Results!=nil||len(f.Body.List)!=1{return false}
 if !typeField(f.Type.Params.List[0],[]string{"c"},"Clients"){return false}
 a,ok:=f.Body.List[0].(*ast.AssignStmt);if !ok||a.Tok!=token.ASSIGN||len(a.Lhs)!=1||len(a.Rhs)!=1||!literal(a.Rhs[0],"new"){return false}
 field,ok:=a.Lhs[0].(*ast.SelectorExpr);if !ok||field.Sel.Name!="Value"{return false}
 base,ok:=field.X.(*ast.SelectorExpr);return ok&&ident(base.X,"c")&&base.Sel.Name=="Future"
}
// Analyze rejects imports, comments, extra declarations/statement shapes,
// ill-typed source and hidden mutation. Within that closed grammar it derives
// equality of the two heap pointers via their common allocation origin.
func Analyze(src string)(Result,error){
 fs:=token.NewFileSet()
 f,err:=parser.ParseFile(fs,"fixture.go",src,parser.ParseComments|parser.AllErrors)
 if err!=nil||f==nil||f.Name.Name!="fixture"||len(f.Comments)!=0||len(f.Decls)!=4||len(f.Imports)!=0{return Result{},ErrOutsideGrammar}
 if !typeDecl(f.Decls[0],"Cell",[]string{"Value"},"string")||!typeDecl(f.Decls[1],"Clients",[]string{"Legacy","Future"},"*Cell"){return Result{},ErrOutsideGrammar}
 shared,ok:=build(f.Decls[2]);if !ok||!write(f.Decls[3]){return Result{},ErrOutsideGrammar}
 if _,err=(&types.Config{}).Check("fixture",fs,[]*ast.File{f},nil);err!=nil{return Result{},ErrOutsideGrammar}
 legacy:="stable";if shared{legacy="new"}
 return Result{Shared:shared,LegacyInitial:"stable",FutureInitial:"stable",LegacyAfterWrite:legacy,FutureAfterWrite:"new"},nil
}
