//go:build chi_feature

package r6chi

import (
 "bytes"
 "net/http"
 "net/http/httptest"
 "testing"
 "github.com/go-chi/chi/v5/middleware"
)
func TestNewDiscardCapabilityInOriginalFactory(t *testing.T){
 rec:=httptest.NewRecorder()
 w:=middleware.NewWrapResponseWriter(rec,1)
 var sink bytes.Buffer
 w.Tee(&sink)
 w.Discard()
 _,err:=w.Write([]byte("CUT"))
 if err!=nil{t.Fatal(err)}
 if rec.Body.String()!=""||sink.String()!="CUT"||w.BytesWritten()!=3{
  t.Fatalf("original postchange factory feature semantics rec=%q tee=%q wrote=%d",rec.Body.String(),sink.String(),w.BytesWritten())
 }
 // The decorated writer tracked status; real underlying record is untouched.
 _ = http.MethodGet
 t.Log("R6_CHI_POST_CHANGE_FACTORY_DISCARD_SEMANTICS_PASS")
}
