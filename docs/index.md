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

## Example: Monads

This library includes monadic patterns such as State, Maybe and Writer monads.
In the case of the monad that I call _Pipeline_, it incorporates all three to
remove the painful-to-maintain if/then/elses used for logging activities, early
returns, and input validating in a chain of responsibility akin to a Jenkins or
Concourse CI/CD service.

Of interest to a TDD[^2] enthusiast is the IO monad, used to hide not only
system calls but any other side effect or non-deterministic value that plays
havoc with the correctness of a function. It is used in dependency
injection[^1], so there would be no need to use monkeypatching in unit tests.

## Training Materials

Functional programming holds the promise of easy-to-follow, easily maintainable,
and correct software. Sound familiar? Object-oriented programming also holds
that promise ... so long as the developers use best practice testing and SOLID
principles.

BOth FP and OOP can be difficult to exploit without painful education or
experience. My notes and other materials are posted here to assist folks with
_their_ painful education or experience.

## Statement on the Use of AI

See my [personal policy on the use of artificial
intelligence](content/ai_policy.md).

## Project layout

```text
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
fp/
    monads/
```

[^1]: That is to say, converting a system call made from inside a function to
an argument of that function.

[^2]: Test-driven development, used to encourage technical correctness. It
works alongside BDD (Behaviour-Driven Development for system behaviour), and
ATDD (Acceptance Test-Driven Development as an Agile collaboration with
stakeholders).
