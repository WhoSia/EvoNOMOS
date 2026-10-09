package jsonparser

import (
 "bytes"
 "fmt"
 "strconv"
)

// P37 Q23 opt-in repair. Unlike gjson, original ObjectEach exposes decoded
// key bytes; reconstruct the source spelling from the retained raw meta object.
// Scope is the frozen scalar-only Q23 grammar. It is NOT an all-JSON parser.
func p37Q23RawKeys(meta []byte)([]string,error){
 i:=0
 skip:=func(){for i<len(meta)&&(meta[i]==' '||meta[i]=='\n'||meta[i]=='\t'||meta[i]=='\r'){i++}}
 skip();if i>=len(meta)||meta[i]!='{'{return nil,fmt.Errorf("not object")};i++
 keys:=[]string{}
 for {
  skip();if i>=len(meta){return nil,fmt.Errorf("truncated")}
  if meta[i]=='}'{return keys,nil}
  if meta[i]!='"'{return nil,fmt.Errorf("missing quoted key")}
  begin:=i;i++
  for i<len(meta){
   if meta[i]=='\\' {i+=2;continue}
   if meta[i]=='"'{i++;break}
   i++
  }
  if i>len(meta)||meta[i-1]!='"'{return nil,fmt.Errorf("bad quoted key")}
  raw:=string(meta[begin:i])
  if _,err:=strconv.Unquote(raw);err!=nil{return nil,err}
  keys=append(keys,raw)
  skip();if i>=len(meta)||meta[i]!=':'{return nil,fmt.Errorf("missing colon")};i++;skip()
  if i>=len(meta){return nil,fmt.Errorf("no value")}
  if meta[i]=='"'{i++;for i<len(meta){if meta[i]=='\\'{i+=2;continue};if meta[i]=='"'{i++;break};i++}}else{
   for i<len(meta)&&meta[i]!=','&&meta[i]!='}'{i++}
  }
  skip();if i<len(meta)&&meta[i]==','{i++;continue}
  if i<len(meta)&&meta[i]=='}'{return keys,nil}
  return nil,fmt.Errorf("bad field separator")
 }
}
func P37Q23SelectOriginalKey(doc []byte,policy string)(string,string,bool,error){
 if policy!="first"&&policy!="last"{return "","",false,fmt.Errorf("invalid policy")}
 if len(doc)==0{return "","",false,fmt.Errorf("empty")}
 meta,kind,_,err:=Get(doc,"meta")
 if err!=nil||kind!=Object{return "","",false,fmt.Errorf("meta not object: %v",err)}
 rawKeys,err:=p37Q23RawKeys(meta);if err!=nil{return "","",false,err}
 var rk,rv string;found:=false;count:=0
 err=ObjectEach(doc,func(key,value []byte,typ ValueType,offset int)error{
  if count>=len(rawKeys){return fmt.Errorf("raw/decoded traversal length mismatch")}
  quoted:=rawKeys[count];count++
  decoded,err:=strconv.Unquote(quoted)
  if err!=nil||!bytes.Equal(key,[]byte(decoded)){return fmt.Errorf("semantic alignment mismatch")}
  if decoded!="id"{return nil}
  if typ!=Number{return fmt.Errorf("nonnumeric id")}
  if !found||policy=="last"{rk,rv=quoted,string(value)}
  found=true;return nil
 },"meta")
 if err!=nil{return "","",false,err}
 if count!=len(rawKeys){return "","",false,fmt.Errorf("unmatched raw fields")}
 return rk,rv,found,nil
}
