#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

export PYTHONPATH="$PWD"

uvicorn src.api:app --reload
