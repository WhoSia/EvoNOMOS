package sourcecert
import ("errors";"os";"path/filepath";"strings";"testing")
const a = "package fixture\ntype Left struct { Value string }\nfunc Legacy() string { return \"old\" }\nfunc FutureA() string { return (Left{Value: \"a0\"}).Value }\n"
const b = "package fixture\ntype Right struct { Value string }\nfunc FutureB() string { return (Right{Value: \"b0\"}).Value }\n"
func write(t *testing.T,l,r string)string{
 t.Helper();root:=t.TempDir()
 for n,data:=range map[string]string{"a.go":l,"b.go":r}{
  if err:=os.WriteFile(filepath.Join(root,n),[]byte(data),0600);err!=nil{t.Fatal(err)}
 }
 return root
}
func TestPositive(t *testing.T){r,e:=CheckDir(write(t,a,b),true,true);if e!=nil||r.Legacy!="old"||r.Left!="a0"||r.Right!="b0"||len(r.ScopeSHA256)!=64||r.Grade!="DIRECTORY_AND_AST_CHECKED_RIGHTS_UNVERIFIED"{t.Fatal(r,e)}}
func TestCrossAliasAndPureLanguageHOLD(t *testing.T){
 cases:=[]struct{name,l,r string}{
  {"pointer",strings.Replace(a,"Value string","Value *string",1),b},
  {"interface",strings.Replace(a,"Value string","Value interface{}",1),b},
  {"shared-global",a+"\nvar Shared = 3",b},
  {"import",strings.Replace(a,"package fixture","package fixture\nimport \"fmt\"",1),b},
  {"cross-call",strings.Replace(a,"return (Left{Value: \"a0\"}).Value","return FutureB()",1),b},
  {"cross-type",strings.Replace(a,"Left{Value: \"a0\"}","Right{Value: \"a0\"}",1),b},
  {"dynamic-value",strings.Replace(a,"Value: \"a0\"","Value: FutureB()",1),b},
  {"method",a+"\nfunc (x Left) X() string{return x.Value}",b},
  {"statement",strings.Replace(a,"return (Left{Value: \"a0\"}).Value","x := Left{Value:\"a0\"}; return x.Value",1),b},
  {"build-directive",a+"\n//go:build linux\n",b},
  {"other-package",strings.Replace(a,"package fixture","package other",1),b},
  {"renamed-field",strings.Replace(a,"Value string","Other string",1),b},
  {"alias-type",strings.Replace(a,"type Left struct { Value string }","type Left = *Right",1),b},
  {"right-side-call",a,strings.Replace(b,"return (Right{Value: \"b0\"}).Value","return Legacy()",1)},
 }
 for _,v:=range cases{t.Run(v.name,func(t *testing.T){_,err:=CheckDir(write(t,v.l,v.r),true,true);if !errors.Is(err,ErrHold){t.Fatalf("expected HOLD: %v",err)}})}
}
func TestOtherFileHOLD(t *testing.T){root:=write(t,a,b);os.WriteFile(filepath.Join(root,"hidden.go"),[]byte("package fixture"),0600);_,e:=CheckDir(root,true,true);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestSymlinkHOLD(t *testing.T){root:=write(t,a,b);os.Remove(filepath.Join(root,"a.go"));target:=filepath.Join(t.TempDir(),"a.go");os.WriteFile(target,[]byte(a),0600);if err:=os.Symlink(target,filepath.Join(root,"a.go"));err!=nil{t.Skip(err)};_,e:=CheckDir(root,true,true);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestGrantHOLD(t *testing.T){_,e:=CheckDir(write(t,a,b),false,true);if !errors.Is(e,ErrHold){t.Fatal(e)}}
func TestHashMutation(t *testing.T){x,_:=CheckDir(write(t,a,b),true,true);y,_:=CheckDir(write(t,strings.Replace(a,"\"a0\"","\"new\"",1),b),true,true);if x.ScopeSHA256==y.ScopeSHA256{t.Fatal("digest collision")}}
