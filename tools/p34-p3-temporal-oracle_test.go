package main

// P34-P3: source-exact Go mock-HTTP oracle, exercised via local httptest.
// This tests actual frozen handlers, response wire shapes and JSONL event
// order; it does not run either old TypeScript treatment or real vendors.
import (
  "bytes"
  "encoding/json"
  "fmt"
  "net/http"
  "net/http/httptest"
  "os"
  "path/filepath"
  "strings"
  "testing"
)

type p34Step struct {
  Name string `json:"name"`
  Path string `json:"path"`
  Status int `json:"status"`
  HasResults bool `json:"has_results"`
}
func p34Request(t *testing.T, client *http.Client, target, method, path, header, secret, body string, expected int) p34Step {
  t.Helper()
  req,err:=http.NewRequest(method,target+path,strings.NewReader(body))
  if err!=nil { t.Fatal(err) }
  if header!="" { req.Header.Set(header,secret) }
  req.Header.Set("content-type","application/json")
  res,err:=client.Do(req)
  if err!=nil { t.Fatal(err) }
  defer res.Body.Close()
  if res.StatusCode!=expected { t.Fatalf("%s %s: got status %d, want %d",method,path,res.StatusCode,expected) }
  var payload map[string]any
  if err:=json.NewDecoder(res.Body).Decode(&payload);err!=nil {t.Fatal(err)}
  if expected==200 {
    hits,ok:=payload["results"].([]any)
    if !ok||len(hits)<1 { t.Fatalf("missing structured fixture results: %s",path) }
    first,ok:=hits[0].(map[string]any)
    if !ok||len(first)==0 {t.Fatalf("bad result fixture at %s",path)}
    if _,ok:=first["url"].(string);!ok {t.Fatalf("no URL in %s",path)}
  } else {
    if payload["error"]==nil&&payload["detail"]==nil {t.Fatalf("bad failure contract at %s",path)}
  }
  return p34Step{Name:method+" "+path,Path:path,Status:expected,HasResults:expected==200}
}
func TestP34FrozenHTTPTemporalContract(t *testing.T) {
  logfile:=filepath.Join(t.TempDir(),"ledger.jsonl")
  server:=httptest.NewServer(newHandler(logfile))
  defer server.Close()
  client:=server.Client()
  var steps []p34Step
  perform:=func(method,path,header,secret,body string,status int) {
    steps=append(steps,p34Request(t,client,server.URL,method,path,header,secret,body,status))
  }
  perform("POST","/exa/search","","",`{"query":"evo"}`,401)
  perform("POST","/exa/search","x-api-key","exa-test-key",`{"query":"evo"}`,200)
  perform("POST","/exa/contents","x-api-key","exa-test-key",`{"urls":["https://fixture.invalid/page"],"text":true}`,200)
  perform("GET","/exa/contents","x-api-key","exa-test-key","",405)
  perform("POST","/exa/contents","x-api-key","exa-test-key",`{"urls":[]}`,400)
  perform("POST","/tavily/search","X-Tavily-Access-Mode","keyless",`{"query":"evo"}`,200)
  perform("POST","/tavily/extract","","",`{"urls":["https://fixture.invalid/page"]}`,401)
  perform("POST","/tavily/extract","Authorization","Bearer tavily-test-key",`{"urls":["https://fixture.invalid/page"]}`,200)
  perform("POST","/tavily/extract","Authorization","Bearer tavily-test-key",`{}`,400)
  perform("POST","/tavily/search","Authorization","Bearer tavily-test-key",`{"query":""}`,400)
  raw,err:=os.ReadFile(logfile)
  if err!=nil {t.Fatal(err)}
  lines:=bytes.Split(bytes.TrimSpace(raw),[]byte{10})
  if len(lines)!=4 {t.Fatalf("ledger expected 4 successful calls, got %d",len(lines))}
  want:=[]struct{Provider,Surface,Class,Auth string}{
    {"exa","search","demand-required","x-api-key"},
    {"exa","fetch","conformance-only","x-api-key"},
    {"tavily","search","demand-required","keyless"},
    {"tavily","fetch","conformance-only","bearer"},
  }
  for i,line:=range lines {
    var ev ledgerEvent
    if err:=json.Unmarshal(line,&ev);err!=nil {t.Fatal(err)}
    w:=want[i]
    if ev.Provider!=w.Provider||ev.Surface!=w.Surface||ev.Class!=w.Class||ev.AuthMode!=w.Auth {
      t.Fatalf("ledger order/class mismatch at step %d: %+v",i,ev)
    }
    if ev.At=="" {t.Fatalf("missing oracle time at event %d",i)}
  }
  report:=map[string]any{
    "schema":"P34_P3_FROZEN_GO_ORACLE_WIRE_TEMPORAL_V1",
    "exact_oracle":"ORIGIN-R1-P11 Go provider-surface-v01 from immutable historical EvoNOMOS checkout",
    "http_steps":len(steps),"successful_ledger_events":len(lines),
    "negative_attempts_excluded_from_ledger":len(steps)-len(lines),
    "ordered_event_classes":[]string{"exa/search/demand-required","exa/fetch/conformance-only","tavily/search/demand-required","tavily/fetch/conformance-only"},
    "checks":"HTTP status, structured body, auth, failure transitions, time-ordered successful request ledger",
    "limits":"Mock HTTP only; not TypeScript treatments, real vendor, runtime tool exposure, or client-progress theorem",
    "verdict":"P34_P3_SOURCE_EXACT_GO_ORACLE_TEMPORAL_WIRE_PASS",
  }
  if file:=os.Getenv("P34_OUT");file!="" {
    content,err:=json.MarshalIndent(report,"","  ")
    if err!=nil {t.Fatal(err)}
    if err=os.WriteFile(file,append(content,10),0644);err!=nil {t.Fatal(err)}
  }
  fmt.Printf("P34_WIRE_TRACE_PASS steps=%d ledger=%d rejected=%d\n",len(steps),len(lines),len(steps)-len(lines))
}
