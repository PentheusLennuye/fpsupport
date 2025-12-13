#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
HOOKS=${SCRIPT_DIR}/../.git/hooks

if [ -d $HOOKS ]; then
    rm -rf $HOOKS/*
else
    mkdir -p $HOOKS
fi
cp $SCRIPT_DIR/githooks/* $HOOKS
find $HOOKS -type f -exec chmod 0755 {} \;
