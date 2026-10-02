#!/usr/bin/env bash
set -euo pipefail

mode=${1:-core}

if [[ "$mode" != "core" && "$mode" != "webshop" ]]; then
  printf 'Usage: %s [core|webshop]\n' "$0" >&2
  exit 2
fi

git submodule update --init --recursive
python -m pip install --upgrade pip setuptools wheel
python -m pip install torch==2.5.0
python -m pip install flash-attn==2.7.4.post1 --no-build-isolation
python -m pip install -r requirements.txt
python -m pip install -e verl --no-dependencies

if [[ "$mode" == "webshop" ]]; then
  python -m pip install -e ".[webshop]"
  python -m pip install -e external/webshop-minimal --no-dependencies
  python -m spacy download en_core_web_sm
else
  python -m pip install -e .
fi
