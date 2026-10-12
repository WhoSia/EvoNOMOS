//go:build grpc_codec_v2

package r6grpc

import(
 "testing"
 "google.golang.org/grpc/encoding"
 "google.golang.org/grpc/mem"
)

type alternateV2Codec struct{}
func (*alternateV2Codec)Name()string{return "r6-v2"}
func (*alternateV2Codec)Marshal(_ any)(mem.BufferSlice,error){return nil,nil}
func (*alternateV2Codec)Unmarshal(_ mem.BufferSlice,_ any)error{return nil}
func TestNewParallelCodecInterface(t *testing.T){
 var c encoding.CodecV2 = &alternateV2Codec{}
 encoding.RegisterCodecV2(c)
 if got:=encoding.GetCodecV2("r6-v2");got==nil||got.Name()!="r6-v2"{t.Fatal("parallel new codec not registered")}
 t.Log("R6_GRPC_PARALLEL_CODEC_V2_SOURCE_CAPABILITY_PASS")
}
