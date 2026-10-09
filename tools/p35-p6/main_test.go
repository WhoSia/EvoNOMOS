package main
import "testing"
func TestChangeOperator(t *testing.T) {
 cases:=[]struct{a,b,want string}{
 {"package cobra\ntype X struct{ A int }","package cobra\ntype X struct{ A string }","TYPE_SHAPE"},
 {"package cobra\nfunc f()int{return 1}","package cobra\nfunc f()int{return 2}","FUNCTION_ONLY"},
 {"package cobra\n// before\nfunc f(){}","package cobra\n// after\nfunc f(){}","NO_DECL_CHANGE"},
 }
 for _,c:=range cases{got,e:=classifyText(c.a,c.b);if e!=nil||got!=c.want{t.Fatalf("operator %q => %q, error %v (want %q)",c.b,got,e,c.want)}}
}
func TestNoEditAndAbstentionGate(t *testing.T){
 if got:=b1Gate(3,3,"command.go");got!=abstain{t.Fatal(got)}
 if got:=b1Gate(10,4,"command.go");got!=none{t.Fatal(got)}
 if got:=b1Gate(10,5,"command.go");got!="command.go"{t.Fatal(got)}
}
func TestB2FrozenMapping(t *testing.T){
 for _,name:=range triad{if b2[name]==""||name==b2[name]{t.Fatal(name)}}
}

func TestReceiverTypeASTFormatting(t *testing.T) {
 before:="package cobra\ntype X struct{}\nfunc (x *X) Run() int {return 1}"
 after:="package cobra\ntype X struct{}\nfunc (x *X) Run() int {return 2}"
 got,e:=classifyText(before,after)
 if e!=nil||got!="FUNCTION_ONLY"{t.Fatalf("got %q error=%v",got,e)}
}
