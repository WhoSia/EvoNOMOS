package oci

import (
	"context"
	stderrors "errors"
	"path"
	"strings"

	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/objectstorage"
	"github.com/restic/restic/internal/backend/layout"
)

type Config struct {
	Namespace   string
	Bucket      string
	Prefix      string
	Connections uint
}

func NewConfig() Config {
	return Config{Connections: 5}
}

func ParseConfig(s string) (*Config, error) {
	if !strings.HasPrefix(s, "oci:") {
		return nil, stderrors.New("oci: invalid format")
	}
	parts := strings.SplitN(strings.TrimPrefix(s, "oci:"), "/", 3)
	if len(parts) < 2 || parts[0] == "" || parts[1] == "" {
		return nil, stderrors.New("oci: namespace and bucket are required")
	}
	cfg := NewConfig()
	cfg.Namespace = parts[0]
	cfg.Bucket = parts[1]
	if len(parts) == 3 {
		cfg.Prefix = strings.Trim(path.Clean("/"+parts[2]), "/")
	}
	return &cfg, nil
}

type objectClient interface {
	PutObject(ctx context.Context, request objectstorage.PutObjectRequest) (objectstorage.PutObjectResponse, error)
	GetObject(ctx context.Context, request objectstorage.GetObjectRequest) (objectstorage.GetObjectResponse, error)
	HeadObject(ctx context.Context, request objectstorage.HeadObjectRequest) (objectstorage.HeadObjectResponse, error)
	ListObjects(ctx context.Context, request objectstorage.ListObjectsRequest) (objectstorage.ListObjectsResponse, error)
	DeleteObject(ctx context.Context, request objectstorage.DeleteObjectRequest) (objectstorage.DeleteObjectResponse, error)
}

var _ objectClient = objectstorage.ObjectStorageClient{}

var errObjectNotFound = stderrors.New("oci object not found")

func isObjectNotFound(err error) bool {
	if stderrors.Is(err, errObjectNotFound) {
		return true
	}
	if serviceErr, ok := common.IsServiceError(err); ok {
		return serviceErr.GetHTTPStatusCode() == 404
	}
	return false
}

func defaultLayout(cfg Config) layout.Layout {
	return &layout.DefaultLayout{Path: cfg.Prefix, Join: path.Join}
}
