package grpc

import (
    "bytes"
    "testing"
)
type r11P4LegacyCodec struct{}
func (r11P4LegacyCodec) Marshal(v any) ([]byte,error) {
    return []byte(v.(string)),nil
}
func (r11P4LegacyCodec) Unmarshal(d []byte,v any) error {
    *(v.(*string))=string(d); return nil
}
func (r11P4LegacyCodec) String() string {return "r11p4-original-bridge"}
func TestR11P4OriginalLegacyBridgeContract(t *testing.T) {
    // Calls the real historical grpc codecV0Bridge.Marshal implementation,
    // which switched from mem.NewBuffer(&data,nil) to mem.SliceBuffer(data)
    // in the separate real as h2k maintainer commit #7827.
    bridge:=newCodecV0Bridge(r11P4LegacyCodec{})
    result,err:=bridge.Marshal("original-2024-payload")
    if err!=nil {t.Fatal(err)}
    if !bytes.Equal(result.Materialize(),[]byte("original-2024-payload")) {
        t.Fatalf("original codec Marshal output changed")
    }
    var decoded string
    if err:=bridge.Unmarshal(result,&decoded);err!=nil || decoded!="original-2024-payload" {
        t.Fatalf("original codec Unmarshal changed: %q %v",decoded,err)
    }
    result.Free()
    t.Log("R11_P4_REAL_GRPC_NATIVE_CODEC_CALLSITE_CONTRACT_PASS")
}
