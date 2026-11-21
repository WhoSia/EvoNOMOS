// Package cert recognizes a closed two-file, no-escape Go fresh-pointer grammar.
// User-asserted editor grants are NOT independently authenticated.
package cert

import (
 "bytes"
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
 "strings"
)

var ErrHold=errors.New("HOLD: source, scope or grant not certified")
type Receipt struct {
 Grade string
 SourceSHA256 string
 Legacy string
 A string
 B string
 RightsEvidence string
}
type EditReceipt struct { Before Receipt; After Receipt; Port string; Cost int }
type span struct {start,end int}

// CheckDir reads ONLY an explicitly closed two-file research-language snapshot.
// It does not attest a whole repository or the external provenance of grants.
func CheckDir(dir string,grants map[string]bool)(Receipt,error){
 if !grants["A"]||!grants["B"] {return Receipt{},fmt.Errorf("%w: absent grant",ErrHold)}
 entries,err:=os.ReadDir(dir);if err!=nil{return Receipt{},err}
 if len(entries)!=2{return Receipt{},fmt.Errorf("%w: unexpected directory entries",ErrHold)}
 data:=map[string][]byte{}
 for _,e:=range entries{
  name:=e.Name()
  if name!="a.go"&&name!="b.go"{return Receipt{},fmt.Errorf("%w: unexpected file",ErrHold)}
  st,err:=os.Lstat(filepath.Join(dir,name));if err!=nil{return Receipt{},err}
  if !st.Mode().IsRegular(){return Receipt{},fmt.Errorf("%w: not regular file",ErrHold)}
  bytes,err:=os.ReadFile(filepath.Join(dir,name));if err!=nil{return Receipt{},err}
  data[name]=bytes
 }
 a,oka:=data["a.go"];b,okb:=data["b.go"]
 if !oka||!okb{return Receipt{},fmt.Errorf("%w: missing source",ErrHold)}
 old,va,_,err:=parse(a,"Left","FutureA",true);if err!=nil{return Receipt{},err}
 _,vb,_,err:=parse(b,"Right","FutureB",false);if err!=nil{return Receipt{},err}
 h:=sha256.New();h.Write([]byte("a.go\x00"));h.Write(a);h.Write([]byte("\x00b.go\x00"));h.Write(b)
 return Receipt{"DIRECTORY_AST_FRESH_POINTER_RIGHTS_UNVERIFIED",hex.EncodeToString(h.Sum(nil)),old,va,vb,"caller grant only; no external attestation"},nil
}

// parse allows exactly a fresh &T{Value:"literal"} bound to p and return p.Value.
// No global pointers, name aliasing, function calls, methods or escape sites.
func parse(src []byte,typename,future string,needsOld bool)(string,string,span,error){
 bad:=func(why string)(string,string,span,error){return "","",span{},fmt.Errorf("%w: %s",ErrHold,why)}
 fs:=token.NewFileSet()
 f,err:=parser.ParseFile(fs,"source.go",src,parser.AllErrors|parser.ParseComments)
 if err!=nil{return bad("syntax")}
 if f.Name.Name!="fixture"||len(f.Imports)!=0||len(f.Comments)!=0{return bad("package/import/comment")}
 expected:=2;if needsOld{expected=3}
 if len(f.Decls)!=expected{return bad("declaration count")}
 decl,ok:=f.Decls[0].(*ast.GenDecl);if !ok||decl.Tok!=token.TYPE||len(decl.Specs)!=1{return bad("type declaration")}
 spec,ok:=decl.Specs[0].(*ast.TypeSpec)
 if !ok||spec.Name.Name!=typename||spec.TypeParams!=nil||spec.Assign.IsValid(){return bad("type name or alias")}
 typ,ok:=spec.Type.(*ast.StructType);if !ok||typ.Fields==nil||len(typ.Fields.List)!=1{return bad("struct")}
 field:=typ.Fields.List[0]
 if len(field.Names)!=1||field.Names[0].Name!="Value"||field.Tag!=nil{return bad("field")}
 kind,ok:=field.Type.(*ast.Ident);if !ok||kind.Name!="string"{return bad("pointer/interface field")}
 vals:=map[string]string{};loc:=span{}
 for _,d:=range f.Decls[1:]{
  fn,ok:=d.(*ast.FuncDecl)
  if !ok||fn.Recv!=nil||fn.Type.TypeParams!=nil||fn.Type.Params==nil||len(fn.Type.Params.List)!=0||fn.Type.Results==nil||len(fn.Type.Results.List)!=1||len(fn.Type.Results.List[0].Names)!=0||fn.Body==nil{return bad("function signature")}
  retType,ok:=fn.Type.Results.List[0].Type.(*ast.Ident);if !ok||retType.Name!="string"{return bad("result type")}
  name:=fn.Name.Name
  if _,exists:=vals[name];exists{return bad("duplicate function")}
  if name=="Legacy"&&needsOld{
   if len(fn.Body.List)!=1{return bad("legacy statements")}
   ret,ok:=fn.Body.List[0].(*ast.ReturnStmt);if !ok||len(ret.Results)!=1{return bad("legacy return")}
   lit,ok:=ret.Results[0].(*ast.BasicLit);if !ok||lit.Kind!=token.STRING{return bad("legacy dynamic")}
   v,e:=strconv.Unquote(lit.Value);if e!=nil{return bad("legacy literal")}
   vals[name]=v
  }else if name==future{
   if len(fn.Body.List)!=2{return bad("future statements")}
   a,ok:=fn.Body.List[0].(*ast.AssignStmt)
   if !ok||a.Tok!=token.DEFINE||len(a.Lhs)!=1||len(a.Rhs)!=1{return bad("local binding")}
   p,ok:=a.Lhs[0].(*ast.Ident);if !ok||p.Name!="p"{return bad("local pointer name")}
   ptr,ok:=a.Rhs[0].(*ast.UnaryExpr);if !ok||ptr.Op!=token.AND{return bad("fresh address")}
   ct,ok:=ptr.X.(*ast.CompositeLit);if !ok||len(ct.Elts)!=1{return bad("fresh struct")}
   id,ok:=ct.Type.(*ast.Ident);if !ok||id.Name!=typename{return bad("cross type")}
   kv,ok:=ct.Elts[0].(*ast.KeyValueExpr);if !ok{return bad("initializer")}
   k,ok:=kv.Key.(*ast.Ident);if !ok||k.Name!="Value"{return bad("initializer key")}
   lit,ok:=kv.Value.(*ast.BasicLit);if !ok||lit.Kind!=token.STRING{return bad("dynamic initializer")}
   v,e:=strconv.Unquote(lit.Value)
   if e!=nil||!strings.HasPrefix(lit.Value,"\"")||strconv.Quote(v)!=lit.Value{return bad("noncanonical string")}
   r,ok:=fn.Body.List[1].(*ast.ReturnStmt);if !ok||len(r.Results)!=1{return bad("return")}
   sel,ok:=r.Results[0].(*ast.SelectorExpr);if !ok||sel.Sel.Name!="Value"{return bad("selector")}
   ident,ok:=sel.X.(*ast.Ident);if !ok||ident.Name!="p"{return bad("escaped/aliased pointer")}
   vals[name]=v
   loc=span{fs.Position(lit.Pos()).Offset,fs.Position(lit.End()).Offset}
  }else{return bad("unexpected function")}
 }
 if len(vals)!=expected-1{return bad("missing functions")}
 v,ok:=vals[future];if !ok{return bad("missing future")}
 if needsOld{old,ok:=vals["Legacy"];if !ok{return bad("missing legacy")};return old,v,loc,nil}
 return "",v,loc,nil
}

// CheckEdit proves exactly ONE change at a source literal token and no others.
// It does not validate grant provenance, atomic filesystem snapshot, or actual build.
func CheckEdit(before,after,port string,grants map[string]bool)(EditReceipt,error){
 old,err:=CheckDir(before,grants);if err!=nil{return EditReceipt{},err}
 next,err:=CheckDir(after,grants);if err!=nil{return EditReceipt{},err}
 file,typ,fn:="a.go","Left","FutureA"
 from,to:=old.A,next.A
 if port=="B"{file,typ,fn="b.go","Right","FutureB";from,to=old.B,next.B}else if port!="A"{return EditReceipt{},fmt.Errorf("%w: unknown port",ErrHold)}
 if from==to{return EditReceipt{},fmt.Errorf("%w: no change",ErrHold)}
 other:="b.go";if file=="b.go"{other="a.go"}
 x,err:=os.ReadFile(filepath.Join(before,other));if err!=nil{return EditReceipt{},err}
 y,err:=os.ReadFile(filepath.Join(after,other));if err!=nil{return EditReceipt{},err}
 if !bytes.Equal(x,y){return EditReceipt{},fmt.Errorf("%w: opposite file changed",ErrHold)}
 src,err:=os.ReadFile(filepath.Join(before,file));if err!=nil{return EditReceipt{},err}
 target,err:=os.ReadFile(filepath.Join(after,file));if err!=nil{return EditReceipt{},err}
 _,_,loc,err:=parse(src,typ,fn,file=="a.go");if err!=nil{return EditReceipt{},err}
 expected:=append(append([]byte{},src[:loc.start]...),[]byte(strconv.Quote(to))...)
 expected=append(expected,src[loc.end:]...)
 if !bytes.Equal(expected,target){return EditReceipt{},fmt.Errorf("%w: unapproved byte changes",ErrHold)}
 return EditReceipt{old,next,port,1},nil
}
