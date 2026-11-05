package sourcealias

import (
 "errors"
 "strings"
 "testing"
)

func TestTransportExactWhitespaceVariationAndClassicalBaseline(t *testing.T){
 for _,shared:=range []bool{true,false}{
  source:=fixture(shared)
  cert,seal,err:=Issue(source);if err!=nil{t.Fatal(err)}
  // Whitespace changes do not alter canonical parsed Go syntax.
  revised:=strings.Replace(source,"func Build() Clients{","func Build() Clients {\n\n",1)
  revised=strings.Replace(revised,"func Write(c Clients){","func Write(c Clients) {\n",1)
  status,err:=Verify(revised,cert,seal)
  if err!=nil||status!=Reused{t.Fatalf("shared=%v status=%s err=%v",shared,status,err)}
  rival,err:=Analyze(revised)
  if err!=nil||rival.Shared!=cert.Shared||rival.LegacyAfterWrite!=cert.LegacyAfterWrite{
   t.Fatalf("source-aware classical disagreed on unchanged AST: %+v %v",rival,err)
  }
  t.Logf("CERT_TRANSPORT shared=%v formatting_only_reuse=true classical_full_reanalysis_agrees=true",shared)
 }
}
func TestAliasingChangeInvalidatesRatherThanFalseSafety(t *testing.T){
 source:=fixture(true);cert,seal,err:=Issue(source);if err!=nil{t.Fatal(err)}
 changed:=fixture(false)
 status,err:=Verify(changed,cert,seal)
 if err!=nil||status!=Invalidated{t.Fatalf("changed alias not invalidated status=%s err=%v",status,err)}
 rival,err:=Analyze(changed)
 if err!=nil||rival.Shared||rival.LegacyAfterWrite!="stable"{t.Fatal(rival,err)}
 t.Log("CERT_INVALIDATION shared_to_disjoint=true full_classical_reanalysis_needed=true")
}
func TestUnsupportedMutationYieldsUnknown(t *testing.T){
 source:=fixture(false);cert,seal,err:=Issue(source);if err!=nil{t.Fatal(err)}
 cases:=[]string{
  "//go:build ignore\n"+source,
  "package fixture\nfunc Build(){",
 }
 for _,bad:=range cases{
  status,err:=Verify(bad,cert,seal)
  if status!=Unknown||!errors.Is(err,ErrUnsupportedSource){t.Fatalf("unexpected unsupported verdict %s/%v",status,err)}
 }
}
func TestForgedFactsWithoutTrustedSealRejected(t *testing.T){
 original:=fixture(false);cert,seal,err:=Issue(original);if err!=nil{t.Fatal(err)}
 cert.Shared=true
 cert.LegacyAfterWrite="new"
 if status,err:=Verify(original,cert,seal);status!=Unknown||!errors.Is(err,ErrCertificateIntegrity){t.Fatalf("forged untrusted content accepted %s %v",status,err)}
 t.Log("CERT_TAMPER trusted_evidence_seal_rejects_mutated_source_facts=true")
}
func TestHarmlessIdentifierRenameIsConservativelyInvalidated(t *testing.T){
 src:=fixture(true);cert,seal,err:=Issue(src);if err!=nil{t.Fatal(err)}
 revised:=strings.ReplaceAll(src,"Legacy:p,Future:p","Legacy:p,Future:p")
 revised=strings.ReplaceAll(revised,"p:=&Cell","another:=&Cell")
 revised=strings.ReplaceAll(revised,"Legacy:p,Future:p","Legacy:another,Future:another")
 if _,err:=Analyze(revised);err==nil{t.Fatal("current closed grammar must reject identifier rename until grammar expanded")}
 status,err:=Verify(revised,cert,seal)
 if err!=nil||status!=Invalidated{t.Fatalf("rename should invalidate source AST cache %s %v",status,err)}
 t.Log("CERT_CONSERVATIVE_FALSE_INVALIDATION identifier_rename_not_reusable=true")
}
