package sourcealias

import (
 "bytes"
 "go/ast"
 "go/format"
 "go/parser"
 "go/token"
)

// DetachFutureSource is a REAL Go source transformation limited to the
// closed grammar accepted by Analyze. It inserts a new allocation q and
// changes the Future field reference from p to q in Build(), leaving
// the previously declared Write(c) implementation unchanged.
//
// This is one DECLARED patch operation, not a claim about the number of
// arbitrary Go source changes or measured developer engineering effort.
func DetachFutureSource(src string)(string,error){
 facts,err:=Analyze(src)
 if err!=nil{return "",err}
 if !facts.Shared{return src,nil}
 fs:=token.NewFileSet()
 file,err:=parser.ParseFile(fs,"fixture.go",src,parser.AllErrors|parser.ParseComments)
 if err!=nil{return "",ErrOutsideGrammar}
 build:=file.Decls[2].(*ast.FuncDecl)
 if len(build.Body.List)!=2{return "",ErrOutsideGrammar}
 newCell,err:=parser.ParseExpr(`&Cell{Value:"stable"}`)
 if err!=nil{return "",ErrOutsideGrammar}
 assign:=&ast.AssignStmt{Lhs:[]ast.Expr{ast.NewIdent("q")},Tok:token.DEFINE,Rhs:[]ast.Expr{newCell}}
 originalReturn:=build.Body.List[1].(*ast.ReturnStmt)
 composite:=originalReturn.Results[0].(*ast.CompositeLit)
 for _,field:=range composite.Elts{
  pair:=field.(*ast.KeyValueExpr)
  if ident(pair.Key,"Future"){pair.Value=ast.NewIdent("q")}
 }
 build.Body.List=[]ast.Stmt{build.Body.List[0],assign,originalReturn}
 var buf bytes.Buffer
 if err=format.Node(&buf,fs,file);err!=nil{return "",err}
 result:=buf.String()
 after,err:=Analyze(result)
 if err!=nil||after.Shared||after.LegacyInitial!="stable"||after.LegacyAfterWrite!="stable"||after.FutureAfterWrite!="new"{
  return "",ErrOutsideGrammar
 }
 return result,nil
}

// SafeSourcePatchCost measures only the declared source-patch grammar:
// identity patch cost 0; DetachFutureSource patch cost 1 when needed.
// The later Write(c) call is a RUNTIME action, not another source patch.
func SafeSourcePatchCost(src string)(int,error){
 f,err:=Analyze(src);if err!=nil{return -1,err}
 if !f.Shared{return 0,nil}
 _,err=DetachFutureSource(src)
 if err!=nil{return -1,err}
 return 1,nil
}
