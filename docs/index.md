---
date: 2025-11-06
tags: [functional programming, python, installation, library]
author: George Cummings
---

# Functional Programming Support

This project offers Python functional programming helpers not covered by the
official Python function programming tools.

There are, of course, many quality Python projects doing the same thing. I
encourage Python developers to explore them and see if they suit their needs.

!!! note ""
    This is my FP library. There are many like it, but this one is mine...

## Installation

```sh
pip install fpsupport
```

## Training Materials

Functional programming holds the promise of easy-to-follow, easily maintainable,
and correct software. Sound familiar? Object-oriented programming also holds
that promise ... so long as the developers use best practice testing and SOLID
principles.

Both FP and OOP can be difficult to exploit without painful education or
experience. My notes and other materials are posted here to assist folks with
_their_ painful education or experience.

Training materials will be published as I become more proficient at both
functional programming in Python and in documentation. In the meantime, I
recommend you watch Boot Dev's [Functional Programming Full Course](https://youtu.be/5QZYGU0C2OA?si=X6n3TtgSBZZUsiC7).

## Statement on the Use of AI

See my [personal policy on the use of artificial intelligence](content/ai_policy.md).


## Project layout

```text
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
examples/     # How to use the library
fpsupport/    # The library. As it expands, so will the folders
test/         # Unit testing. Functional and integration testing are not applicable.
```

## Examples

### Monads

This library includes monadic patterns such as State, Maybe and Writer monads.
In the case of the monad that I call _Pipeline_, it incorporates all three to
be used as a logged chain-of-responsibility[^1] pattern.

Of interest to a TDD[^2] enthusiast is the use of the monad for IO, used to hide
not only system calls but any other side effect or non-deterministic[^3] value
that plays havoc with the proof of a function. It is used in dependency
injection[^4], so there would be no need to use monkeypatching in unit tests.

#### Are monads Pythonic?

This will be debated in the training materials once written. The answer is,
quite frankly, up to the writer. They certainly seem to add complication at
first glance, violating _simple is better than complex_. However, it enforces
_explicit is better than implicit_ and, properly used, is the epitome of
_readability counts_.

See [The Zen of Python](https://peps.python.org/pep-0020/).

[^1]: Refactoring.Guru. [Chain of Responsibility]
(https://refactoring.guru/design-patterns/chain-of-responsibility), retrieved
Nov 26, 2025.

[^2]: Test-driven development, used to encourage technical correctness. It
works alongside BDD (Behaviour-Driven Development for system behaviour), and
ATDD (Acceptance Test-Driven Development as an Agile collaboration with
stakeholders).

[^3]: For example, a random number generator.

[^4]: That is to say, converting a system call made from inside a function to
      an argument of that function.
