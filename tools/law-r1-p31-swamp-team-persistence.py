#!/usr/bin/env python3
"""Extend the exact source-pinned P31 Team treatment to persisted programmatic filters.
No UI claims. Every output is written only into temporary upstream worktrees.
"""
from pathlib import Path
import json
import subprocess
import argparse

MIGRATION="""-- +goose Up
-- +goose StatementBegin
-- P31: allow a field already present in postings and both ingestion/display projections.
CREATE TABLE company_filters_team (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL REFERENCES companies(id),
    field TEXT NOT NULL CHECK (field IN ('department', 'location', 'team')),
    value TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO company_filters_team (id,company_id,field,value,created_at)
SELECT id,company_id,field,value,created_at FROM company_filters;
DROP TABLE company_filters;
ALTER TABLE company_filters_team RENAME TO company_filters;
CREATE INDEX idx_company_filters_company_id ON company_filters(company_id);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- A downgrade containing team rows fails its CHECK and rolls back rather
-- than silently deleting previously stored filters.
CREATE TABLE company_filters_no_team (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL REFERENCES companies(id),
    field TEXT NOT NULL CHECK (field IN ('department', 'location')),
    value TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO company_filters_no_team (id,company_id,field,value,created_at)
SELECT id,company_id,field,value,created_at FROM company_filters;
DROP TABLE company_filters;
ALTER TABLE company_filters_no_team RENAME TO company_filters;
CREATE INDEX idx_company_filters_company_id ON company_filters(company_id);
-- +goose StatementEnd
"""
STORE_TEST="""package store

import (
 "context"
 "testing"
)

func TestP31TeamFilterPersistenceAndSchema(t *testing.T) {
 s:=newTestStore(t)
 ctx:=context.Background()
 company:=mustCreateCompany(t,s,"P31","ashby","p31")
 if _,err:=s.CreateCompanyFilter(ctx,company.ID,"team","Platform");err!=nil{t.Fatalf("persist team filter: %v",err)}
 if _,err:=s.CreateCompanyFilter(ctx,company.ID,"unsupported","x");err==nil{t.Fatal("unexpected acceptance of unsupported field")}
 rows,err:=s.ListCompanyFilters(ctx,company.ID)
 if err!=nil||len(rows)!=1||rows[0].Field!="team"||rows[0].Value!="Platform"{t.Fatalf("stored Team rows = %+v err=%v",rows,err)}
}
"""
SYNC_TEST="""package sync

import (
 "context"
 "testing"
 "github.com/dklassen/swamp/jobboard"
)

func TestP31TeamFilterCreatesOnlyMatchingIngestion(t *testing.T) {
 s:=newTestStore(t)
 ctx:=context.Background()
 c:=mustCreateCompany(t,s,"P31","ashby","p31-team")
 if _,err:=s.CreateCompanyFilter(ctx,c.ID,"team","Platform");err!=nil{t.Fatalf("store Team: %v",err)}
 first:=samplePosting("job-1","Engineer","Engineering","Remote")
 second:=samplePosting("job-2","Engineer","Engineering","Remote")
 first.Team="platform"
 second.Team="Infrastructure"
 fetch:=&fakeFetcher{postings: map[string][]jobboard.Posting{"p31-team":{first,second}}}
 result,err:=New(s,map[string]PostingFetcher{"ashby":fetch}).SyncCompany(ctx,c.ID)
 if err!=nil{t.Fatalf("SyncCompany Team: %v",err)}
 if result.Fetched!=2||result.Created!=1{t.Fatalf("Team filter result = %+v",result)}
 rows,err:=s.ListPostingsByCompany(ctx,c.ID)
 if err!=nil||len(rows)!=1||rows[0].Team!="platform"{t.Fatalf("Team filtered postings %+v err=%v",rows,err)}
}
"""

def create(root):
    migration=root/"db/migrations/00006_p31_team_filter.sql"
    if migration.exists(): raise ValueError(f"migrate conflict: {migration}")
    migration.write_text(MIGRATION)
    for name,txt in [("store/p31_team_store_test.go",STORE_TEST),("sync/p31_team_sync_test.go",SYNC_TEST)]:
        f=root/name
        if f.exists():raise ValueError(f"test conflict: {f}")
        f.write_text(txt)
        subprocess.run(["gofmt","-w",str(f)],check=True)
    return {"root":str(root),"migration":str(migration.relative_to(root)),
            "tests":["store/p31_team_store_test.go","sync/p31_team_sync_test.go"],
            "scope":"PERSISTED_TEAM_FILTER_PROGRAMMATIC_API__NO_TUI_PICKER"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--direct",required=True)
    ap.add_argument("--shared",required=True)
    v=ap.parse_args()
    print(json.dumps({"arms":[create(Path(v.direct)),create(Path(v.shared))],
                      "evidence_status":"SOURCE_MATERIALIZATION_ONLY"}))
if __name__=="__main__":main()
