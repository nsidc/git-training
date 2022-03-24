#!/bin/bash
#
# Build the docs!
set -euo pipefail

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
DOCS_DIR="$(realpath "$THIS_DIR/../doc")"
VENV_DIR="/tmp/venv-git-training"


# This is pretty fast and "almost idempotent" (if you already have an
# environment, it will succeed, but the new environment could have different
# dependency versions). TODO: Figure out a clean way to skip this step if an
# environment exists. What if we change the requirements.txt and want to force
# recreation of the env?
virtualenv "$VENV_DIR"
echo "virtual environment is at $VENV_DIR."
. "$VENV_DIR/bin/activate"
pip install -r "$DOCS_DIR/requirements.txt"

cd $DOCS_DIR
make clean && make html

echo "Docs built in $DOCS_DIR."
