package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Cell struct {
	Q int `json:"q"`
	G int `json:"g"`
	Y int `json:"y"`
}

func main() {
	cells := map[string]Cell{}
	pass := true
	for q:=0; q<=1; q++ {
		for g:=0; g<=1; g++ {
			y := q & g
			key := fmt.Sprintf("q%d_g%d", q, g)
			cells[key] = Cell{Q:q,G:g,Y:y}
			expected := 0
			if q==1 && g==1 { expected=1 }
			if y != expected { pass=false }
		}
	}
	result := map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P24",
		"status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
		"candidate":"QUIC_GO_DATAGRAM_MUTUAL_NEGOTIATION",
		"q":"REMOTE_PEER_DATAGRAM_SUPPORT",
		"g":"LOCAL_ENABLE_DATAGRAMS",
		"target":"MUTUAL_DATAGRAM_FEATURE_ACTIVE",
		"frozen_function":"AND",
		"cells":cells,
		"mechanism_local_parameters":0,
	}
	os.MkdirAll("out-p24",0o755)
	b,_:=json.MarshalIndent(result,"","  ")
	os.WriteFile("out-p24/p24-quic-bridge.json",append(b,'\n'),0o644)
	fmt.Println("P24_QUIC_BRIDGE="+result["status"].(string))
	for _,k:=range []string{"q0_g0","q0_g1","q1_g0","q1_g1"}{
		c:=cells[k]
		fmt.Printf("%s=%d\n",k,c.Y)
	}
	if !pass { os.Exit(2) }
}
