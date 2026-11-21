package boundaries

import "testing"

var benchmarkRecord Record

func BenchmarkReadLazy(b *testing.B) {
 v,err:=Config();if err!=nil{b.Fatal(err)}
 l:=Lazy{}
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{benchmarkRecord=l.Read(v)}
}
func BenchmarkReadSnapshot(b *testing.B){
 v,err:=Config();if err!=nil{b.Fatal(err)}
 s:=Snapshot{}
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{benchmarkRecord=s.Read(v)}
}
func BenchmarkReadJournal(b *testing.B){
 v,err:=Config();if err!=nil{b.Fatal(err)}
 j:=NewJournal()
 b.ReportAllocs();b.ResetTimer()
 for i:=0;i<b.N;i++{benchmarkRecord=j.Read(v)}
}
