package p35pair

import (
	"bytes"
	"context"
	"errors"
	"io"
	"os"
	"testing"

	"github.com/restic/restic/internal/restic"
)

func armBackend(t *testing.T) restic.Backend {
	t.Helper()
	if os.Getenv("P35_ARM") == "u" {
		return newUnified()
	}
	if os.Getenv("P35_ARM") == "c" {
		return newComposed()
	}
	t.Fatal("P35_ARM must be u or c")
	return nil
}
func readAll(t *testing.T, b restic.Backend, h restic.Handle) []byte {
	t.Helper()
	var got []byte
	count := 0
	err := b.Load(context.Background(), h, 0, 0, func(r io.Reader) error { count++; var e error; got, e = io.ReadAll(r); return e })
	if err != nil || count != 1 {
		t.Fatalf("load err=%v count=%d", err, count)
	}
	return got
}
func TestP35P1LocalKeyFile(t *testing.T) {
	b := armBackend(t)
	ctx := context.Background()
	h := restic.Handle{Type: restic.KeyFile, Name: "key-bound"}
	original := []byte("12345678")
	if err := b.Save(ctx, h, restic.NewByteReader(original, b.Hasher())); err != nil {
		t.Fatal(err)
	}
	err := b.Save(ctx, h, restic.NewByteReader([]byte("123456789"), b.Hasher()))
	if err == nil || err.Error() != "P35_KEYFILE_LIMIT_EXCEEDED" {
		t.Fatalf("must reject >8 KeyFile, got %v", err)
	}
	if got := readAll(t, b, h); !bytes.Equal(got, original) {
		t.Fatalf("rejected overwrite corrupted state: %q", got)
	}
	p := restic.Handle{Type: restic.PackFile, Name: "pack-unbounded"}
	long := bytes.Repeat([]byte{'p'}, 1024)
	if err := b.Save(ctx, p, restic.NewByteReader(long, b.Hasher())); err != nil {
		t.Fatal(err)
	}
	if got := readAll(t, b, p); !bytes.Equal(got, long) {
		t.Fatal("unrelated PackFile limited or changed")
	}
	fi, err := b.Stat(ctx, h)
	if err != nil || fi.Size != 8 {
		t.Fatalf("stat %v %+v", err, fi)
	}
	t.Log("P35_LOCAL_BOUNDED_SOURCE_RULE=PASS")
}
func TestP35P1VersionedStorage(t *testing.T) {
	b := armBackend(t)
	ctx := context.Background()
	for _, data := range [][]byte{[]byte("fresh-payload"), {}, []byte("P35:1:\x00\xff")} {
		h := restic.Handle{Type: restic.PackFile, Name: "fresh" + string('a'+rune(len(data)))}
		if err := b.Save(ctx, h, restic.NewByteReader(data, b.Hasher())); err != nil {
			t.Fatal(err)
		}
		raw := rawPayload(t, b, h)
		if !bytes.HasPrefix(raw, []byte("P35:1:")) {
			t.Fatalf("storage is not tagged encoded: raw=%q", raw)
		}
		if bytes.Equal(raw, data) {
			t.Fatal("encoding did not change physical bytes")
		}
		if got := readAll(t, b, h); !bytes.Equal(got, data) {
			t.Fatalf("roundtrip %q != %q", got, data)
		}
		fi, err := b.Stat(ctx, h)
		if err != nil || fi.Size != int64(len(data)) {
			t.Fatalf("logical stat %v %+v", err, fi)
		}
		var listed bool
		err = b.List(ctx, restic.PackFile, func(x restic.FileInfo) error {
			if x.Name == h.Name {
				listed = x.Size == int64(len(data))
			}
			return nil
		})
		if err != nil || !listed {
			t.Fatalf("logical list does not preserve size %q", data)
		}
	}
	// Legacy payloads can start with exactly the encoding magic; prefix-only
	// decoding is not injective across the union of old and new encodings.
	legacy := restic.Handle{Type: restic.PackFile, Name: "legacy-prefix-collision"}
	prior := []byte("P35:1:\x00\xffNO_MIGRATION")
	injectLegacy(t, b, legacy, prior)
	if got := readAll(t, b, legacy); !bytes.Equal(got, prior) {
		t.Fatalf("legacy magic collision CORRUPTED: %q != %q", got, prior)
	}
	fi, err := b.Stat(ctx, legacy)
	if err != nil || fi.Size != int64(len(prior)) {
		t.Fatal("legacy stat not logical")
	}
	if err := b.Remove(ctx, legacy); err != nil {
		t.Fatal(err)
	}
	if err := b.Load(ctx, legacy, 0, 0, func(io.Reader) error { return nil }); !errors.Is(err, os.ErrNotExist) {
		t.Fatal("legacy removal invalid")
	}
	t.Log("P35_VERSIONED_REPRESENTATION_AND_LEGACY_COLLISION=PASS")
}
func rawPayload(t *testing.T, b restic.Backend, h restic.Handle) []byte {
	t.Helper()
	switch x := b.(type) {
	case *unified:
		x.mu.RLock()
		defer x.mu.RUnlock()
		return bytes.Clone(x.objects[h].payload)
	case *composed:
		x.mu.RLock()
		defer x.mu.RUnlock()
		return bytes.Clone(x.write.blobs[h])
	}
	t.Fatal("unhandled backend")
	return nil
}
func injectLegacy(t *testing.T, b restic.Backend, h restic.Handle, prior []byte) {
	t.Helper()
	switch x := b.(type) {
	case *unified:
		x.mu.Lock()
		defer x.mu.Unlock()
		x.objects[h] = record{payload: bytes.Clone(prior), logicalLength: int64(len(prior))}
	case *composed:
		x.mu.Lock()
		defer x.mu.Unlock()
		x.write.blobs[h] = bytes.Clone(prior)
		x.index.set(h, int64(len(prior)))
	default:
		t.Fatal("unhandled backend")
	}
}
