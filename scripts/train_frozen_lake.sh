#!/usr/bin/env bash
set -euo pipefail

python train.py --config-name frozen_lake "$@"
