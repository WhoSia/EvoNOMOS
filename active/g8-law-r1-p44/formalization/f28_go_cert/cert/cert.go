// Package cert checks a closed, deliberately tiny Go syntax fragment.
// It does NOT authenticate actor permissions or hidden source-file completeness.
package cert

import (
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "strconv"
)

var ErrHold = errors.New("HOLD: source or permits not independently certified")
type Case struct { Filename string; Source []byte; Future string }
type Receipt struct { SourceSHA256, Legacy, A, B, Scope, Assumption string }

func Check(a,b Case, actorA,actorB string, grantA,grantB bool)(Receipt,error){
 if !grantA || !grantB || actorA=="" || actorB=="" {return Receipt{},fmt.Errorf("%w: absent grant",ErrHold)}
 if a.Filename!="a.go"||b.Filename!="b.go"||a.Future!="FutureA"||b.Future!="FutureB" {return Receipt{},fmt.Errorf("%w: incorrect file",ErrHold)}
 old,x,err:=parseA(a.Source);if err!=nil{return Receipt{},err}
 y,err:=parseB(b.Source);if err!=nil{return Receipt{},err}
 h:=sha256.New();h.Write([]byte("a.go\x00"));h.Write(a.Source);h.Write([]byte("\x00b.go\x00"));h.Write(b.Source)
 return Receipt{hex.EncodeToString(h.Sum(nil)),old,x,y,"exactly two source files with literal-only functions","caller grants supplied, NOT independently verified"},nil
}
func parseA(data []byte)(string,string,error){
 values,err:=parse(data);if err!=nil{return "","",err}
 if len(values)!=2{return "","",fmt.Errorf("%w: expected exactly two functions",ErrHold)}
 old,ok:=values["Legacy"];if !ok{return "","",fmt.Errorf("%w: no Legacy",ErrHold)}
 x,ok:=values["FutureA"];if !ok{return "","",fmt.Errorf("%w: no FutureA",ErrHold)}
 return old,x,nil
}
func parseB(data []byte)(string,error){
 values,err:=parse(data);if err!=nil{return "",err}
 if len(values)!=1{return "",fmt.Errorf("%w: expected exactly one function",ErrHold)}
 x,ok:=values["FutureB"];if !ok{return "",fmt.Errorf("%w: no FutureB",ErrHold)}
 return x,nil
}
func parse(data []byte)(map[string]string,error){
 f,err:=parser.ParseFile(token.NewFileSet(),"fixture.go",data,parser.AllErrors|parser.ParseComments)
 if err!=nil{return nil,fmt.Errorf("%w: parse error: %v",ErrHold,err)}
 if f.Name.Name!="fixture"||len(f.Comments)!=0{return nil,fmt.Errorf("%w: package or comments",ErrHold)}
 out:=make(map[string]string)
 for _,d:=range f.Decls{
  fn,ok:=d.(*ast.FuncDecl)
  if !ok||fn.Recv!=nil||fn.Type.TypeParams!=nil||fn.Type.Params==nil||len(fn.Type.Params.List)!=0||fn.Type.Results==nil||len(fn.Type.Results.List)!=1||fn.Type.Results.List[0].Names!=nil{return nil,fmt.Errorf("%w: declaration",ErrHold)}
  kind,ok:=fn.Type.Results.List[0].Type.(*ast.Ident)
  if !ok||kind.Name!="string"||fn.Body==nil||len(fn.Body.List)!=1{return nil,fmt.Errorf("%w: function grammar",ErrHold)}
  ret,ok:=fn.Body.List[0].(*ast.ReturnStmt)
  if !ok||len(ret.Results)!=1{return nil,fmt.Errorf("%w: return grammar",ErrHold)}
  lit,ok:=ret.Results[0].(*ast.BasicLit)
  if !ok||lit.Kind!=token.STRING{return nil,fmt.Errorf("%w: nonliteral return",ErrHold)}
  value,err:=strconv.Unquote(lit.Value);if err!=nil{return nil,fmt.Errorf("%w: string",ErrHold)}
  if _,dup:=out[fn.Name.Name];dup{return nil,fmt.Errorf("%w: duplicate name",ErrHold)}
  out[fn.Name.Name]=value
 }
 return out,nil
}
// RepairCost uses ONLY the declared two-demand, unit-cost literal-edit grammar.
// It neither searches unrestricted Go nor proves rights or source completeness.
func RepairCost(a,b string,word []string)(int,error){
 seenA,seenB:=false,false;sum:=0
 for _,d:=range word{
  switch d{
  case "A=new":if !seenA{if a!="new"{sum++};seenA=true}
  case "B=new":if !seenB{if b!="new"{sum++};seenB=true}
  default:return 0,fmt.Errorf("%w: undeclared demand",ErrHold)
  }
 }
 return sum,nil
}
