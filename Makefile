.PHONY: setup
setup:
# Initiate and install the Python modules in a virtual environment. Also,
# install the git hooks to impose discipline on the otherwise wonderful
# developer.
	scripts/setup.sh
  
.PHONY: clean-all
clean-all:
# Wipe out the virtual environment 
	rm -rf .venv

.PHONY: unittest
unittest:
	poetry run python -m pytest test/unit

.PHONY: coverage
coverage:
	poetry run python -m pytest test/unit --cov --cov-report=term-missing

.PHONY: lint
lint:
	poetry run python -m pylint fpsupport
	
.PHONY: docstyle
docstyle:
	poetry run pydocstyle

.PHONY: doclint
doclint:
# Give a Flesch-Kincaid score for each document file, along with technical
# writing hints
	poetry run python scripts/score_docs.py

.PHONY: inspect
inspect: unittest coverage lint docstyle doclint