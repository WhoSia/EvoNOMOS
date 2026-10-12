package p42r4_test

import (
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "os"
 "testing"

 "example.org/evonomos/p42r4/states/single"
 "example.org/evonomos/p42r4/states/split"
)
type DemandSeq struct{
 ID string `json:"id"`
 Stream []string `json:"stream"`
 Paths map[string][]string `json:"paths"`
 EditCount map[string]int `json:"edit_count"`
}
type Frozen struct {FrozenSequences []DemandSeq `json:"frozen_sequences"`}
type Trace struct{
 Sequence string `json:"sequence"`
 Start string `json:"start"`
 Stage int `json:"stage"`
 Demand string `json:"demand"`
 State string `json:"state"`
 Path string `json:"path"`
 Status int `json:"status"`
 Body string `json:"body"`
 Handler string `json:"handler"`
}
func TestR4SourceDemandStreams(t *testing.T){
 if os.Getenv("P42_R4_ECHO_SHA")!="f085ffbe8f99de165bd920746920000ab56bd6bc"{
  t.Fatal("missing original Echo v4 source pin")
 }
 bytes,err:=os.ReadFile("../p2-r4/frozen_demand_edit_game.json")
 if err!=nil{t.Fatal(err)}
 var specification Frozen
 if err:=json.Unmarshal(bytes,&specification);err!=nil{t.Fatal(err)}
 if len(specification.FrozenSequences)!=6{t.Fatal("expected frozen six demand histories")}
 paths:=[]string{"/health","/r/foo:cancel","/r/foo","/r/foo:other"}
 for _,seq:=range specification.FrozenSequences{
  for _,start:=range []string{"SINGLE","SPLIT"}{
   history:=seq.Paths[start]
   if len(history)!=len(seq.Stream)+1{t.Fatalf("bad frozen history %s %s",seq.ID,start)}
   for i,state:=range history{
    var build interface {ServeHTTP(http.ResponseWriter,*http.Request)}
    if state=="SINGLE"{build=single.Build()}else if state=="SPLIT"{build=split.Build()}else{t.Fatal("unknown state")}
    demand:="D0"
    if i>0{demand=seq.Stream[i-1]}
    for _,path:=range paths{
     w:=httptest.NewRecorder()
     build.ServeHTTP(w,httptest.NewRequest(http.MethodGet,path,nil))
     row:=Trace{Sequence:seq.ID,Start:start,Stage:i,Demand:demand,State:state,
       Path:path,Status:w.Code,Body:w.Body.String(),Handler:w.Header().Get("X-Evo-Route")}
     output,err:=json.Marshal(row)
     if err!=nil{t.Fatal(err)}
     t.Log("P42_R4_ACTUAL_GO "+string(output))
    }
   }
  }
 }
}
