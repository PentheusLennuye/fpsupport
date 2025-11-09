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

Machine- and deep-learning techniques with one exception are a great benefit to
humanity. The one exception is the unregulated, ignorant, and inhumane use of
generative AI.

I do not use generative AI to directly compose my work. I have three reasons:

- I believe the use of generative AI is good for quick answers, but its repeated
  use removes the barriers a student needs to overcome in order to truly
  understand a concept[^3] [^4]
- I dislike the abuse and displacement of the work made by hard-working humans
  for profit
- I take pride in my abilities as admin, developer, student, and technical
  writer. If ordered by my paid profession to use gen AI for its goals, I will
  do so (and probably be amazed, let's be honest). However, this is my project
  and I am not under any sponsorship or orders.

Sometimes, search engines defaults come to play and is unavoidable. As of Q4
2025, there are still enough errors in the answers to warrant caution and
review.

!!! info "The Use of this Library in AI Development is Welcome"
    The use of this library to develop AI techniques and models is welcome,
    including the development of generative AI techniques for education. The author wishes that its
    use to train generative AI models should have as its goal the assistance
    of humans rather than their displacement.

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

[^3]: Soenke, Ahrens. 2022. _How to Take Smart Notes: One Simple Technique to
Boost Writing, Learning and Thinking_, 2nd ed, Self-published.
[^4]: Cal Newport. 2021. _A World Without Email: Reimaginig Work in an Age of Communication Overload_, Portfolio.