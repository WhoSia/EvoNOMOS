package fixture
import "testing"
func TestClients(t *testing.T){if Legacy()!="old"||FutureA()!="a0"||FutureB()!="b0"{t.Fatal("old or initial future contract violated")}}
