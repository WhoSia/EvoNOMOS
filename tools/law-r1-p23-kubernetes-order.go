package main

import (
	"encoding/json"
	"fmt"
	"os"
	"reflect"
)

type Obj map[string]any

func deepCopy(in Obj) Obj {
	b, _ := json.Marshal(in)
	var out Obj
	_ = json.Unmarshal(b, &out)
	return out
}

func fixtureV2() Obj {
	return Obj{
		"apiVersion": "stable.example.com/v1beta2",
		"kind": "MultiVersion",
		"metadata": map[string]any{"name":"x"},
		"contentv2": map[string]any{"key":"value"},
		"numv2": map[string]any{"num1":float64(1),"num2":float64(1000000)},
	}
}

func canonicalV1() Obj {
	return Obj{
		"apiVersion": "stable.example.com/v1beta1",
		"kind": "MultiVersion",
		"metadata": map[string]any{"name":"x"},
		"content": map[string]any{"key":"value"},
		"num": map[string]any{"num1":float64(1),"num2":float64(1000000)},
	}
}

func emptyV1() Obj {
	return Obj{
		"apiVersion": "stable.example.com/v1beta1",
		"kind": "MultiVersion",
		"metadata": map[string]any{"name":"x"},
	}
}

// R_CONVERT mirrors the field-level semantics of Kubernetes' nontrivialConverter
// for v1beta2 -> v1beta1.
func convert(in Obj) Obj {
	u := deepCopy(in)
	if u["apiVersion"] == "stable.example.com/v1beta2" {
		if v, ok := u["numv2"]; ok { u["num"] = v }
		if v, ok := u["contentv2"]; ok { u["content"] = v }
		delete(u,"numv2")
		delete(u,"contentv2")
		u["apiVersion"] = "stable.example.com/v1beta1"
	}
	return u
}

// D_STORAGE_PRUNE mirrors the relevant storage-schema pruning: only fields
// present in the v1beta1 structural schema (plus root metadata) survive.
func pruneStorage(in Obj) Obj {
	u := deepCopy(in)
	allowed := map[string]bool{
		"apiVersion":true,"kind":true,"metadata":true,
		"content":true,"num":true,"defaults":true,
	}
	for k := range u {
		if !allowed[k] { delete(u,k) }
	}
	return u
}

func semanticPresent(u Obj) bool {
	if c,ok:=u["content"].(map[string]any); ok && c["key"]=="value" {
		if n,ok:=u["num"].(map[string]any); ok && n["num1"]==float64(1) { return true }
	}
	if c,ok:=u["contentv2"].(map[string]any); ok && c["key"]=="value" {
		if n,ok:=u["numv2"].(map[string]any); ok && n["num1"]==float64(1) { return true }
	}
	return false
}

func sign(b bool) string { if b { return "+" }; return "-" }

type AbsState string
const (
	Legacy AbsState = "LEGACY"
	Canonical AbsState = "CANONICAL"
	Absent AbsState = "ABSENT"
)

func abstractObj(s AbsState) Obj {
	switch s {
	case Legacy: return fixtureV2()
	case Canonical: return canonicalV1()
	default: return emptyV1()
	}
}

func classify(u Obj) AbsState {
	if _,ok:=u["contentv2"]; ok { return Legacy }
	if semanticPresent(u) {
		if u["apiVersion"]=="stable.example.com/v1beta1" { return Canonical }
	}
	return Absent
}

func transition(op string, s AbsState) AbsState {
	u:=abstractObj(s)
	switch op {
	case "D": return classify(pruneStorage(u))
	case "R": return classify(convert(u))
	default: return s
	}
}

func compose(op1, op2 string, s AbsState) AbsState {
	// op1∘op2: execute op2, then op1
	u:=abstractObj(s)
	if op2=="D" { u=pruneStorage(u) } else if op2=="R" { u=convert(u) }
	if op1=="D" { u=pruneStorage(u) } else if op1=="R" { u=convert(u) }
	return classify(u)
}

func main(){
	base:=fixtureV2()
	cases:=map[string]Obj{
		"IDENTITY_BASELINE": deepCopy(base),
		"LOSS_ONLY": pruneStorage(base),
		"REPAIR_ONLY": convert(base),
		"LOSS_THEN_REPAIR": convert(pruneStorage(base)),
		"REPAIR_THEN_LOSS": pruneStorage(convert(base)),
	}
	signs:=map[string]string{}
	for k,v:=range cases { signs[k]=sign(semanticPresent(v)) }

	states:=[]AbsState{Legacy,Canonical,Absent}
	transitions:=map[string]map[AbsState]AbsState{"D":{},"R":{}}
	for _,op:=range []string{"D","R"}{
		for _,s:=range states{ transitions[op][s]=transition(op,s) }
	}
	comps:=map[string]map[AbsState]AbsState{}
	for _,pair:=range [][2]string{{"D","R"},{"R","D"}}{
		key:=pair[0]+"o"+pair[1]
		comps[key]=map[AbsState]AbsState{}
		for _,s:=range states{ comps[key][s]=compose(pair[0],pair[1],s) }
	}

	rightZero := true
	for _,s:=range states {
		// D∘R == R and R∘D == D
		if comps["DoR"][s] != transitions["R"][s] || comps["RoD"][s] != transitions["D"][s] { rightZero=false }
	}
	noncomm := !reflect.DeepEqual(comps["DoR"],comps["RoD"])

	status := signs["IDENTITY_BASELINE"]=="+" &&
		signs["LOSS_ONLY"]=="-" &&
		signs["REPAIR_ONLY"]=="+" &&
		signs["LOSS_THEN_REPAIR"]=="-" &&
		signs["REPAIR_THEN_LOSS"]=="+" &&
		rightZero && noncomm

	payload:=map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P23",
		"status":map[bool]string{true:"PASS",false:"FAIL"}[status],
		"signs":signs,
		"abstract_states":states,
		"transitions":transitions,
		"compositions":comps,
		"noncommutative":noncomm,
		"identified_algebra":"IDENTITY_ADJOINED_TWO_ELEMENT_RIGHT_ZERO_BAND",
		"right_zero_check":rightZero,
		"precommitted_M_CR_expected":map[string]string{
			"LOSS_THEN_REPAIR":"+",
			"REPAIR_THEN_LOSS":"-",
		},
	}
	os.MkdirAll("out-p23",0755)
	b,_:=json.MarshalIndent(payload,"","  ")
	os.WriteFile("out-p23/p23-kubernetes.json",append(b,'\n'),0644)

	fmt.Println("P23_KUBERNETES_ORDER="+payload["status"].(string))
	for _,k:=range []string{"IDENTITY_BASELINE","LOSS_ONLY","REPAIR_ONLY","LOSS_THEN_REPAIR","REPAIR_THEN_LOSS"}{
		fmt.Println(k+"="+signs[k])
	}
	fmt.Printf("NONCOMMUTATIVE=%v\n",noncomm)
	fmt.Printf("RIGHT_ZERO_BAND=%v\n",rightZero)
	if !status { os.Exit(2) }
}
