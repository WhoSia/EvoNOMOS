package sourcecert
import (
 "bytes"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "os"
 "path/filepath"
 "strconv"
)
type EditReceipt struct {
 Before,After Receipt
 Port string
 Cost int
 ValidatedRule string
}
// CheckLiteralEdit validates exactly one authorized literal-token rewrite.
// Actor grants, repository closure and build identity are still unverified.
func CheckLiteralEdit(before,after,port string,grantA,grantB bool)(EditReceipt,error){
 prev,err:=CheckDir(before,grantA,grantB);if err!=nil{return EditReceipt{},err}
 next,err:=CheckDir(after,grantA,grantB);if err!=nil{return EditReceipt{},err}
 var file,fn,oldVal,newVal string
 switch port{
 case "A":file,fn,oldVal,newVal="a.go","FutureA",prev.Left,next.Left
 case "B":file,fn,oldVal,newVal="b.go","FutureB",prev.Right,next.Right
 default:return EditReceipt{},fmt.Errorf("%w: unknown port",ErrHold)
 }
 if oldVal==newVal{return EditReceipt{},fmt.Errorf("%w: unchanged value",ErrHold)}
 other:="a.go";if file=="a.go"{other="b.go"}
 former,err:=os.ReadFile(filepath.Join(before,other));if err!=nil{return EditReceipt{},err}
 latter,err:=os.ReadFile(filepath.Join(after,other));if err!=nil{return EditReceipt{},err}
 if !bytes.Equal(former,latter){return EditReceipt{},fmt.Errorf("%w: other file changed",ErrHold)}
 oldSrc,err:=os.ReadFile(filepath.Join(before,file));if err!=nil{return EditReceipt{},err}
 newSrc,err:=os.ReadFile(filepath.Join(after,file));if err!=nil{return EditReceipt{},err}
 start,stop,err:=targetLiteral(oldSrc,fn);if err!=nil{return EditReceipt{},err}
 expected:=append([]byte{},oldSrc[:start]...)
 expected=append(expected,[]byte(strconv.Quote(newVal))...)
 expected=append(expected,oldSrc[stop:]...)
 if !bytes.Equal(expected,newSrc){return EditReceipt{},fmt.Errorf("%w: additional byte edits",ErrHold)}
 return EditReceipt{Before:prev,After:next,Port:port,Cost:1,ValidatedRule:"one literal token only; opposite source file byte-identical"},nil
}
func targetLiteral(data []byte,name string)(int,int,error){
 fset:=token.NewFileSet();f,err:=parser.ParseFile(fset,"source.go",data,parser.AllErrors)
 if err!=nil{return 0,0,fmt.Errorf("%w: parse",ErrHold)}
 for _,dec:=range f.Decls{
  fn,ok:=dec.(*ast.FuncDecl);if !ok||fn.Name.Name!=name{continue}
  ret:=fn.Body.List[0].(*ast.ReturnStmt)
  sel:=ret.Results[0].(*ast.SelectorExpr)
  comp:=sel.X.(*ast.ParenExpr).X.(*ast.CompositeLit)
  lit:=comp.Elts[0].(*ast.KeyValueExpr).Value.(*ast.BasicLit)
  return fset.Position(lit.Pos()).Offset,fset.Position(lit.End()).Offset,nil
 }
 return 0,0,fmt.Errorf("%w: target missing",ErrHold)
}
