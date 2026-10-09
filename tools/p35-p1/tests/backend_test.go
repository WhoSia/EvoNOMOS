package p35pair

import (
	"bytes"
	"context"
	"errors"
	"github.com/restic/restic/internal/restic"
	"io"
	"os"
	"reflect"
	"testing"
)

func exercise(t *testing.T, b restic.Backend) []string {
	t.Helper()
	ctx := context.Background()
	h := restic.Handle{Type: restic.PackFile, Name: "alpha"}
	key := restic.Handle{Type: restic.KeyFile, Name: "k"}
	events := []string{}
	save := func(h restic.Handle, s string) {
		t.Helper()
		if err := b.Save(ctx, h, restic.NewByteReader([]byte(s), b.Hasher())); err != nil {
			t.Fatal(err)
		}
		events = append(events, "save:"+h.Name)
	}
	save(h, "abcd")
	save(key, "secret")
	fi, err := b.Stat(ctx, h)
	if err != nil || fi.Size != 4 {
		t.Fatalf("stat %v %+v", err, fi)
	}
	events = append(events, "stat:4")
	var out []byte
	count := 0
	err = b.Load(ctx, h, 2, 1, func(r io.Reader) error { count++; var e error; out, e = io.ReadAll(r); return e })
	if err != nil || count != 1 || !bytes.Equal(out, []byte("bc")) {
		t.Fatalf("load %q %v", out, err)
	}
	events = append(events, "load:bc")
	listed := []string{}
	err = b.List(ctx, restic.PackFile, func(fi restic.FileInfo) error { listed = append(listed, fi.Name); return nil })
	if err != nil || !reflect.DeepEqual(listed, []string{"alpha"}) {
		t.Fatalf("list %v %v", listed, err)
	}
	events = append(events, "list:alpha")
	sentinel := errors.New("stop")
	err = b.List(ctx, restic.PackFile, func(restic.FileInfo) error { return sentinel })
	if !errors.Is(err, sentinel) {
		t.Fatal("list callback error lost")
	}
	events = append(events, "list:stop")
	count = 0
	err = b.Load(ctx, restic.Handle{Type: restic.PackFile, Name: "missing"}, 0, 0, func(io.Reader) error { count++; return nil })
	if !b.IsNotExist(err) || count != 0 {
		t.Fatal("missing callback violated")
	}
	events = append(events, "missing")
	err = b.Load(ctx, h, 0, 0, func(io.Reader) error { return sentinel })
	if !errors.Is(err, sentinel) {
		t.Fatal("load callback error lost")
	}
	events = append(events, "load:stop")
	cancelled, cancel := context.WithCancel(ctx)
	cancel()
	err = b.Save(cancelled, h, restic.NewByteReader([]byte("bad"), b.Hasher()))
	if !errors.Is(err, context.Canceled) {
		t.Fatal("cancelled save mutated")
	}
	events = append(events, "cancel")
	save(h, "xyz")
	fi, err = b.Stat(ctx, h)
	if err != nil || fi.Size != 3 {
		t.Fatal("overwrite")
	}
	events = append(events, "overwrite:3")
	if err = b.Remove(ctx, h); err != nil {
		t.Fatal(err)
	}
	if err = b.Remove(ctx, h); !errors.Is(err, os.ErrNotExist) {
		t.Fatal("remove missing")
	}
	events = append(events, "remove")
	if err = b.Delete(ctx); err != nil {
		t.Fatal(err)
	}
	if _, err = b.Stat(ctx, key); !errors.Is(err, os.ErrNotExist) {
		t.Fatal("delete not cleared")
	}
	events = append(events, "delete")
	return events
}
func TestP35PairedContract(t *testing.T) {
	a := exercise(t, newUnified())
	b := exercise(t, newComposed())
	if !reflect.DeepEqual(a, b) {
		t.Fatalf("traces differ %v %v", a, b)
	}
	t.Logf("P35_P0_PUBLIC_TRACE_EQUAL PASS events=%d", len(a))
}
func TestP35DistinctPhysicalStores(t *testing.T) {
	c := newComposed()
	if c.write == nil || c.index == nil || c.read == nil || c.remove == nil {
		t.Fatal("missing capability")
	}
	if c.write.blobs == nil || c.index.lengths == nil {
		t.Fatal("independent stores missing")
	}
	t.Log("P35_P0_SEPARATE_PAYLOAD_AND_METADATA_STORES PASS")
}
