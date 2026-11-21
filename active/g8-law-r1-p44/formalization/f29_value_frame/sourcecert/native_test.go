package sourcecert
import ("errors";"fmt";"os";"os/exec";"path/filepath";"strings";"testing")
func runNative(t *testing.T,root,expectedA,expectedB string) {
 t.Helper()
 source:=fmt.Sprintf("package fixture\nimport \"testing\"\nfunc TestClient(t *testing.T){if Legacy()!=\"old\"||FutureA()!=%q||FutureB()!=%q{t.Fatal(\"observation mismatch\")}}\n",expectedA,expectedB)
 if err:=os.WriteFile(filepath.Join(root,"client_test.go"),[]byte(source),0600);err!=nil{t.Fatal(err)}
 cmd:=exec.Command("go","test","-count=1","./...")
 cmd.Dir=root;cmd.Env=append(os.Environ(),"GO111MODULE=off")
 out,err:=cmd.CombinedOutput()
 if err!=nil{t.Fatalf("native Go test failed: %v\n%s",err,out)}
}
func TestFourNativeSourceVariants(t *testing.T){
 for _,l:=range []string{"a0","new"}{for _,r:=range []string{"b0","new"}{
  t.Run(l+"_"+r,func(t *testing.T){
   left:=strings.Replace(a,"\"a0\"",fmt.Sprintf("%q",l),1)
   right:=strings.Replace(b,"\"b0\"",fmt.Sprintf("%q",r),1)
   root:=write(t,left,right)
   receipt,err:=CheckDir(root,true,true)
   if err!=nil||receipt.Left!=l||receipt.Right!=r||receipt.Legacy!="old"{t.Fatal(receipt,err)}
   runNative(t,root,l,r)
   // Re-checking the directory after a new source file appears must HOLD.
   if _,err:=CheckDir(root,true,true);!errors.Is(err,ErrHold){t.Fatal("scope modification not detected")}
  })
 }}
}
// A Go-compiler-valid, legacy-client-safe program can violate the frame.
// This is independent proof that old regression tests don't certify
// future cross-port independence.
func TestOldClientsPassButCrossComponentEffect(t *testing.T){
 cross:=strings.Replace(a,`return (Left{Value: "a0"}).Value`, `return FutureB()`,1)
 for _,r:=range []string{"b0","new"}{t.Run(r,func(t *testing.T){
  root:=write(t,cross,strings.Replace(b,"\"b0\"",fmt.Sprintf("%q",r),1))
  if _,err:=CheckDir(root,true,true);!errors.Is(err,ErrHold){t.Fatal("cross dependency falsely certified")}
  runNative(t,root,r,r)
 })}
}
