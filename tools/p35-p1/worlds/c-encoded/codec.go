package p35pair

// P35-P1 is a synthetic reversible encoding, not encryption.
var p35Header = []byte{'P', '3', '5', ':', '1', ':'}

func encodePayload(b []byte) []byte {
	out := make([]byte, len(p35Header)+len(b))
	copy(out, p35Header)
	for i, v := range b {
		out[len(p35Header)+i] = v ^ 0xA5
	}
	return out
}

// This function is called only when trusted metadata identifies v1 encoding.
func decodePayload(b []byte) []byte {
	if len(b) < len(p35Header) {
		return nil
	}
	out := make([]byte, len(b)-len(p35Header))
	for i, v := range b[len(p35Header):] {
		out[i] = v ^ 0xA5
	}
	return out
}
