package middleware

import (
 "bytes"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
)

func TestR11P9RealChiReadFromAccountingUnderOriginalUnmergedProposal(t *testing.T) {
  phase:=os.Getenv("R11P9_SOURCE_PHASE")
  if phase!="old" && phase!="unmerged" {t.Fatal("missing source phase")}
  recorder:=httptest.NewRecorder()
  w:=&httpFancyWriter{basicWriter:basicWriter{ResponseWriter:recorder}}
  var tee bytes.Buffer
  w.Tee(&tee)
  n,err:=w.ReadFrom(strings.NewReader("hello world"))
  if err!=nil || n!=11 {t.Fatalf("original ReadFrom returned n=%d err=%v",n,err)}
  if recorder.Body.String()!="hello world" || tee.String()!="hello world"{
   t.Fatalf("original response or tee output diverged: body=%q tee=%q",recorder.Body.String(),tee.String())
  }
  wanted:=11
  if phase=="old" {wanted=22}
  if w.BytesWritten()!=wanted {
   t.Fatalf("SOURCE_PHASE=%s original core accounted %d, wanted %d",phase,w.BytesWritten(),wanted)
  }
  if recorder.Code!=http.StatusOK {t.Fatalf("original response status %d !=200",recorder.Code)}
  t.Logf("R11_P9_NATIVE_ORIGINAL_CHI_%s_ACCOUNTING_PREDICTION_PASS status=%d payload=%d tee=%d counted=%d",phase,recorder.Code,recorder.Body.Len(),tee.Len(),w.BytesWritten())
}
