#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

export PYTHONPATH="$PWD"

streamlit run src/ui_demo.py
