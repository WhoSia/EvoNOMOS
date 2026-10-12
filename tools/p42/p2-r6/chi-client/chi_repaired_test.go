//go:build chi_repaired

package r6chi

import (
 "io"
 "net/http"
 "testing"
 "github.com/go-chi/chi/v5/middleware"
)

type repairedWriter struct{http.ResponseWriter}
func (*repairedWriter)Status()int{return 200}
func (*repairedWriter)BytesWritten()int{return 0}
func (*repairedWriter)Tee(io.Writer){}
func (w *repairedWriter)Unwrap()http.ResponseWriter{return w.ResponseWriter}
func (*repairedWriter)Discard(){} // structural repair only, NOT semantic implementation
func TestRepairedInterfaceShape(t *testing.T){
 var w middleware.WrapResponseWriter = &repairedWriter{}
 if w.Status()!=200 {t.Fatal("base method changed")}
 t.Log("R6_CHI_REPAIRED_METHOD_SET_PASS_STRUCTURAL_ONLY")
}
