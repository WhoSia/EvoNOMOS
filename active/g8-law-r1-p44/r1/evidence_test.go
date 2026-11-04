package r1

import (
 "strings"
 "testing"
)

func TestRawChiDivergesOnKnownHEADAndEncodedPaths(t *testing.T) {
 for _,p:=range []Probe{
  {"HEAD","/items/alpha"},{"GET","/items/a%2Fb"},{"GET","/items/%61lpha"},
 } {
  x,e:=ObserveWire(Standard(0),p);if e!=nil{t.Fatal(e)}
  y,e:=ObserveWire(RawChi(0),p);if e!=nil{t.Fatal(e)}
  if x==y{t.Fatalf("known counterexample vanished on %v: %+v",p,x)}
  t.Logf("ORIGINAL_COUNTEREXAMPLE %s %s std=%+v chi=%+v",p.Method,p.Path,x,y)
 }
}

func TestNarrowControlMatchesHEADAdapter(t *testing.T) {
 miss,e:=Compare(Standard(0),Chi(0,ChiAdapterSettings{RegisterHEAD:true}),Narrow)
 if e!=nil||len(miss)!=0{t.Fatalf("narrow failed: %v %v",miss,e)}
}

func TestBroadContractFullAdapter(t *testing.T){
 miss,e:=Compare(Standard(0),FullChi(0),Broad())
 if e!=nil{t.Fatal(e)}
 if len(miss)>0{t.Fatalf("broad mismatch (%d): %s",len(miss),strings.Join(miss,"\n"))}
 t.Logf("BROAD_MATCHED count=%d adapter_units=3",len(Broad()))
}
