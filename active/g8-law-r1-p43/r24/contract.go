package r24

import (
 "net/http"
 "net/http/httptest"
 "strings"
)

type Observation struct { Method, Target string; Status int; Body, Allow, Location string }

func StandardMux() http.Handler {
 mux:=http.NewServeMux()
 mux.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){
  w.Header().Set("Content-Type","text/plain; charset=utf-8")
  w.WriteHeader(http.StatusOK)
  _,_=w.Write([]byte(r.PathValue("id")))
 })
 return mux
}

func Observe(handler http.Handler, method,target string) Observation {
 req:=httptest.NewRequest(method,target,nil)
 rec:=httptest.NewRecorder()
 handler.ServeHTTP(rec,req)
 res:=rec.Result()
 defer res.Body.Close()
 return Observation{Method:method,Target:target,Status:res.StatusCode,Body:strings.TrimSpace(rec.Body.String()),Allow:res.Header.Get("Allow"),Location:res.Header.Get("Location")}
}

func EquivalentOn(a,b http.Handler, probes [][2]string) (bool, []string) {
 var mismatches []string
 for _,p:=range probes {
  x,y:=Observe(a,p[0],p[1]),Observe(b,p[0],p[1])
  if x.Status!=y.Status||x.Body!=y.Body||x.Allow!=y.Allow||x.Location!=y.Location {mismatches=append(mismatches,p[0]+" "+p[1])}
 }
 return len(mismatches)==0,mismatches
}
