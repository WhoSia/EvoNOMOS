#!/usr/bin/env bash
set -euo pipefail
root="$(pwd)"
up="$root/chi"
out="$root/out/p35-math3-o2"
mkdir -p "$out"
test "$(git -C "$up" rev-parse HEAD)" = "67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
go version | tee "$out/go-version.txt"
cp tools/p35-p7/tests/*.go "$up/middleware/"
cp tools/p35-math2/tests/*.go "$up/middleware/"
cp tools/p35-math2b/tests/*.go "$up/middleware/"
attempted=0
first_pass=0
complete_pass=0
same_both=0
for architecture in live snapshot; do
  for style in inline helper; do
    for order in d9-d10 d10-d9; do
      attempted=$((attempted+1))
      if [[ "$order" == "d9-d10" ]]; then
        first_demand=d9
        stage='^TestP35P7|^TestP35Math2D9'
      else
        first_demand=d10
        stage='^TestP35P7|^TestP35Math2D10CommaDelimitedTokens/second-comma-token-matches'
      fi
      base="$root/tools/p35-math2/arms/$architecture/$style/$first_demand/route_headers.go"
      final="$root/tools/p35-math3/o2/$architecture/$style/$order/route_headers.go"
      existing="$root/tools/p35-math2/arms/$architecture/$style/both/route_headers.go"
      label="$architecture-$style-$order"
      cp "$base" "$up/middleware/route_headers.go"
      (cd "$up" && go test -count=1 -run "$stage" ./middleware) > "$out/$label-first.log" 2>&1 || { cat "$out/$label-first.log"; exit 31; }
      first_pass=$((first_pass+1))
      if cmp -s "$base" "$final"; then echo "NO_SECOND_SOURCE_CHANGE" >&2; exit 32; fi
      diff -u "$base" "$final" > "$out/$label-first-to-second.patch" || [[ "$?" -eq 1 ]]
      sha256sum "$base" "$final" "$existing" > "$out/$label-sources-sha256.txt"
      if cmp -s "$final" "$existing"; then
        same_both=$((same_both+1))
        echo 'POSTCONFLICT_ENDPOINT_EQUALS_PRIOR_CANONICAL_BOTH__NO_INDEPENDENT_REPLICATION_CLAIM' > "$out/$label-byte-relation.txt"
      else
        echo 'POSTCONFLICT_ENDPOINT_DIFFERS_FROM_PRIOR_CANONICAL_BOTH' > "$out/$label-byte-relation.txt"
      fi
      cp "$final" "$up/middleware/route_headers.go"
      (cd "$up" && go vet ./middleware && go test -race -count=1 ./middleware && go test -count=1 ./...) > "$out/$label-native.log" 2>&1 || { cat "$out/$label-native.log"; exit 33; }
      complete_pass=$((complete_pass+1))
      echo "P35_MATH3_O2_${label}_TWO_STAGE_GO_NATIVE_PASS" | tee "$out/$label.verdict"
    done
  done
done
printf 'PATHS=%s\nFIRST_STAGE_NATIVE_PASS=%s\nSECOND_STAGE_NATIVE_PASS=%s\nENDPOINTS_EQUAL_PRIOR_BOTH=%s\n' "$attempted" "$first_pass" "$complete_pass" "$same_both" | tee "$out/summary.txt"
test "$attempted" -eq 8 && test "$first_pass" -eq 8 && test "$complete_pass" -eq 8 || exit 34
echo 'P35_MATH3_O2_EIGHT_ACTUAL_GO_SEQUENTIAL_SOURCE_REPAIRS_PASS__FINITE_WITNESSES_ONLY' | tee "$out/classification.txt"
