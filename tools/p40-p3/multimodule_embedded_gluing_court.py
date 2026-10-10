"""P40-P3: separately valid Go packages can fail under unchanged old client.

Direct Fast.Next and versioned adapter both compile in new-feature packages.
Original Composite{fast.Fast;other.Other}.Next() compiles before adding Fast.Next;
after direct Fast.Next, it becomes an ambiguous promoted method.
The wrapper keeps original Fast intact and preserves old Composite.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import os
import subprocess

MOD = "example.org/evonomos/p40p3multi"


def package(root, name, source):
    path = root / name
    path.mkdir(parents=True, exist_ok=True)
    (path / (name + ".go")).write_text(source)


def build(root, architecture):
    (root / "go.mod").write_text(f"module {MOD}\n\ngo 1.22\n")
    package(root, "fast", """package fast
type Fast struct{}
func (Fast) Run() int {return 7}
""" + ("func (Fast) Next() int {return 42}\n" if architecture == "direct" else ""))
    package(root, "other", """package other
type Other struct{}
func (Other) Next() int {return 99}
""")
    package(root, "client", f"""package client
import "{MOD}/fast"
import "{MOD}/other"
type Composite struct{{fast.Fast; other.Other}}
func Old(c Composite) int {{return c.Next()}}
""")
    if architecture == "wrapper":
        package(root, "adapter", f"""package adapter
import "{MOD}/fast"
type FastAdapter struct{{fast.Fast}}
func (FastAdapter) Next() int {{return 42}}
""")
    factory = "fast.Fast{}" if architecture == "direct" else "adapter.FastAdapter{Fast:fast.Fast{}}"
    modern = f"""package modern
import "{MOD}/fast"
"""
    if architecture == "wrapper":
        modern += f'import "{MOD}/adapter"\n'
    modern += f"""type Advanced interface{{Run() int; Next() int}}
func Open() Advanced {{return {factory}}}
"""
    package(root, "modern", modern)
    (root / "modern" / "modern_test.go").write_text("""package modern
import "testing"
func TestFuture(t *testing.T) {
    if Open().Run()!=7 || Open().Next()!=42 {t.Fatal("future capability")}
}
""")
    (root / "client" / "client_test.go").write_text("""package client
import "testing"
func TestOld(t *testing.T) {
    if Old(Composite{})!=99 {t.Fatal("old embedding contract")}
}
""")


def run_go(root, args):
    env = dict(os.environ, GOWORK="off", GOPROXY="off", GOSUMDB="off", GOTOOLCHAIN="local")
    return subprocess.run(["go", "test", "-count=1", *args],
                          cwd=root, env=env, text=True,
                          capture_output=True, timeout=100)


def main():
    for arch in ("direct", "wrapper"):
        with TemporaryDirectory(prefix="evonomos-p40p3-multi-") as td:
            root = Path(td)
            build(root, arch)
            components = run_go(root, ["./fast", "./other", "./modern"])
            old_client = run_go(root, ["./client"])
            integrated = run_go(root, ["./..."])
            assert components.returncode == 0, (arch, components.stdout, components.stderr)
            assert (old_client.returncode == 0) == (arch == "wrapper"), (
                arch, old_client.stdout, old_client.stderr)
            assert (integrated.returncode == 0) == (arch == "wrapper"), (
                arch, integrated.stdout, integrated.stderr)
            if arch == "direct":
                assert "ambiguous selector c.Next" in old_client.stderr
        outcome = "PASS" if arch == "wrapper" else "FAIL_EXPECTED"
        print(f"P40_P3_MULTI_MODULE arch={arch} component_go_test=PASS "
              f"integration_old_client={outcome} PASS")
    print("P40_P3_LOCAL_COMPONENT_COMPILE_NOT_CONTEXTUALLY_COMPOSITIONAL_PASS")


if __name__ == "__main__":
    main()
