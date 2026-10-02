package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"os"
)

type baseWriter struct {
	h       http.Header
	flushed bool
}

func (w *baseWriter) Header() http.Header {
	if w.h == nil {
		w.h = make(http.Header)
	}
	return w.h
}
func (w *baseWriter) Write(p []byte) (int, error) { return len(p), nil }
func (w *baseWriter) WriteHeader(statusCode int)  {}
func (w *baseWriter) Flush()                      { w.flushed = true }

type opaqueWrapper struct{ http.ResponseWriter }

type unwrapWrapper struct{ http.ResponseWriter }

func (w unwrapWrapper) Unwrap() http.ResponseWriter { return w.ResponseWriter }

type Case struct {
	Name       string `json:"name"`
	State      string `json:"state"`
	Predicted  string `json:"predicted_sign"`
	Observed   string `json:"observed_sign"`
	Success    bool   `json:"success"`
	Error      string `json:"error,omitempty"`
	Flushed    bool   `json:"flushed"`
	Wrapper    bool   `json:"wrapper"`
	PathLength int    `json:"path_length"`
	CarrierGap bool   `json:"carrier_gap"`
}

func run(name, state, predicted string, rw http.ResponseWriter, base *baseWriter, wrapper bool, pathLength int, carrierGap bool) Case {
	err := http.NewResponseController(rw).Flush()
	success := err == nil && base.flushed
	sign := "-"
	if success {
		sign = "+"
	}
	errText := ""
	if err != nil {
		errText = err.Error()
	}
	return Case{
		Name:       name,
		State:      state,
		Predicted:  predicted,
		Observed:   sign,
		Success:    success,
		Error:      errText,
		Flushed:    base.flushed,
		Wrapper:    wrapper,
		PathLength: pathLength,
		CarrierGap: carrierGap,
	}
}

func main() {
	directBase := &baseWriter{}
	direct := run(
		"DIRECT_CAPABILITY",
		"DIRECT_PRESERVING_BOUNDARY",
		"+",
		directBase,
		directBase,
		false,
		0,
		false,
	)

	opaqueBase := &baseWriter{}
	opaque := run(
		"OPAQUE_WRAPPER",
		"NONPRESERVING_INTERMEDIATE_BOUNDARY",
		"-",
		opaqueWrapper{opaqueBase},
		opaqueBase,
		true,
		1,
		true,
	)
	opaqueUnsupported := opaque.Error != "" && errors.Is(
		http.NewResponseController(opaqueWrapper{&baseWriter{}}).Flush(),
		http.ErrNotSupported,
	)

	unwrapBase := &baseWriter{}
	unwrapped := run(
		"UNWRAP_WRAPPER",
		"EXPLICIT_END_TO_END_CHANNEL",
		"+",
		unwrapWrapper{unwrapBase},
		unwrapBase,
		true,
		1,
		false,
	)

	cases := []Case{direct, opaque, unwrapped}
	pass := true
	for _, c := range cases {
		if c.Predicted != c.Observed {
			pass = false
		}
	}
	if !opaqueUnsupported {
		pass = false
	}

	payload := map[string]any{
		"stage": "EvoNOMOS Generation VIII LAW-R1-P21",
		"tool": "go",
		"status": map[bool]string{true: "PASS", false: "FAIL"}[pass],
		"cases": cases,
		"opaque_err_not_supported": opaqueUnsupported,
		"required_pattern": "+/-/+",
	}

	if err := os.MkdirAll("out-p21", 0o755); err != nil {
		panic(err)
	}
	b, _ := json.MarshalIndent(payload, "", "  ")
	if err := os.WriteFile("out-p21/p21-go.json", append(b, '\n'), 0o644); err != nil {
		panic(err)
	}

	fmt.Printf("P21_GO_SIGN=%s\n", payload["status"])
	for _, c := range cases {
		fmt.Printf("%s=%s\n", c.Name, c.Observed)
	}
	fmt.Printf("OPAQUE_ERR_NOT_SUPPORTED=%v\n", opaqueUnsupported)
	if !pass {
		os.Exit(2)
	}
}
