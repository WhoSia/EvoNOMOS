package fixture
import "testing"
func TestOriginalClient(t *testing.T) { if Legacy() != "old" { t.Fatal("old client broken") } }
func TestInitialPorts(t *testing.T) { if FutureA() != "a0" || FutureB() != "b0" { t.Fatal("unexpected initial values") } }
