#!/usr/bin/env python3
"""Real old-schema to Team-schema Go migration regression (scratch DB only)."""
from pathlib import Path
import argparse,json,subprocess
TEST='''package store
import (
  "context"
  "database/sql"
  "testing"
  "github.com/pressly/goose/v3"
  _ "modernc.org/sqlite"
  "github.com/dklassen/swamp/db/migrations"
)
func TestP31ExistingRowsSurviveTeamMigration(t *testing.T) {
 db,err:=sql.Open("sqlite","file:"+t.TempDir()+"/upgrade.db")
 if err!=nil{t.Fatal(err)}
 defer db.Close()
 goose.SetBaseFS(migrations.FS)
 if err=goose.SetDialect("sqlite3");err!=nil{t.Fatal(err)}
 if err=goose.UpTo(db,".",5);err!=nil{t.Fatalf("pre-Team schema: %v",err)}
 prior:=New(db)
 c:=mustCreateCompany(t,prior,"Existing Company","ashby","existing")
 f,err:=prior.CreateCompanyFilter(context.Background(),c.ID,"department","Engineering")
 if err!=nil{t.Fatalf("old filter: %v",err)}
 if err=goose.Up(db,".");err!=nil{t.Fatalf("migrate existing DB: %v",err)}
 next:=New(db)
 found,err:=next.ListCompanyFilters(context.Background(),c.ID)
 if err!=nil||len(found)!=1||found[0].ID!=f.ID||found[0].Field!="department"||found[0].Value!="Engineering"{t.Fatalf("old filter lost %+v %v",found,err)}
 _,err=next.CreateCompanyFilter(context.Background(),c.ID,"team","Platform")
 if err!=nil{t.Fatalf("new Team filter rejected: %v",err)}
 found,err=next.ListCompanyFilters(context.Background(),c.ID)
 if err!=nil||len(found)!=2||found[1].Field!="team"{t.Fatalf("new filtered rows %+v %v",found,err)}
 var indexes int
 if err=db.QueryRow("SELECT count(*) FROM sqlite_master WHERE type='index' AND name='idx_company_filters_company_id'").Scan(&indexes);err!=nil||indexes!=1{t.Fatalf("index lost %d %v",indexes,err)}
}
'''
def main():
 p=argparse.ArgumentParser();p.add_argument("--direct",required=True);p.add_argument("--shared",required=True)
 a=p.parse_args()
 for x in [a.direct,a.shared]:
  f=Path(x)/"store/p31_upgrade_existing_test.go"
  f.write_text(TEST);subprocess.run(["gofmt","-w",str(f)],check=True)
 print(json.dumps({"status":"FIXTURE_MATERIALIZED_NOT_VERIFIED","old_version":5,"new_version":6,"arm_count":2}))
if __name__=="__main__": main()
