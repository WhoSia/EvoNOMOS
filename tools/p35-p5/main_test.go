package main
import "testing"
func TestTieBreaker(t *testing.T){
 got,n:=pick("mux.go",map[string]int{"tree.go":2,"context.go":2})
 if got!="context.go"||n!=2{t.Fatalf("%s %d",got,n)}
}
func TestB2Mappings(t *testing.T){
 for _,p:=range triad {if b2[p]==""||b2[p]==p{t.Fatal("invalid Parnas mapping",p)}}
}
