package gjson

import (
 "bytes"
 "fmt"
 "sync"
 "testing"
)

func TestP36O12LexicalProvenanceQ22(t *testing.T) {
 cases:=[]struct{name,doc,policy,want string;found,err bool}{
  {"first-exp",`{"meta":{"id":1e+0,"other":9,"id":2.00}}`,"first","1e+0",true,false},
  {"last-decimal",`{"meta":{"id":1e+0,"other":9,"id":2.00}}`,"last","2.00",true,false},
  {"signed-zero",`{"meta":{"id":-0,"id":3E-2,"id":10}}`,"first","-0",true,false},
  {"last-of-three",`{"meta":{"id":-0,"id":3E-2,"id":10}}`,"last","10",true,false},
  {"missing-first",`{"meta":{"other":1}}`,"first","",false,false},
  {"missing-last",`{"meta":{"other":1}}`,"last","",false,false},
  {"unique-first",`{"meta":{"id":4}}`,"first","4",true,false},
  {"unique-last",`{"meta":{"id":4}}`,"last","4",true,false},
  {"nonnumeric-first",`{"meta":{"id":"1","id":2}}`,"first","",false,true},
  {"nonnumeric-last",`{"meta":{"id":"1","id":2}}`,"last","",false,true},
  {"empty-policy",`{"meta":{"id":1}}`,"","",false,true},
  {"invalid-policy",`{"meta":{"id":1}}`,"middle","",false,true},
  {"nil-doc","","first","",false,true},
 }
 for _,tc:=range cases {
  t.Run(tc.name,func(t *testing.T){
   doc:=[]byte(tc.doc)
   old:=append([]byte(nil),doc...)
   token,found,err:=P36O12SelectRaw(doc,tc.policy)
   if (err!=nil)!=tc.err {t.Fatalf("P36_O12_Q22_MISMATCH err=%v wantErr=%v",err,tc.err)}
   if !tc.err&&(token!=tc.want||found!=tc.found){
    t.Fatalf("P36_O12_Q22_MISMATCH got=(%q,%v) want=(%q,%v)",token,found,tc.want,tc.found)
   }
   if !bytes.Equal(doc,old){t.Fatal("P36_O12_Q22_SOURCE_MUTATION")}
  })
 }
}
func TestP36O12ConcurrentReadOnlyQ22(t *testing.T){
 doc:=[]byte(`{"meta":{"id":1e+0,"other":2,"id":2.00}}`)
 var wg sync.WaitGroup
 errs:=make(chan error,12)
 for i:=0;i<12;i++ {
  wg.Add(1)
  go func(i int) {
   defer wg.Done()
   policy,want:="first","1e+0"
   if i%2==0{policy,want="last","2.00"}
   for j:=0;j<100;j++ {
    got,ok,err:=P36O12SelectRaw(doc,policy)
    if err!=nil||!ok||got!=want {errs<-fmt.Errorf("policy=%s got=%s ok=%v err=%v",policy,got,ok,err);return}
   }
  }(i)
 }
 wg.Wait();close(errs)
 for err:=range errs{t.Error(err)}
}
var p36O12Sink string
func BenchmarkP36O12Selection(b *testing.B) {
 for _,policy:=range []string{"first","last"} {
  for _,position:=range []string{"front","back"} {
   for _,padding:=range []int{0,64} {
    b.Run(fmt.Sprintf("%s/%s/padding%03d",policy,position,padding),func(b *testing.B) {
     var buf bytes.Buffer
     buf.WriteString(`{"meta":{`)
     if position=="front"{buf.WriteString(`"id":1e+0,`)}
     for i:=0;i<padding;i++{fmt.Fprintf(&buf,`"padding_%03d":%d,`,i,i)}
     if position=="back"{buf.WriteString(`"id":1e+0,`)}
     buf.WriteString(`"end":9}}`)
     doc:=buf.Bytes()
     var last string
     b.ReportAllocs();b.ResetTimer()
     for i:=0;i<b.N;i++ {
      token,ok,err:=P36O12SelectRaw(doc,policy)
      if err!=nil||!ok{b.Fatalf("Q22 benchmark failed token=%s ok=%v err=%v",token,ok,err)}
      last=token
     }
     p36O12Sink=last
    })
   }
  }
 }
}
