package middleware

import (
 "net/http"
 "net/http/httptest"
 "sync/atomic"
 "testing"
)

// Historical regression probe written after reading real upstream #1045.
// This test is not a blind discovery and is independent of D18.
func TestP36O8EmptyRouteHeadersInvokeNextExactlyOnce(t *testing.T){
 var calls atomic.Int32
 h:=RouteHeaders().Handler(http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  calls.Add(1)
  w.WriteHeader(http.StatusOK)
 }))
 w:=httptest.NewRecorder()
 h.ServeHTTP(w,httptest.NewRequest(http.MethodGet,"/",nil))
 if got:=calls.Load();got!=1{
  t.Fatalf("P36_O8_UPSTREAM_EMPTY_MAP_DOUBLE_DISPATCH actual=%d wanted=1",got)
 }
}
