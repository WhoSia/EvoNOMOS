#!/usr/bin/env bash
set -euo pipefail
ROOT="$(pwd)"
UP="$ROOT/chi"
OUT="$ROOT/out/p35-p4b"
PIN="67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
mkdir -p "$OUT/original"
test "$(git -C "$UP" rev-parse HEAD)" = "$PIN"
go version | tee "$OUT/go-version.txt"
echo "$PIN" > "$OUT/upstream-sha.txt"
for name in content_charset.go content_type.go; do cp "$UP/middleware/$name" "$OUT/original/$name"; done
cp tools/p35-p4/tests/acceptance_test.go "$UP/middleware/p35_p4_acceptance_test.go"
cp tools/p35-p4b/tests/second_demand_test.go "$UP/middleware/p35_p4b_second_demand_test.go"
for arm in independent shared; do
 cp "$OUT/original/content_charset.go" "$UP/middleware/content_charset.go"
 cp "$OUT/original/content_type.go" "$UP/middleware/content_type.go"
 rm -f "$UP/middleware/content_media_parse.go"
 cp tools/p35-p4/arms/"$arm"/*.go "$UP/middleware/"
 # D4 treatment must satisfy original D4 acceptance, and fail D5 at specified boundary.
 (cd "$UP" && go test -count=1 -run '^TestP35P4CanonicalContentPolicy$' ./middleware) > "$OUT/$arm-D4-precondition.log" 2>&1 || {cat "$OUT/$arm-D4-precondition.log";exit 20;}
 set +e
 (cd "$UP" && go test -count=1 -run '^TestP35P4BHeaderLengthBudget$' ./middleware) > "$OUT/$arm-D5-negative.log" 2>&1
 rc=$?
 set -e
 if [[ "$rc" == 0 ]];then echo "P35P4B_UNEXPECTED_BASELINE_PASS $arm";exit 21;fi
 grep -q 'P35P4B_LENGTH_BUDGET_FAILURE' "$OUT/$arm-D5-negative.log" || {cat "$OUT/$arm-D5-negative.log";exit 22;}
 echo "P35P4B_D4_ARM_EXPECTED_D5_FAIL=$arm"
 # No unsealed test modifications: same exact D4 + D5 frozen oracles.
 cp "$OUT/original/content_charset.go" "$UP/middleware/content_charset.go"
 cp "$OUT/original/content_type.go" "$UP/middleware/content_type.go"
 rm -f "$UP/middleware/content_media_parse.go"
 cp tools/p35-p4b/arms/"$arm"/*.go "$UP/middleware/"
 (cd "$UP" && go test -race -count=1 ./middleware) > "$OUT/$arm-race.log" 2>&1 || {cat "$OUT/$arm-race.log";exit 23;}
 (cd "$UP" && go test -count=1 ./...) > "$OUT/$arm-entire-repo.log" 2>&1 || {cat "$OUT/$arm-entire-repo.log";exit 24;}
 (cd "$UP" && go test -v -count=1 -run '^TestP35P4(CanonicalContentPolicy|BHeaderLengthBudget)$' ./middleware) > "$OUT/$arm-two-demands.log" 2>&1 || {cat "$OUT/$arm-two-demands.log";exit 25;}
 grep -q '^--- PASS: TestP35P4CanonicalContentPolicy' "$OUT/$arm-two-demands.log"
 grep -q '^--- PASS: TestP35P4BHeaderLengthBudget' "$OUT/$arm-two-demands.log"
 echo "P35P4B_NATIVE_CHI_D5_PASS=$arm" | tee "$OUT/$arm.verdict"
done
go build -o "$OUT/semantic_ast" tools/p35-p3/semantic_ast.go
python3 tools/p35-p4b/audit.py "$OUT/semantic_ast" > "$OUT/incremental-audit.json"
python3 - <<'PY'
import json
j=json.load(open("out/p35-p4b/incremental-audit.json"))
assert j["incremental"]["independent"]["changed_files"]==2
assert j["incremental"]["shared"]["changed_files"]==1
assert j["comparison"]["sign_reversal_in_incremental_edit_count"] is True
assert j["comparison"]["overall_lifecycle_winner"]=="NOT_IDENTIFIED"
print("P35P4B_PRESEALED_INCREMENTAL_SIGN_REVERSAL=PASS")
PY
find tools/p35-p4b -type f -print0 | sort -z | xargs -0 sha256sum > "$OUT/source-sha256.txt"
(cd "$OUT" && sha256sum ./*.log ./*.json ./*.txt ./*.verdict > artifact-sha256.txt)
echo "P35P4B_NATIVE_ORIGINAL_CHI_D4_AND_D5_PASS"
