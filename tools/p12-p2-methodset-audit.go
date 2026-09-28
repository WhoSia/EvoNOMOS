package main

import (
	"encoding/json"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"sort"
)

type report struct {
	Required       []string `json:"required"`
	FullMethods    []string `json:"full_methods"`
	ComposedMethods []string `json:"composed_methods"`
	Equal          bool     `json:"equal"`
	RequiredPresent bool    `json:"required_present"`
	Status         string   `json:"status"`
}

func backendMethods(path string) ([]string, error) {
	f, err := parser.ParseFile(token.NewFileSet(), path, nil, 0)
	if err != nil { return nil, err }
	set := map[string]bool{}
	for _, d := range f.Decls {
		fn, ok := d.(*ast.FuncDecl)
		if !ok || fn.Recv == nil || len(fn.Recv.List) != 1 { continue }
		switch x := fn.Recv.List[0].Type.(type) {
		case *ast.StarExpr:
			if id, ok := x.X.(*ast.Ident); ok && id.Name == "Backend" { set[fn.Name.Name] = true }
		case *ast.Ident:
			if x.Name == "Backend" { set[fn.Name.Name] = true }
		}
	}
	out := make([]string,0,len(set))
	for m := range set { out = append(out,m) }
	sort.Strings(out)
	return out,nil
}

func contains(xs []string, x string) bool {
	for _, v := range xs { if v == x { return true } }
	return false
}

func equal(a,b []string) bool {
	if len(a)!=len(b) { return false }
	for i := range a { if a[i]!=b[i] { return false } }
	return true
}

func main() {
	if len(os.Args)!=4 { panic("usage: methodset-audit <full.go> <composed.go> <out.json>") }
	full,err:=backendMethods(os.Args[1]); if err!=nil { panic(err) }
	composed,err:=backendMethods(os.Args[2]); if err!=nil { panic(err) }
	required:=[]string{"Close","Connections","Delete","HasAtomicReplace","Hasher","IsNotExist","List","Load","Location","Remove","Save","Stat"}
	sort.Strings(required)
	present:=true
	for _,m:=range required {
		if !contains(full,m)||!contains(composed,m){present=false}
	}
	ok:=equal(full,composed)&&present
	status:="HOLD"; if ok { status="PASS" }
	r:=report{Required:required,FullMethods:full,ComposedMethods:composed,Equal:equal(full,composed),RequiredPresent:present,Status:status}
	b,_:=json.MarshalIndent(r,"","  "); b=append(b,'
')
	if err:=os.WriteFile(os.Args[3],b,0644); err!=nil { panic(err) }
	fmt.Println("P12_P2_METHODSET="+status)
	if !ok { os.Exit(1) }
}
