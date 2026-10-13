package mem_test

import (
    "bytes"
    "os"
    "testing"

    "google.golang.org/grpc/mem"
)

type r11P4TrackingPool struct {
    puts int
    seen *[]byte
}
func (p *r11P4TrackingPool) Get(size int) *[]byte {
    data := make([]byte,size)
    return &data
}
func (p *r11P4TrackingPool) Put(data *[]byte) {
    p.puts++
    p.seen=data
}
func TestR11P4OriginalPoolRepairCourt(t *testing.T) {
    expectation:=os.Getenv("R11_P4_EXPECT_SHORT_LONG_POOL")
    if expectation!="0" && expectation!="1" {
        t.Fatal("missing preregistered expected pooling from frozen commit")
    }
    // The allocation is larger than the threshold (1024) but has few
    // logical bytes. Existing source imports, code and Go compiler are real.
    data:=make([]byte,512,2048)
    copy(data,[]byte("old-observer"))
    pool:=new(r11P4TrackingPool)
    b:=mem.NewBuffer(&data,pool)
    if b.Len()!=512 || !bytes.Equal(b.ReadOnlyData()[:12],[]byte("old-observer")) {
        t.Fatal("old data contract changed")
    }
    b.Free()
    expectPut:=expectation=="1"
    if (pool.puts==1)!=expectPut {
        t.Fatalf("real source pooling mismatch: expected %t, observed put count %d",expectPut,pool.puts)
    }
    // Smaller backing arrays should never be returned in this context.
    small:=make([]byte,512,512)
    p2:=new(r11P4TrackingPool)
    x:=mem.NewBuffer(&small,p2)
    if x.Len()!=512 { t.Fatal("small old Len") }
    x.Free()
    if p2.puts!=0 {t.Fatal("small capacity incorrectly pooled")}
    t.Logf("R11_P4_REAL_GRPC_NATIVE_CAPACITY_REPAIR_PASS: large puts=%d; small puts=%d",pool.puts,p2.puts)
}
func TestR11P4OriginalNoPoolEquivalence(t *testing.T) {
    data:=make([]byte,17,2048)
    copy(data,[]byte("shared observer"))
    one:=mem.NewBuffer(&data,nil)
    two:=mem.SliceBuffer(data)
    if one.Len()!=two.Len() || !bytes.Equal(one.ReadOnlyData(),two.ReadOnlyData()) {
        t.Fatal("no-pool source alternatives differ on declared old observation")
    }
    one.Free(); two.Free()
    if !bytes.Equal(data[:15],[]byte("shared observer")) {
        t.Fatal("nil-pool release changed original backing data")
    }
    t.Log("R11_P4_REAL_GRPC_NATIVE_NIL_POOL_EQUIVALENCE_PASS")
}
