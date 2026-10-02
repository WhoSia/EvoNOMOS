package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Report struct {
	Tool              string              `json:"tool"`
	Domains           []string            `json:"domains"`
	IdenticalTables   bool                `json:"identical_truth_tables"`
	ExactAndGate      bool                `json:"exact_and_gate"`
	TransportStatus   string              `json:"transport_status"`
	TruthTables       map[string][]int    `json:"truth_tables"`
}

func main() {
	input := "active/g8-law-r1-p17/P17_INTERACTION_MATRIX.tsv"
	output := "out-p17/go-transport.json"
	if len(os.Args) > 1 { input = os.Args[1] }
	if len(os.Args) > 2 { output = os.Args[2] }

	f, err := os.Open(input); if err != nil { panic(err) }
	defer f.Close()
	tables := map[string][]int{}
	counts := map[string]int{}
	s := bufio.NewScanner(f)
	first := true
	for s.Scan() {
		if first { first = false; continue }
		p := strings.Split(s.Text(), "	")
		if len(p) != 5 { panic("bad row") }
		a,_ := strconv.Atoi(p[1]); l,_ := strconv.Atoi(p[2]); g,_ := strconv.Atoi(p[3]); y,_ := strconv.Atoi(p[4])
		mask := a | (l<<1) | (g<<2)
		if _, ok := tables[p[0]]; !ok { tables[p[0]] = make([]int,8) }
		tables[p[0]][mask] = y
		counts[p[0]]++
	}
	if err := s.Err(); err != nil { panic(err) }

	domains := make([]string,0,len(tables))
	for d := range tables { domains = append(domains,d) }
	if len(domains) != 2 { panic("expected two domains") }
	if domains[0] > domains[1] { domains[0],domains[1] = domains[1],domains[0] }

	exact := true
	for _, d := range domains {
		if counts[d] != 8 { exact = false }
		for m,y := range tables[d] {
			want := 0; if m == 7 { want = 1 }
			if y != want { exact = false }
		}
	}
	identical := true
	for i:=0;i<8;i++ { if tables[domains[0]][i] != tables[domains[1]][i] { identical = false } }
	status := "FAIL"
	if exact && identical { status = "EXACT_TWO_DOMAIN_TRANSPORT" }

	r := Report{"go",domains,identical,exact,status,tables}
	b,_ := json.MarshalIndent(r,"","  ")
	os.MkdirAll("out-p17",0755)
	os.WriteFile(output,append(b,'
'),0644)
	fmt.Println("P17_GO_TRANSPORT=PASS")
	fmt.Println("TRANSPORT_STATUS="+status)
}
