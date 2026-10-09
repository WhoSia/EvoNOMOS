package p35pair

import (
	"bytes"
	"context"
	"crypto/sha256"
	"errors"
	"hash"
	"io"
	"os"
	"sort"
	"sync"

	"github.com/restic/restic/internal/restic"
)

type backendMeta struct{}

func (backendMeta) Location() string          { return "p35-inmemory" }
func (backendMeta) Connections() uint         { return 1 }
func (backendMeta) Hasher() hash.Hash         { return sha256.New() }
func (backendMeta) HasAtomicReplace() bool    { return true }
func (backendMeta) IsNotExist(err error) bool { return errors.Is(err, os.ErrNotExist) }
func (backendMeta) Close() error              { return nil }

// UNIFIED: one authoritative mapping owns payload and logical metadata together.
type record struct {
	payload       []byte
	logicalLength int64
}
type unified struct {
	backendMeta
	mu      sync.RWMutex
	objects map[restic.Handle]record
}

func newUnified() *unified { return &unified{objects: make(map[restic.Handle]record)} }
func (u *unified) Save(ctx context.Context, h restic.Handle, r restic.RewindReader) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	if err := h.Valid(); err != nil {
		return err
	}
	b, err := io.ReadAll(r)
	if err != nil {
		return err
	}
	if err = ctx.Err(); err != nil {
		return err
	}
	u.mu.Lock()
	defer u.mu.Unlock()
	if err = ctx.Err(); err != nil {
		return err
	}
	u.objects[h] = record{payload: bytes.Clone(b), logicalLength: int64(len(b))}
	return nil
}
func (u *unified) Load(ctx context.Context, h restic.Handle, n int, off int64, cb func(io.Reader) error) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	u.mu.RLock()
	r, ok := u.objects[h]
	b := bytes.Clone(r.payload)
	u.mu.RUnlock()
	if !ok {
		return os.ErrNotExist
	}
	return serveRange(ctx, b, n, off, cb)
}
func (u *unified) Stat(ctx context.Context, h restic.Handle) (restic.FileInfo, error) {
	if err := ctx.Err(); err != nil {
		return restic.FileInfo{}, err
	}
	u.mu.RLock()
	r, ok := u.objects[h]
	u.mu.RUnlock()
	if !ok {
		return restic.FileInfo{}, os.ErrNotExist
	}
	return restic.FileInfo{Name: h.Name, Size: r.logicalLength}, nil
}
func (u *unified) List(ctx context.Context, t restic.FileType, cb func(restic.FileInfo) error) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	u.mu.RLock()
	a := make([]restic.FileInfo, 0)
	for h, r := range u.objects {
		if h.Type == t {
			a = append(a, restic.FileInfo{Name: h.Name, Size: r.logicalLength})
		}
	}
	u.mu.RUnlock()
	return publishList(ctx, a, cb)
}
func (u *unified) Remove(ctx context.Context, h restic.Handle) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	u.mu.Lock()
	defer u.mu.Unlock()
	if err := ctx.Err(); err != nil {
		return err
	}
	if _, ok := u.objects[h]; !ok {
		return os.ErrNotExist
	}
	delete(u.objects, h)
	return nil
}
func (u *unified) Delete(ctx context.Context) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	u.mu.Lock()
	defer u.mu.Unlock()
	if err := ctx.Err(); err != nil {
		return err
	}
	u.objects = make(map[restic.Handle]record)
	return nil
}

// COMPOSED: independent payload bytes and metadata index. The coordinator
// maintains a cross-store consistency boundary, not a shared vault kernel.
type storedPayload struct {
	data    []byte
	version uint8
}
type payloadStore struct {
	blobs map[restic.Handle]storedPayload
}

func newPayloadStore() *payloadStore {
	return &payloadStore{blobs: make(map[restic.Handle]storedPayload)}
}
func (p *payloadStore) put(h restic.Handle, b []byte) {
	p.blobs[h] = storedPayload{data: encodePayload(b), version: 1}
}
func (p *payloadStore) get(h restic.Handle) ([]byte, bool, bool) {
	v, ok := p.blobs[h]
	return bytes.Clone(v.data), v.version == 1, ok
}
func (p *payloadStore) erase(h restic.Handle) { delete(p.blobs, h) }
func (p *payloadStore) clear() {
	p.blobs = make(map[restic.Handle]storedPayload)
}

type metadataIndex struct{ lengths map[restic.Handle]int64 }

func newMetadataIndex() *metadataIndex                     { return &metadataIndex{lengths: make(map[restic.Handle]int64)} }
func (m *metadataIndex) set(h restic.Handle, n int64)      { m.lengths[h] = n }
func (m *metadataIndex) get(h restic.Handle) (int64, bool) { n, ok := m.lengths[h]; return n, ok }
func (m *metadataIndex) snapshot(t restic.FileType) []restic.FileInfo {
	a := make([]restic.FileInfo, 0)
	for h, n := range m.lengths {
		if h.Type == t {
			a = append(a, restic.FileInfo{Name: h.Name, Size: n})
		}
	}
	return a
}
func (m *metadataIndex) erase(h restic.Handle) { delete(m.lengths, h) }
func (m *metadataIndex) clear()                { m.lengths = make(map[restic.Handle]int64) }

type composed struct {
	backendMeta
	mu     sync.RWMutex
	write  *payloadStore
	read   *readEngine
	index  *metadataIndex
	remove *removalCoordinator
}
type readEngine struct{ source *payloadStore }

func (e *readEngine) decode(h restic.Handle) ([]byte, bool) {
	b, encoded, ok := e.source.get(h)
	if !ok {
		return nil, false
	}
	if encoded {
		b = decodePayload(b)
	}
	return b, true
}

type removalCoordinator struct {
	data  *payloadStore
	index *metadataIndex
}

func (r *removalCoordinator) erase(h restic.Handle) { r.data.erase(h); r.index.erase(h) }
func (r *removalCoordinator) clear()                { r.data.clear(); r.index.clear() }
func newComposed() *composed {
	data := newPayloadStore()
	index := newMetadataIndex()
	return &composed{write: data, read: &readEngine{source: data}, index: index, remove: &removalCoordinator{data: data, index: index}}
}
func (c *composed) Save(ctx context.Context, h restic.Handle, r restic.RewindReader) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	if err := h.Valid(); err != nil {
		return err
	}
	b, err := io.ReadAll(r)
	if err != nil {
		return err
	}
	if err = ctx.Err(); err != nil {
		return err
	}
	c.mu.Lock()
	defer c.mu.Unlock()
	if err = ctx.Err(); err != nil {
		return err
	}
	c.write.put(h, b)
	c.index.set(h, int64(len(b)))
	return nil
}
func (c *composed) Load(ctx context.Context, h restic.Handle, n int, off int64, cb func(io.Reader) error) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	c.mu.RLock()
	b, ok := c.read.decode(h)
	c.mu.RUnlock()
	if !ok {
		return os.ErrNotExist
	}
	return serveRange(ctx, b, n, off, cb)
}
func (c *composed) Stat(ctx context.Context, h restic.Handle) (restic.FileInfo, error) {
	if err := ctx.Err(); err != nil {
		return restic.FileInfo{}, err
	}
	c.mu.RLock()
	n, ok := c.index.get(h)
	c.mu.RUnlock()
	if !ok {
		return restic.FileInfo{}, os.ErrNotExist
	}
	return restic.FileInfo{Name: h.Name, Size: n}, nil
}
func (c *composed) List(ctx context.Context, t restic.FileType, cb func(restic.FileInfo) error) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	c.mu.RLock()
	a := c.index.snapshot(t)
	c.mu.RUnlock()
	return publishList(ctx, a, cb)
}
func (c *composed) Remove(ctx context.Context, h restic.Handle) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	c.mu.Lock()
	defer c.mu.Unlock()
	if err := ctx.Err(); err != nil {
		return err
	}
	if _, ok := c.index.get(h); !ok {
		return os.ErrNotExist
	}
	c.remove.erase(h)
	return nil
}
func (c *composed) Delete(ctx context.Context) error {
	if err := ctx.Err(); err != nil {
		return err
	}
	c.mu.Lock()
	defer c.mu.Unlock()
	if err := ctx.Err(); err != nil {
		return err
	}
	c.remove.clear()
	return nil
}
func serveRange(ctx context.Context, b []byte, n int, off int64, cb func(io.Reader) error) error {
	if off < 0 || off > int64(len(b)) || n < 0 {
		return errors.New("invalid range")
	}
	b = b[off:]
	if n > 0 && n < len(b) {
		b = b[:n]
	}
	if err := ctx.Err(); err != nil {
		return err
	}
	return cb(bytes.NewReader(b))
}
func publishList(ctx context.Context, a []restic.FileInfo, cb func(restic.FileInfo) error) error {
	sort.Slice(a, func(i, j int) bool { return a[i].Name < a[j].Name })
	for _, fi := range a {
		if err := ctx.Err(); err != nil {
			return err
		}
		if err := cb(fi); err != nil {
			return err
		}
	}
	return nil
}

var _ restic.Backend = (*unified)(nil)
var _ restic.Backend = (*composed)(nil)
