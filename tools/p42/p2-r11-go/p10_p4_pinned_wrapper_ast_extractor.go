// P42 R11-P10-P4: syntax-evidence-only source extractor (Go stdlib).
// Parse success does NOT prove program semantics, grant upstream authority,
// or establish that any unobserved client is protected.
package main

import (
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "flag"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "os"
 "path/filepath"
 "sort"
)

func receiverName(e ast.Expr) string {
 if star,ok:=e.(*ast.StarExpr);ok {e=star.X}
 if t,ok:=e.(*ast.Ident);ok {return t.Name}
 return ""
}
func isSelector(e ast.Expr, lhs,rhs string) bool {
 s,ok:=e.(*ast.SelectorExpr)
 if !ok || s.Sel.Name!=rhs {return false}
 base,ok:=s.X.(*ast.Ident)
 return ok&&base.Name==lhs
}
func extract(repo,commit,root,file,receiver string) (map[string]interface{},error) {
 filename:=filepath.Join(root,file)
 b,err:=os.ReadFile(filename);if err!=nil{return nil,err}
 parsed,err:=parser.ParseFile(token.NewFileSet(),filename,b,parser.AllErrors);if err!=nil{return nil,err}
 sum:=sha256.Sum256(b)
 methods:=map[string]bool{}
 hasAssert,hasController,hasPanic:=false,false,false
 for _,decl:=range parsed.Decls {
  fd,ok:=decl.(*ast.FuncDecl)
  if !ok||fd.Recv==nil||len(fd.Recv.List)!=1 {continue}
  if receiverName(fd.Recv.List[0].Type)!=receiver {continue}
  methods[fd.Name.Name]=true
  if fd.Name.Name!="Flush"||fd.Body==nil {continue}
  ast.Inspect(fd.Body,func(n ast.Node) bool {
   switch q:=n.(type) {
   case *ast.TypeAssertExpr:
    if isSelector(q.Type,"http","Flusher") {hasAssert=true}
   case *ast.CallExpr:
    if isSelector(q.Fun,"http","NewResponseController"){hasController=true}
    if id,ok:=q.Fun.(*ast.Ident);ok&&id.Name=="panic"{hasPanic=true}
   }
   return true
  })
 }
 names:=[]string{}
 for m:=range methods {names=append(names,m)}
 sort.Strings(names)
 if !methods["Flush"]||!methods["Unwrap"] {
  return nil,fmt.Errorf("%s: wrapper %s lacks source-declared Flush or Unwrap",repo,receiver)
 }
 return map[string]interface{}{
  "repository":repo,"source_commit":commit,"source_path":file,
  "source_file_sha256":hex.EncodeToString(sum[:]),"wrapper_type":receiver,
  "declared_receiver_methods":names,"declares_flush":methods["Flush"],
  "declares_unwrap":methods["Unwrap"],
  "flush_ast_type_assert_http_flusher":hasAssert,
  "flush_ast_calls_http_new_response_controller":hasController,
  "flush_ast_has_panic_call":hasPanic,
  "old_client_semantics":"UNKNOWN_UNTIL_INDEPENDENT_NATIVE_TEST",
  "upstream_source_edit_authority":"UNKNOWN",
  "human_edit_cost":"UNKNOWN",
  "type_system_proof":"NOT_DONE_BY_AST_SYNTAX_SCAN",
  "evidence_level":"SOURCE_SHA256_AND_PINNED_GIT_BLOB_AST_ONLY",
 },nil
}
func main(){
 ginRoot:=flag.String("gin","","pinned Gin repo checkout")
 echoRoot:=flag.String("echo","","pinned Echo repo checkout")
 dest:=flag.String("out","out/p42-r11-p10-p4/source-ast-evidence.json","report path")
 flag.Parse()
 if *ginRoot==""||*echoRoot=="" {fmt.Fprintln(os.Stderr,"both roots required");os.Exit(2)}
 specs:=[]struct{repo,commit,root,file,typ string}{
  {"gin-gonic/gin","d3ffc9985281dcf4d3bef604cce4e662b1a327a6",*ginRoot,"response_writer.go","responseWriter"},
  {"labstack/echo","86d0223c7aa39b865a9452de3479897fcb5a3939",*echoRoot,"response.go","Response"},
 }
 out:=map[string]interface{}{
  "protocol":"EVONOMOS_P42_R11_P10_P4_PINNED_SOURCE_AST_FACTS",
  "contract":"AST syntax facts only; no semantic effects, rights, dynamic linking, complete clients, or real costs certified."}
 sources:=[]interface{}{}
 for _,s:=range specs {
  e,err:=extract(s.repo,s.commit,s.root,s.file,s.typ)
  if err!=nil {fmt.Fprintln(os.Stderr,"EXTRACTOR_HOLD:",err);os.Exit(1)}
  sources=append(sources,e)
  fmt.Printf("AST_SOURCE %s methods=%v FlusherAssert=%v Controller=%v Panic=%v RIGHTS_UNKNOWN\n",
   s.repo,e["declared_receiver_methods"],e["flush_ast_type_assert_http_flusher"],
   e["flush_ast_calls_http_new_response_controller"],e["flush_ast_has_panic_call"])
 }
 out["sources"]=sources
 b,err:=json.MarshalIndent(out,"","  ");if err!=nil{panic(err)}
 if err:=os.MkdirAll(filepath.Dir(*dest),0755);err!=nil{panic(err)}
 if err:=os.WriteFile(*dest,append(b,'\n'),0644);err!=nil{panic(err)}
 fmt.Println("P10_P4_PINNED_SOURCE_AST_EXTRACTION_PASS")
}
