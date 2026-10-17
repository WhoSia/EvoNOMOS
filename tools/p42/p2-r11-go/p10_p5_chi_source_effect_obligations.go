// Pure Go AST proof-obligation extractor for authentic Chi #1185 source.
// Recognizes a deliberately small AST language. Everything else is UNKNOWN,
// not an invented source-to-trace simulation theorem.
package main

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "flag"
 "fmt"
 "go/ast"
 "go/format"
 "go/parser"
 "go/token"
 "os"
 "path/filepath"
 "strings"
)

type Report struct {
 Protocol string `json:"protocol"`
 Original Source `json:"original"`
 Merged Source `json:"merged"`
 Verdict string `json:"verdict"`
 Unresolved []string `json:"unresolved"`
}
type Source struct {
 SHA256 string `json:"source_sha256"`
 FlushMethods []string `json:"flush_receiver_types"`
 AllFlushASTCalls []string `json:"flush_ast_calls"`
 HelperGuard string `json:"helper_sink_guard"`
 DirectSinkCount int `json:"direct_sink_methods"`
 HelperDelegations int `json:"helper_delegated_methods"`
 GuardedSink bool `json:"guarded_underlying_sink"`
 Status string `json:"status"`
}
func render(fset *token.FileSet,node ast.Node) string {
 var b bytes.Buffer
 if err:=format.Node(&b,fset,node);err!=nil{panic(err)}
 return b.String()
}
func receiver(e ast.Expr) string {
 if ptr,ok:=e.(*ast.StarExpr);ok {e=ptr.X}
 if id,ok:=e.(*ast.Ident);ok{return id.Name}
 return ""
}
func extract(path string, old bool) (Source,error) {
 bytes,err:=os.ReadFile(path);if err!=nil{return Source{},err}
 fset:=token.NewFileSet()
 root,err:=parser.ParseFile(fset,path,bytes,parser.AllErrors);if err!=nil{return Source{},err}
 sum:=sha256.Sum256(bytes)
 s:=Source{SHA256:hex.EncodeToString(sum[:]),HelperGuard:"NOT_FOUND",
 Status:"RESTRICTED_AST_PATTERN_ONLY_SEMANTIC_PROOF_OPEN"}
 for _,d:=range root.Decls {
  fn,ok:=d.(*ast.FuncDecl);if !ok||fn.Recv==nil||fn.Body==nil {continue}
  typ:=receiver(fn.Recv.List[0].Type)
  if fn.Name.Name=="Flush" && typ!="basicWriter" {
   s.FlushMethods=append(s.FlushMethods,typ)
   src:=render(fset,fn.Body)
   s.AllFlushASTCalls=append(s.AllFlushASTCalls,src)
   if strings.Contains(src,"ResponseWriter.(http.Flusher)") && strings.Contains(src,"fl.Flush()") {
    s.DirectSinkCount++
   } else if strings.Contains(src,"basicWriter.flush()") {
    s.HelperDelegations++
   } else {return Source{},fmt.Errorf("unsupported Flush syntax in %s",typ)}
  }
  if fn.Name.Name=="flush" && typ=="basicWriter" {
   src:=render(fset,fn.Body)
   s.HelperGuard="UNRECOGNIZED"
   // Here we inspect actual AST structure, not merely a string search:
   // an if with NOT(b.discard), whose sole arm includes downstream Flush.
   for _,st:=range fn.Body.List {
    cond,ok:=st.(*ast.IfStmt);if !ok{continue}
    condition:=render(fset,cond.Cond)
    if condition!="!b.discard" {continue}
    sink:=false
    ast.Inspect(cond.Body,func(node ast.Node)bool{
     call,ok:=node.(*ast.CallExpr)
     if ok && strings.Contains(render(fset,call.Fun),"ResponseWriter.(http.Flusher).Flush") {
      sink=true
     }
     return true
    })
    if sink && cond.Else==nil {
     s.HelperGuard="!b.discard"
     s.GuardedSink=true
    }
   }
   _=src
  }
 }
 if len(s.FlushMethods)!=4{return Source{},fmt.Errorf("expected four specific original Chi variants, got %d",len(s.FlushMethods))}
 expected:=map[string]bool{"flushWriter":true,"flushHijackWriter":true,"httpFancyWriter":true,"http2FancyWriter":true}
 for _,name:=range s.FlushMethods{
  if !expected[name]{return Source{},fmt.Errorf("unexpected source wrapper %s",name)}
  delete(expected,name)
 }
 if old {
  if s.DirectSinkCount!=4||s.HelperDelegations!=0||s.GuardedSink {
   return Source{},fmt.Errorf("old source fails exact AST contract")
  }
 } else {
  if s.DirectSinkCount!=0||s.HelperDelegations!=4||!s.GuardedSink {
   return Source{},fmt.Errorf("merged source fails exact guarded AST contract: %+v",s)
  }
 }
 return s,nil
}
func main() {
 old:=flag.String("old","","pinned old middleware/wrap_writer.go")
 merged:=flag.String("merged","","pinned merged middleware/wrap_writer.go")
 out:=flag.String("out","out/p42-r11-p10-p5/source-effect-obligations.json","output")
 flag.Parse()
 if *old==""||*merged==""{fmt.Fprintln(os.Stderr,"missing old/merged source");os.Exit(2)}
 a,err:=extract(*old,true);if err!=nil{fmt.Fprintln(os.Stderr,"OLD_AST_HOLD:",err);os.Exit(1)}
 b,err:=extract(*merged,false);if err!=nil{fmt.Fprintln(os.Stderr,"NEW_AST_HOLD:",err);os.Exit(1)}
 r:=Report{Protocol:"EVONOMOS_R11_P10_P5_CHI1185_RESTRICTED_AST_PROOF_OBLIGATIONS",
 Original:a,Merged:b,Verdict:"SOURCE_AST_PATTERN_CERTIFIED_GLOBAL_SEMANTICS_UNPROVEN",
 Unresolved:[]string{
  "G1: prove Go selector/type-assertion semantics for the pinned build and all eligible receiver values",
  "G2: prove b.discard read is stable between Discard and Flush under admissible concurrency/reentrancy",
  "G3: prove the exact call graph has no alternative dynamic sink and middleware wrapper type is the actual call target",
  "G4: prove maybeWriteHeader effects meet the declared protected client observations",
  "G5: prove old client set and runtime/resource trace alphabet are complete for the claimed refinement",
  "G6: independently verify authority to perform each upstream source edit; GitHub access is not source ownership",
  "G7: certify real repair action costs and stagewise effects; AST paths alone have no human-time estimates",
 }}
 body,err:=json.MarshalIndent(r,"","  ");if err!=nil{panic(err)}
 if err:=os.MkdirAll(filepath.Dir(*out),0755);err!=nil{panic(err)}
 if err:=os.WriteFile(*out,append(body,'\n'),0644);err!=nil{panic(err)}
 fmt.Printf("P10_P5_AUTHENTIC_CHI_AST_PROOF_OBLIGATIONS_PASS oldDirect=%d mergedDelegated=%d mergedDiscardGuard=%t unresolved=%d\n",a.DirectSinkCount,b.HelperDelegations,b.GuardedSink,len(r.Unresolved))
}
