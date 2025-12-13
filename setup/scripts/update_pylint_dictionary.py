#!/usr/bin/env python
"""update_pylint_dictionary ensures that the whitelist used by pylint is the same as cSpell."""

import json
import os
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = f"{SCRIPT_DIR}/../preferences/examples"
PROJECT_ROOT = f"{SCRIPT_DIR}/../.."
WHITELIST = f"{PROJECT_ROOT}/setup/dictionaries/whitelist"


code_whitelist: list
dict_string: str
whitelist: list

try:
    with open(f"{PROJECT_ROOT}/code.code-workspace", "r", encoding="utf-8") as fp:
        dict_string = json.load(fp)
except FileNotFoundError:
    print("No code.code-workspace found in the project root. Not touching the whitelist.")
    sys.exit(0)

if "cSpell.words" in dict_string["settings"]:
    code_whitelist = dict_string["settings"]["cSpell.words"]
else:
    print("No cSpell.words in code.code-workspace. Not touching the whitelist.")
    sys.exit(0)

# Open the whitelist
with open(WHITELIST, "r", encoding="utf-8") as fp:
    whitelist = fp.read().split("\n")

# Merge
new_whitelist = list(set(whitelist + code_whitelist))
new_whitelist.sort()
if new_whitelist[0].strip() == "":
    new_whitelist = new_whitelist[1:]

with open(WHITELIST, "w", encoding="utf-8") as fp:
    fp.write("\n".join(new_whitelist))
