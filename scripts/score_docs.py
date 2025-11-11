"""Scores and suggests corrections on the doc files."""

import os
import textstat

LANG = "en"
PUBLIC_DOCS = [
    "index.md",
    "content/ai_policy.md"
]
PUBLIC_TARGET = 8
TECHNICAL_DOCS = [

]
TECHNICAL_TARGET = 11

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = f"{CURRENT_DIR}/.."

textstat.set_lang(LANG)

print("\nDOCUMENT SCORING")
print("=" * 42)
headers = ("file", "FD", "TGT")
print(f"{headers[0]:>30} {headers[1]:<5} {headers[2]}")
print("-" * 42)
for d in PUBLIC_DOCS:
    with open(f"{ROOT_DIR}/docs/{d}", "r", encoding="utf-8") as fd:
        grade = textstat.flesch_kincaid_grade(fd.read())
        print(f"{d:>30} {grade:.2f} {PUBLIC_TARGET:.2f}")
