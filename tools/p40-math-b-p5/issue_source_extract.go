package main

// P40-MATH-B-P5 mechanized extraction of source-local AST anchors, NOT
// mechanically sound whole-Go semantics and NOT a proof of maintainer intent.
import (
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "fmt"
 "go/ast"
 "go/parser"
 "go/printer"
 "go/token"
 "os"
 "path/filepath"
 "strings"
)
type Anchor struct {
 Ecosystem string `json:"ecosystem"`
 Filename string `json:"filename"`
 Symbol string `json:"symbol"`
 Position int `json:"position"`
 Key string `json:"key"`
 ASTBodySHA256 string `json:"ast_body_sha256"`
}
func source(root,fn,owner,name,term,eco string) Anchor {
 p:=filepath.Join(root,fn)
 fset:=token.NewFileSet()
 n,err:=parser.ParseFile(fset,p,nil,parser.AllErrors)
 if err!=nil{panic(err)}
 for _,d:=range n.Decls{
  fd,ok:=d.(*ast.FuncDecl)
  if !ok || fd.Name.Name!=name{continue}
  if owner=="" && fd.Recv!=nil{continue}
  if owner!=""{
   if fd.Recv==nil{continue}
   var repr strings.Builder
   if err:=printer.Fprint(&repr,fset,fd.Recv.List[0].Type);err!=nil{panic(err)}
   if strings.TrimPrefix(repr.String(),"*")!=owner{continue}
  }
  var out strings.Builder
  if err:=printer.Fprint(&out,fset,fd.Body);err!=nil{panic(err)}
  if !strings.Contains(out.String(),term){
   panic("AST function exists but declared source anchor absent: "+eco+"/"+name+": "+term)
  }
  h:=sha256.Sum256([]byte(out.String()))
  return Anchor{eco,fn,owner+"."+name,fset.Position(fd.Pos()).Line,term,hex.EncodeToString(h[:])}
 }
 panic("declared Go source function absent: "+eco+"/"+owner+"."+name)
}
func main(){
 if len(os.Args)!=3{panic("usage issue_source_extract.go ECHO_SOURCE GIN_SOURCE")}
 e,g:=os.Args[1],os.Args[2]
 a:=[]Anchor{
  source(e,"router.go","routeMethods","find","autoHandleHEAD && r == nil","echo"),
  source(e,"router.go","routeMethods","find","r = m.head","echo"),
  source(e,"router.go","","NewRouter","autoHandleHEAD:","echo"),
  source(e,"echo.go","","NewWithConfig","config.Router != nil","echo"),
  source(g,"tree.go","","findWildcard","escapeColon := false","gin"),
  source(g,"tree.go","","findWildcard","c == ':'","gin"),
  source(g,"tree.go","node","addRoute","conflicts with existing wildcard","gin"),
  source(g,"tree.go","node","insertChild","findWildcard(path)","gin"),
 }
 if err:=json.NewEncoder(os.Stdout).Encode(struct{
  Protocol string `json:"protocol"`
  Anchors []Anchor `json:"anchors"`
 }{"P40_P5_ISSUE_SOURCE_AST_ANCHORS_V1",a});err!=nil{panic(err)}
 fmt.Fprintln(os.Stderr,"P40_P5_AST_ISSUE_SOURCE_ANCHORS_PASS",len(a))
}
