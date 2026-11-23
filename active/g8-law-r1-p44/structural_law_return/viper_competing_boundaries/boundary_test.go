package boundaries

import (
 "os"
 "testing"
)

func withEnv(t *testing.T, present bool, value string, f func()) {
 t.Helper()
 old,exists:=os.LookupEnv(envName)
 if present {if err:=os.Setenv(envName,value);err!=nil{t.Fatal(err)}}else{if err:=os.Unsetenv(envName);err!=nil{t.Fatal(err)}}
 defer func() {var err error;if exists{err=os.Setenv(envName,old)}else{err=os.Unsetenv(envName)};if err!=nil{t.Error(err)}}()
 f()
}
type observations struct {
 lazyValue string
 lazyGuess Source
 snapValue string
 snapHistor Source
 journalValue string
 journalHistor Source
 liveSource Source
}
func makeWorld(t *testing.T, originAtRead bool, finalEnv bool) observations {
 t.Helper()
 var o observations
 withEnv(t,originAtRead,"same-token",func(){
  v,err:=Config();if err!=nil{t.Fatal(err)}
  la,sa,ja:=Lazy{},Snapshot{},NewJournal()
  lr:=la.Read(v);sr:=sa.Read(v);jr:=ja.Read(v)
  if lr.Value!="same-token"||sr.Value!="same-token"||jr.Value!="same-token"{t.Fatal("old client mismatch")}
  o.lazyValue,o.snapValue,o.journalValue=lr.Value,sr.Value,jr.Value
  withEnv(t,finalEnv,"same-token",func(){
   o.lazyGuess=la.GuessHistorical(lr)
   var ok bool
   o.snapHistor,ok=sa.Historical(sr);if !ok{t.Fatal("missing snapshot")}
   o.journalHistor,ok=ja.Historical(jr);if !ok{t.Fatal("missing journal")}
   o.liveSource=sa.OriginNow()
   if o.liveSource!=ja.OriginNow()||o.liveSource!=la.OriginNow(){t.Fatal("live source rival mismatch")}
  })
 })
 return o
}
func TestOldClientParityForAllThreeArchitectures(t *testing.T) {
 for _,present:=range []bool{false,true}{
  o:=makeWorld(t,present,present)
  if o.lazyValue!=o.snapValue||o.snapValue!=o.journalValue{t.Fatal("value parity broke")}
 }
}
func TestHistoricalFiberCollisionAfterSameCurrentEnvironment(t *testing.T){
 a:=makeWorld(t,false,true)
 b:=makeWorld(t,true,true)
 if a.lazyValue!=b.lazyValue||a.lazyGuess!=b.lazyGuess||a.liveSource!=b.liveSource {
  t.Fatalf("corrected identical-late-observation fiber falsified A=%+v B=%+v",a,b)
 }
 if a.lazyGuess!=Environment||b.lazyGuess!=Environment{t.Fatalf("expected both current environment: %+v / %+v",a,b)}
 if a.snapHistor!=File||a.journalHistor!=File||b.snapHistor!=Environment||b.journalHistor!=Environment{
  t.Fatalf("the historically different source bit was not preserved: A=%+v B=%+v",a,b)
 }
 t.Log("EVO_MATCHED_LATE_OBSERVATION true; lazy historical policy must fail one world; snapshot and journal preserve the bit")
}
func TestHistoricalWhenEnvRemoved(t *testing.T){
 o:=makeWorld(t,true,false)
 if o.lazyGuess!=File||o.snapHistor!=Environment||o.journalHistor!=Environment||o.liveSource!=File{
  t.Fatalf("historical/live divergence under removal not reproduced: %+v",o)
 }
}
func TestLivePolicyDistinctFromHistoricalPolicy(t *testing.T){
 a:=makeWorld(t,false,true)
 if a.liveSource!=Environment||a.snapHistor!=File||a.journalHistor!=File{t.Fatalf("live vs archived source mismatch: %+v",a)}
 b:=makeWorld(t,true,false)
 if b.liveSource!=File||b.snapHistor!=Environment||b.journalHistor!=Environment{t.Fatalf("reverse live mismatch: %+v",b)}
}
func TestClassicalExplicitAuditLogTiesSnapshot(t *testing.T){
 // One ordinary known-name env lookup recorded at t0 stores the same relevant
 // bit as an app-owned provenance snapshot. No interface novelty inferred.
 recorded:=makeWorld(t,false,true)
 if recorded.journalHistor!=recorded.snapHistor{t.Fatalf("a classical log already suffices: %+v",recorded)}
 other:=makeWorld(t,true,true)
 if other.journalHistor!=other.snapHistor{t.Fatalf("classical logger mismatch: %+v",other)}
}
