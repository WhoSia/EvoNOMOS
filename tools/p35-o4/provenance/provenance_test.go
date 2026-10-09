package provenance

import (
	"reflect"
	"testing"
)

func TestO3QuoteOriginErasure(t *testing.T) {
	for name, parse := range map[string]func(string) ([]string, bool){
		"csv": CSVErased, "scanner": ScannerErased,
	} {
		bare, okBare := parse("ping")
		quoted, okQuoted := parse("\"ping\"")
		if !okBare || !okQuoted || !reflect.DeepEqual(bare, []string{"ping"}) ||
			!reflect.DeepEqual(bare, quoted) {
			t.Fatalf("%s lost the controlled D11 equivalence: %v %v", name, bare, quoted)
		}
	}
}

func TestD12ReferenceSeparatesExactlyTheErasedPair(t *testing.T) {
	bare, okBare := OriginAware("ping")
	quoted, okQuoted := OriginAware("\"ping\"")
	if !okBare || !okQuoted || len(bare) != 1 || len(quoted) != 1 ||
		bare[0].Quoted || !quoted[0].Quoted || bare[0].Value != quoted[0].Value {
		t.Fatalf("D12 limited oracle failed: bare=%v quoted=%v", bare, quoted)
	}
}

func TestNoDecodedOnlyMatcherCanSeparateTheseInputs(t *testing.T) {
	a, _ := CSVErased("ping")
	b, _ := CSVErased("\"ping\"")
	for _, matcher := range []func([]string) bool{
		func(tokens []string) bool { return len(tokens) != 0 },
		func(tokens []string) bool { return len(tokens) == 1 && tokens[0] == "ping" },
		func(tokens []string) bool { return len(tokens) == 1 && tokens[0] == "other" },
	} {
		if matcher(a) != matcher(b) {
			t.Fatal("equal decoder outputs were distinguished by a decoded-only matcher")
		}
	}
}
