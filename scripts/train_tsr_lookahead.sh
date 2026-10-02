#!/usr/bin/env bash
set -euo pipefail

environment="${1:-sokoban}"
if (( $# > 0 )); then
  shift
fi

case "$environment" in
  sokoban|frozen_lake) ;;
  *)
    echo "Usage: $0 {sokoban|frozen_lake} [Hydra overrides...]" >&2
    exit 2
    ;;
esac

python train.py --config-name "tsr_lookahead_${environment}" "$@"
