package sourcealias

import "testing"

func BenchmarkF19FullClassicalTwoFileAnalysis(b *testing.B){
 pair:=f19pair(true,`"changed"`)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  facts,err:=ClassicalFullSliceReanalysis(pair)
  if err!=nil||!facts.Shared{b.Fatal(err)}
 }
}
func BenchmarkF19ClassicalDependencyCache(b *testing.B){
 original:=f19pair(true,`"original"`)
 cert,_,err:=IssueSlice(original);if err!=nil{b.Fatal(err)}
 changed:=f19pair(true,`"changed"`)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  ok,err:=ClassicalDependencyCache(changed,cert.CoreTokenDigest)
  if err!=nil||!ok{b.Fatal(err)}
 }
}
func BenchmarkF19CertificateSliceTransport(b *testing.B){
 original:=f19pair(true,`"original"`)
 cert,seal,err:=IssueSlice(original);if err!=nil{b.Fatal(err)}
 changed:=f19pair(true,`"changed"`)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  status,err:=VerifySlice(changed,cert,seal)
  if err!=nil||status!=SliceReused{b.Fatal(status,err)}
 }
}
func BenchmarkF19InitialIssueWithTwoFiles(b *testing.B){
 original:=f19pair(true,`"original"`)
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{
  cert,seal,err:=IssueSlice(original)
  if err!=nil||len(cert.CoreTokenDigest)!=64||len(seal.Digest)!=64{b.Fatal(err)}
 }
}
