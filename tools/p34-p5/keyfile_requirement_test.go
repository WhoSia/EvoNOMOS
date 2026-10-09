package p34pair

// New demand-specific test, identical in all source worlds.
import (
 "bytes"
 "context"
 "io"
 "os"
 "strings"
 "testing"

 "github.com/restic/restic/internal/restic"
)
func TestP34P5KeyFileLengthBound(t *testing.T){
 var backend restic.Backend
 if os.Getenv("P34_ARM")=="composed"{backend=newComposed()}else{backend=newDirect()}
 ctx:=context.Background()
 h:=restic.Handle{Type:restic.KeyFile,Name:"key-test"}
 stored:=[]byte("12345678")
 if err:=backend.Save(ctx,h,restic.NewByteReader(stored,nil));err!=nil{t.Fatal(err)}
