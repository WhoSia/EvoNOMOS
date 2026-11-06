// Package sourcecert certifies a closed pure-value Go syntax fragment.
package sourcecert
import (
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "os"
 "path/filepath"
 "strconv"
)
var ErrHold=errors.New("HOLD: outside closed source/rights contract")
type Receipt struct {
 Grade string
 ScopeSHA256 string
 Legacy,Left,Right string
 CertifiedSourceDirectory string
 RightsEvidence string
}
// CheckDir inventories exactly a.go and b.go. Actor grants are caller claims.
func CheckDir(root string,leftGrant,rightGrant bool)(Receipt,error){
 if !leftGrant||!rightGrant{return Receipt{},fmt.Errorf("%w: missing grants",ErrHold)}
 entries,err:=os.ReadDir(root);if err!=nil{return Receipt{},err}
 if len(entries)!=2{return Receipt{},fmt.Errorf("%w: extra/missing file",ErrHold)}
 data:=map[string][]byte{}
 for _,entry:=range entries{
  name:=entry.Name()
  if name!="a.go"&&name!="b.go"{return Receipt{},fmt.Errorf("%w: unexpected file %s",ErrHold,name)}
  info,err:=os.Lstat(filepath.Join(root,name));if err!=nil{return Receipt{},err}
  if !info.Mode().IsRegular(){return Receipt{},fmt.Errorf("%w: nonregular file",ErrHold)}
  data[name],err=os.ReadFile(filepath.Join(root,name));if err!=nil{return Receipt{},err}
 }
 a,ok:=data["a.go"];if !ok{return Receipt{},fmt.Errorf("%w: no a.go",ErrHold)}
 b,ok:=data["b.go"];if !ok{return Receipt{},fmt.Errorf("%w: no b.go",ErrHold)}
 old,left,err:=parseSource(a,"Left","FutureA",true);if err!=nil{return Receipt{},err}
 _,right,err:=parseSource(b,"Right","FutureB",false);if err!=nil{return Receipt{},err}
 h:=sha256.New();h.Write([]byte("a.go\x00"));h.Write(a);h.Write([]byte("\x00b.go\x00"));h.Write(b)
 return Receipt{Grade:"DIRECTORY_AND_AST_CHECKED_RIGHTS_UNVERIFIED",ScopeSHA256:hex.EncodeToString(h.Sum(nil)),Legacy:old,Left:left,Right:right,CertifiedSourceDirectory:root,RightsEvidence:"caller-supplied grants; not independent authorization"},nil
}
func parseSource(data []byte,typename,future string,legacy bool)(string,string,error){
 file,err:=parser.ParseFile(token.NewFileSet(),"source.go",data,parser.AllErrors|parser.ParseComments)
 if err!=nil{return "","",fmt.Errorf("%w: parse: %v",ErrHold,err)}
 if file.Name.Name!="fixture"||len(file.Comments)!=0||len(file.Imports)!=0{return "","",fmt.Errorf("%w: package or import/comment",ErrHold)}
 expected:=2;if legacy{expected=3}
 if len(file.Decls)!=expected{return "","",fmt.Errorf("%w: declarations",ErrHold)}
 gen,ok:=file.Decls[0].(*ast.GenDecl);if !ok||gen.Tok!=token.TYPE||len(gen.Specs)!=1{return "","",fmt.Errorf("%w: type declaration",ErrHold)}
 ts,ok:=gen.Specs[0].(*ast.TypeSpec);if !ok||ts.Name.Name!=typename||ts.TypeParams!=nil||ts.Assign!=token.NoPos{return "","",fmt.Errorf("%w: type spec",ErrHold)}
 st,ok:=ts.Type.(*ast.StructType);if !ok||st.Fields==nil||len(st.Fields.List)!=1{return "","",fmt.Errorf("%w: value struct",ErrHold)}
 field:=st.Fields.List[0];typ,ok:=field.Type.(*ast.Ident)
 if !ok||typ.Name!="string"||len(field.Names)!=1||field.Names[0].Name!="Value"||field.Tag!=nil{return "","",fmt.Errorf("%w: field",ErrHold)}
 values:=map[string]string{}
 for _,decl:=range file.Decls[1:]{
  fn,ok:=decl.(*ast.FuncDecl)
  if !ok||fn.Recv!=nil||fn.Type.TypeParams!=nil||fn.Type.Params==nil||len(fn.Type.Params.List)!=0||fn.Type.Results==nil||len(fn.Type.Results.List)!=1||fn.Type.Results.List[0].Names!=nil||fn.Body==nil||len(fn.Body.List)!=1{return "","",fmt.Errorf("%w: function",ErrHold)}
  res,ok:=fn.Type.Results.List[0].Type.(*ast.Ident);if !ok||res.Name!="string"{return "","",fmt.Errorf("%w: result type",ErrHold)}
  ret,ok:=fn.Body.List[0].(*ast.ReturnStmt);if !ok||len(ret.Results)!=1{return "","",fmt.Errorf("%w: return",ErrHold)}
  var value string
  if fn.Name.Name=="Legacy"&&legacy{
   lit,ok:=ret.Results[0].(*ast.BasicLit);if !ok||lit.Kind!=token.STRING{return "","",fmt.Errorf("%w: legacy literal",ErrHold)}
   value,err=strconv.Unquote(lit.Value);if err!=nil{return "","",fmt.Errorf("%w: literal",ErrHold)}
  }else if fn.Name.Name==future{
   sel,ok:=ret.Results[0].(*ast.SelectorExpr);if !ok||sel.Sel.Name!="Value"{return "","",fmt.Errorf("%w: selector",ErrHold)}
   paren,ok:=sel.X.(*ast.ParenExpr);if !ok{return "","",fmt.Errorf("%w: parenthesis",ErrHold)}
   comp,ok:=paren.X.(*ast.CompositeLit);if !ok||len(comp.Elts)!=1{return "","",fmt.Errorf("%w: struct construction",ErrHold)}
   ident,ok:=comp.Type.(*ast.Ident);if !ok||ident.Name!=typename{return "","",fmt.Errorf("%w: cross-type",ErrHold)}
   kv,ok:=comp.Elts[0].(*ast.KeyValueExpr);if !ok{return "","",fmt.Errorf("%w: field initializer",ErrHold)}
   fieldname,ok:=kv.Key.(*ast.Ident);if !ok||fieldname.Name!="Value"{return "","",fmt.Errorf("%w: initializer field",ErrHold)}
   lit,ok:=kv.Value.(*ast.BasicLit);if !ok||lit.Kind!=token.STRING{return "","",fmt.Errorf("%w: dynamic initializer",ErrHold)}
   value,err=strconv.Unquote(lit.Value);if err!=nil{return "","",fmt.Errorf("%w: literal",ErrHold)}
  }else{return "","",fmt.Errorf("%w: undeclared function",ErrHold)}
  if _,duplicate:=values[fn.Name.Name];duplicate{return "","",fmt.Errorf("%w: duplicate",ErrHold)}
  values[fn.Name.Name]=value
 }
 if len(values)!=expected-1{return "","",fmt.Errorf("%w: missing functions",ErrHold)}
 value,ok:=values[future];if !ok{return "","",fmt.Errorf("%w: missing future",ErrHold)}
 if legacy{old,ok:=values["Legacy"];if !ok{return "","",fmt.Errorf("%w: missing Legacy",ErrHold)};return old,value,nil}
 return "",value,nil
}
