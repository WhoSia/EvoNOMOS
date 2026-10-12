//go:build chi_legacy

package r6chi

import (
 "io"
 "net/http"
 "testing"
 "github.com/go-chi/chi/v5/middleware"
)

type legacyWriter struct{http.ResponseWriter}
func (*legacyWriter)Status()int{return 200}
func (*legacyWriter)BytesWritten()int{return 0}
func (*legacyWriter)Tee(io.Writer){}
func (w *legacyWriter)Unwrap()http.ResponseWriter{return w.ResponseWriter}
func TestLegacyExternalImplementer(t *testing.T){
 var w middleware.WrapResponseWriter = &legacyWriter{}
 if w.Status()!=200 {t.Fatal("stable existing client observation")}
 t.Log("R6_CHI_LEGACY_PROVIDER_STRUCTURAL_PASS")
}
