# fpsupport/Makefile Copyright 2025 George Cummings
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing permissions and limitations under the
# License.

.DEFAULT_GOAL := setup
.SILENT:

# Environment ---------------------------------------------------------------

.PHONY: venv
venv:
	poetry install

.PHONY: githooks
githooks:
	setup/githook_setup.sh

.PHONY: setup
setup: venv githooks

# Linting --------------------------------------------------------------------
.PHONY: pylint
pylint:
	echo "Running pylint"
	poetry run pylint fpsupport examples

.PHONY: pydocstyle
pydocstyle:
	echo "Running pydocstyle..."
	poetry run pydocstyle --convention=google fpsupport examples
	echo "ok."

.PHONY: black 
black:
	echo "Running black to force formatting"
	poetry run black fpsupport examples

.PHONY: black-diff
black-diff:
	echo "Running black --check --diff"
	poetry run black --check --diff fpsupport examples

.PHONY: lint
lint: pylint pydocstyle black-diff

# Spelling --------------------------------------------------------------------
# This requires the "enchant" binary package installed on your system or home
.PHONY: spellcheck
spellcheck:
	echo "Adjusting the whitelist from code.code-workspace"
	poetry run setup/scripts/update_pylint_dictionary.py
	poetry run python -c 'import enchant' || (echo "Please install enchant on your system" && false)
	poetry run pylint --disable all --enable spelling --spelling-dict en_CA \
	  --spelling-private-dict-file=setup/dictionaries/whitelist fpsupport examples

# Testing --------------------------------------------------------------------

.PHONY: unittest
unittest:
	echo "Running python unit tests."; \
	poetry run python -m pytest test/unit

.PHONY: coverage
coverage:
	echo "Running python unit tests for all green at 100% coverage."; \
	poetry run python -m pytest test/unit \
	--cov --cov-report=term-missing | grep 'TOTAL.*100%'

.PHONY: tests
tests: unittest coverage
