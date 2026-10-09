#!/usr/bin/env bash
set -euo pipefail
root="$(pwd)"
out="$root/out/p35-math3-order"
mkdir -p "$out"
test "$(git -C chi rev-parse HEAD)" = "67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
go version | tee "$out/go-version.txt"
git --version | tee "$out/git-version.txt"
cp tools/p35-p7/tests/*.go chi/middleware/
cp tools/p35-math2/tests/*.go chi/middleware/
cp tools/p35-math2b/tests/*.go chi/middleware/
attempted=0
clean=0
conflicted=0
native=0
for architecture in live snapshot; do
  base="$root/tools/p35-p7/d8/$architecture/route_headers.go"
  for style in inline helper; do
    prefix="$root/tools/p35-math2/arms/$architecture/$style"
    for order in d9-d10 d10-d9; do
      attempted=$((attempted+1))
      if [[ "$order" == "d9-d10" ]]; then
        first="$prefix/d9/route_headers.go"
        second="$prefix/d10/route_headers.go"
        demand="D9"
      else
        first="$prefix/d10/route_headers.go"
        second="$prefix/d9/route_headers.go"
        demand="D10"
      fi
      p="$out/$architecture-$style-$order"
      cp "$first" chi/middleware/route_headers.go
      if [[ "$demand" == "D9" ]]; then
        stage='^TestP35P7|^TestP35Math2D9'
      else
        stage="^TestP35P7|^TestP35Math2D10CommaDelimitedTokens/second-comma-token-matches"
      fi
      (cd chi && go test -count=1 -run "$stage" ./middleware) > "$p-first-demand.log" 2>&1 || { cat "$p-first-demand.log"; echo "STAGE_FAIL" > "$p.verdict"; exit 31; }
      sha256sum "$base" "$first" "$second" > "$p-input-sha256.txt"
      set +e
      git merge-file -p "$first" "$base" "$second" > "$p-source.go" 2> "$p-merge.log"
      code=$?
      set -e
      # git merge-file returns the count of conflict regions (up to 127).
      # A status >1 is NOT necessarily a tool crash. Classify from markers.
      if [[ "$code" -ne 0 ]] && grep -q '^<<<<<<< ' "$p-source.go"; then
        conflicted=$((conflicted+1))
        printf 'PATCH_REPLAY_CONFLICT_HOLD: %s/%s/%s (noncommutation NOT inferred)\n' "$architecture" "$style" "$order" | tee "$p.verdict"
        continue
      fi
      if [[ "$code" -ne 0 ]]; then
        cat "$p-merge.log"
        echo "MERGE_TOOL_FAILURE_WITHOUT_CONFLICT_MARKERS" > "$p.verdict"
        exit 32
      fi
      clean=$((clean+1))
      cp "$p-source.go" chi/middleware/route_headers.go
      if (cd chi && go vet ./middleware && go test -race -count=1 ./middleware && go test -count=1 ./... ) > "$p-native.log" 2>&1; then
        native=$((native+1))
        sha256sum "$p-source.go" > "$p-merged-sha256.txt"
        echo "CLEAN_MERGE_NATIVE_FULL_PASS: $architecture/$style/$order" | tee "$p.verdict"
      else
        echo "CLEAN_MERGE_SEMANTIC_OR_COMPILE_HOLD: $architecture/$style/$order" | tee "$p.verdict"
        tail -n 65 "$p-native.log"
      fi
    done
    f="$out/$architecture-$style"
    if [[ -f "$f-d9-d10-merged-sha256.txt" && -f "$f-d10-d9-merged-sha256.txt" ]]; then
      if cmp -s "$f-d9-d10-source.go" "$f-d10-d9-source.go"; then
        echo 'SELECTED_TWO_ORDER_SOURCE_BYTES_EQUAL' > "$f-order-compare.txt"
      else
        echo 'SELECTED_TWO_ORDER_SOURCE_BYTES_DIFFER (semantics require separate checks)' > "$f-order-compare.txt"
      fi
    else
      echo 'SELECTED_TWO_ORDER_COMPARISON_HOLD: at least one route not natively verified' > "$f-order-compare.txt"
    fi
  done
done
printf 'ATTEMPTED=%s\nCLEAN_MERGES=%s\nTEXTUAL_CONFLICTS=%s\nNATIVE_FULL_PASS=%s\n' "$attempted" "$clean" "$conflicted" "$native" | tee "$out/summary.txt"
[[ "$attempted" -eq 8 ]] || exit 40
# A classification PASS does NOT mean scientific commutation was proven.
echo 'P35_MATH3_EIGHT_SELECTED_SOURCE_ORDER_REPLAYS_CLASSIFIED' | tee "$out/classification.txt"

      fi
      (cd chi && go test -count=1 -run "$stage" ./middleware) > "$p-first-demand.log" 2>&1 || { cat "$p-first-demand.log"; echo "STAGE_FAIL" > "$p.verdict"; exit 31; }
      sha256sum "$base" "$first" "$second" > "$p-input-sha256.txt"
      set +e
      git merge-file -p "$first" "$base" "$second" > "$p-source.go" 2> "$p-merge.log"
      code=$?
      set -e
      # git merge-file returns the count of conflict regions (up to 127).
      # A status >1 is NOT necessarily a tool crash. Classify from markers.
      if [[ "$code" -ne 0 ]] && grep -q '^<<<<<<< ' "$p-source.go"; then
        conflicted=$((conflicted+1))
        printf 'PATCH_REPLAY_CONFLICT_HOLD: %s/%s/%s (noncommutation NOT inferred)\n' "$architecture" "$style" "$order" | tee "$p.verdict"
        continue
      fi
      if [[ "$code" -ne 0 ]]; then
        cat "$p-merge.log"
        echo "MERGE_TOOL_FAILURE_WITHOUT_CONFLICT_MARKERS" > "$p.verdict"
        exit 32
      fi
      clean=$((clean+1))
      cp "$p-source.go" chi/middleware/route_headers.go
      if (cd chi && go vet ./middleware && go test -race -count=1 ./middleware && go test -count=1 ./... ) > "$p-native.log" 2>&1; then
        native=$((native+1))
        sha256sum "$p-source.go" > "$p-merged-sha256.txt"
        echo "CLEAN_MERGE_NATIVE_FULL_PASS: $architecture/$style/$order" | tee "$p.verdict"
      else
        echo "CLEAN_MERGE_SEMANTIC_OR_COMPILE_HOLD: $architecture/$style/$order" | tee "$p.verdict"
        tail -n 65 "$p-native.log"
      fi
    done
    f="$out/$architecture-$style"
    if [[ -f "$f-d9-d10-merged-sha256.txt" && -f "$f-d10-d9-merged-sha256.txt" ]]; then
      if cmp -s "$f-d9-d10-source.go" "$f-d10-d9-source.go"; then
        echo 'SELECTED_TWO_ORDER_SOURCE_BYTES_EQUAL' > "$f-order-compare.txt"
      else
        echo 'SELECTED_TWO_ORDER_SOURCE_BYTES_DIFFER (semantics require separate checks)' > "$f-order-compare.txt"
      fi
    else
      echo 'SELECTED_TWO_ORDER_COMPARISON_HOLD: at least one route not natively verified' > "$f-order-compare.txt"
    fi
  done
done
printf 'ATTEMPTED=%s\nCLEAN_MERGES=%s\nTEXTUAL_CONFLICTS=%s\nNATIVE_FULL_PASS=%s\n' "$attempted" "$clean" "$conflicted" "$native" | tee "$out/summary.txt"
[[ "$attempted" -eq 8 ]] || exit 40
# A classification PASS does NOT mean scientific commutation was proven.
echo 'P35_MATH3_EIGHT_SELECTED_SOURCE_ORDER_REPLAYS_CLASSIFIED' | tee "$out/classification.txt"
