package r24

import (
 "net/http"
 "testing"
)

var ExtendedProbes=[][2]string{
 {"GET","/items/alpha"}, {"HEAD","/items/alpha"}, {"POST","/items/alpha"},
 {"OPTIONS","/items/alpha"},{"GET","/items/a%2Fb"},{"GET","/items/%61lpha"},
 {"GET","/items/"},{"GET","/items/alpha/"},{"PUT","/items/alpha"},
 {"GET","/items/123"},{"HEAD","/items/a%2Fb"},{"GET","/items/%2e%2e"},
}

func TestStdlibProbeExpectations(t *testing.T) {
 h:=StandardMux()
 cases:=[]struct{method,target string; status int}{
  {"GET","/items/alpha",200},{"HEAD","/items/alpha",200},
  {"POST","/items/alpha",405},{"OPTIONS","/items/alpha",405},
  {"GET","/items/a%2Fb",200},{"GET","/items/%61lpha",200},
  {"GET","/items/",404},{"GET","/items/alpha/",404},
  {"PUT","/items/alpha",405},{"GET","/items/123",200},
  {"HEAD","/items/a%2Fb",200},
 }
 for _,tc:=range cases {t.Run(tc.method+tc.target,func(t *testing.T){got:=Observe(h,tc.method,tc.target);if got.Status!=tc.status {t.Fatalf("%+v want status %d",got,tc.status)}})}
}

func TestObservationProjectionCatchesMethodDivergence(t *testing.T) {
 a:=StandardMux()
 b:=http.NewServeMux()
 b.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){if r.Method==http.MethodHead {http.NotFound(w,r);return};w.WriteHeader(200);_,_=w.Write([]byte(r.PathValue("id")))})
 eq,miss:=EquivalentOn(a,b,[][2]string{{"HEAD","/items/alpha"}})
 if eq||len(miss)!=1 {t.Fatalf("method divergence not observed: eq=%v miss=%v",eq,miss)}
}

func TestSameHandlerEquivalentOnFiniteProbeSet(t *testing.T){h:=StandardMux();ok,miss:=EquivalentOn(h,h,ExtendedProbes);if !ok {t.Fatalf("identical handler diverged: %v",miss)}}
