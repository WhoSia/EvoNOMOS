package r1

import "testing"

// The three probes are independent *feature-removal witnesses* in this
// explicitly bounded three-switch grammar, not a universally minimal HTTP suite.
func TestThreeWitnessCertificateForEightAdapterConfigurations(t *testing.T) {
 witness := []Probe{
  {"HEAD","/items/alpha"},      // H
  {"GET","/items/a%2Fb"},        // D
  {"POST","/items/alpha"},      // M
 }
 for mask:=0;mask<8;mask++{
  c:=ChiAdapterSettings{mask&1!=0,mask&2!=0,mask&4!=0}
  miss,e:=Compare(Standard(0),Chi(0,c),witness)
  if e!=nil{t.Fatal(e)}
  if (len(miss)==0)!=(mask==7){t.Fatalf("mask=%03b witness fails: %v",mask,miss)}
  t.Logf("CERTIFICATE mask=%03b mismatch_count=%d",mask,len(miss))
 }
}

func TestSyntheticNormalizationCostIsThreeWithinNamedGrammar(t *testing.T) {
 min:=4
 var minimizers []int
 for mask:=0;mask<8;mask++{
  c:=ChiAdapterSettings{mask&1!=0,mask&2!=0,mask&4!=0}
  miss,e:=Compare(Standard(0),Chi(0,c),Broad())
  if e!=nil{t.Fatal(e)}
  if len(miss)>0{continue}
  cost:=0
  for i:=0;i<3;i++{if mask&(1<<i)!=0{cost++}}
  if cost<min{min=cost;minimizers=[]int{mask}}else if cost==min{minimizers=append(minimizers,mask)}
 }
 if min!=3||len(minimizers)!=1||minimizers[0]!=7{t.Fatalf("minimum=%d minimizers=%v",min,minimizers)}
 t.Logf("FINITE_GRAMMAR_MIN_COST=%d unique_mask=%03b",min,minimizers[0])
}
