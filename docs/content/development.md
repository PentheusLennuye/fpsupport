# Development

## Preliminaries

Set up your workstation for Gitflow:

```sh
./setup.sh
```

## A. Framework

Development of this library is within the framework of test-driven development.
As this library does not have any sponsors, BDD and ATDD are not in scope.

## B. Branches

The default branch is _main_. It will not accept direct pushes, but only merges
from the _develop_ branch or a _hotfix_ branch.

The _develop_ branch is used to collect features before a release. It will only
accept push requests from the _main_, _feature*_ and _bugfix*_ branches.

## C. Versioning

This library uses [semver](https://semver.org/) version 2.

## D. Release Cycle

There is no continuous release cycle.

## E. Development Cyle

No branch will be accepted into the _develop_ or _main_ branch unless

- The CODEOWNER says so
- All unit tests are green.
- The code has 100% coverage in the unit tests
- _pyproject.yaml_ has its version updated
- CHANGELOG.md has its latest version matching _pyproject.yaml_'s, and its
  versions are listed in reverse order of time
- _docs_/ has been scanned for grammar and good technical writing.

## F. Linting

This project's code conforms to PEP8, with 79-character columns. Other elements
taken from [Google's Python Style
Guide](https://google.github.io/styleguide/pyguide.html) are useful to me:

- _import_ statements are used for packages and modules only.
- _import_ statements use full pathnames for the module.
- Exceptions are used sparingly. This is, after all, an FP library which is
  hardly Pythonic to begin with. The exceptions should be caught as early as
  possible.
- Since FP loves immutable data, a global state is anathema.
- Use nested/local/inner functions only as closures.

### F.1 Other style decisions

- Use FP when possible, but if recursion becomes a problem, fall back to using
  _for_ loops or a generator.
- Being an example of FP, this library uses immutable data but do not be dumb
  about it. We're pragmatic, not idealists.
- Generators are lovely as they are efficient and do not look like loops.
- Although it is not _pythonic_, use typing and type hints. Enforce types, but
  use _Optional[T]_ for base classes.

### F.2 Docstrings

Use PEP 257.
