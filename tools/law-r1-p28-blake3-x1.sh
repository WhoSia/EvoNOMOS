#!/usr/bin/env bash
set -euo pipefail

SRC="${1:?BLAKE3 source dir required}"
OUT="${2:?output json required}"
ROOT="$(pwd)"
TMP="${ROOT}/out-p28/blake3-build"
mkdir -p "$TMP"

cat > "$TMP/build_arm.sh" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail
name="$1"
extra="$2"
src="$3"
root="$4"
dir="$root/out-p28/blake3-build/$name"
mkdir -p "$dir"
sources=(
  "$src/c/blake3.c"
  "$src/c/blake3_dispatch.c"
  "$src/c/blake3_portable.c"
  "$src/c/blake3_sse2_x86-64_unix.S"
  "$src/c/blake3_sse41_x86-64_unix.S"
)
if [[ "$name" == "baseline" ]]; then
  sources+=("$src/c/blake3_avx2_x86-64_unix.S")
fi
cc -O2 -I"$src/c" -DBLAKE3_NO_AVX512 $extra   "$root/tools/law-r1-p28-blake3-probe.c" "${sources[@]}" -o "$dir/probe"
"$dir/probe" | tee "$dir/probe.txt"
EOS
chmod +x "$TMP/build_arm.sh"

"$TMP/build_arm.sh" baseline "" "$SRC" "$ROOT"
"$TMP/build_arm.sh" no_avx2 "-DBLAKE3_NO_AVX2" "$SRC" "$ROOT"

baseline_degree="$(sed -n 's/^SIMD_DEGREE=//p' "$TMP/baseline/probe.txt")"
drop_degree="$(sed -n 's/^SIMD_DEGREE=//p' "$TMP/no_avx2/probe.txt")"
baseline_digest="$(sed -n 's/^DIGEST=//p' "$TMP/baseline/probe.txt")"
drop_digest="$(sed -n 's/^DIGEST=//p' "$TMP/no_avx2/probe.txt")"

if [[ "$baseline_degree" != "8" ]]; then
  echo "P28_BLAKE3_BASELINE_AVX2=HOLD degree=$baseline_degree" >&2
  exit 42
fi
if [[ "$drop_degree" -ge 8 ]]; then
  echo "P28_BLAKE3_NO_AVX2_DROP=FAIL degree=$drop_degree" >&2
  exit 43
fi
if [[ "$baseline_digest" != "$drop_digest" ]]; then
  echo "P28_BLAKE3_DIGEST_EQ=FAIL" >&2
  exit 44
fi

(
  cd "$SRC"
  cargo test --features no_avx512 --quiet
) 2>&1 | tee "$ROOT/out-p28/p28-blake3-baseline-tests.txt"
(
  cd "$SRC"
  cargo test --features no_avx512,no_avx2 --quiet
) 2>&1 | tee "$ROOT/out-p28/p28-blake3-no-avx2-tests.txt"

python3 - "$OUT" "$baseline_degree" "$drop_degree" "$baseline_digest" "$drop_digest" <<'PY'
import json,sys
out,bd,dd,bhash,dhash=sys.argv[1:]
obj={
  "candidate":"BLAKE3-team/BLAKE3",
  "source_commit":"f55849f89cd85083c1c9daa2c5de20766f309c00",
  "intervention":"UPSTREAM_DROP_AVX2",
  "baseline":{"q":1,"g":1,"y":1,"simd_degree":int(bd),"digest":bhash},
  "drop":{"q":0,"g":0,"y":1,"simd_degree":int(dd),"digest":dhash},
  "kernel":[-1,-1,0],
  "label":"X1_CROSS_COUPLED_BYPASS_OBSTRUCTION",
  "digest_equal":bhash==dhash,
  "upstream_tests":{"baseline":"PASS","no_avx2":"PASS"},
  "direct_y_intervention":False
}
with open(out,"w") as f:
    json.dump(obj,f,indent=2,sort_keys=True)
print("P28_BLAKE3_X1=PASS")
print("P28_KERNEL=(-1,-1,0)")
print("P28_DIGEST="+bhash)
PY
