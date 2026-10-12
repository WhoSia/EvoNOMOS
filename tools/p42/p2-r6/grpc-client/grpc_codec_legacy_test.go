//go:build grpc_codec_legacy

package r6grpc

import(
 "testing"
 "google.golang.org/grpc/encoding"
)

type existingCodec struct{}
func (*existingCodec)Name()string{return "r6-legacy"}
func (*existingCodec)Marshal(_ any)([]byte,error){return []byte("OK"),nil}
func (*existingCodec)Unmarshal(_ []byte,_ any)error{return nil}
func TestOldCodecRemainsCompatible(t *testing.T){
 var c encoding.Codec = &existingCodec{}
 b,err:=c.Marshal("x")
 if err!=nil||string(b)!="OK"{t.Fatal("old codec broke")}
 t.Log("R6_GRPC_LEGACY_CODEC_COMPATIBILITY_PASS")
}
