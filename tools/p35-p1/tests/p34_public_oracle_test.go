package p35pair

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"github.com/restic/restic/internal/restic"
	"io"
	"os"
	"reflect"
	"testing"
)

// Behavioral port of the 18-operation P34 public Restic core history.
// Original P34's adapter-to-capability visit count is intentionally excluded:
// the P35 physical engine topology has different dispatch semantics.
func replayP34History(t *testing.T, b restic.Backend) []string {
	t.Helper()
	ctx := context.Background()
	h := restic.Handle{Type: restic.PackFile, Name: "alpha"}
	h2 := restic.Handle{Type: restic.PackFile, Name: "beta"}
	h3 := restic.Handle{Type: restic.KeyFile, Name: "key-1"}
	events := []string{}
	push := func(label string, err error) {
		if err == nil {
			events = append(events, label+":OK")
		} else if errors.Is(err, os.ErrNotExist) {
			events = append(events, label+":NOT_FOUND")
		} else if errors.Is(err, context.Canceled) {
			events = append(events, label+":CANCELED")
		} else {
			events = append(events, label+":ERR:"+err.Error())
		}
	}
	save := func(label string, h restic.Handle, bts []byte) {
		err := b.Save(ctx, h, restic.NewByteReader(bts, b.Hasher()))
		push(label, err)
		if err != nil {
			t.Fatal(label, err)
		}
	}
	save("save_alpha", h, []byte("abcd"))
	save("save_beta", h2, []byte("bb"))
	save("save_key", h3, []byte("secret"))
	fi, err := b.Stat(ctx, h)
	push("stat_alpha", err)
	if err != nil || fi.Size != 4 {
		t.Fatal("stat")
	}
	cbCalls := 0
	got := []byte(nil)
	err = b.Load(ctx, h, 0, 0, func(r io.Reader) error { cbCalls++; var e error; got, e = io.ReadAll(r); return e })
	push("load_full", err)
	if err != nil || cbCalls != 1 || !bytes.Equal(got, []byte("abcd")) {
		t.Fatal("load full")
	}
	cbCalls = 0
	err = b.Load(ctx, h, 2, 1, func(r io.Reader) error { cbCalls++; var e error; got, e = io.ReadAll(r); return e })
	push("load_partial", err)
	if err != nil || cbCalls != 1 || !bytes.Equal(got, []byte("bc")) {
		t.Fatal("load partial")
	}
	names := []string{}
	err = b.List(ctx, restic.PackFile, func(f restic.FileInfo) error { names = append(names, fmt.Sprintf("%s:%d", f.Name, f.Size)); return nil })
	push("list_pack", err)
	if err != nil || !reflect.DeepEqual(names, []string{"alpha:4", "beta:2"}) {
		t.Fatal("list", names)
	}
	sentinelList := errors.New("STOP_LIST")
	called := 0
	err = b.List(ctx, restic.PackFile, func(f restic.FileInfo) error { called++; return sentinelList })
	push("list_early_error", err)
	if !errors.Is(err, sentinelList) || called != 1 {
		t.Fatal("list stop")
	}
	cbCalls = 0
	err = b.Load(ctx, restic.Handle{Type: restic.PackFile, Name: "absent"}, 0, 0, func(io.Reader) error { cbCalls++; return nil })
	push("load_missing", err)
	if !b.IsNotExist(err) || cbCalls != 0 {
		t.Fatal("missing")
	}
	cbCalls = 0
	sentinelLoad := errors.New("STOP_LOAD")
	err = b.Load(ctx, h, 0, 0, func(io.Reader) error { cbCalls++; return sentinelLoad })
	push("load_callback_error", err)
	if !errors.Is(err, sentinelLoad) || cbCalls != 1 {
		t.Fatal("load stop")
	}
	cancelled, cancel := context.WithCancel(ctx)
	cancel()
	err = b.Save(cancelled, h, restic.NewByteReader([]byte("SHOULD_NOT_WRITE"), b.Hasher()))
	push("save_cancelled", err)
	if !errors.Is(err, context.Canceled) {
		t.Fatal("cancel")
	}
	save("save_overwrite", h, []byte("abcdef"))
	fi, err = b.Stat(ctx, h)
	push("stat_overwrite", err)
	if err != nil || fi.Size != 6 {
		t.Fatal("overwrite")
	}
	err = b.Remove(ctx, h2)
	push("remove_beta", err)
	if err != nil {
		t.Fatal(err)
	}
	err = b.Remove(ctx, h2)
	push("remove_missing", err)
	if !b.IsNotExist(err) {
		t.Fatal("remove missing")
	}
	err = b.Delete(ctx)
	push("delete_all", err)
	if err != nil {
		t.Fatal(err)
	}
	_, err = b.Stat(ctx, h)
	push("stat_after_delete", err)
	if !b.IsNotExist(err) {
		t.Fatal("stat after delete")
	}
	n := 0
	err = b.List(ctx, restic.PackFile, func(restic.FileInfo) error { n++; return nil })
	push("list_after_delete", err)
	if err != nil || n != 0 {
		t.Fatal("list after delete")
	}
	if len(events) != 18 {
		t.Fatalf("expected 18 calls got %d", len(events))
	}
	return events
}
func TestP35P1P34BehavioralRegression(t *testing.T) {
	a := replayP34History(t, newUnified())
	b := replayP34History(t, newComposed())
	if !reflect.DeepEqual(a, b) {
		t.Fatalf("P34 18-step public trace diverged %v vs %v", a, b)
	}
	t.Logf("P34_PUBLIC_HISTORY_18_OF_18=PASS")
}
