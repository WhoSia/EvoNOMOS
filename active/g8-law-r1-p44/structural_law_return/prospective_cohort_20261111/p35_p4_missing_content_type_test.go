package middleware

import (
	"net/http"
	"net/http/httptest"
	"os"
	"strings"
	"testing"
)

func TestP44P35P4MissingContentType(t *testing.T) {
	var want int
	switch os.Getenv("P44_PARSER_ARM") {
	case "independent":
		want = http.StatusUnsupportedMediaType
	case "shared":
		want = http.StatusNoContent
	default:
		t.Fatal("set P44_PARSER_ARM to independent or shared")
	}

	handler := AllowContentType("")(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNoContent)
	}))
	request := httptest.NewRequest(http.MethodPost, "/", strings.NewReader("hello"))
	recorder := httptest.NewRecorder()
	handler.ServeHTTP(recorder, request)
	t.Logf("missing Content-Type with body and empty allowlist entry: status=%d", recorder.Code)
	if recorder.Code != want {
		t.Fatalf("status=%d, want=%d", recorder.Code, want)
	}
}
