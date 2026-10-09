package p35pair

import (
  "go/ast"
  "go/parser"
  "go/token"
  "testing"
)

// Not an ordinary public trace check: this is the pre-declared treatment
// constraint that the reader, not the writer's store, owns decoding.
func TestP35P3FrozenIndependentDecoder(t *testing.T) {
 f,err:=parser.ParseFile(token.NewFileSet(),"backend.go",nil,0)
 if err!=nil {t.Fatal(err)}
 foundReader,foundStore:=false,false
 for _,d:=range f.Decls {
  fn,ok:=d.(*ast.FuncDecl);if !ok||fn.Recv==nil||len(fn.Recv.List)==0 {continue}
  ptr,ok:=fn.Recv.List[0].Type.(*ast.StarExpr);if !ok {continue}
  receiver,ok:=ptr.X.(*ast.Ident);if !ok {continue}
  if receiver.Name=="readEngine"&&fn.Name.Name=="decode" {
   foundReader=true; foundDecodeCall:=false
   ast.Inspect(fn.Body,func(n ast.Node)bool {if c,ok:=n.(*ast.CallExpr);ok {if id,ok:=c.Fun.(*ast.Ident);ok&&id.Name=="decodePayload"{foundDecodeCall=true}};return true})
   if !foundDecodeCall {t.Fatal("P35_ARCHITECTURAL_DRIFT: independent readEngine does not decode")}
  }
  if receiver.Name=="payloadStore"&&fn.Name.Name=="get" {
   foundStore=true
   ast.Inspect(fn.Body,func(n ast.Node)bool {if c,ok:=n.(*ast.CallExpr);ok {if id,ok:=c.Fun.(*ast.Ident);ok&&id.Name=="decodePayload"{t.Error("P35_ARCHITECTURAL_DRIFT: payloadStore.get relocated decode")}};return true})
  }
 }
 if !foundReader||!foundStore{t.Fatal("P35 missing decoder/storage methods")}
 c:=newComposed()
 if c.read.source!=c.write || c.index==nil || c.remove==nil {t.Fatal("P35 capability wiring broken")}
 t.Log("P35_P3_FROZEN_READ_DECODER=PASS")
}
