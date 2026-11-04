package r1

import "testing"

// A one-feature ablation tests necessity on declared witnesses, not global
// minimality among all possible alternative adapter implementations.
func TestEachAdapterFeatureHasIndependentWitness(t *testing.T){
 cases:=[]struct{name string;c ChiAdapterSettings;probe Probe}{
  {"no-head",ChiAdapterSettings{false,true,true},Probe{"HEAD","/items/alpha"}},
  {"no-decode",ChiAdapterSettings{true,false,true},Probe{"GET","/items/a%2Fb"}},
  {"no-method-error",ChiAdapterSettings{true,true,false},Probe{"POST","/items/alpha"}},
 }
 for _,tc:=range cases {t.Run(tc.name,func(t *testing.T){
  x,e:=ObserveWire(Standard(0),tc.probe);if e!=nil{t.Fatal(e)}
  y,e:=ObserveWire(Chi(0,tc.c),tc.probe);if e!=nil{t.Fatal(e)}
  if x==y{t.Fatalf("ablation not detected %+v",tc.probe)}
  t.Logf("ABLATION_WITNESS %+v std=%+v chi=%+v",tc.probe,x,y)
 })}
}

func TestFiniteAdapterTruthTable(t *testing.T){
 for mask:=0;mask<8;mask++{
  settings:=ChiAdapterSettings{mask&1!=0,mask&2!=0,mask&4!=0}
  misses,e:=Compare(Standard(0),Chi(0,settings),Broad())
  if e!=nil{t.Fatal(e)}
  t.Logf("ADAPTER_MASK=%03b mismatches=%d",mask,len(misses))
  if (len(misses)==0)!=(mask==7){t.Errorf("unexpected finite signature mask=%03b misses=%v",mask,misses)}
 }
}
