#!/usr/bin/env bash
# Run manually. No CI workflow or bot commit is created.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if ! command -v lean >/dev/null 2>&1; then
  echo "BLOCKED: Lean compiler unavailable" >&2
  exit 127
fi
version="$(lean --version)"
printf '%s\n' "$version"
if [[ "$version" != *"version 4.19.0,"* ]]; then
  echo "BLOCKED: expected pinned Lean 4.19.0" >&2
  exit 1
fi
for f in PathCertificate.lean InformationCertificate.lean DiagonalCover.lean; do
  output="$(lean "$f" 2>&1)" || { printf '%s\n' "$output"; exit 1; }
  printf '%s\n' "$output"
  if grep -Eq 'sorryAx|declaration uses .sorry.|^[[:space:]]*error:' <<< "$output"; then
    echo "FAIL: proof admission or error in $f" >&2
    exit 1
  fi
done
echo "PASS_R92_LEAN_KERNEL_CHECKS"
