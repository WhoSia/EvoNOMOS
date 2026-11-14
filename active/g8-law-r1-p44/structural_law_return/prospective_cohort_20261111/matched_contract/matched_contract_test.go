package middleware

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestP44P35P4MatchedContract(t *testing.T) {
	cases := []struct {
		name, header, body string
		present, unknownLength, charset bool
		allow string
		want int
	}{
		{name: "missing_type_with_body", body: "hello", want: 415},
		{name: "explicit_empty_type_with_body", present: true, body: "hello", want: 415},
		{name: "whitespace_type_with_body", present: true, header: " \t", body: "hello", want: 415},
		{name: "missing_type_with_unknown_length", body: "hello", unknownLength: true, want: 415},
		{name: "empty_body_bypass", want: 204},
		{name: "valid_type", present: true, header: "application/json", body: "hello", allow: "Application/JSON", want: 204},
		{name: "malformed_type", present: true, header: `application/json; x="bad`, body: "hello", allow: "application/json", want: 415},
		{name: "empty_charset_allows_missing_header", body: "hello", charset: true, want: 204},
		{name: "explicit_charset_rejects_missing_header", body: "hello", charset: true, allow: "UTF-8", want: 415},
		{name: "quoted_charset", present: true, header: `application/json; charset="UTF-8"`, body: "hello", charset: true, allow: "UTF-8", want: 204},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			wrap := AllowContentType(tc.allow)
			if tc.charset {
				wrap = ContentCharset(tc.allow)
			}
			reached := 0
			handler := wrap(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				reached++
				w.WriteHeader(http.StatusNoContent)
			}))
			req := httptest.NewRequest(http.MethodPost, "/", strings.NewReader(tc.body))
			if tc.present {
				req.Header.Set("Content-Type", tc.header)
			}
			if tc.unknownLength {
				req.ContentLength = -1
			}
			rec := httptest.NewRecorder()
			handler.ServeHTTP(rec, req)
			wantReached := 0
			if tc.want == http.StatusNoContent {
				wantReached = 1
			}
			if rec.Code != tc.want || reached != wantReached {
				t.Fatalf("status=%d calls=%d, want status=%d calls=%d", rec.Code, reached, tc.want, wantReached)
			}
		})
	}
}
