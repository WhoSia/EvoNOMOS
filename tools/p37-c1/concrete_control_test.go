package p37c1_test

import (
 "bytes"
 "net/http"
 "net/http/httptest"
 "testing"

 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/archive"
 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/concreteingress"
)
func TestP37C1DConcreteOwnerDependencyAndHistoricalRecovery(t *testing.T){
 for _,tc:=range []struct{data,want string}{
  {`{"id":7}`,`"id"`},
  {`{"i\u0064":7}`,`"i\u0064"`},
 }{
  store:=archive.New()
  // This module is explicitly *concrete*-dependent, no StorePort argument.
  h:=concreteingress.New(store)
  w:=httptest.NewRecorder()
  h.ServeHTTP(w,httptest.NewRequest(http.MethodPost,"/events",bytes.NewBufferString(tc.data)))
  if w.Code!=http.StatusNoContent{t.Fatalf("status=%d",w.Code)}
  got,err:=store.OriginalKeyAt(0)
  if err!=nil||got!=tc.want{t.Fatalf("DIP-negative control got=%q want=%q err=%v",got,tc.want,err)}
  state:=httptest.NewRecorder()
  h.ServeHTTP(state,httptest.NewRequest(http.MethodGet,"/state",nil))
  if state.Code!=200 || !bytes.Contains(state.Body.Bytes(),[]byte(`"revision":1`)){
   t.Fatalf("existing client changed: %q",state.Body.String())
  }
 }
}
