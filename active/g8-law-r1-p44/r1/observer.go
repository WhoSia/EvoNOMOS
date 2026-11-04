package r1

import (
 "fmt"
 "io"
 "net/http"
 "net/http/httptest"
 "strings"
)

type Probe struct{Method,Path string}
type Observation struct{Status int;Body,Allow,Location string}

// ObserveWire intentionally uses a live HTTP server: HEAD body semantics differ
// between handler-level ResponseRecorder and bytes received by a real client.
func ObserveWire(h http.Handler,p Probe)(Observation,error){
 s:=httptest.NewServer(h); defer s.Close()
 req,e:=http.NewRequest(p.Method,s.URL+p.Path,nil)
 if e!=nil{return Observation{},e}
 client:=&http.Client{CheckRedirect:func(*http.Request,[]*http.Request)error{return http.ErrUseLastResponse}}
 resp,e:=client.Do(req)
 if e!=nil{return Observation{},e}
 defer resp.Body.Close()
 body,e:=io.ReadAll(io.LimitReader(resp.Body,1<<20))
 if e!=nil{return Observation{},e}
 return Observation{resp.StatusCode,strings.TrimSpace(string(body)),resp.Header.Get("Allow"),resp.Header.Get("Location")},nil
}
func Compare(a,b http.Handler,ps []Probe)([]string,error){
 var mismatches []string
 for _,p:=range ps{
  x,e:=ObserveWire(a,p);if e!=nil{return nil,e}
  y,e:=ObserveWire(b,p);if e!=nil{return nil,e}
  if x!=y{mismatches=append(mismatches,fmt.Sprintf("%s %s: std=%+v chi=%+v",p.Method,p.Path,x,y))}
 }
 return mismatches,nil
}
