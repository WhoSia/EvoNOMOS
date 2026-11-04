package static
import("os";"path/filepath";"testing")
func TestClassicalSourceAwareAliasFacts(t *testing.T){
 f,e:=ReadFacts(filepath.Join("..","core","model.go"),filepath.Join("..","native","routers.go"));if e!=nil{t.Fatal(e)}
 if !f.All(){t.Fatalf("source structure changed: %+v",f)}
 t.Logf("AST_CLASSICAL_SOURCE_FACTS %+v",f)
}
func TestParserRejectsInvalidSource(t *testing.T){
 p:=filepath.Join(t.TempDir(),"bad.go")
 if e:=os.WriteFile(p,[]byte("package bad\nfunc missing("),0600);e!=nil{t.Fatal(e)}
 if _,e:=ReadFacts(p,"../native/routers.go");e==nil{t.Fatal("invalid source admitted")}
}
