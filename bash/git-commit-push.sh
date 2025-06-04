#!/bin/bash

# Source shared flow
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$SCRIPT_DIR/shared-flow.sh"

# Configuration
REPO_URL="git@github.com:dantweb/g2c-test-py.git"
REPO_BRANCH="${PIPELINE_BRANCH:-feature/loopai-g2c-test}"
REPO_DIR="${REPO_DIR:-/app/var/users/1/loops/83/filesystem/g2c-test-py}"



main() {
    # Prepare git environment
    prepare_git_environment

    # Change to repository directory
    cd "$REPO_DIR"

    # Create commit message with timestamp
    COMMIT_MESSAGE="Automated pipeline commit: $(date '+%Y-%m-%d %H:%M:%S')"

    # Check for changes
    if ! git diff-index --quiet HEAD --; then
        git add .
        git commit -m "$COMMIT_MESSAGE"
        git push origin "$REPO_BRANCH"
        log "Committed and pushed changes: $COMMIT_MESSAGE"
    else
        log "No changes to commit"
    fi
}

main "$@"