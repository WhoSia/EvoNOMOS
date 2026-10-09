// P36-O12: opt-in Q22 research source in pinned ORIGINAL buger/jsonparser.
// Original upstream parser source and APIs remain unchanged.
package jsonparser

import (
 "bytes"
 "fmt"
)

func P36O12SelectRaw(doc []byte,policy string)(string,bool,error){
 if policy!="first"&&policy!="last"{return "",false,fmt.Errorf("P36-O12 unsupported policy %q",policy)}
 if len(doc)==0{return "",false,fmt.Errorf("P36-O12 empty input")}
 token:="";found:=false
 err:=ObjectEach(doc,func(key,value []byte,typ ValueType,offset int)error{
  if !bytes.Equal(key,[]byte("id")){return nil}
  if typ!=Number{return fmt.Errorf("P36-O12 nonnumeric id")}
  if !found||policy=="last"{token=string(value)}
  found=true
  return nil
 },"meta")
 if err!=nil{return "",false,err}
 return token,found,nil
}
