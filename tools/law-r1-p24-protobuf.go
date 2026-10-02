package main

import (
	"encoding/json"
	"fmt"
	"os"

	"google.golang.org/protobuf/encoding/protowire"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protodesc"
	"google.golang.org/protobuf/reflect/protoreflect"
	"google.golang.org/protobuf/types/descriptorpb"
	"google.golang.org/protobuf/types/dynamicpb"
)

type State struct {
	raw []byte
	msg *dynamicpb.Message
}

func fileDescriptor() protoreflect.MessageDescriptor {
	fdp := &descriptorpb.FileDescriptorProto{
		Name:    proto.String("p24.proto"),
		Package: proto.String("p24"),
		Syntax:  proto.String("proto3"),
		MessageType: []*descriptorpb.DescriptorProto{{
			Name: proto.String("M"),
			Field: []*descriptorpb.FieldDescriptorProto{{
				Name:   proto.String("known"),
				Number: proto.Int32(1),
				Label:  descriptorpb.FieldDescriptorProto_LABEL_OPTIONAL.Enum(),
				Type:   descriptorpb.FieldDescriptorProto_TYPE_INT32.Enum(),
			}},
		}},
	}
	fd, err := protodesc.NewFile(fdp, nil)
	if err != nil {
		panic(err)
	}
	return fd.Messages().ByName("M")
}

func rawPayload() []byte {
	var b []byte
	b = protowire.AppendTag(b, 1, protowire.VarintType)
	b = protowire.AppendVarint(b, 7)
	b = protowire.AppendTag(b, 2, protowire.VarintType)
	b = protowire.AppendVarint(b, 9)
	return b
}

func R(s *State) {
	if err := proto.Unmarshal(s.raw, s.msg); err != nil {
		panic(err)
	}
}

func D(s *State) {
	s.msg.ProtoReflect().SetUnknown(nil)
}

func unknownPresent(m *dynamicpb.Message) bool {
	return len(m.ProtoReflect().GetUnknown()) > 0
}

func knownValue(m *dynamicpb.Message, fd protoreflect.FieldDescriptor) int64 {
	return m.ProtoReflect().Get(fd).Int()
}

func abstract(m *dynamicpb.Message) string {
	if unknownPresent(m) {
		return "UNKNOWN_PRESENT"
	}
	return "UNKNOWN_ABSENT"
}

func newState(md protoreflect.MessageDescriptor, raw []byte) *State {
	return &State{raw: append([]byte(nil), raw...), msg: dynamicpb.NewMessage(md)}
}

func main() {
	md := fileDescriptor()
	known := md.Fields().ByNumber(1)
	raw := rawPayload()

	// Shared-boundary property-index test.
	keep := dynamicpb.NewMessage(md)
	if err := proto.Unmarshal(raw, keep); err != nil { panic(err) }
	drop := dynamicpb.NewMessage(md)
	if err := (proto.UnmarshalOptions{DiscardUnknown: true}).Unmarshal(raw, drop); err != nil { panic(err) }

	knownKeep := knownValue(keep, known)
	knownDrop := knownValue(drop, known)
	unknownKeep := unknownPresent(keep)
	unknownDrop := unknownPresent(drop)

	// Algebra test: R restores unknowns from immutable raw; D clears only unknown storage.
	a := newState(md, raw)
	R(a)
	R(a)
	rIdem := abstract(a) == "UNKNOWN_PRESENT"
	D(a)
	D(a)
	dIdem := abstract(a) == "UNKNOWN_ABSENT"

	dr := newState(md, raw)
	R(dr)
	D(dr) // D∘R
	drState := abstract(dr)
	drKnown := knownValue(dr.msg, known)

	rd := newState(md, raw)
	D(rd)
	R(rd) // R∘D
	rdState := abstract(rd)
	rdKnown := knownValue(rd.msg, known)

	leftZero := rIdem && dIdem &&
		drState == "UNKNOWN_ABSENT" &&
		rdState == "UNKNOWN_PRESENT"

	propertyIndexed := knownKeep == 7 && knownDrop == 7 &&
		unknownKeep && !unknownDrop &&
		drKnown == 7 && rdKnown == 7

	status := leftZero && propertyIndexed

	result := map[string]any{
		"stage": "EvoNOMOS Generation VIII LAW-R1-P24",
		"status": map[bool]string{true:"PASS", false:"FAIL"}[status],
		"candidate": "PROTOBUF_GO_UNKNOWN_FIELD_TRANSPORT",
		"observed_orientation": map[bool]string{true:"LEFT_ZERO_IDENTITY", false:"NOT_LEFT_ZERO"}[leftZero],
		"predicted_orientation": "LEFT_ZERO_IDENTITY",
		"predicted_min_faithful_degree": 2,
		"composition": map[string]string{
			"D_o_R": drState,
			"R_o_D": rdState,
		},
		"idempotence": map[string]bool{"D":dIdem,"R":rIdem},
		"property_index": map[string]any{
			"known_default": knownKeep,
			"known_discard_unknown": knownDrop,
			"unknown_default_present": unknownKeep,
			"unknown_discard_present": unknownDrop,
			"shared_boundary_distinct_transport": propertyIndexed,
		},
	}

	if err := os.MkdirAll("out-p24", 0o755); err != nil { panic(err) }
	b, _ := json.MarshalIndent(result, "", "  ")
	if err := os.WriteFile("out-p24/p24-protobuf.json", append(b, '\n'), 0o644); err != nil { panic(err) }

	fmt.Println("P24_PROTOBUF=" + result["status"].(string))
	fmt.Println("ORIENTATION=" + result["observed_orientation"].(string))
	fmt.Printf("KNOWN_DEFAULT=%d\n", knownKeep)
	fmt.Printf("KNOWN_DISCARD=%d\n", knownDrop)
	fmt.Printf("UNKNOWN_DEFAULT=%v\n", unknownKeep)
	fmt.Printf("UNKNOWN_DISCARD=%v\n", unknownDrop)
	fmt.Printf("PROPERTY_INDEXED=%v\n", propertyIndexed)

	if !status { os.Exit(2) }
}
