package static
import ("errors";"go/ast";"go/parser";"go/token";"strconv";"strings")
var ErrMissingDemands=errors.New("FrozenDemands source literal not found")
func ExtractFrozenPaths(filename string)([]string,error){
 f,e:=parser.ParseFile(token.NewFileSet(),filename,nil,0);if e!=nil{return nil,e}
 var paths []string
 ast.Inspect(f,func(n ast.Node)bool{
  v,ok:=n.(*ast.ValueSpec);if !ok{return true}
  if len(v.Names)!=1||v.Names[0].Name!="FrozenDemands"||len(v.Values)!=1{return true}
  list,ok:=v.Values[0].(*ast.CompositeLit);if !ok{return true}
  for _,part:=range list.Elts{
   entry,ok:=part.(*ast.CompositeLit);if !ok||len(entry.Elts)<2{continue}
   value,ok:=entry.Elts[1].(*ast.BasicLit);if !ok||value.Kind!=token.STRING{continue}
   path,e:=strconv.Unquote(value.Value);if e==nil{paths=append(paths,path)}
  }
  return false
 })
 if len(paths)==0{return nil,ErrMissingDemands}
 return paths,nil
}
func overlapPath(a,b string)bool{
 x,y:=strings.Split(strings.Trim(a,"/"),"/"),strings.Split(strings.Trim(b,"/"),"/")
 if len(x)!=len(y){return false}
 for i:=range x{
  if x[i]==y[i]||strings.HasPrefix(x[i],"{")&&strings.HasSuffix(x[i],"}")||strings.HasPrefix(y[i],"{")&&strings.HasSuffix(y[i],"}"){continue}
  return false
 }
 return true
}
func DisjointSourcePaths(paths []string)bool{
 for i:=range paths{for j:=i+1;j<len(paths);j++{if overlapPath(paths[i],paths[j]){return false}}}
 return true
}
