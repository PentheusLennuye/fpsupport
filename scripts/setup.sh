#!/usr/bin/env bash
#
# File: setup.sh
#
# Install workstation development

HOOKS_SOURCE_DIR=scripts/githooks
GITHOOKS_DIR=.git/hooks

echo "Installing poetry packages"
_=$(which poetry) || (
    echo "poetry not installed on this workstation. Install pipx and poetry, "
    echo "then try again."
    exit 1
)
poetry install

echo "Setting up git hooks"
if [ -d $GITHOOKS_DIR ]; then
    rm -f $GITHOOKS_DIR/*
else
    mkdir -p $GITHOOKS_DIR
fi

find $HOOKS_SOURCE_DIR -type f -exec cp {} $GITHOOKS_DIR \;
