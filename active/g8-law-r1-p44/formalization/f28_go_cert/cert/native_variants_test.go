package cert
import ("fmt";"os";"os/exec";"path/filepath";"strings";"testing")
func TestNativeGoAllFourSourceEditStates(t *testing.T){
 for _,a:=range []string{"a0","new"}{
  for _,b:=range []string{"b0","new"}{
   t.Run(a+"_"+b,func(t *testing.T){
    root:=t.TempDir()
    sourceA:=fmt.Sprintf("package fixture\nfunc Legacy() string{return %q}\nfunc FutureA() string{return %q}\n","old",a)
    sourceB:=fmt.Sprintf("package fixture\nfunc FutureB() string{return %q}\n",b)
    for file,s:=range map[string]string{"a.go":sourceA,"b.go":sourceB}{
     if err:=os.WriteFile(filepath.Join(root,file),[]byte(s),0600);err!=nil{t.Fatal(err)}
    }
    if _,err:=Check(Case{"a.go",[]byte(sourceA),"FutureA"},Case{"b.go",[]byte(sourceB),"FutureB"},"synthetic-a","synthetic-b",true,true);err!=nil{t.Fatal(err)}
    tst:=fmt.Sprintf("package fixture\nimport \"testing\"\nfunc TestClient(t *testing.T){if Legacy()!=\"old\"||FutureA()!=%q||FutureB()!=%q{t.Fatal(\"client mismatch\")}}\n",a,b)
    if err:=os.WriteFile(filepath.Join(root,"fixture_test.go"),[]byte(tst),0600);err!=nil{t.Fatal(err)}
    cmd:=exec.Command("go","test","-count=1","./...")
    cmd.Dir=root;cmd.Env=append(os.Environ(),"GO111MODULE=off")
    data,err:=cmd.CombinedOutput()
    if err!=nil{t.Fatalf("native go failed %s: %v",strings.TrimSpace(string(data)),err)}
   })
  }
 }
}
