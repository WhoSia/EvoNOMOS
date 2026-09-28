package oci

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"sort"
	"strconv"
	"strings"
	"sync"
	"testing"

	"github.com/oracle/oci-go-sdk/v65/objectstorage"
	"github.com/restic/restic/internal/restic"
)

type fakeObjectClient struct {
	mu      sync.Mutex
	objects map[string][]byte
	calls   map[string]int
}

func newFakeObjectClient() *fakeObjectClient {
	return &fakeObjectClient{objects: map[string][]byte{}, calls: map[string]int{}}
}

func (f *fakeObjectClient) PutObject(_ context.Context, req objectstorage.PutObjectRequest) (objectstorage.PutObjectResponse, error) {
	f.mu.Lock()
	defer f.mu.Unlock()
	f.calls["PutObject"]++
	if req.NamespaceName == nil || *req.NamespaceName != "ns0" || req.BucketName == nil || *req.BucketName != "bucket0" {
		return objectstorage.PutObjectResponse{}, fmt.Errorf("wrong OCI namespace/bucket")
	}
	if req.ObjectName == nil || req.PutObjectBody == nil {
		return objectstorage.PutObjectResponse{}, fmt.Errorf("incomplete PutObject request")
	}
	b, err := io.ReadAll(req.PutObjectBody)
	if err != nil {
		return objectstorage.PutObjectResponse{}, err
	}
	f.objects[*req.ObjectName] = append([]byte(nil), b...)
	return objectstorage.PutObjectResponse{}, nil
}

func parseRange(raw *string, n int) (int, int, error) {
	if raw == nil || *raw == "" {
		return 0, n, nil
	}
	s := strings.TrimPrefix(*raw, "bytes=")
	parts := strings.SplitN(s, "-", 2)
	if len(parts) != 2 {
		return 0, 0, fmt.Errorf("bad range %q", *raw)
	}
	start, err := strconv.Atoi(parts[0])
	if err != nil {
		return 0, 0, err
	}
	end := n
	if parts[1] != "" {
		last, err := strconv.Atoi(parts[1])
		if err != nil {
			return 0, 0, err
		}
		end = last + 1
	}
	if start < 0 || start > n || end < start || end > n {
		return 0, 0, fmt.Errorf("range out of bounds %q", *raw)
	}
	return start, end, nil
}

func (f *fakeObjectClient) GetObject(_ context.Context, req objectstorage.GetObjectRequest) (objectstorage.GetObjectResponse, error) {
	f.mu.Lock()
	defer f.mu.Unlock()
	f.calls["GetObject"]++
	if req.ObjectName == nil {
		return objectstorage.GetObjectResponse{}, fmt.Errorf("missing object name")
	}
	b, ok := f.objects[*req.ObjectName]
	if !ok {
		return objectstorage.GetObjectResponse{}, errObjectNotFound
	}
	start, end, err := parseRange(req.Range, len(b))
	if err != nil {
		return objectstorage.GetObjectResponse{}, err
	}
	out := append([]byte(nil), b[start:end]...)
	n := int64(len(out))
	return objectstorage.GetObjectResponse{Content: io.NopCloser(bytes.NewReader(out)), ContentLength: &n}, nil
}

func (f *fakeObjectClient) HeadObject(_ context.Context, req objectstorage.HeadObjectRequest) (objectstorage.HeadObjectResponse, error) {
	f.mu.Lock()
	defer f.mu.Unlock()
	f.calls["HeadObject"]++
	if req.ObjectName == nil {
		return objectstorage.HeadObjectResponse{}, fmt.Errorf("missing object name")
	}
	b, ok := f.objects[*req.ObjectName]
	if !ok {
		return objectstorage.HeadObjectResponse{}, errObjectNotFound
	}
	n := int64(len(b))
	return objectstorage.HeadObjectResponse{ContentLength: &n}, nil
}

func (f *fakeObjectClient) ListObjects(_ context.Context, req objectstorage.ListObjectsRequest) (objectstorage.ListObjectsResponse, error) {
	f.mu.Lock()
	defer f.mu.Unlock()
	f.calls["ListObjects"]++
	prefix := ""
	if req.Prefix != nil {
		prefix = *req.Prefix
	}
	names := make([]string, 0)
	for name := range f.objects {
		if strings.HasPrefix(name, prefix) {
			names = append(names, name)
		}
	}
	sort.Strings(names)
	items := make([]objectstorage.ObjectSummary, 0, len(names))
	for _, name := range names {
		n := name
		size := int64(len(f.objects[name]))
		items = append(items, objectstorage.ObjectSummary{Name: &n, Size: &size})
	}
	return objectstorage.ListObjectsResponse{ListObjects: objectstorage.ListObjects{Objects: items}}, nil
}

func (f *fakeObjectClient) DeleteObject(_ context.Context, req objectstorage.DeleteObjectRequest) (objectstorage.DeleteObjectResponse, error) {
	f.mu.Lock()
	defer f.mu.Unlock()
	f.calls["DeleteObject"]++
	if req.ObjectName == nil {
		return objectstorage.DeleteObjectResponse{}, fmt.Errorf("missing object name")
	}
	if _, ok := f.objects[*req.ObjectName]; !ok {
		return objectstorage.DeleteObjectResponse{}, errObjectNotFound
	}
	delete(f.objects, *req.ObjectName)
	return objectstorage.DeleteObjectResponse{}, nil
}

func TestMandatoryCapabilityOracle(t *testing.T) {
	ctx := context.Background()
	client := newFakeObjectClient()
	cfg := Config{Namespace: "ns0", Bucket: "bucket0", Prefix: "root", Connections: 5}
	be := newBackendForTest(cfg, client)

	id := strings.Repeat("ab", 32)
	h := restic.Handle{Type: restic.PackFile, Name: id}
	payload := []byte("evonomos-oci-phase0-payload")

	if err := be.Save(ctx, h, restic.NewByteReader(payload, be.Hasher())); err != nil {
		t.Fatalf("Save: %v", err)
	}
	expectedObject := "root/data/ab/" + id
	if got := string(client.objects[expectedObject]); got != string(payload) {
		t.Fatalf("provider object mismatch")
	}

	fi, err := be.Stat(ctx, h)
	if err != nil || fi.Name != id || fi.Size != int64(len(payload)) {
		t.Fatalf("Stat mismatch: %+v %v", fi, err)
	}

	var whole []byte
	if err := be.Load(ctx, h, 0, 0, func(r io.Reader) error {
		var err error
		whole, err = io.ReadAll(r)
		return err
	}); err != nil {
		t.Fatalf("Load whole: %v", err)
	}
	if !bytes.Equal(whole, payload) {
		t.Fatalf("Load whole mismatch")
	}

	var part []byte
	if err := be.Load(ctx, h, 5, 3, func(r io.Reader) error {
		var err error
		part, err = io.ReadAll(r)
		return err
	}); err != nil {
		t.Fatalf("Load range: %v", err)
	}
	if !bytes.Equal(part, payload[3:8]) {
		t.Fatalf("Load range mismatch")
	}

	var listed []restic.FileInfo
	if err := be.List(ctx, restic.PackFile, func(fi restic.FileInfo) error {
		listed = append(listed, fi)
		return nil
	}); err != nil {
		t.Fatalf("List: %v", err)
	}
	if len(listed) != 1 || listed[0].Name != id || listed[0].Size != int64(len(payload)) {
		t.Fatalf("List mismatch: %+v", listed)
	}

	if err := be.Remove(ctx, h); err != nil {
		t.Fatalf("Remove: %v", err)
	}
	if _, err := be.Stat(ctx, h); err == nil || !be.IsNotExist(err) {
		t.Fatalf("IsNotExist/Stat mismatch: %v", err)
	}

	h2 := restic.Handle{Type: restic.PackFile, Name: strings.Repeat("cd", 32)}
	h3 := restic.Handle{Type: restic.KeyFile, Name: strings.Repeat("ef", 32)}
	if err := be.Save(ctx, h2, restic.NewByteReader([]byte("p2"), be.Hasher())); err != nil {
		t.Fatalf("Save pack for Delete: %v", err)
	}
	if err := be.Save(ctx, h3, restic.NewByteReader([]byte("key"), be.Hasher())); err != nil {
		t.Fatalf("Save key for Delete: %v", err)
	}
	if err := be.Delete(ctx); err != nil {
		t.Fatalf("Delete: %v", err)
	}
	if len(client.objects) != 0 {
		t.Fatalf("Delete left provider objects")
	}

	requiredProviderCalls := []string{"PutObject", "GetObject", "HeadObject", "ListObjects", "DeleteObject"}
	for _, name := range requiredProviderCalls {
		if client.calls[name] == 0 {
			t.Fatalf("provider operation not exercised: %s", name)
		}
	}
}
