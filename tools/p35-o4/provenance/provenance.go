package provenance

import (
	"encoding/csv"
	"strings"
)

type Token struct {
	Value  string
	Quoted bool
}

// CSVErased models the O3 decoder output: values, without quoting provenance.
func CSVErased(raw string) ([]string, bool) {
	r := csv.NewReader(strings.NewReader(raw))
	r.TrimLeadingSpace = true
	r.FieldsPerRecord = -1
	tokens, err := r.Read()
	if err != nil {
		return nil, false
	}
	out := make([]string, 0, len(tokens))
	for _, token := range tokens {
		if token = strings.TrimSpace(token); token != "" {
			out = append(out, token)
		}
	}
	return out, true
}

// ScannerErased implements the separately developed O3 scanner shape.
func ScannerErased(raw string) ([]string, bool) {
	const (
		start = iota
		bare
		quoted
		afterQuoted
	)
	state := start
	out := []string{}
	var token strings.Builder
	push := func() {
		if v := strings.TrimSpace(token.String()); v != "" {
			out = append(out, v)
		}
		token.Reset()
	}
	for i := 0; i < len(raw); i++ {
		c := raw[i]
		switch state {
		case start:
			switch c {
			case ' ', '\t', ',':
				continue
			case '"':
				state = quoted
			default:
				token.WriteByte(c)
				state = bare
			}
		case bare:
			if c == '"' {
				return nil, false
			}
			if c == ',' {
				push()
				state = start
				continue
			}
			token.WriteByte(c)
		case quoted:
			if c == '"' {
				if i+1 < len(raw) && raw[i+1] == '"' {
					token.WriteByte('"')
					i++
				} else {
					state = afterQuoted
				}
			} else {
				token.WriteByte(c)
			}
		case afterQuoted:
			if c == ',' {
				push()
				state = start
				continue
			}
			if c != ' ' && c != '\t' {
				return nil, false
			}
		}
	}
	if state == quoted {
		return nil, false
	}
	push()
	return out, true
}

// OriginAware is a restricted independent reference for the one D12 query,
// not a full source-level fix or a complete CSV/HTTP parser.
func OriginAware(raw string) ([]Token, bool) {
	switch raw {
	case "ping":
		return []Token{{Value: "ping", Quoted: false}}, true
	case "\"ping\"":
		return []Token{{Value: "ping", Quoted: true}}, true
	default:
		return nil, false
	}
}
