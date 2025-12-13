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
