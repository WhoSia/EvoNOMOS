package static
import "testing"
func TestSourceParsedIndependentFrozenDemands(t *testing.T){
 paths,e:=ExtractFrozenPaths("../router.go");if e!=nil{t.Fatal(e)}
 if len(paths)!=3{t.Fatalf("paths=%v",paths)}
 if !DisjointSourcePaths(append(paths,"/items/{id}")){t.Fatalf("collision under bounded segment grammar: %v",paths)}
 t.Logf("STATIC_ORACLE source_paths=%v pairwise_disjoint_with_old=true",paths)
}
func TestClassicalOverlapNegativeControls(t *testing.T){
 if DisjointSourcePaths([]string{"/ledger/{id}/audit","/ledger/{sku}/audit"}){t.Fatal("param overlap missed")}
 if DisjointSourcePaths([]string{"/ledger/alpha/audit","/ledger/{id}/audit"}){t.Fatal("static/wildcard overlap missed")}
 if !DisjointSourcePaths([]string{"/ledger/{id}/revisions","/ledger/{id}/audit"}){t.Fatal("false collision")}
}
