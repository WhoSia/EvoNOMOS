package math2

import "testing"
func TestRepairCountermodel(t *testing.T){
 r:=Evaluate()
 if !r.MayHelper||r.MustHelper||len(r.AdmissiblePatches)!=2{t.Fatalf("C-CHOICE failure %+v",r)}
}
func TestOrderSensitiveTwoStep(t *testing.T){
 r:=Evaluate()
 if !Contains(r.AB,Three)||Contains(r.BA,Three)||!Contains(r.BA,Four)||Contains(r.AB,Four)||r.PathsCommute{
  t.Fatalf("C-NONCOMMUTE failure %+v",r)
 }
}
