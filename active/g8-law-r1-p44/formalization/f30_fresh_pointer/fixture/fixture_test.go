package fixture
import "testing"
func TestInitialClients(t *testing.T) {if Legacy()!="old" || FutureA()!="a0" || FutureB()!="b0" {t.Fatal("contract changed")}}
