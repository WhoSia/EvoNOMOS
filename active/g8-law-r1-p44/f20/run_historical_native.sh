#!/usr/bin/env bash
set -euo pipefail
# RETROSPECTIVE COURT: parent/post original upstream commit, posthoc source oracle.
# This is NOT a sealed future-demand prediction.
case "$COHORT" in
 chi)
  remote="go-chi/chi"
  before="882c15e6462ce0630529d04c330e84942ebd059d"
  after="6ceb498b221efa11f559602beb2463b8b52c2161"
  fixture="chi_nested_find_test.go"
  upstream="^TestMuxFind$"
  ;;
 httprouter)
  remote="julienschmidt/httprouter"
  before="ef8578da8d8e1217ea44313b23edf46154b198ab"
  after="484018016424d215c0b87c42f4c9b57d980fbd00"
  fixture="httprouter_options_test.go"
  upstream="^TestRouterOPTIONS$"
  ;;
 gin)
  remote="gin-gonic/gin"
  before="9d11234efec1e5517b2887a6e7dfbc9c017bc52c"
  after="ea53388e6ee4a6a0a1647b390c56eeed780e7e56"
  fixture="gin_wildcard_panic_test.go"
  upstream="^TestTreeWildcardConflict$"
  ;;
 *) echo "Unknown cohort" >&2; exit 2 ;;
esac

tool_root="$GITHUB_WORKSPACE/active/g8-law-r1-p44/f20"
go version
echo "F20_ORIGINAL_REMOTE=$remote"
for stage in parent post; do
 sha="$before"; if [[ "$stage" == "post" ]]; then sha="$after"; fi
 scratch="$RUNNER_TEMP/f20-$COHORT-$stage"
 mkdir -p "$scratch"
 cd "$scratch"
 git init -q
 git remote add origin "https://github.com/$remote.git"
 git -c protocol.version=2 fetch --quiet --depth=1 origin "$sha"
 git -c advice.detachedHead=false checkout --quiet --detach FETCH_HEAD
 observed="$(git rev-parse HEAD)"
 if [[ "$observed" != "$sha" ]]; then echo "F20_SHA_MISMATCH=$observed" >&2; exit 3; fi
 echo "F20_SOURCE_SHA stage=$stage sha=$observed"
 sha256sum go.mod || true
 export GOWORK=off
 if ! go test -count=1 -run "$upstream" . >"$scratch/upstream.log" 2>&1; then
   cat "$scratch/upstream.log"
   echo "F20_UPSTREAM_BASELINE_FAILURE stage=$stage cohort=$COHORT" >&2
   exit 4
 fi
 cp "$tool_root/oracles/$fixture" "./f20_historical_oracle_test.go"
 set +e
 go test -count=1 -run '^TestF20' -v . >"$scratch/historical.log" 2>&1
 status=$?
 set -e
 cat "$scratch/historical.log"
 if [[ "$stage" == "parent" ]]; then
   if [[ "$status" == "0" ]]; then
     echo "F20_PARENT_UNEXPECTED_PASS: retrospective discriminator did not detect historical issue" >&2
     exit 5
   fi
   if ! grep -q -- '--- FAIL: TestF20' "$scratch/historical.log"; then
     echo "F20_PARENT_COMPILE_OR_ENV_FAIL_NOT_SEMANTIC_EVIDENCE" >&2
     exit 6
   fi
   echo "F20_PARENT_EXPECTED_REGRESSION cohort=$COHORT"
 else
   if [[ "$status" != "0" ]]; then
     echo "F20_POST_EXPECTED_FIX_FAILED cohort=$COHORT" >&2
     exit 7
   fi
   echo "F20_POST_HISTORICAL_ORACLE_PASS cohort=$COHORT"
 fi
done
echo "F20_HISTORICAL_PARENT_POST_REPRO_PASS cohort=$COHORT"
