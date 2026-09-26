package main

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func post(t *testing.T, client *http.Client, url string, headers map[string]string, body map[string]any) *http.Response {
	t.Helper()
	b, err := json.Marshal(body)
	if err != nil {
		t.Fatal(err)
	}
	req, err := http.NewRequest(http.MethodPost, url, bytes.NewReader(b))
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Set("content-type", "application/json")
	for k, v := range headers {
		req.Header.Set(k, v)
	}
	res, err := client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	return res
}

func TestExaSurfaces(t *testing.T) {
	s := httptest.NewServer(newHandler(""))
	defer s.Close()

	res := post(t, s.Client(), s.URL+"/exa/search", map[string]string{"x-api-key": "exa-test-key"}, map[string]any{"query": "fixture"})
	if res.StatusCode != 200 {
		t.Fatalf("search status=%d", res.StatusCode)
	}
	res.Body.Close()

	res = post(t, s.Client(), s.URL+"/exa/contents", map[string]string{"x-api-key": "exa-test-key"}, map[string]any{"urls": []string{"https://fixture.invalid/page"}, "text": true})
	if res.StatusCode != 200 {
		t.Fatalf("contents status=%d", res.StatusCode)
	}
	res.Body.Close()

	res = post(t, s.Client(), s.URL+"/exa/search", nil, map[string]any{"query": "fixture"})
	if res.StatusCode != 401 {
		t.Fatalf("missing key status=%d", res.StatusCode)
	}
	res.Body.Close()
}

func TestTavilyKeyedAndKeylessSearchAndExtract(t *testing.T) {
	s := httptest.NewServer(newHandler(""))
	defer s.Close()

	res := post(t, s.Client(), s.URL+"/tavily/search", map[string]string{"Authorization": "Bearer tavily-test-key"}, map[string]any{"query": "fixture"})
	if res.StatusCode != 200 {
		t.Fatalf("keyed search status=%d", res.StatusCode)
	}
	res.Body.Close()

	res = post(t, s.Client(), s.URL+"/tavily/search", map[string]string{"X-Tavily-Access-Mode": "keyless"}, map[string]any{"query": "fixture"})
	if res.StatusCode != 200 {
		t.Fatalf("keyless search status=%d", res.StatusCode)
	}
	res.Body.Close()

	res = post(t, s.Client(), s.URL+"/tavily/extract", map[string]string{"Authorization": "Bearer tavily-test-key"}, map[string]any{"urls": []string{"https://fixture.invalid/page"}})
	if res.StatusCode != 200 {
		t.Fatalf("extract status=%d", res.StatusCode)
	}
	res.Body.Close()
}

func TestUnknownSurfaceIsNotAccidentallyAccepted(t *testing.T) {
	s := httptest.NewServer(newHandler(""))
	defer s.Close()
	res, err := s.Client().Get(s.URL + "/exa/crawl")
	if err != nil {
		t.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 404 {
		t.Fatalf("unknown surface status=%d", res.StatusCode)
	}
}
