package cert
import ("errors";"strings";"testing")
const a = "package fixture\nfunc Legacy() string { return \"old\" }\nfunc FutureA() string { return \"a0\" }\n"
const b = "package fixture\nfunc FutureB() string { return \"b0\" }\n"
func valid(x,y string)(Receipt,error){return Check(Case{"a.go",[]byte(x),"FutureA"},Case{"b.go",[]byte(y),"FutureB"},"owner-a","owner-b",true,true)}
func TestClosedSourceAndHash(t *testing.T){r,e:=valid(a,b);if e!=nil||r.Legacy!="old"||r.A!="a0"||r.B!="b0"||len(r.SourceSHA256)!=64{t.Fatal(r,e)}}
func TestHashChangesWithSource(t *testing.T){r,_:=valid(a,b);s,_:=valid(strings.Replace(a,`"a0"`, `"new"`,1),b);if r.SourceSHA256==s.SourceSHA256{t.Fatal("source hash unchanged")}}
func TestHOLDOnCrossCall(t *testing.T){_,e:=valid(strings.Replace(a,`return "a0"`, `return FutureB()`,1),b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnSharedVariable(t *testing.T){_,e:=valid(a+"\nvar shared = 0",b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnImport(t *testing.T){_,e:=valid(strings.Replace(a,"package fixture","package fixture\nimport \"fmt\"",1),b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnComment(t *testing.T){_,e:=valid(a+"//go:build ignore",b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnExtraFunction(t *testing.T){_,e:=valid(a+"func Hidden() string{return \"x\"}",b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnDynamicExpression(t *testing.T){_,e:=valid(strings.Replace(a,`return "a0"`, `return "a"+"0"`,1),b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnPackage(t *testing.T){_,e:=valid(strings.Replace(a,"package fixture","package other",1),b);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnMissingGrant(t *testing.T){_,e:=Check(Case{"a.go",[]byte(a),"FutureA"},Case{"b.go",[]byte(b),"FutureB"},"owner-a","owner-b",true,false);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHOLDOnBadFilename(t *testing.T){_,e:=Check(Case{"x.go",[]byte(a),"FutureA"},Case{"b.go",[]byte(b),"FutureB"},"owner-a","owner-b",true,true);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestCostBoth(t *testing.T){n,e:=RepairCost("a0","b0",[]string{"A=new","B=new"});if e!=nil||n!=2{t.Fatal(n,e)}}
func TestCostOrder(t *testing.T){for _,w:=range [][]string{{"B=new","A=new"},{"A=new","A=new","B=new"}}{n,e:=RepairCost("a0","b0",w);if e!=nil||n!=2{t.Fatal(n,e)}}}
func TestCostZero(t *testing.T){n,e:=RepairCost("new","new",[]string{"B=new","A=new"});if e!=nil||n!=0{t.Fatal(n,e)}}
func TestUnknownDemand(t *testing.T){_,e:=RepairCost("a0","b0",[]string{"unknown"});if !errors.Is(e,ErrHold){t.Fatal(e)}}
