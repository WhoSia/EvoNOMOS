package main
import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "go/ast"
 "go/format"
 "go/parser"
 "go/token"
 "os"
)
func main(){
 out:=map[string]string{}
 for _,p:=range os.Args[1:]{
  f,e:=parser.ParseFile(token.NewFileSet(),p,nil,0);if e!=nil{panic(e)}
  for _,d:=range f.Decls{
   if fn,ok:=d.(*ast.FuncDecl);ok{
    key:="func:"+fn.Name.Name
    if fn.Recv!=nil{
     switch rx:=fn.Recv.List[0].Type.(type){
     case *ast.StarExpr:if id,ok:=rx.X.(*ast.Ident);ok{key="func:"+id.Name+"."+fn.Name.Name}
     case *ast.Ident:key="func:"+rx.Name+"."+fn.Name.Name
     }
    }
    b:=new(bytes.Buffer);if e:=format.Node(b,token.NewFileSet(),fn);e!=nil{panic(e)}
    sum:=sha256.Sum256(b.Bytes());out[key]=hex.EncodeToString(sum[:])
    continue
   }
   if g,ok:=d.(*ast.GenDecl);ok{
    for _,sp:=range g.Specs{if t,ok:=sp.(*ast.TypeSpec);ok{
     b:=new(bytes.Buffer);if e:=format.Node(b,token.NewFileSet(),t);e!=nil{panic(e)}
     sum:=sha256.Sum256(b.Bytes());out["type:"+t.Name.Name]=hex.EncodeToString(sum[:])
    }}
   }
  }
 }
 if e:=json.NewEncoder(os.Stdout).Encode(out);e!=nil{panic(e)}
}
