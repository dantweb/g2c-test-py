#!/bin/bash

# Source shared flow
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$SCRIPT_DIR/shared-flow.sh"

# Configuration
REPO_URL="git@github.com:dantweb/g2c-test-py.git"
REPO_BRANCH="${PIPELINE_BRANCH:-feature/loopai-g2c-test}"
REPO_DIR="${REPO_DIR:-/var/users/1/loops/83/filesystem/_generated/g2c-test-py}"

main() {
    # Prepare git environment
    prepare_git_environment

    # Ensure directory exists without requiring write permissions
    [ -d "$REPO_DIR" ] || mkdir -p "$REPO_DIR"

    # Change to repository directory
    cd "$REPO_DIR"

    # Force pull the specific branch
    git init
    git remote add origin "$REPO_URL" 2>/dev/null || true
    git fetch origin "$REPO_BRANCH" --force
    git checkout "$REPO_BRANCH"
    git reset --hard "origin/$REPO_BRANCH"

    log "Repository forcefully updated to latest $REPO_BRANCH"
}

main "$@"