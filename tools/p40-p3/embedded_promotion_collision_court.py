"""P40-P3 independent Go embedded method-promotion collision court.

Tests original Composite{Fast; Other}.Next() old client, which originally
resolves Other.Next(). Adding Fast.Next() later causes ambiguous selector,
whereas separate versioned wrapper leaves original Fast untouched.

3 architectures × 2 protected-old cases × 8 edit states = 48 Go builds.
"""
from itertools import product
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import os
import subprocess

from architectural_rival_source_court import ARCHES, make_source


def run_case(spec):
    arch, protected, bits = spec
    src, test = make_source(arch, bits, protected)
    src += """
type Other struct{}
func (Other) Next() int {return 99}
type Composite struct {Fast; Other}
func OldComposite(c Composite) int {return c.Next()}
"""
    test += """
func TestOldEmbedded(t *testing.T) {
    if OldComposite(Composite{}) != 99 {
        t.Fatal("original method promotion changed")
    }
}
"""
    with TemporaryDirectory(prefix="evonomos-p40p3-embedded-") as td:
        root = Path(td)
        (root / "go.mod").write_text("module example.org/evonomos/p40p3/embedding\n\ngo 1.22\n")
        (root / "source.go").write_text(src)
        (root / "source_test.go").write_text(test)
        env = dict(os.environ, GOPROXY="off", GOSUMDB="off",
                   GOWORK="off", GOTOOLCHAIN="local")
        proc = subprocess.run(["go", "test", "-count=1", "./..."],
                              cwd=root, env=env, text=True,
                              capture_output=True, timeout=100)
    return spec, proc.returncode == 0, (proc.stdout + proc.stderr)[-1000:]


def main():
    inputs = list(product(ARCHES, (False, True), tuple(product((0, 1), repeat=3))))
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_case, inputs))
    assert len(results) == 48
    for (arch, protected, bits), ok, diag in results:
        T, X, F = bits
        expected = (not (X and arch != "versioned_adapter")
                    and not (arch == "coupled" and T and (not X or protected))
                    and not (F and not (T and X)))
        assert ok == expected, ((arch, protected, bits), ok, diag)
        if arch != "versioned_adapter" and X:
            assert "ambiguous selector c.Next" in diag, diag
    for arch in ARCHES:
        for protected in (False, True):
            states = {bits: ok for (a, p, bits), ok, _ in results
                      if (a, p) == (arch, protected)}
            paths = (int(states[(0, 0, 0)] and states[(1, 0, 0)] and
                         states[(1, 1, 0)] and states[(1, 1, 1)]) +
                     int(states[(0, 0, 0)] and states[(0, 1, 0)] and
                         states[(1, 1, 0)] and states[(1, 1, 1)]))
            expected_states = 5 if arch == "versioned_adapter" else 2 if arch == "direct" else 1
            expected_paths = 2 if arch == "versioned_adapter" else 0
            assert sum(states.values()) == expected_states and paths == expected_paths
            print(f"P40_P3_EMBEDDED_OLD_CLIENT arch={arch} protected={int(protected)} "
                  f"safe_states={sum(states.values())} safe_paths={paths} PASS")
    print("P40_P3_EMBEDDED_METHOD_COLLISION_48_REAL_GO_SOURCE_STATES_PASS")
    print("P40_P3_OFFICIAL_GO_COMPATIBILITY_PRIOR_DEFEATS_CONCRETE_METHOD_ADDITION_LAW")


if __name__ == "__main__":
    main()
