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

type capabilityContext struct {
	cfg    Config
	client objectClient
	layout layout.Layout
}

type saveCapability struct{ c *capabilityContext }
type loadCapability struct{ c *capabilityContext }
type statCapability struct{ c *capabilityContext }
type listCapability struct{ c *capabilityContext }
type removeCapability struct{ c *capabilityContext }
type deleteCapability struct{}

type Backend struct {
	c      *capabilityContext
	save   saveCapability
	load   loadCapability
	stat   statCapability
	list   listCapability
	remove removeCapability
	delete deleteCapability
}

var _ restic.Backend = (*Backend)(nil)

func NewWithSDKClient(cfg Config, client objectstorage.ObjectStorageClient) *Backend {
	return newBackend(cfg, client)
}

func newBackendForTest(cfg Config, client objectClient) *Backend {
	return newBackend(cfg, client)
}

func newBackend(cfg Config, client objectClient) *Backend {
	c := &capabilityContext{cfg: cfg, client: client, layout: defaultLayout(cfg)}
	return &Backend{
		c:      c,
		save:   saveCapability{c: c},
		load:   loadCapability{c: c},
		stat:   statCapability{c: c},
		list:   listCapability{c: c},
		remove: removeCapability{c: c},
		delete: deleteCapability{},
	}
}

func (be *Backend) Location() string {
	return fmt.Sprintf("oci:%s/%s/%s", be.c.cfg.Namespace, be.c.cfg.Bucket, be.c.cfg.Prefix)
}

func (be *Backend) Connections() uint {
	return be.c.cfg.Connections
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
	return be.save.Save(ctx, h, rd)
}

func (be *Backend) Load(ctx context.Context, h restic.Handle, length int, offset int64, fn func(io.Reader) error) error {
	return be.load.Load(ctx, h, length, offset, fn)
}

func (be *Backend) Stat(ctx context.Context, h restic.Handle) (restic.FileInfo, error) {
	return be.stat.Stat(ctx, h)
}

func (be *Backend) List(ctx context.Context, t restic.FileType, fn func(restic.FileInfo) error) error {
	return be.list.List(ctx, t, fn)
}

func (be *Backend) Remove(ctx context.Context, h restic.Handle) error {
	return be.remove.Remove(ctx, h)
}

func (be *Backend) Delete(ctx context.Context) error {
	return be.delete.Delete(ctx, be)
}

func (op saveCapability) Save(ctx context.Context, h restic.Handle, rd restic.RewindReader) error {
	name := op.c.layout.Filename(h)
	length := rd.Length()
	_, err := op.c.client.PutObject(ctx, objectstorage.PutObjectRequest{
		NamespaceName: &op.c.cfg.Namespace,
		BucketName:    &op.c.cfg.Bucket,
		ObjectName:    &name,
		ContentLength: &length,
		PutObjectBody: io.NopCloser(rd),
	})
	return err
}

func (op loadCapability) Load(ctx context.Context, h restic.Handle, length int, offset int64, fn func(io.Reader) error) error {
	name := op.c.layout.Filename(h)
	var byteRange *string
	switch {
	case length > 0:
		r := fmt.Sprintf("bytes=%d-%d", offset, offset+int64(length)-1)
		byteRange = &r
	case offset > 0:
		r := fmt.Sprintf("bytes=%d-", offset)
		byteRange = &r
	}
	resp, err := op.c.client.GetObject(ctx, objectstorage.GetObjectRequest{
		NamespaceName: &op.c.cfg.Namespace,
		BucketName:    &op.c.cfg.Bucket,
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

func (op statCapability) Stat(ctx context.Context, h restic.Handle) (restic.FileInfo, error) {
	name := op.c.layout.Filename(h)
	resp, err := op.c.client.HeadObject(ctx, objectstorage.HeadObjectRequest{
		NamespaceName: &op.c.cfg.Namespace,
		BucketName:    &op.c.cfg.Bucket,
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

func (op listCapability) List(ctx context.Context, t restic.FileType, fn func(restic.FileInfo) error) error {
	prefix, _ := op.c.layout.Basedir(t)
	if !strings.HasSuffix(prefix, "/") {
		prefix += "/"
	}
	fields := "name,size"
	var start *string
	for {
		resp, err := op.c.client.ListObjects(ctx, objectstorage.ListObjectsRequest{
			NamespaceName: &op.c.cfg.Namespace,
			BucketName:    &op.c.cfg.Bucket,
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

func (op removeCapability) Remove(ctx context.Context, h restic.Handle) error {
	name := op.c.layout.Filename(h)
	_, err := op.c.client.DeleteObject(ctx, objectstorage.DeleteObjectRequest{
		NamespaceName: &op.c.cfg.Namespace,
		BucketName:    &op.c.cfg.Bucket,
		ObjectName:    &name,
	})
	if isObjectNotFound(err) {
		return nil
	}
	return err
}

func (deleteCapability) Delete(ctx context.Context, owner restic.Backend) error {
	return backend.DefaultDelete(ctx, owner)
}
