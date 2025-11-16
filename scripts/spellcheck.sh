#!/usr/bin/env bash
#
# spellcheck.sh is a shortcut to check the spelling of a document against more
# than one dictionary.
#
# It depends on [hunspell](https://hunspell.github.io) being installed.
#
# Usage: spellcheck.sh <file>
#
#
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
DICTIONARIES=$SCRIPT_DIR/dictionaries

which hunspell >/dev/null || (
    echo "hunspell is not installed"
    exit 1
)

hunspell -d $DICTIONARIES/en_CA,$DICTIONARIES/controlled $1

