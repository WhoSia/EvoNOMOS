#!/usr/bin/env bash
set -euo pipefail
PIN="67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
ROOT="$(pwd)"
UP="$ROOT/chi"
OUT="$ROOT/out/p35-p4"
mkdir -p "$OUT/original"
test "$(git -C "$UP" rev-parse HEAD)" = "$PIN"
go version | tee "$OUT/go-version.txt"
printf 'go_chi_pin=%s\n' "$PIN" > "$OUT/upstream.txt"
for name in content_charset.go content_type.go; do cp "$UP/middleware/$name" "$OUT/original/$name"; done
cp tools/p35-p4/tests/acceptance_test.go "$UP/middleware/p35_p4_acceptance_test.go"
set +e
(cd "$UP" && go test -count=1 -run '^TestP35P4CanonicalContentPolicy$' ./middleware) > "$OUT/baseline-negative.log" 2>&1
code=$?
set -e
if [ "$code" -eq 0 ]; then echo 'P35P4_BASELINE_UNEXPECTED_PASS'; exit 21; fi
grep -q 'P35P4_POLICY_FAILURE' "$OUT/baseline-negative.log" || { cat "$OUT/baseline-negative.log"; echo 'BASELINE_WRONG_FAILURE'; exit 22; }
echo 'P35P4_UNMODIFIED_BASELINE_EXPECTED_FAIL=PASS'
for arm in independent shared; do
 cp "$OUT/original/content_charset.go" "$UP/middleware/content_charset.go"
 cp "$OUT/original/content_type.go" "$UP/middleware/content_type.go"
 rm -f "$UP/middleware/content_media_parse.go"
 cp tools/p35-p4/arms/"$arm"/*.go "$UP/middleware/"
 (cd "$UP" && go test -race -count=1 ./middleware) > "$OUT/$arm-middleware-race.log" 2>&1 || { cat "$OUT/$arm-middleware-race.log"; exit 23; }
 (cd "$UP" && go test -count=1 ./...) > "$OUT/$arm-whole-module.log" 2>&1 || { cat "$OUT/$arm-whole-module.log"; exit 24; }
 (cd "$UP" && go test -v -count=1 -run '^TestP35P4CanonicalContentPolicy$' ./middleware) > "$OUT/$arm-acceptance.log" 2>&1 || { cat "$OUT/$arm-acceptance.log"; exit 25; }
 grep -q '^--- PASS: TestP35P4CanonicalContentPolicy' "$OUT/$arm-acceptance.log"
 echo "P35P4_NATIVE_CHI_ARM_PASS=$arm" | tee "$OUT/$arm.verdict"
done
go build -o "$OUT/go_ast" tools/p35-p3/semantic_ast.go
python3 tools/p35-p4/audit.py "$OUT/original" "$OUT/go_ast" > "$OUT/source-rival-audit.json"
python3 - <<'PY'
import json
j=json.load(open("out/p35-p4/source-rival-audit.json"))
assert j["arms"]["independent"]["changed_file_count"]==2
assert j["arms"]["shared"]["changed_file_count"]==3
assert j["rivals"]["B0plus_static_impact"]["recall"]==1
assert j["rivals"]["B2_Parnas_information_hiding"]["recall"]==1
assert j["rivals"]["B1_cochange"]["status"]=="INSUFFICIENT_HISTORY_TO_PREDICT_PAIR"
print("P35P4_FROZEN_RIVALS_AND_ACTUAL_SOURCE_DIFF=PASS")
PY
find tools/p35-p4 -type f -print0 | sort -z | xargs -0 sha256sum > "$OUT/source-sha256.txt"
(cd "$OUT" && sha256sum ./*.log ./*.json ./*.verdict ./*.txt > receipt-sha256.txt)
echo 'P35_P4_ORIGINAL_CHI_BOTH_ARMS_WHOLE_MODULE_AND_RACE_PASS'
