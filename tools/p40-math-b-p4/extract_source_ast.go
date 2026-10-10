// P40-MATH-B-P4: pinned Go AST source-evidence extractor.
// This parses original files and checks narrowly declared syntactic witness
// signatures. It does NOT prove a complete router source semantics.
package main

import (
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

type Claim struct {
 Source string `json:"source"`
 Symbol string `json:"symbol"`
 File string `json:"file"`
 Line int `json:"line"`
 Needle string `json:"needle"`
 Found bool `json:"found"`
}
type Receipt struct {
 Protocol string `json:"protocol"`
 Claims []Claim `json:"claims"`
}
func functionIn(path, owner, name string) (*ast.FuncDecl,*token.FileSet,error) {
 fset:=token.NewFileSet()
 file,err:=parser.ParseFile(fset,path,nil,parser.AllErrors|parser.ParseComments)
 if err!=nil{return nil,nil,err}
 for _,decl:=range file.Decls{
  fd,ok:=decl.(*ast.FuncDecl);if !ok||fd.Name.Name!=name{continue}
  if owner=="" && fd.Recv==nil {return fd,fset,nil}
  if owner!="" && fd.Recv!=nil {
   var rec strings.Builder
   _=printer.Fprint(&rec,fset,fd.Recv.List[0].Type)
   if strings.TrimPrefix(rec.String(),"*")==owner{return fd,fset,nil}
  }
 }
 return nil,nil,fmt.Errorf("symbol %s.%s not found in %s",owner,name,path)
}
func statement(path,source,owner,name,needle string)Claim {
 fd,fset,err:=functionIn(path,owner,name)
 if err!=nil {panic(err)}
 var text strings.Builder
 if err:=printer.Fprint(&text,fset,fd.Body);err!=nil{panic(err)}
 body:=text.String()
 cl:=Claim{Source:source,Symbol:owner+"."+name,File:filepath.Base(path),Line:fset.Position(fd.Pos()).Line,Needle:needle,Found:strings.Contains(body,needle)}
 if !cl.Found{panic(fmt.Sprintf("AST source signal missing %s: %s",cl.Symbol,needle))}
 return cl
}
func main(){
 if len(os.Args)!=4{
  fmt.Fprintln(os.Stderr,"usage: extract_source_ast.go CHI_ROOT HTTPROUTER_ROOT ECHO_ROOT")
  os.Exit(2)
 }
 chi,hr,echo:=os.Args[1],os.Args[2],os.Args[3]
 claims:=[]Claim{
  statement(filepath.Join(chi,"mux.go"),"chi","Mux","Mount","findPattern"),
  statement(filepath.Join(chi,"mux.go"),"chi","Mux","Mount","subr.tree == mx.tree"),
  statement(filepath.Join(chi,"mux.go"),"chi","Mux","Mount","mALL"),
  statement(filepath.Join(chi,"mux.go"),"chi","Mux","Use","mx.handler != nil"),
  statement(filepath.Join(hr,"router.go"),"httprouter","Router","Handle","r.trees[method]"),
  statement(filepath.Join(hr,"tree.go"),"httprouter","node","addRoute","Wildcard conflict"),
  statement(filepath.Join(hr,"tree.go"),"httprouter","node","addRoute","a handle is already registered"),
  statement(filepath.Join(echo,"router.go"),"echo","DefaultRouter","Add","allowOverwritingRoute"),
  statement(filepath.Join(echo,"router.go"),"echo","DefaultRouter","insert","addStaticChild"),
  statement(filepath.Join(echo,"router.go"),"echo","DefaultRouter","insert","paramChild"),
  statement(filepath.Join(echo,"router.go"),"echo","DefaultRouter","insert","anyChild"),
  statement(filepath.Join(echo,"echo.go"),"echo","","New","AllowOverwritingRoute: true"),
 }
 enc:=json.NewEncoder(os.Stdout);enc.SetIndent("","  ")
 if err:=enc.Encode(Receipt{Protocol:"P40_P4_AST_SIGNAL_RECEIPT_V1",Claims:claims});err!=nil{panic(err)}
}
