#!/bin/bash
#
# Build the docs every time a change is made. Currently only compatible with
# Linux. PRs accepted from OSX/Windows users :D
set -euo pipefail

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
DOCS_DIR="$(realpath "$THIS_DIR/../doc")"

cd $DOCS_DIR

# NOTE: If `-e delete` or `-e create` event triggers are used with inotifywait,
# the build may be triggered too frequently, e.g. when VIM .swp files are
# created and deleted.
while inotifywait -e close_write --recursive $DOCS_DIR; do
    # Allow build to fail without crashing this script
    set +e
    $THIS_DIR/build_docs.sh
    set -e
done
