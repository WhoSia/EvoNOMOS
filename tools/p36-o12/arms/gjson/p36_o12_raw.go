// P36-O12: opt-in Q22 research source in pinned ORIGINAL tidwall/gjson.
// Original upstream parser source and APIs remain unchanged.
// Q22 is a new client contract, not a claim about duplicate-key JSON standards.
package gjson

import "fmt"

func P36O12SelectRaw(doc []byte,policy string)(string,bool,error){
 if policy!="first"&&policy!="last"{return "",false,fmt.Errorf("P36-O12 unsupported policy %q",policy)}
 if len(doc)==0 {return "",false,fmt.Errorf("P36-O12 empty input")}
 obj:=ParseBytes(doc).Get("meta")
 if !obj.Exists()||!obj.IsObject(){return "",false,fmt.Errorf("P36-O12 missing meta object")}
 token:="";found:=false
 var bad error
 obj.ForEach(func(key,value Result) bool{
  if key.Str!="id"{return true}
  if value.Type!=Number {
   bad=fmt.Errorf("P36-O12 nonnumeric id")
   return false
  }
  if !found||policy=="last"{token=value.Raw}
  found=true
  // Always scan all id occurrences so that a later invalid occurrence
  // invalidates both first and last policies.
  return true
 })
 if bad!=nil{return "",false,bad}
 return token,found,nil
}
