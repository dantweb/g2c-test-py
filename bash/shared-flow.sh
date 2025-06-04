#!/bin/bash

# SSH and Git Configuration Utility

# Logging function
log() {
    local log_file="/tmp/pipeline.log"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$log_file" >&2
}

# Verify SSH key
verify_ssh_key() {
    local ssh_key_paths=(
        "$HOME/.ssh/id_rsa"
        "/home/appuser/.ssh/id_rsa"
        "/app/var/users/1/loops/83/filesystem/id_rsa"
        "/root/.ssh/id_rsa"
        "/ssh/id_rsa"
    )

    for key_path in "${ssh_key_paths[@]}"; do
        if [ -f "$key_path" ] && [ -r "$key_path" ]; then
            export GIT_SSH_COMMAND="ssh -i $key_path -o StrictHostKeyChecking=no"
            log "Using SSH key: $key_path"
            return 0
        fi
    done

    log "ERROR: No readable SSH key found"
    return 1
}

# Configure git environment
prepare_git_environment() {
    # Use appuser context
    git config --global user.email "appuser@loopai.io"
    git config --global user.name "LoopAI Pipeline"

    # Add safe directory if needed
    git config --global --add safe.directory "*"

    # Verify SSH key
    verify_ssh_key
}