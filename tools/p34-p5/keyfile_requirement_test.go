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
 err:=backend.Save(ctx,h,restic.NewByteReader([]byte("123456789"),nil))
 if err==nil || err.Error()!="P34_KEYFILE_LIMIT_EXCEEDED"{
  t.Fatalf("new requirement violated: expected stable size rejection, got %v",err)
 }
 var got []byte
 err=backend.Load(ctx,h,0,0,func(r io.Reader)error{var e error;got,e=io.ReadAll(r);return e})
 if err!=nil||!bytes.Equal(got,stored){t.Fatalf("rejected overwrite mutated stored value: %v %q",err,got)}
 p:=restic.Handle{Type:restic.PackFile,Name:"unlimited-pack"}
 if err=backend.Save(ctx,p,restic.NewByteReader([]byte(strings.Repeat("p",64)),nil));err!=nil{
  t.Fatalf("PackFile unexpectedly limited: %v",err)
 }
 t.Logf("P34_P5_NEW_MAINTENANCE_CONTRACT=PASS arm=%s",os.Getenv("P34_ARM"))
}
