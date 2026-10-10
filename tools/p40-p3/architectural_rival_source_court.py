"""P40-P3: actual Go source-edit architecture rivals, no external dependencies.
48 source-state builds plus 6 terminal nominal-contract tests: 54 go test runs.
Source edit events T: public contract; X: direct method OR new wrapper;
F: new client factory. Owner edit rights are tested separately in the model.
"""
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from pathlib import Path
from tempfile import TemporaryDirectory
import os
import subprocess

ARCHES = ("coupled", "direct", "versioned_adapter")


def make_source(arch, bits, protected, nominal=False):
    T, X, F = bits
    assert arch in ARCHES
    baseline = """package court
type Port interface { Run() int }
type Fast struct{}
func (Fast) Run() int {return 7}
type Legacy struct{}
func (Legacy) Run() int {return 9}
func Old(p Port) int {return p.Run()}
var _ Port = Fast{}
"""
    if arch == "coupled":
        baseline = """package court
type Port interface { Run() int%s }
type Fast struct{}
func (Fast) Run() int {return 7}
type Legacy struct{}
func (Legacy) Run() int {return 9}
func Old(p Port) int {return p.Run()}
var _ Port = Fast{}
""" % ("; Next() int" if T else "")
    src = baseline
    if protected:
        src += "var _ Port = Legacy{}\n"
    if T:
        if arch == "coupled":
            src += "type Advanced = Port\n"
        elif arch == "direct":
            src += "type Advanced interface { Port; Next() int }\n"
        else:
            src += "type PortV2 interface {Port; Next() int}\ntype Advanced = PortV2\n"
    if X:
        if arch == "versioned_adapter":
            src += "type FastAdapter struct {Fast}\nfunc (FastAdapter) Next() int {return 42}\n"
        else:
            src += "func (Fast) Next() int {return 42}\n"
    if F:
        val = "FastAdapter{Fast{}}" if arch == "versioned_adapter" else "Fast{}"
        src += f"func OpenAdvanced() Advanced {{return {val}}}\n"
        src += "func New(p Advanced) int {return p.Run()+p.Next()}\n"
    tst = """package court
import "testing"
func TestOld(t *testing.T) {if Old(Fast{}) != 7 {t.Fatal("Fast old contract")}}
"""
    if protected:
        tst += 'func TestLegacy(t *testing.T) {if Old(Legacy{}) != 9 {t.Fatal("protected Legacy")}}\n'
    if T and X and F:
        tst += """func TestFutureStructural(t *testing.T) {
    got:=OpenAdvanced()
    if got.Run()!=7 || got.Next()!=42 || New(got)!=49 {
        t.Fatal("future structural contract")
    }
}
"""
    if nominal and T and X and F:
        tst += """func TestConcreteFast(t *testing.T) {
    if _,ok:=any(OpenAdvanced()).(Fast); !ok {
        t.Fatal("future client requires concrete Fast identity")
    }
}
"""
    return src, tst


def run_go(spec):
    arch, protected, bits, nominal = spec
    with TemporaryDirectory(prefix="evonomos-p40p3-") as td:
        root = Path(td)
        (root / "go.mod").write_text("module example.org/evonomos/p40p3\n\ngo 1.22\n")
        src, test = make_source(arch, bits, protected, nominal)
        (root / "court.go").write_text(src)
        (root / "court_test.go").write_text(test)
        env = dict(os.environ, GOPROXY="off", GOSUMDB="off", GOWORK="off", GOTOOLCHAIN="local")
        proc = subprocess.run(["go", "test", "-count=1", "./..."], cwd=root,
                              text=True, capture_output=True, timeout=100, env=env)
        return spec, proc.returncode == 0, (proc.stdout + proc.stderr)[-1200:]


def expected(arch, protected, bits):
    T, X, F = bits
    if arch == "coupled" and T and (not X or protected):
        return False
    if F and not (T and X):
        return False
    return True


def main():
    # 3 architectures × 2 protected-old cases × 2^3 source edit states
    inputs = [(a, p, b, False) for a, p, b in
              product(ARCHES, (False, True), tuple(product((0, 1), repeat=3)))]
    # Extra terminal-client type-identity contract, tested in the Go runtime
    inputs += [(a, p, (1, 1, 1), True) for a, p in product(ARCHES, (False, True))]
    assert len(inputs) == 54
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_go, inputs))
    for (a, p, b, nominal), ok, diagnostic in results:
        target = expected(a, p, b) and not (nominal and a == "versioned_adapter")
        assert ok == target, ((a, p, b, nominal), ok, diagnostic)
        if not ok:
            assert any(t in diagnostic for t in
                       ("undefined: Advanced", "undefined: FastAdapter",
                        "does not implement Port", "does not implement Advanced",
                        "missing method Next", "requires concrete Fast identity")), diagnostic
    print("P40_P3_REAL_GO_COMPILER_REVISION_COURT cases=54 all_expected_pass=54 PASS")
    for arch in ARCHES:
        for protected in (False, True):
            states = {b: ok for ((a, p, b, nominal), ok, _) in results
                      if (a, p) == (arch, protected) and not nominal}
            paths = (int(states[(0, 0, 0)] and states[(1, 0, 0)] and
                         states[(1, 1, 0)] and states[(1, 1, 1)]) +
                     int(states[(0, 0, 0)] and states[(0, 1, 0)] and
                         states[(1, 1, 0)] and states[(1, 1, 1)]))
            expected_paths = 0 if arch == "coupled" and protected else (1 if arch == "coupled" else 2)
            expected_states = 2 if arch == "coupled" and protected else (4 if arch == "coupled" else 5)
            assert paths == expected_paths and sum(states.values()) == expected_states
            print(f"P40_P3_STATE_CUBE arch={arch} protected={int(protected)} "
                  f"safe_states={sum(states.values())} sequential_safe_paths={paths} PASS")
    for arch in ARCHES:
        cases = {p: ok for ((a, p, b, nominal), ok, _) in results
                 if a == arch and b == (1, 1, 1) and nominal}
        expected_cases = ({False: True, True: False} if arch == "coupled" else
                          {False: False, True: False} if arch == "versioned_adapter" else
                          {False: True, True: True})
        assert cases == expected_cases
        print(f"P40_P3_GO_DYNAMIC_TYPE_CONTRACT arch={arch} identity_results={cases} PASS")
    print("P40_P3_REAL_GO_COMPILATION_REPRODUCIBLE_AND_CLASSICAL_PRIOR_PASS")


if __name__ == "__main__":
    main()
