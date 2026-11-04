package r1
import "testing"

// Once the six-probe contract is established by the HEAD app registration,
// the later D and M adaptations preserve every old protected observation.
func TestStagewiseNormalizationPreservesNarrowOldClients(t *testing.T){
 configs:=[]ChiAdapterSettings{
  {RegisterHEAD:true},
  {RegisterHEAD:true,DecodeParam:true},
  {RegisterHEAD:true,DecodeParam:true,MatchMethodError:true},
 }
 prior:=Standard(0)
 for stage,c:=range configs{
  miss,e:=Compare(prior,Chi(0,c),Narrow)
  if e!=nil||len(miss)>0{t.Fatalf("normalization stage %d breaks old clients: %v %v",stage,miss,e)}
  broad,e:=Compare(prior,Chi(0,c),Broad());if e!=nil{t.Fatal(e)}
  t.Logf("ADAPTER_STAGE=%d narrow_protected=%d broad_remaining=%d cumulative_edit_units=%d",stage,len(Narrow),len(broad),stage+1)
 }
}
