package middleware

import (
	"mime"
	"strings"
)

// parseCanonicalContentType preserves the observation needed by both
// existing middlewares. Return false for malformed media parameters.
// Empty input is syntactically absent, not an accepted media type.
func parseCanonicalContentType(raw string) (mediaType string, charset string, valid bool) {
	if len(raw) > 128 { return "", "", false }
	if raw == "" { return "", "", true }
	media, params, err := mime.ParseMediaType(raw)
	if err != nil { return "", "", false }
	return media, strings.ToLower(params["charset"]), true
}
