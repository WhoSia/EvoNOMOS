package gjson

import "fmt"

// P37 Q23 opt-in addition: original GJSON source remains unmodified.
func P37Q23SelectOriginalKey(doc []byte,policy string)(string,string,bool,error){
 if policy!="first"&&policy!="last"{return "","",false,fmt.Errorf("invalid policy")}
 if len(doc)==0{return "","",false,fmt.Errorf("empty")}
 obj:=ParseBytes(doc).Get("meta")
 if !obj.Exists()||!obj.IsObject(){return "","",false,fmt.Errorf("missing meta")}
 var rk,rv string;var found bool;var bad error
 obj.ForEach(func(k,v Result)bool{
  if k.Str!="id"{return true}
  if v.Type!=Number{bad=fmt.Errorf("nonnumeric id");return false}
  if !found||policy=="last"{rk,rv=k.Raw,v.Raw};found=true
  return true
 })
 if bad!=nil{return "","",false,bad}
 return rk,rv,found,nil
}
