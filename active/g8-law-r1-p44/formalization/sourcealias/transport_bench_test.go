package sourcealias
import "testing"

// All benchmarks receive the SAME small accepted Go source and build context.
// They are NOT evidence of a program-scale incremental-analysis speedup.
func BenchmarkF18TransportVerify(b *testing.B){
 src:=fixture(true);cert,seal,err:=Issue(src);if err!=nil{b.Fatal(err)}
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  st,err:=Verify(src,cert,seal)
  if err!=nil||st!=Reused{b.Fatal(st,err)}
 }
}
func BenchmarkF18ClassicalFullReanalysis(b *testing.B){
 src:=fixture(true)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  result,err:=Analyze(src)
  if err!=nil||!result.Shared{b.Fatal(result,err)}
 }
}
func BenchmarkF18ClassicalExactTokenCache(b *testing.B){
 src:=fixture(true);cert,_,err:=Issue(src);if err!=nil{b.Fatal(err)}
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  digest,err:=CanonicalDigest(src)
  if err!=nil||digest!=cert.CanonicalSourceDigest{b.Fatal(digest,err)}
 }
}
func BenchmarkF18CertificateIssuance(b *testing.B){
 src:=fixture(true)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  cert,seal,err:=Issue(src)
  if err!=nil||len(cert.CanonicalSourceDigest)!=64||len(seal.EvidenceDigest)!=64{b.Fatal(err)}
 }
}
