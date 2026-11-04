package r24

import (
 "io"
 "net/http"
 "net/http/httptest"
 "strings"
)

// WireObserve records what a real HTTP client sees, unlike handler-level Observe.
// It deliberately disables redirects so the response can be compared as sent.
func WireObserve(h http.Handler, method, target string) (Observation, error) {
 server := httptest.NewServer(h)
 defer server.Close()
 client := &http.Client{CheckRedirect: func(_ *http.Request, _ []*http.Request) error { return http.ErrUseLastResponse }}
 req, err := http.NewRequest(method, server.URL+target, nil)
 if err != nil {return Observation{}, err}
 res, err := client.Do(req)
 if err != nil {return Observation{}, err}
 defer res.Body.Close()
 body, err := io.ReadAll(res.Body)
 if err != nil {return Observation{}, err}
 return Observation{Method: method, Target: target, Status: res.StatusCode, Body: strings.TrimSpace(string(body)), Allow: res.Header.Get("Allow"), Location: res.Header.Get("Location")}, nil
}
