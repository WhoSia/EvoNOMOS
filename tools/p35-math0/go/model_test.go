package math0

import "testing"

func TestFiniteTwoModels(t *testing.T) {
    models:=Enumerate()
    if len(models)!=2 {t.Fatalf("want 2, got %d",len(models))}
    if models[0].Start || !models[1].Start {t.Fatalf("both start bits needed: %#v",models)}
    for _,v:=range models{
        if !v.InitialAgreement || !v.LaterDisagreement {t.Fatalf("countermodel invalid: %#v",v)}
    }
}

func TestObservationalIndistinguishabilityIsLocal(t *testing.T){
    for _,b:=range []bool{false,true}{
        w:=Initial(b)
        if Observe(Live,w)!=Observe(Snapshot,w){t.Fatal("initial disagreement")}
        next:=Update(w)
        if Observe(Live,next)==Observe(Snapshot,next){t.Fatal("update did not distinguish")}
    }
}
