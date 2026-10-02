#!/usr/bin/env bash
set -euo pipefail

environment="${1:-sokoban}"
if (( $# > 0 )); then
  shift
fi

case "$environment" in
  sokoban|frozen_lake|webshop) ;;
  *)
    echo "Usage: $0 {sokoban|frozen_lake|webshop} [Hydra overrides...]" >&2
    exit 2
    ;;
esac

python train.py --config-name "tsr_beam_search_${environment}" "$@"
