package sourcecourt

import ("errors";"strings";"testing")

const fixture=`package fixture
func Legacy() string { return "stable" }
func Future() string { return "off" }
`
func TestAllDeclaredSourceEditsCompleteAndProtected(t *testing.T){
 p:=Policy{Allowed:[]string{"off","on","beta"}}
 g,e:=Enumerate(fixture,p)
 if e!=nil{t.Fatal(e)}
 if len(g.States)!=3||len(g.Edges)!=6{t.Fatalf("closed grammar wrong |V|=%d |E|=%d",len(g.States),len(g.Edges))}
 seen:=map[string]bool{}
 for _,ed:=range g.Edges{
  seen[ed.From+"->"+ed.To]=true
  s,e:=Observe(g.States[ed.To])
  if e!=nil||s.Legacy!="stable"||s.Future!=ed.To{t.Fatalf("unsafe edge %+v %v",ed,e)}
 }
 for _,a:=range p.Allowed{for _,b:=range p.Allowed{
  if a!=b&&!seen[a+"->"+b]{t.Fatalf("missing authorized edit %s -> %s",a,b)}
 }}
 k,e:=ExactDistance(g,"off","beta")
 if e!=nil||k!=1{t.Fatal(k,e)}
 t.Logf("SOURCE_DSL complete_declared_edits=6 legacy_invariant=true exact_classical_cost=%d",k)
}
func TestGeneratedSourceASTSemanticObservation(t *testing.T){
 p:=Policy{Allowed:[]string{"off","on","beta"}}
 src,e:=PatchFuture(fixture,p,"on")
 if e!=nil{t.Fatal(e)}
 if !strings.Contains(src,`return "on"`){t.Fatal(src)}
 original,_:=Observe(fixture);newer,e:=Observe(src)
 if e!=nil||original.Legacy!=newer.Legacy||newer.Future!="on"{t.Fatal(original,newer,e)}
}
func TestSourceGrammarRejectsUnmodeledGoSemantics(t *testing.T){
 cases:=[]string{
  `package fixture
  import "fmt"
  func Legacy() string{return "stable"}
  func Future() string{return fmt.Sprint("off")}`,
  `package fixture
  func Legacy() string{return "stable"}
  func Future() string{if true{return "on"};return "off"}`,
  `package fixture
  func Legacy() string{return "stable"}
  func Future() string{return "off"}
  func Undeclared() string{return "hidden"}`,
  `package fixture
  func Legacy() string{return "stable"}
  func Future() string{return "off"+"on"}`,
 }
 for _,source:=range cases{
  if _,e:=Parse(source);!errors.Is(e,ErrOutsideGrammar){t.Fatalf("out-of-grammar source accepted: %v",e)}
 }
}
func TestUnapprovedEditAndDuplicatePolicyRejected(t *testing.T){
 if _,e:=PatchFuture(fixture,Policy{Allowed:[]string{"off","on"}},"beta");!errors.Is(e,ErrUnauthorized){t.Fatal(e)}
 if _,e:=Enumerate(fixture,Policy{Allowed:[]string{"off","off"}});!errors.Is(e,ErrUnauthorized){t.Fatal(e)}
}
func TestCurrentSourceMustBeInPermittedDomain(t *testing.T){
 if _,e:=Enumerate(fixture,Policy{Allowed:[]string{"on","beta"}});!errors.Is(e,ErrUnauthorized){t.Fatal(e)}
}
