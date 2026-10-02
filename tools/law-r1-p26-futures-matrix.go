package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

func writeProbe(dir, dep string, g int) error {
	if err := os.MkdirAll(filepath.Join(dir, "src"), 0o755); err != nil {
		return err
	}
	features := ""
	if g == 1 {
		features = ", features = [\"alloc\"]"
	}
	cargo := fmt.Sprintf("[package]\nname = \"p26_futures_probe\"\nversion = \"0.1.0\"\nedition = \"2021\"\n\n[lib]\npath = \"src/lib.rs\"\n\n[dependencies]\nfutures-util = { path = %q, default-features = false%s }\n", filepath.ToSlash(dep), features)
	lib := "#![no_std]\nuse futures_util::future::abortable;\n\npub fn p26_probe() {\n    let _ = abortable(core::future::ready(()));\n}\n"
	if err := os.WriteFile(filepath.Join(dir, "Cargo.toml"), []byte(cargo), 0o644); err != nil {
		return err
	}
	return os.WriteFile(filepath.Join(dir, "src", "lib.rs"), []byte(lib), 0o644)
}

func tail(s string, n int) string {
	if len(s) <= n {
		return s
	}
	return s[len(s)-n:]
}

func runCell(base, dep, name string, q, g int) (map[string]any, error) {
	dir := filepath.Join(base, name)
	if err := os.RemoveAll(dir); err != nil {
		return nil, err
	}
	if err := writeProbe(dir, dep, g); err != nil {
		return nil, err
	}
	args := []string{"check", "--quiet", "--manifest-path", filepath.Join(dir, "Cargo.toml")}
	if q == 0 {
		args = append(args, "--target", "thumbv6m-none-eabi")
	}
	cmd := exec.Command("cargo", args...)
	out, err := cmd.CombinedOutput()
	ok := err == nil
	y := 0
	if ok {
		y = 1
	}
	return map[string]any{
		"mechanism":     "FUTURES_RS_ABORTABLE_CAPABILITY_GATE",
		"intervention":  strings.Split(name, "_")[0],
		"q":             q,
		"g":             g,
		"y":             y,
		"gate_before":   g,
		"gate_after":    g,
		"command_ok":    ok,
		"log_tail":      tail(string(out), 1200),
	}, nil
}

func main() {
	dep := os.Getenv("P26_FUTURES_UTIL")
	if dep == "" {
		dep = "out-p26/futures-rs/futures-util"
	}
	abs, err := filepath.Abs(dep)
	if err != nil {
		panic(err)
	}
	base := "out-p26/futures-probe"
	type cell struct {
		name string
		q, g int
	}
	cells := []cell{
		{"baseline_0", 1, 0},
		{"drop_0", 0, 0},
		{"restore_0", 1, 0},
		{"baseline_1", 1, 1},
		{"drop_1", 0, 1},
		{"restore_1", 1, 1},
	}
	rows := make([]map[string]any, 0, len(cells))
	for _, c := range cells {
		r, err := runCell(base, abs, c.name, c.q, c.g)
		if err != nil {
			panic(err)
		}
		rows = append(rows, r)
	}

	expected := map[string]int{
		"baseline/0": 0,
		"drop/0":     0,
		"restore/0":  0,
		"baseline/1": 1,
		"drop/1":     0,
		"restore/1":  1,
	}
	pass := true
	for _, r := range rows {
		name := r["intervention"].(string)
		g := r["g"].(int)
		q := r["q"].(int)
		y := r["y"].(int)
		k := fmt.Sprintf("%s/%d", name, g)
		if expected[k] != y || r["gate_before"].(int) != g || r["gate_after"].(int) != g {
			pass = false
		}
		if name == "drop" && q != 0 {
			pass = false
		}
		if (name == "baseline" || name == "restore") && q != 1 {
			pass = false
		}
	}

	payload := map[string]any{
		"stage":     "EvoNOMOS Generation VIII LAW-R1-P26",
		"mechanism": "FUTURES_RS_ABORTABLE_CAPABILITY_GATE",
		"status":    map[bool]string{true: "PASS", false: "FAIL"}[pass],
		"rows":      rows,
	}
	path := os.Getenv("P26_OUT_FUTURES")
	if path == "" {
		path = "out-p26/p26-futures.json"
	}
	f, err := os.Create(path)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	enc := json.NewEncoder(f)
	enc.SetIndent("", "  ")
	if err := enc.Encode(payload); err != nil {
		panic(err)
	}
	fmt.Printf("P26_FUTURES=%s\n", payload["status"])
	for _, r := range rows {
		fmt.Printf("%s q=%d g=%d y=%d ok=%v\n", r["intervention"], r["q"], r["g"], r["y"], r["command_ok"])
	}
	if !pass {
		os.Exit(2)
	}
}
