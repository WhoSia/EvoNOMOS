package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net"
	"net/http"
	"os"
	"sync"
	"time"
)

type ledgerEvent struct {
	At       string `json:"at"`
	Provider string `json:"provider"`
	Surface  string `json:"surface"`
	Class    string `json:"class"`
	AuthMode string `json:"auth_mode"`
}

type oracle struct {
	mu     sync.Mutex
	ledger string
}

func (o *oracle) record(e ledgerEvent) {
	if o.ledger == "" {
		return
	}
	o.mu.Lock()
	defer o.mu.Unlock()
	f, err := os.OpenFile(o.ledger, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0o644)
	if err != nil {
		log.Printf("ledger open: %v", err)
		return
	}
	defer f.Close()
	e.At = time.Now().UTC().Format(time.RFC3339Nano)
	_ = json.NewEncoder(f).Encode(e)
}

func jsonOut(w http.ResponseWriter, status int, v any) {
	w.Header().Set("content-type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(v)
}

func requirePost(w http.ResponseWriter, r *http.Request) bool {
	if r.Method != http.MethodPost {
		jsonOut(w, http.StatusMethodNotAllowed, map[string]any{"error": "POST required"})
		return false
	}
	return true
}

func exaAuth(r *http.Request) (string, bool) {
	if r.Header.Get("x-api-key") == "exa-test-key" {
		return "x-api-key", true
	}
	if r.Header.Get("Authorization") == "Bearer exa-test-key" {
		return "bearer", true
	}
	return "", false
}

func tavilyAuth(r *http.Request) (string, bool) {
	if r.Header.Get("Authorization") == "Bearer tavily-test-key" {
		return "bearer", true
	}
	if r.Header.Get("X-Tavily-Access-Mode") == "keyless" {
		return "keyless", true
	}
	return "", false
}

func decodeBody(w http.ResponseWriter, r *http.Request, dst any) bool {
	if err := json.NewDecoder(r.Body).Decode(dst); err != nil {
		jsonOut(w, http.StatusBadRequest, map[string]any{"error": "invalid json"})
		return false
	}
	return true
}

func (o *oracle) exaSearch(w http.ResponseWriter, r *http.Request) {
	if !requirePost(w, r) {
		return
	}
	auth, ok := exaAuth(r)
	if !ok {
		jsonOut(w, http.StatusUnauthorized, map[string]any{"error": "missing or invalid Exa key"})
		return
	}
	var body struct {
		Query string `json:"query"`
	}
	if !decodeBody(w, r, &body) || body.Query == "" {
		if body.Query == "" {
			jsonOut(w, http.StatusBadRequest, map[string]any{"error": "query required"})
		}
		return
	}
	o.record(ledgerEvent{Provider: "exa", Surface: "search", Class: "demand-required", AuthMode: auth})
	jsonOut(w, http.StatusOK, map[string]any{
		"results": []map[string]any{{
			"title":         "Exa fixture",
			"url":           "https://fixture.invalid/exa",
			"publishedDate": "2026-09-20T00:00:00Z",
			"text":          "exa deterministic snippet",
		}},
		"requestId": "exa-fixture-request",
	})
}

func (o *oracle) exaContents(w http.ResponseWriter, r *http.Request) {
	if !requirePost(w, r) {
		return
	}
	auth, ok := exaAuth(r)
	if !ok {
		jsonOut(w, http.StatusUnauthorized, map[string]any{"error": "missing or invalid Exa key"})
		return
	}
	var body struct {
		URLs []string `json:"urls"`
		Text any      `json:"text"`
	}
	if !decodeBody(w, r, &body) || len(body.URLs) == 0 {
		if len(body.URLs) == 0 {
			jsonOut(w, http.StatusBadRequest, map[string]any{"error": "urls required"})
		}
		return
	}
	o.record(ledgerEvent{Provider: "exa", Surface: "fetch", Class: "conformance-only", AuthMode: auth})
	jsonOut(w, http.StatusOK, map[string]any{
		"results": []map[string]any{{
			"id":    body.URLs[0],
			"title": "Exa contents fixture",
			"url":   body.URLs[0],
			"text":  "exa deterministic page content",
		}},
		"statuses": []map[string]any{{"id": body.URLs[0], "status": "success", "source": "cached"}},
	})
}

func (o *oracle) tavilySearch(w http.ResponseWriter, r *http.Request) {
	if !requirePost(w, r) {
		return
	}
	auth, ok := tavilyAuth(r)
	if !ok {
		jsonOut(w, http.StatusUnauthorized, map[string]any{"detail": map[string]any{"error": "Unauthorized: missing or invalid API key."}})
		return
	}
	var body struct {
		Query string `json:"query"`
	}
	if !decodeBody(w, r, &body) || body.Query == "" {
		if body.Query == "" {
			jsonOut(w, http.StatusBadRequest, map[string]any{"detail": map[string]any{"error": "query required"}})
		}
		return
	}
	o.record(ledgerEvent{Provider: "tavily", Surface: "search", Class: "demand-required", AuthMode: auth})
	jsonOut(w, http.StatusOK, map[string]any{
		"query": body.Query,
		"results": []map[string]any{{
			"title":   "Tavily fixture",
			"url":     "https://fixture.invalid/tavily",
			"content": "tavily deterministic snippet",
			"score":   0.9,
		}},
		"request_id": "tavily-fixture-request",
	})
}

func (o *oracle) tavilyExtract(w http.ResponseWriter, r *http.Request) {
	if !requirePost(w, r) {
		return
	}
	auth, ok := tavilyAuth(r)
	if !ok {
		jsonOut(w, http.StatusUnauthorized, map[string]any{"detail": map[string]any{"error": "Unauthorized: missing or invalid API key."}})
		return
	}
	var body struct {
		URLs any `json:"urls"`
	}
	if !decodeBody(w, r, &body) || body.URLs == nil {
		if body.URLs == nil {
			jsonOut(w, http.StatusBadRequest, map[string]any{"detail": map[string]any{"error": "urls required"}})
		}
		return
	}
	o.record(ledgerEvent{Provider: "tavily", Surface: "fetch", Class: "conformance-only", AuthMode: auth})
	jsonOut(w, http.StatusOK, map[string]any{
		"results": []map[string]any{{
			"url":         "https://fixture.invalid/page",
			"raw_content": "tavily deterministic page content",
		}},
		"failed_results": []any{},
		"request_id":     "tavily-extract-fixture-request",
	})
}

func newHandler(ledger string) http.Handler {
	o := &oracle{ledger: ledger}
	mux := http.NewServeMux()
	mux.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
		jsonOut(w, http.StatusOK, map[string]any{"status": "ok"})
	})
	mux.HandleFunc("/exa/search", o.exaSearch)
	mux.HandleFunc("/exa/contents", o.exaContents)
	mux.HandleFunc("/tavily/search", o.tavilySearch)
	mux.HandleFunc("/tavily/extract", o.tavilyExtract)
	return mux
}

func main() {
	listen := flag.String("listen", "127.0.0.1:0", "listen address")
	ledger := flag.String("ledger", "", "optional JSONL request ledger")
	flag.Parse()

	ln, err := net.Listen("tcp", *listen)
	if err != nil {
		log.Fatal(err)
	}
	addr := "http://" + ln.Addr().String()
	ready, _ := json.Marshal(map[string]any{"status": "READY", "base_url": addr})
	fmt.Println(string(ready))

	srv := &http.Server{Handler: newHandler(*ledger)}
	if err := srv.Serve(ln); err != nil && err != http.ErrServerClosed {
		log.Fatal(err)
	}
}
