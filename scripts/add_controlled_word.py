#!/usr/bin/env python
"""Add a word to the sap_gcid_cep_controlled dictionary.

The "controlled" dictionary adds abbreviations, proper names, and
other technically-focused vocabulary to the dictionaries against which
spell-checks are conducted.

Spell Checking is through Hunspell.

Usage: add_controlled_word.py <word>
"""

import bisect
import os
import sys

# Edit as required -------------------------------------------------
SCRIPTS = os.path.dirname(os.path.realpath(__file__))
DICTIONARY=os.path.join(SCRIPTS, "dictionaries", "controlled.dic")
# ------------------------------------------------------


# pylint: disable=broad-exception-caught


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <word>")

try:
    with open(DICTIONARY, "r", encoding="utf-8") as fp:
        dictionary = fp.readlines()[1:]  # First line is the word count
except Exception as e: #
    print(f"failed to open {DICTIONARY}:", str(e))


bisect.insort_left(dictionary, sys.argv[1] + "\n")
dictionary.insert(0, str(len(dictionary)) + "\n")
try:
    with open(DICTIONARY, "w", encoding="utf-8") as fp:
        fp.writelines(dictionary)
except Exception as e:
    print(f"failed to write {DICTIONARY}:", str(e))

print(f"{sys.argv[1]} added")
