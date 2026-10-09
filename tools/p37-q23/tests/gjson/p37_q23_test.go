package gjson

import (
 "bytes"
 "sync"
 "testing"
)
func TestP37Q23SemanticKeyAndExactLexeme(t *testing.T) {
 cases:=[]struct{name,doc,policy,wk,wv string;found,bad bool}{
  {"first-escaped-second",`{"meta":{"id":1e+0,"i\u0064":2.00}}`,"first",`"id"`,"1e+0",true,false},
  {"last-escaped-second",`{"meta":{"id":1e+0,"i\u0064":2.00}}`,"last",`"i\u0064"`,"2.00",true,false},
  {"first-escaped-first",`{"meta":{"i\u0064":-0,"id":3E-2}}`,"first",`"i\u0064"`,"-0",true,false},
  {"last-plain-second",`{"meta":{"i\u0064":-0,"id":3E-2}}`,"last",`"id"`,"3E-2",true,false},
  {"no-match",`{"meta":{"other":2}}`,"first","","",false,false},
  {"string-invalid",`{"meta":{"id":1,"i\u0064":"bad"}}`,"first","","",false,true},
  {"invalid-policy",`{"meta":{"id":1}}`,"middle","","",false,true},
  {"empty-input","","first","","",false,true},
 }
 for _,tc:=range cases {
  t.Run(tc.name,func(t *testing.T){
   doc:=[]byte(tc.doc);before:=append([]byte(nil),doc...)
   k,v,ok,err:=P37Q23SelectOriginalKey(doc,tc.policy)
   if (err!=nil)!=tc.bad{t.Fatalf("P37_Q23_ERROR_CLASS err=%v expected=%v",err,tc.bad)}
   if !tc.bad&&(k!=tc.wk||v!=tc.wv||ok!=tc.found){t.Fatalf("P37_Q23_LEXICAL_MISMATCH k=%q v=%q ok=%v expected k=%q v=%q ok=%v",k,v,ok,tc.wk,tc.wv,tc.found)}
   if !bytes.Equal(doc,before){t.Fatal("P37_Q23_MUTATED_SOURCE")}
  })
 }
}
func TestP37Q23ConcurrentReadOnly(t *testing.T){
 doc:=[]byte(`{"meta":{"id":1e+0,"i\u0064":2.00}}`)
 var w sync.WaitGroup
 errors:=make(chan bool,8)
 for i:=0;i<8;i++ {w.Add(1);go func(i int){defer w.Done();policy,want:="first",`"id"`;if i%2==0 {policy,want="last",`"i\u0064"`};for j:=0;j<64;j++{k,_,ok,err:=P37Q23SelectOriginalKey(doc,policy);if err!=nil||!ok||k!=want{errors<-true;return}}}(i)}
 w.Wait();close(errors);for range errors{t.Fatal("P37_Q23_CONCURRENT_FAILURE")}
}
