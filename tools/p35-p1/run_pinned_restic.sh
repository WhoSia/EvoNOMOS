#!/usr/bin/env bash
# P35-P2: exact original Restic module, source-only user-authored treatments.
# Run from the EvoNOMOS repository root after checkout of pinned Restic.
set -euo pipefail

PIN="495982232cf1af184eac0a97871ef8161e8708ee"
ORIGIN="$(pwd)"
UPSTREAM="${P35_UPSTREAM_DIR:-$ORIGIN/restic}"
OUT="${P35_OUT_DIR:-$ORIGIN/out/p35-real-restic}"
mkdir -p "$OUT"
cd "$UPSTREAM"
HEAD="$(git rev-parse HEAD)"
if [[ "$HEAD" != "$PIN" ]]; then
  echo "RESTIC_PIN_MISMATCH expected=$PIN actual=$HEAD" >&2
  exit 42
fi
go version | tee "$OUT/go-version.txt"
printf 'restic_commit=%s\n' "$HEAD" | tee "$OUT/upstream.txt"

TARGET="internal/backend/p35pair"
for world in baseline u-local c-local u-encoded c-encoded c-encoded-instore c-encoded-tagged c-encoded-compact; do
  rm -rf "$TARGET"
  mkdir -p "$TARGET"
  cp "$ORIGIN/tools/p35-p1/worlds/$world/"*.go "$TARGET/"
  cp "$ORIGIN/tools/p35-p1/tests/backend_test.go" "$TARGET/"
  cp "$ORIGIN/tools/p35-p1/tests/p34_public_oracle_test.go" "$TARGET/"
  if [[ "$world" == c-encoded-tagged || "$world" == c-encoded-compact ]]; then
    cp "$ORIGIN/tools/p35-p1/tests/demand_tagged_test.go" "$TARGET/demand_test.go"
  else
    cp "$ORIGIN/tools/p35-p1/tests/demand_test.go" "$TARGET/"
  fi
  echo "BEGIN_ACTUAL_RESTIC $world"
  arm=c
  [[ "$world" == baseline || "$world" == u-* ]] && arm=u
  pattern='^TestP35(PairedContract|DistinctPhysicalStores|P1P34BehavioralRegression)$'
  expected="NONE"
  if [[ "$world" == u-local || "$world" == c-local ]]; then
    pattern='^TestP35(PairedContract|DistinctPhysicalStores|P1P34BehavioralRegression|P1LocalKeyFile)$'
    expected='P35_LOCAL_BOUNDED_SOURCE_RULE=PASS'
  elif [[ "$world" == *-encoded* ]]; then
    pattern='^TestP35(PairedContract|DistinctPhysicalStores|P1P34BehavioralRegression|P1VersionedStorage)$'
    expected='P35_VERSIONED_REPRESENTATION_AND_LEGACY_COLLISION=PASS'
  fi
  if ! (P35_ARM="$arm" go vet "./$TARGET" && P35_ARM="$arm" go test -race -count=1 -v -run "$pattern" "./$TARGET") >"$OUT/$world.log" 2>&1; then
    cat "$OUT/$world.log"
    echo "PINNED_RESTIC_FAIL $world" >&2
    exit 43
  fi
  cat "$OUT/$world.log"
  grep -q 'P34_PUBLIC_HISTORY_18_OF_18=PASS' "$OUT/$world.log" || { echo "P34_REGRESSION_MISSING $world" >&2; exit 44; }
  grep -q 'P35_P0_PUBLIC_TRACE_EQUAL PASS' "$OUT/$world.log" || { echo "PAIRED_BEHAVIOR_MISSING $world" >&2; exit 45; }
  if [[ "$expected" != NONE ]]; then
    grep -q "$expected" "$OUT/$world.log" || { echo "DEMAND_ORACLE_MISSING $world" >&2; exit 46; }
  fi
  echo "PINNED_RESTIC_PASS $world" | tee "$OUT/$world.verdict"
done

# Untouched baseline MUST fail each newly introduced requirement with expected reason.
rm -rf "$TARGET"
mkdir -p "$TARGET"
cp "$ORIGIN/tools/p35-p1/worlds/baseline/backend.go" "$TARGET/"
cp "$ORIGIN/tools/p35-p1/tests/"{backend_test.go,p34_public_oracle_test.go,demand_test.go} "$TARGET/"
for requirement in LocalKeyFile VersionedStorage; do
  set +e
  P35_ARM=u go test -count=1 -run "^TestP35P1${requirement}$" "./$TARGET" >"$OUT/baseline-negative-$requirement.log" 2>&1
  ec=$?
  set -e
  if [[ "$ec" -eq 0 ]]; then
    echo "NEGATIVE_CONTROL_UNEXPECTED_PASS $requirement" >&2
    exit 47
  fi
  case "$requirement" in
    LocalKeyFile) expected='must reject >8 KeyFile' ;;
    VersionedStorage) expected='storage is not tagged encoded' ;;
  esac
  grep -q "$expected" "$OUT/baseline-negative-$requirement.log" || { echo "WRONG_NEGATIVE_REASON $requirement"; cat "$OUT/baseline-negative-$requirement.log"; exit 48; }
  echo "EXPECTED_BASELINE_FAIL $requirement"
done

# A behaviorally compatible implementation can still violate the frozen capability design.
# Explicitly report (do not secretly treat as architecture-fixed controls).
cat > "$OUT/architecture-admissibility.tsv" <<'EOF'
world	independent_read_decoder	classification
baseline	true	P0
u-local	true	U_LOCAL
c-local	true	C_LOCAL
u-encoded	true	U_ENCODED
c-encoded	true	C_ENCODED
c-encoded-tagged	true	C_ENCODED_P35_FIXED
c-encoded-instore	false	EXPLORATORY_READ_DECODER_RELOCATED
c-encoded-compact	false	EXPLORATORY_READ_DECODER_RELOCATED
EOF
(cd "$ORIGIN" && find tools/p35-p1/worlds tools/p35-p1/tests -type f -print0 | sort -z | xargs -0 sha256sum) > "$OUT/source-sha256.txt"
(cd "$OUT" && sha256sum ./*.log ./*.verdict ./*.tsv ./*.txt > run-sha256.txt)
echo "P35_PINNED_RESTIC_EIGHT_WORLDS_AND_TWO_NEGATIVE_CONTROLS_PASS__ARCHITECTURE_BOUNDARY_RECORDED"
