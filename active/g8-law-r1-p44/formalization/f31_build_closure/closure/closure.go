// Package closure binds a narrow F30 source receipt to a compiled, frozen Go snapshot.
// No claim of authentic maintainer rights or entire-repository closure is made.
package closure

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "errors"
 "fmt"
 "os"
 "os/exec"
 "path/filepath"
 "sort"
 "strings"
 f30 "evonomos/f30/cert"
)

var ErrHold=errors.New("HOLD: source/build closure not certified")
const ModuleText="module example.com/evonomos-f31-closed\n\ngo 1.23\n"
const Grade="FROZEN_PACKAGE_GO_BUILD_AND_AST_RIGHTS_UNVERIFIED"
type Receipt struct {
 Grade string
 FrozenSHA256 string
 GoVersion string
 CompilerGoFiles []string
 ASTSourceSHA256 string
 Legacy,A,B string
 RightsEvidence string
}
type listRecord struct {
 GoFiles,CgoFiles,IgnoredGoFiles,InvalidGoFiles,TestGoFiles,XTestGoFiles,OtherFiles,EmbedFiles,Imports,Deps []string
 Error *struct{Err string}
 Incomplete bool
}
func runGo(dir string,args ...string)([]byte,error){
 cmd:=exec.Command("go",args...)
 cmd.Dir=dir
 cmd.Env=append(os.Environ(),"GO111MODULE=on","GOFLAGS=","GOWORK=off",
  "CGO_ENABLED=0","GOTOOLCHAIN=local","GOPROXY=off","GOSUMDB=off",
  "GOOS=linux","GOARCH=amd64")
 out,err:=cmd.CombinedOutput()
 if err!=nil{return nil,fmt.Errorf("%w: go %v: %v: %.500s",ErrHold,args,err,out)}
 return out,nil
}
// Check pins the build inputs to a freshly copied package and verifies
// standard go list / go build + F30 source grammar on the SAME copied bytes.
func Check(root string, grants map[string]bool)(Receipt,error){
 entries,err:=os.ReadDir(root)
 if err!=nil{return Receipt{},fmt.Errorf("%w: source list: %v",ErrHold,err)}
 if len(entries)!=3{return Receipt{},fmt.Errorf("%w: unexpected file count",ErrHold)}
 files:=map[string][]byte{}
 for _,ent:=range entries{
  name:=ent.Name()
  if name!="a.go"&&name!="b.go"&&name!="go.mod"{return Receipt{},fmt.Errorf("%w: extra entry %q",ErrHold,name)}
  st,err:=os.Lstat(filepath.Join(root,name))
  if err!=nil||!st.Mode().IsRegular(){return Receipt{},fmt.Errorf("%w: nonregular file %q",ErrHold,name)}
  files[name],err=os.ReadFile(filepath.Join(root,name))
  if err!=nil{return Receipt{},fmt.Errorf("%w: reading file: %v",ErrHold,err)}
 }
 if len(files)!=3||!bytes.Equal(files["go.mod"],[]byte(ModuleText)){
  return Receipt{},fmt.Errorf("%w: unexpected go.mod",ErrHold)
 }
 frozen,err:=os.MkdirTemp("","evonomos-f31-frozen-*")
 if err!=nil{return Receipt{},err}
 defer os.RemoveAll(frozen)
 astDir,err:=os.MkdirTemp("","evonomos-f31-ast-*")
 if err!=nil{return Receipt{},err}
 defer os.RemoveAll(astDir)
 for _,name:=range []string{"go.mod","a.go","b.go"}{
  if err=os.WriteFile(filepath.Join(frozen,name),files[name],0600);err!=nil{return Receipt{},err}
  if name!="go.mod"{
   if err=os.WriteFile(filepath.Join(astDir,name),files[name],0600);err!=nil{return Receipt{},err}
  }
 }
 ast,err:=f30.CheckDir(astDir,grants)
 if err!=nil{return Receipt{},fmt.Errorf("%w: source AST: %v",ErrHold,err)}
 v,err:=runGo(frozen,"version")
 if err!=nil{return Receipt{},err}
 version:=strings.TrimSpace(string(v))
 if !strings.HasPrefix(version,"go version go1.23.2 "){
  return Receipt{},fmt.Errorf("%w: compiler unpinned %q",ErrHold,version)
 }
 output,err:=runGo(frozen,"list","-json",".")
 if err!=nil{return Receipt{},err}
 var pkg listRecord
 if err=json.Unmarshal(output,&pkg);err!=nil{return Receipt{},fmt.Errorf("%w: bad go list",ErrHold)}
 sort.Strings(pkg.GoFiles)
 if len(pkg.GoFiles)!=2||pkg.GoFiles[0]!="a.go"||pkg.GoFiles[1]!="b.go"||
   len(pkg.CgoFiles)+len(pkg.IgnoredGoFiles)+len(pkg.InvalidGoFiles)+
   len(pkg.TestGoFiles)+len(pkg.XTestGoFiles)+len(pkg.OtherFiles)+
   len(pkg.EmbedFiles)+len(pkg.Imports)+len(pkg.Deps)!=0||
   pkg.Incomplete||pkg.Error!=nil{
    return Receipt{},fmt.Errorf("%w: compiler source/dependency mismatch",ErrHold)
 }
 if _,err=runGo(frozen,"build","-trimpath",".");err!=nil{return Receipt{},err}
 h:=sha256.New()
 for _,name:=range []string{"go.mod","a.go","b.go"}{
  h.Write([]byte(name+"\x00"));h.Write(files[name]);h.Write([]byte("\x00"))
 }
 for _,name:=range []string{"go.mod","a.go","b.go"}{
  latest,e:=os.ReadFile(filepath.Join(root,name))
  if e!=nil||!bytes.Equal(latest,files[name]){return Receipt{},fmt.Errorf("%w: source drift",ErrHold)}
 }
 return Receipt{
  Grade:Grade,FrozenSHA256:hex.EncodeToString(h.Sum(nil)),
  GoVersion:version,CompilerGoFiles:pkg.GoFiles,ASTSourceSHA256:ast.SourceSHA256,
  Legacy:ast.Legacy,A:ast.A,B:ast.B,
  RightsEvidence:"caller-supplied grant; no independent owner, repo or compiler provenance",
 },nil
}
