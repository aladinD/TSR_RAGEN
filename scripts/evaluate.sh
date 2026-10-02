#!/usr/bin/env bash
set -euo pipefail

environment=${1:?Usage: scripts/evaluate.sh {sokoban|frozen_lake|webshop} [Hydra overrides...]}
shift

case "$environment" in
  sokoban|frozen_lake|webshop) ;;
  *)
    printf 'Unknown environment: %s\n' "$environment" >&2
    exit 2
    ;;
esac

python -m ragen.llm_agent.agent_proxy --config-name "eval_${environment}" "$@"
