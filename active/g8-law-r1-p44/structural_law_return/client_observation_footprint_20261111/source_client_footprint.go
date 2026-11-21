package main

// Conservative, strictly bounded source AST check for the direct client
// NewPattern(pattern).Match(value). NOT whole-Go interprocedural slicing.
import (
 "encoding/json"
 "flag"
 "fmt"
 "go/ast"
 "go/parser"
 "go/printer"
 "go/token"
 "sort"
 "strings"
)

type index struct{
 functions map[string]string
 types map[string]string
 safe bool
 warnings []string
}
func repr(fs *token.FileSet,n ast.Node)string{
 var b strings.Builder
 if err:=printer.Fprint(&b,fs,n);err!=nil{panic(err)}
 return b.String()
}
func key(fs *token.FileSet,f *ast.FuncDecl)string{
 if f.Recv==nil{return f.Name.Name}
 if len(f.Recv.List)!=1{return f.Name.Name}
 return strings.TrimPrefix(repr(fs,f.Recv.List[0].Type),"*")+"."+f.Name.Name
}
func pureDirect(fn *ast.FuncDecl)bool{
 if fn.Body==nil{return false}
 safe:=true
 ast.Inspect(fn.Body,func(n ast.Node)bool{
  switch x:=n.(type){
  case *ast.Ident:
   // In this intentionally tiny pinned Pattern model, any unexpected
   // identifier could denote a mutable global or imported hidden state.
   if !map[string]bool{
     "p":true,"i":true,"value":true,"v":true,"Pattern":true,
     "prefix":true,"suffix":true,"wildcard":true,"strings":true,
     "IndexByte":true,"HasPrefix":true,"HasSuffix":true,"ToLower":true,
     "len":true,"true":true,"false":true,
   }[x.Name]{safe=false}
  case *ast.GoStmt,*ast.DeferStmt,*ast.SendStmt,*ast.SelectStmt,
       *ast.TypeAssertExpr,*ast.FuncLit:
   safe=false
  case *ast.CallExpr:
   switch f:=x.Fun.(type){
   case *ast.Ident: if f.Name!="len"{safe=false}
   case *ast.SelectorExpr:
    pkg,ok:=f.X.(*ast.Ident)
    if !ok||pkg.Name!="strings"||
      !map[string]bool{"IndexByte":true,"HasPrefix":true,"HasSuffix":true,"ToLower":true}[f.Sel.Name]{
       safe=false
    }
   default:safe=false
   }
  case *ast.SelectorExpr:
   id,ok:=x.X.(*ast.Ident)
   if !ok{safe=false;break}
   switch id.Name{
   case "strings":
    if !map[string]bool{"IndexByte":true,"HasPrefix":true,"HasSuffix":true,"ToLower":true}[x.Sel.Name]{safe=false}
   case "p":
    if !map[string]bool{"prefix":true,"suffix":true,"wildcard":true}[x.Sel.Name]{safe=false}
   default:safe=false
   }
  }
  return true
 })
 return safe
}
func read(path string)(index,error){
 fs:=token.NewFileSet()
 file,err:=parser.ParseFile(fs,path,nil,parser.AllErrors)
 if err!=nil{return index{},err}
 out:=index{functions:map[string]string{},types:map[string]string{},safe:true}
 for _,d:=range file.Decls{
  switch v:=d.(type){
  case *ast.FuncDecl:
   n:=key(fs,v)
   out.functions[n]=repr(fs,v)
   if n=="NewPattern"||n=="Pattern.Match"{
    if !pureDirect(v){out.safe=false;out.warnings=append(out.warnings,"unapproved direct declaration: "+n)}
   }
  case *ast.GenDecl:
   for _,spec:=range v.Specs{
    if t,ok:=spec.(*ast.TypeSpec);ok{out.types[t.Name.Name]=repr(fs,t)}
   }
  }
 }
 for _,n:=range []string{"NewPattern","Pattern.Match"}{
  if _,ok:=out.functions[n];!ok{out.safe=false;out.warnings=append(out.warnings,"missing declaration: "+n)}
 }
 if _,ok:=out.types["Pattern"];!ok{
  out.safe=false
  out.warnings=append(out.warnings,"missing Pattern type")
 }
 return out,nil
}
func changed(a,b map[string]string)[]string{
 keys:=map[string]bool{}
 for k:=range a{keys[k]=true}
 for k:=range b{keys[k]=true}
 result:=[]string{}
 for k:=range keys{if a[k]!=b[k]{result=append(result,k)}}
 sort.Strings(result)
 return result
}
func main(){
 before:=flag.String("before","","original source path")
 after:=flag.String("after","","mutated source path")
 flag.Parse()
 if *before==""||*after==""{panic("--before and --after are required")}
 a,err:=read(*before);if err!=nil{panic(err)}
 b,err:=read(*after);if err!=nil{panic(err)}
 functions:=changed(a.functions,b.functions)
 types:=changed(a.types,b.types)
 directCodeEqual:=a.functions["NewPattern"]==b.functions["NewPattern"]&&
  a.functions["Pattern.Match"]==b.functions["Pattern.Match"]&&
  a.types["Pattern"]==b.types["Pattern"]
 preserved:=a.safe&&b.safe&&directCodeEqual
 result:=map[string]interface{}{
  "changed_functions":functions,"changed_types":types,
  "file_baseline_may_affect":len(functions)+len(types)>0,
  "direct_microclient_definitely_preserved":preserved,
  "direct_microclient_may_affect":!preserved,
  "direct_declared_calls_purity_approved":a.safe&&b.safe,
  "scope":"Only direct NewPattern(pattern).Match(value), given original Go imports/toolchain and verified local field-only operations; no Router or other Go clients covered.",
  "warnings":append(a.warnings,b.warnings...),
 }
 encoded,err:=json.MarshalIndent(result,"","  ")
 if err!=nil{panic(err)}
 fmt.Println(string(encoded))
}
