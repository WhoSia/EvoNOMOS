package branchcourt
import("errors";"os";"os/exec";"path/filepath";"strconv";"testing")
const fixture=`package fixture
func Legacy() string{return "stable"}
func Future(flag bool) string{if flag{return "off"}; return "on"}`
func TestCompleteSourceRightsAndExactClassicalCost(t *testing.T){
 p:=Policy{Allowed:[]string{"off","on","beta"}};g,e:=Enumerate(fixture,p)
 if e!=nil{t.Fatal(e)}
 if len(g.Sources)!=9||len(g.Edges)!=36{t.Fatalf("states=%d edges=%d",len(g.Sources),len(g.Edges))}
 counts:=map[State]int{}
 for _,ed:=range g.Edges{
  counts[ed.From]++
  if ed.Cost!=1||ed.Changed=="true"&&(ed.From.T==ed.To.T||ed.From.F!=ed.To.F)||ed.Changed=="false"&&(ed.From.F==ed.To.F||ed.From.T!=ed.To.T){t.Fatal(ed)}
  for _,flag:=range []bool{false,true}{
   legacy,_,err:=Observe(g.Sources[ed.To],flag)
   if err!=nil||legacy!="stable"{t.Fatal(ed,err)}
  }
 }
 for s,count:=range counts{if count!=4{t.Fatalf("missing rights for %v: %d",s,count)}}
 distance,e:=ExactDistance(g,State{"off","on"},State{"beta","off"})
 if e!=nil||distance!=2{t.Fatal(distance,e)}
 t.Logf("BRANCH_GRAMMAR states=9 edits=36 legacy_safe=true classical_cost=%d",distance)
}
func TestMarginalOutputSetsCannotCertifyJointInputContract(t *testing.T){
 g,e:=Enumerate(fixture,Policy{Allowed:[]string{"off","on"}});if e!=nil{t.Fatal(e)}
 original:=g.Sources[State{"off","on"}];swapped:=g.Sources[State{"on","off"}]
 for _,flag:=range []bool{false,true}{
  old,oa,e:=Observe(original,flag);if e!=nil{t.Fatal(e)}
  newer,ob,e:=Observe(swapped,flag);if e!=nil{t.Fatal(e)}
  if old!=newer||oa==ob{t.Fatalf("joint observer missing regression flag=%v",flag)}
 }
 t.Log("JOINT_CONTRACT marginal_sets_equal=true input_output_mapping_regressed=true")
}
func TestRejectSourceGrammarAndRightsEscape(t *testing.T){
 bad:=[]string{
  "//go:build ignore
"+fixture,
  fixture+"
//go:linkname Future runtime.hidden
",
  `package fixture
func Legacy() string{return "stable"}
func Future(flag bool) string{if !flag{return "off"};return "on"}`,
  `package fixture
func Legacy() string{return "stable"}
func Future(flag bool) string{if flag{return "off"}else{return "on"};return "off"}`,
  fixture+"
func Extra() string{return "other"}
",
 }
 for _,source:=range bad{if _,e:=Parse(source);!errors.Is(e,ErrGrammar){t.Fatalf("unmodeled input accepted %v",e)}}
 if _,e:=Rewrite(fixture,Policy{Allowed:[]string{"off","on"}},State{"other","on"});!errors.Is(e,ErrRight){t.Fatal(e)}
}
func TestActualNativeGoRunAcrossNineVersions(t *testing.T){
 g,e:=Enumerate(fixture,Policy{Allowed:[]string{"off","on","beta"}});if e!=nil{t.Fatal(e)}
 for state,source:=range g.Sources{
  directory:=t.TempDir()
  if e:=os.WriteFile(filepath.Join(directory,"go.mod"),[]byte("module fixturerun

go 1.23
"),0644);e!=nil{t.Fatal(e)}
  if e:=os.WriteFile(filepath.Join(directory,"fixture.go"),[]byte(source),0644);e!=nil{t.Fatal(e)}
  check:="package fixture
import "testing"
func TestSource(t *testing.T){if Legacy()!="stable"{t.Fatal("legacy")};if Future(true)!="+strconv.Quote(state.T)+"{t.Fatal("true")};if Future(false)!="+strconv.Quote(state.F)+"{t.Fatal("false")}}
"
  if e:=os.WriteFile(filepath.Join(directory,"fixture_test.go"),[]byte(check),0644);e!=nil{t.Fatal(e)}
  cmd:=exec.Command("go","test","-count=1","./...")
  cmd.Dir=directory;cmd.Env=append(os.Environ(),"GOWORK=off")
  output,e:=cmd.CombinedOutput();if e!=nil{t.Fatalf("Go runtime failed for %+v: %v
%s",state,e,output)}
 }
 t.Log("NATIVE_BRANCH_GO all_nine_generated_sources_compiled_and_ran=true")
}
