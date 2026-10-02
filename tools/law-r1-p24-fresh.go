package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/go-logr/logr"
	"google.golang.org/protobuf/encoding/protowire"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/descriptorpb"
)

const (
	protobufCommit = "dcb66ef29d5e2a9420273f86407f493298804ec3"
	logrCommit     = "e99cde667024c0da5e20141f88fb7952e5f4e582"
)

type protoState struct {
	Known   bool
	Unknown bool
	TypeOK  bool
}

func canonicalWire() []byte {
	m := &descriptorpb.FileDescriptorProto{Name: proto.String("p24.proto")}
	b, err := proto.Marshal(m)
	if err != nil { panic(err) }
	b = protowire.AppendTag(b, 123, protowire.VarintType)
	b = protowire.AppendVarint(b, 7)
	return b
}

func applyProto(discard bool, dst *descriptorpb.FileDescriptorProto, wire []byte) error {
	return (proto.UnmarshalOptions{DiscardUnknown: discard}).Unmarshal(wire, dst)
}

func inspectProto(m *descriptorpb.FileDescriptorProto) protoState {
	return protoState{
		Known: m.GetName() == "p24.proto",
		Unknown: len(m.ProtoReflect().GetUnknown()) > 0,
		TypeOK: string(m.ProtoReflect().Descriptor().FullName()) == "google.protobuf.FileDescriptorProto",
	}
}

func cloneMessage(m *descriptorpb.FileDescriptorProto) *descriptorpb.FileDescriptorProto {
	return proto.Clone(m).(*descriptorpb.FileDescriptorProto)
}

func opOn(discard bool, input *descriptorpb.FileDescriptorProto, wire []byte) (*descriptorpb.FileDescriptorProto, error) {
	out := cloneMessage(input)
	if err := applyProto(discard, out, wire); err != nil { return nil, err }
	return out, nil
}

type gateSink struct { enabled bool }

func (s *gateSink) Init(logr.RuntimeInfo) {}
func (s *gateSink) Enabled(int) bool { return s.enabled }
func (s *gateSink) Info(int, string, ...any) {}
func (s *gateSink) Error(error, string, ...any) {}
func (s *gateSink) WithValues(...any) logr.LogSink { return s }
func (s *gateSink) WithName(string) logr.LogSink { return s }

func bridgeCell(q, g bool) bool {
	if !q {
		var l logr.Logger
		return l.Enabled()
	}
	s := &gateSink{enabled:g}
	return logr.New(s).Enabled()
}

func boolInt(b bool) int { if b { return 1 }; return 0 }

func main() {
	wire := canonicalWire()

	var present descriptorpb.FileDescriptorProto
	if err := applyProto(false, &present, wire); err != nil { panic(err) }
	var absent descriptorpb.FileDescriptorProto
	if err := applyProto(true, &absent, wire); err != nil { panic(err) }

	s0 := inspectProto(&absent)
	s1 := inspectProto(&present)
	if !(s0.Known && !s0.Unknown && s0.TypeOK && s1.Known && s1.Unknown && s1.TypeOK) {
		panic("failed to construct two protobuf abstract states")
	}

	states := []*descriptorpb.FileDescriptorProto{&absent, &present}
	transitions := map[string][]int{"D":{}, "R":{}}
	for _, in := range states {
		d, err := opOn(true, in, wire); if err != nil { panic(err) }
		r, err := opOn(false, in, wire); if err != nil { panic(err) }
		transitions["D"] = append(transitions["D"], boolInt(inspectProto(d).Unknown))
		transitions["R"] = append(transitions["R"], boolInt(inspectProto(r).Unknown))
	}

	compose := func(f, g string, in *descriptorpb.FileDescriptorProto) int {
		firstDiscard := g == "D"
		secondDiscard := f == "D"
		m1, err := opOn(firstDiscard, in, wire); if err != nil { panic(err) }
		m2, err := opOn(secondDiscard, m1, wire); if err != nil { panic(err) }
		return boolInt(inspectProto(m2).Unknown)
	}

	compDR := []int{compose("D","R",states[0]), compose("D","R",states[1])}
	compRD := []int{compose("R","D",states[0]), compose("R","D",states[1])}
	leftZero := fmt.Sprint(compDR)==fmt.Sprint(transitions["D"]) && fmt.Sprint(compRD)==fmt.Sprint(transitions["R"])

	var dmsg, rmsg descriptorpb.FileDescriptorProto
	if err := applyProto(true, &dmsg, wire); err != nil { panic(err) }
	if err := applyProto(false, &rmsg, wire); err != nil { panic(err) }
	ds, rs := inspectProto(&dmsg), inspectProto(&rmsg)
	propertyIndex := ds.Known && rs.Known && !ds.Unknown && rs.Unknown && ds.TypeOK && rs.TypeOK

	bridge := map[string]int{
		"q0_g0":boolInt(bridgeCell(false,false)),
		"q0_g1":boolInt(bridgeCell(false,true)),
		"q1_g0":boolInt(bridgeCell(true,false)),
		"q1_g1":boolInt(bridgeCell(true,true)),
	}
	andPass := bridge["q0_g0"]==0 && bridge["q0_g1"]==0 && bridge["q1_g0"]==0 && bridge["q1_g1"]==1

	status := leftZero && propertyIndex && andPass
	result := map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P24",
		"status":map[bool]string{true:"PASS",false:"FAIL"}[status],
		"pins":map[string]string{"protobuf_go":protobufCommit,"go_logr":logrCommit},
		"protobuf":map[string]any{
			"state0":s0,
			"state1":s1,
			"transitions":transitions,
			"D_o_R":compDR,
			"R_o_D":compRD,
			"orientation":"LEFT_ZERO_IDENTITY",
			"orientation_match":leftZero,
			"minimum_faithful_degree_prediction":2,
			"property_index_strong_replication":propertyIndex,
			"known_current":"PRESERVED_BY_D_AND_R",
			"unknown_future":"PRESERVED_BY_R_DROPPED_BY_D",
			"type_identity":"PRESERVED_BY_D_AND_R",
		},
		"bridge":map[string]any{
			"truth_table":bridge,
			"predicted_function":"AND",
			"held_out_match":andPass,
		},
	}
	b, _ := json.MarshalIndent(result,"","  ")
	if err := os.WriteFile("../p24-fresh.json", append(b,'\n'),0644); err != nil { panic(err) }

	fmt.Println("P24_FRESH="+result["status"].(string))
	fmt.Printf("PROTOBUF_ORIENTATION_MATCH=%v\n",leftZero)
	fmt.Printf("PROTOBUF_PROPERTY_INDEX=%v\n",propertyIndex)
	fmt.Printf("LOGR_AND_BRIDGE=%v\n",andPass)
	fmt.Printf("PROTOBUF_D=%v\n",transitions["D"])
	fmt.Printf("PROTOBUF_R=%v\n",transitions["R"])
	fmt.Printf("D_o_R=%v\n",compDR)
	fmt.Printf("R_o_D=%v\n",compRD)
	fmt.Printf("BRIDGE=%v\n",bridge)
	if !status { os.Exit(2) }
}
