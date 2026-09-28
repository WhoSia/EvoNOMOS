package oci

import (
	"context"
	"fmt"
	"hash"
	"io"
	"path"
	"strings"

	"github.com/oracle/oci-go-sdk/v65/objectstorage"
	"github.com/restic/restic/internal/backend"
	"github.com/restic/restic/internal/backend/layout"
	"github.com/restic/restic/internal/restic"
)

type Backend struct {
	cfg    Config
	client objectClient
	layout layout.Layout
}

var _ restic.Backend = (*Backend)(nil)

func NewWithSDKClient(cfg Config, client objectstorage.ObjectStorageClient) *Backend {
	return newBackend(cfg, client)
}

func newBackendForTest(cfg Config, client objectClient) *Backend {
	return newBackend(cfg, client)
}

func newBackend(cfg Config, client objectClient) *Backend {
	return &Backend{cfg: cfg, client: client, layout: defaultLayout(cfg)}
}

func (be *Backend) Location() string {
	return fmt.Sprintf("oci:%s/%s/%s", be.cfg.Namespace, be.cfg.Bucket, be.cfg.Prefix)
}

func (be *Backend) Connections() uint {
	return be.cfg.Connections
}

func (be *Backend) Hasher() hash.Hash {
	return nil
}

func (be *Backend) HasAtomicReplace() bool {
	return true
}

func (be *Backend) Close() error {
	return nil
}

func (be *Backend) IsNotExist(err error) bool {
	return isObjectNotFound(err)
}

func (be *Backend) Save(ctx context.Context, h restic.Handle, rd restic.RewindReader) error {
	name := be.layout.Filename(h)
	length := rd.Length()
	_, err := be.client.PutObject(ctx, objectstorage.PutObjectRequest{
		NamespaceName: &be.cfg.Namespace,
		BucketName:    &be.cfg.Bucket,
		ObjectName:    &name,
		ContentLength: &length,
		PutObjectBody: io.NopCloser(rd),
	})
	return err
}

func (be *Backend) Load(ctx context.Context, h restic.Handle, length int, offset int64, fn func(io.Reader) error) error {
	name := be.layout.Filename(h)
	var byteRange *string
	switch {
	case length > 0:
		r := fmt.Sprintf("bytes=%d-%d", offset, offset+int64(length)-1)
		byteRange = &r
	case offset > 0:
		r := fmt.Sprintf("bytes=%d-", offset)
		byteRange = &r
	}
	resp, err := be.client.GetObject(ctx, objectstorage.GetObjectRequest{
		NamespaceName: &be.cfg.Namespace,
		BucketName:    &be.cfg.Bucket,
		ObjectName:    &name,
		Range:         byteRange,
	})
	if err != nil {
		return err
	}
	if resp.Content == nil {
		return fmt.Errorf("oci: GetObject returned nil content")
	}
	defer resp.Content.Close()
	return fn(resp.Content)
}

func (be *Backend) Stat(ctx context.Context, h restic.Handle) (restic.FileInfo, error) {
	name := be.layout.Filename(h)
	resp, err := be.client.HeadObject(ctx, objectstorage.HeadObjectRequest{
		NamespaceName: &be.cfg.Namespace,
		BucketName:    &be.cfg.Bucket,
		ObjectName:    &name,
	})
	if err != nil {
		return restic.FileInfo{}, err
	}
	if resp.ContentLength == nil {
		return restic.FileInfo{}, fmt.Errorf("oci: HeadObject returned nil content length")
	}
	return restic.FileInfo{Name: h.Name, Size: *resp.ContentLength}, nil
}

func (be *Backend) List(ctx context.Context, t restic.FileType, fn func(restic.FileInfo) error) error {
	prefix, _ := be.layout.Basedir(t)
	if !strings.HasSuffix(prefix, "/") {
		prefix += "/"
	}
	fields := "name,size"
	var start *string
	for {
		resp, err := be.client.ListObjects(ctx, objectstorage.ListObjectsRequest{
			NamespaceName: &be.cfg.Namespace,
			BucketName:    &be.cfg.Bucket,
			Prefix:        &prefix,
			Start:         start,
			Fields:        &fields,
		})
		if err != nil {
			return err
		}
		for _, item := range resp.Objects {
			if item.Name == nil || item.Size == nil {
				return fmt.Errorf("oci: ListObjects item missing name or size")
			}
			if ctx.Err() != nil {
				return ctx.Err()
			}
			if err := fn(restic.FileInfo{Name: path.Base(*item.Name), Size: *item.Size}); err != nil {
				return err
			}
		}
		if resp.NextStartWith == nil || *resp.NextStartWith == "" {
			return ctx.Err()
		}
		start = resp.NextStartWith
	}
}

func (be *Backend) Remove(ctx context.Context, h restic.Handle) error {
	name := be.layout.Filename(h)
	_, err := be.client.DeleteObject(ctx, objectstorage.DeleteObjectRequest{
		NamespaceName: &be.cfg.Namespace,
		BucketName:    &be.cfg.Bucket,
		ObjectName:    &name,
	})
	if be.IsNotExist(err) {
		return nil
	}
	return err
}

func (be *Backend) Delete(ctx context.Context) error {
	return backend.DefaultDelete(ctx, be)
}
