#!/usr/bin/env python3
"""Research-authored source edit on a pinned contributor checkout, not upstream code."""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: python3 r11_p9q_chi1095_construct_conditional_flusher.py <chi-checkout>")
p = Path(sys.argv[1]) / "middleware/get_head.go"
source = p.read_text(encoding="utf-8")
old = "next.ServeHTTP(&getHeadAllowWriter{ResponseWriter: w}, r)"
new = "next.ServeHTTP(evonomosR11P9QOptionalFlusher(w), r)"
assert source.count(old) == 2, "unexpected proposal source; refuse edit"
assert "evonomosR11P9QOptionalFlusher" not in source
source = source.replace(old, new)
source += """

// Research-only alternative after inspecting PR #1095. This preserves the
// direct Flusher type-assertion surface of the underlying writer exactly.
func evonomosR11P9QOptionalFlusher(w http.ResponseWriter) http.ResponseWriter {
    core := &getHeadAllowWriter{ResponseWriter: w}
    if f, ok := w.(http.Flusher); ok {
        return &evonomosR11P9QFlusherWriter{core: core, delegate: f}
    }
    return core
}

type evonomosR11P9QFlusherWriter struct {
    core *getHeadAllowWriter
    delegate http.Flusher
}

func (w *evonomosR11P9QFlusherWriter) Header() http.Header {
    return w.core.Header()
}
func (w *evonomosR11P9QFlusherWriter) WriteHeader(status int) {
    w.core.WriteHeader(status)
}
func (w *evonomosR11P9QFlusherWriter) Write(b []byte) (int, error) {
    return w.core.Write(b)
}
func (w *evonomosR11P9QFlusherWriter) Flush() {
    w.delegate.Flush()
}
"""
p.write_text(source, encoding="utf-8")
print("RESEARCH_VARIANT_TWO_CONDITIONAL_METHOD_SHAPES_CREATED")
