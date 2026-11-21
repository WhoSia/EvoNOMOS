package static
import("go/ast";"go/parser";"go/token")
type Facts struct{PointerField,MutexField,FrozenAssignment,ContextInjection,LiveRead,CopyRead,OriginalMiddleware bool}
func ReadFacts(corePath,nativePath string)(Facts,error){
 var f Facts
 a,e:=parser.ParseFile(token.NewFileSet(),corePath,nil,0);if e!=nil{return f,e}
 ast.Inspect(a,func(n ast.Node)bool{
  switch x:=n.(type){
  case *ast.Field:
   for _,name:=range x.Names{
    if name.Name=="shared"{_,f.PointerField=x.Type.(*ast.StarExpr)}
    if name.Name=="mu"{f.MutexField=true}
   }
  case *ast.AssignStmt:
   for _,lhs:=range x.Lhs{if s,ok:=lhs.(*ast.SelectorExpr);ok&&s.Sel.Name=="frozen"{f.FrozenAssignment=true}}
  case *ast.CallExpr:
   if s,ok:=x.Fun.(*ast.SelectorExpr);ok{
    if s.Sel.Name=="WithValue"{f.ContextInjection=true}
    if s.Sel.Name=="Value"{f.CopyRead=true}
   }
  case *ast.SelectorExpr:if x.Sel.Name=="shared"{f.LiveRead=true}
  }
  return true
 })
 b,e:=parser.ParseFile(token.NewFileSet(),nativePath,nil,0);if e!=nil{return f,e}
 ast.Inspect(b,func(n ast.Node)bool{if x,ok:=n.(*ast.CallExpr);ok{if s,ok:=x.Fun.(*ast.SelectorExpr);ok&&s.Sel.Name=="RequestID"{f.OriginalMiddleware=true}};return true})
 return f,nil
}
func(f Facts)All()bool{return f.PointerField&&f.MutexField&&f.FrozenAssignment&&f.ContextInjection&&f.LiveRead&&f.CopyRead&&f.OriginalMiddleware}
