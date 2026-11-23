package main

// Source AST custody witness for two fixed P35-P7 Go alternatives.
// It proves syntactic reference/call distinctions only, not runtime semantics.
import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "fmt"
 "go/ast"
 "go/parser"
 "go/printer"
 "go/token"
 "os"
)

type Evidence struct {
 File string `json:"file"`
 ClosureReadsRegistry bool `json:"closure_reads_registry"`
 ClosureReadsGroups bool `json:"closure_reads_groups"`
 PatternASTSHA256 string `json:"pattern_ast_sha256"`
}
func find(f *ast.File, name string)*ast.FuncDecl{
 for _,d:=range f.Decls{if fn,ok:=d.(*ast.FuncDecl);ok&&fn.Name.Name==name{return fn}}
 return nil
}
func returnedClosure(fn *ast.FuncDecl)*ast.FuncLit{
 if fn==nil{return nil}
 for _,s:=range fn.Body.List{
  ret,ok:=s.(*ast.ReturnStmt);if !ok{continue}
  for _,v:=range ret.Results{
   call,ok:=v.(*ast.CallExpr);if !ok{continue}
   for _,arg:=range call.Args{if lit,ok:=arg.(*ast.FuncLit);ok{return lit}}
  }
 }
 return nil
}
func reads(n ast.Node,name string)bool{
 found:=false
 ast.Inspect(n,func(n ast.Node)bool{
  if id,ok:=n.(*ast.Ident);ok&&id.Name==name{found=true}
  return true
 })
 return found
}
func examine(path string)(Evidence,error){
 fs:=token.NewFileSet()
 f,e:=parser.ParseFile(fs,path,nil,parser.AllErrors);if e!=nil{return Evidence{},e}
 handler,pattern:=find(f,"Handler"),find(f,"NewPattern")
 closure:=returnedClosure(handler)
 if closure==nil||pattern==nil{return Evidence{},fmt.Errorf("missing anchored source function at %s",path)}
 var b bytes.Buffer
 if e=printer.Fprint(&b,fs,pattern);e!=nil{return Evidence{},e}
 h:=sha256.Sum256(b.Bytes())
 return Evidence{File:path,ClosureReadsRegistry:reads(closure.Body,"hr"),
  ClosureReadsGroups:reads(closure.Body,"groups"),
  PatternASTSHA256:hex.EncodeToString(h[:])},nil
}
func main(){
 if len(os.Args)!=3{panic("usage: source_ast [LIVE.go] [SNAPSHOT.go]")}
 a,e:=examine(os.Args[1]);if e!=nil{panic(e)}
 b,e:=examine(os.Args[2]);if e!=nil{panic(e)}
 if !a.ClosureReadsRegistry||a.ClosureReadsGroups||b.ClosureReadsRegistry||
  !b.ClosureReadsGroups||a.PatternASTSHA256!=b.PatternASTSHA256{
  panic("source facts changed: no architecture evidence claim")
 }
 out:=map[string]interface{}{"live":a,"snapshot":b,
  "identical_pattern_constructor_ast":true,
  "scope":"Syntax-level reference evidence only; neither contract equivalence nor runtime cost inferred"}
 data,e:=json.MarshalIndent(out,"","  ");if e!=nil{panic(e)}
 fmt.Println(string(data))
}
