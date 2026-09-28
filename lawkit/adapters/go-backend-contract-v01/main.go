package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"sort"
)

type spec struct {
	WorldID        string `json:"world_id"`
	ExpectedCommit string `json:"expected_commit"`
	Interface      struct {
		Path                   string   `json:"path"`
		Name                   string   `json:"name"`
		RequiredCoreMethods    []string `json:"required_core_methods"`
		ExpectedSupportMethods []string `json:"expected_support_methods"`
	} `json:"interface"`
	ConformanceSuite struct {
		Path                    string   `json:"path"`
		RequiredExercisedMethods []string `json:"required_exercised_methods"`
	} `json:"conformance_suite"`
	ForbiddenPatterns []string `json:"forbidden_predemand_provider_patterns"`
}

type output struct {
	Adapter                    string              `json:"adapter"`
	WorldID                    string              `json:"world_id"`
	ExactSourceCommit          string              `json:"exact_source_commit"`
	Interface                  string              `json:"interface"`
	InterfaceMethods           []string            `json:"interface_methods"`
	RequiredCoreMethods        []string            `json:"required_core_methods"`
	CoreMethodCoverage         map[string]string   `json:"core_method_coverage"`
	ConformanceExercised       map[string]string   `json:"conformance_exercised"`
	ForbiddenProviderEvidence map[string][]string `json:"forbidden_provider_evidence"`
	Status                     string              `json:"status"`
}

func gitHead(root string) (string, error) {
	cmd := exec.Command("git", "-C", root, "rev-parse", "HEAD")
	b, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(bytesTrimSpace(b)), nil
}

func bytesTrimSpace(b []byte) []byte {
	i, j := 0, len(b)
	for i < j && (b[i] == ' ' || b[i] == '\n' || b[i] == '\r' || b[i] == '\t') { i++ }
	for j > i && (b[j-1] == ' ' || b[j-1] == '\n' || b[j-1] == '\r' || b[j-1] == '\t') { j-- }
	return b[i:j]
}

func interfaceMethods(path, name string) ([]string, error) {
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, path, nil, 0)
	if err != nil { return nil, err }
	var methods []string
	for _, decl := range f.Decls {
		gd, ok := decl.(*ast.GenDecl)
		if !ok || gd.Tok != token.TYPE { continue }
		for _, raw := range gd.Specs {
			ts, ok := raw.(*ast.TypeSpec)
			if !ok || ts.Name.Name != name { continue }
			it, ok := ts.Type.(*ast.InterfaceType)
			if !ok { return nil, fmt.Errorf("%s is not interface", name) }
			for _, field := range it.Methods.List {
				for _, n := range field.Names { methods = append(methods, n.Name) }
			}
			sort.Strings(methods)
			return methods, nil
		}
	}
	return nil, fmt.Errorf("interface %s not found", name)
}

func selectorNames(path string) (map[string]int, error) {
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, path, nil, 0)
	if err != nil { return nil, err }
	out := map[string]int{}
	ast.Inspect(f, func(n ast.Node) bool {
		sel, ok := n.(*ast.SelectorExpr)
		if ok { out[sel.Sel.Name]++ }
		return true
	})
	return out, nil
}

func contains(xs []string, x string) bool {
	for _, v := range xs { if v == x { return true } }
	return false
}

func scanForbidden(root string, patterns []string) (map[string][]string, error) {
	compiled := make([]*regexp.Regexp, len(patterns))
	for i, p := range patterns {
		r, err := regexp.Compile("(?i)" + p)
		if err != nil { return nil, fmt.Errorf("bad pattern %q: %w", p, err) }
		compiled[i] = r
	}
	out := map[string][]string{}
	for _, p := range patterns { out[p] = []string{} }
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil { return err }
		if info.IsDir() {
			base := filepath.Base(path)
			if base == ".git" || base == "vendor" { return filepath.SkipDir }
			return nil
		}
		if filepath.Ext(path) != ".go" { return nil }
		b, err := os.ReadFile(path)
		if err != nil { return err }
		rel, _ := filepath.Rel(root, path)
		for i, r := range compiled {
			if r.Match(b) { out[patterns[i]] = append(out[patterns[i]], filepath.ToSlash(rel)) }
		}
		return nil
	})
	return out, err
}

func main() {
	root := flag.String("repo", "", "exact Go repository checkout")
	specPath := flag.String("spec", "", "audit spec json")
	outPath := flag.String("out", "", "output json")
	flag.Parse()
	if *root == "" || *specPath == "" || *outPath == "" { panic("repo/spec/out required") }

	var s spec
	b, err := os.ReadFile(*specPath); if err != nil { panic(err) }
	if err := json.Unmarshal(b, &s); err != nil { panic(err) }

	head, err := gitHead(*root); if err != nil { panic(err) }
	if head != s.ExpectedCommit { panic(fmt.Sprintf("commit mismatch: %s", head)) }

	methods, err := interfaceMethods(filepath.Join(*root, s.Interface.Path), s.Interface.Name)
	if err != nil { panic(err) }
	selectors, err := selectorNames(filepath.Join(*root, s.ConformanceSuite.Path))
	if err != nil { panic(err) }

	coreCoverage := map[string]string{}
	testCoverage := map[string]string{}
	ok := true
	for _, m := range s.Interface.RequiredCoreMethods {
		if contains(methods, m) { coreCoverage[m] = "MANDATORY" } else { coreCoverage[m] = "MISSING"; ok = false }
	}
	for _, m := range s.ConformanceSuite.RequiredExercisedMethods {
		if selectors[m] > 0 { testCoverage[m] = "EXERCISED" } else { testCoverage[m] = "NOT_EXERCISED"; ok = false }
	}
	forbidden, err := scanForbidden(*root, s.ForbiddenPatterns)
	if err != nil { panic(err) }
	for _, paths := range forbidden {
		if len(paths) != 0 { ok = false }
	}

	out := output{
		Adapter:"go-backend-contract-v0.1",
		WorldID:s.WorldID,
		ExactSourceCommit:head,
		Interface:s.Interface.Name,
		InterfaceMethods:methods,
		RequiredCoreMethods:s.Interface.RequiredCoreMethods,
		CoreMethodCoverage:coreCoverage,
		ConformanceExercised:testCoverage,
		ForbiddenProviderEvidence:forbidden,
		Status:map[bool]string{true:"PASS",false:"HOLD"}[ok],
	}
	encoded, _ := json.MarshalIndent(out, "", "  ")
	encoded = append(encoded, '\n')
	if err := os.MkdirAll(filepath.Dir(*outPath), 0755); err != nil { panic(err) }
	if err := os.WriteFile(*outPath, encoded, 0644); err != nil { panic(err) }
	fmt.Println("LAWKIT_GO_BACKEND_AUDIT=" + out.Status)
	if !ok { os.Exit(1) }
}
