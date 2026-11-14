package f20audit
import ("testing";"strings")

func TestAllOriginalCohortSHAAndObservationDifferentials(t *testing.T){
 cases:=OriginalCohort()
 if len(cases)!=3{t.Fatalf("expected three independent upstream repos: %d",len(cases))}
 seen:=map[string]bool{}
 for _,c:=range cases{
  if err:=c.Validate();err!=nil{t.Fatalf("%s %v",c.ID,err)}
  if seen[c.Repo]{t.Fatalf("duplicate upstream %s",c.Repo)}
  seen[c.Repo]=true
  if c.Before==c.After{t.Fatalf("%s same observation",c.ID)}
  if !c.SubjectDisclosedBeforeOracle{t.Fatalf("%s wrongly marked blind",c.ID)}
  t.Logf("F20_COHORT_VALIDATED id=%s original_job=%d scope=%s historical=true",c.ID,c.OriginalJobID,c.Observer)
 }
}
func TestTamperedOriginalSHAAndObserverAreRejected(t *testing.T){
 base:=OriginalCohort()[0]
 bad:=base;bad.ParentSHA="deadbeef"
 if bad.Validate()==nil{t.Fatal("short Git object id accepted")}
 bad=base;bad.Before=base.After
 if bad.Validate()==nil{t.Fatal("unchanged observation accepted as differential")}
 bad=base;bad.PublicAPI=false
 if bad.Validate()==nil{t.Fatal("exported Find incorrectly relabelled internal")}
 bad=OriginalCohort()[1];bad.PublicAPI=true
 if bad.Validate()==nil{t.Fatal("private allowed helper incorrectly labelled public")}
 bad=OriginalCohort()[2];bad.PublicAPI=true
 if bad.Validate()==nil{t.Fatal("internal Gin helper incorrectly labelled public")}
 bad=base;bad.AuthoredUTC="not-a-date"
 if bad.Validate()==nil{t.Fatal("invalid source commit date")}
}
func TestDirectGitHubReceiptIDsAreNonEmpty(t *testing.T){
 for _,c:=range OriginalCohort(){
  if c.OriginalJobID<=0||!strings.Contains(c.Repo,"/"){t.Fatal(c)}
 }
}
