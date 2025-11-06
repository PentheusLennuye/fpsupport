# Functional Programming Support

This project adds functional programming helpers up and beyond (and sometimes
parallels) official Python function programming tools.

There are, of course, many many quality Python projects doing the same thing. I
encourage Python developers to explore them and see if they suit their needs.

This is my FP library. There are many like it, but this one is mine...

## Example: Monads

For example, my library includes monadic patterns such as State, Maybe and
Writer monads. In the case of the monad I call _Pipeline_, it incorporates all
three to remove the painful-to-maintain if/then/elses used for logging
activities, early returns, and input validating in a chain of responsibility
akin to a Jenkins or Concourse CI/CD service.

Of interest to a TDD^2 enthusiast is the IO monad, used to hide not only system
calls but any other side effect or non-deterministic value that plays havoc with
the correctness of a function. It is used in dependency injection^1, so there
would be no need to use monkeypatching in unit tests.

## Training Materials

Functional programming holds the promise of easy-to-follow-and-maintain
software. OOP also holds that promise. Functional programming promises
correctness. So does OOP along with a metric ton of tests.

Either can be difficult to comprehend without painful experience. My notes
and other materials are posted here as well.

## Installation

```sh
pip install fpsupport
```
______________________________________________________________________

^1: That is to say, converting a system call made from inside a function to an argument of that function.

^2: Test-driven development, used to encourage technical correctness. It works alongside BDD (Behaviour-Driven Development for system behaviour), and ATDD (Acceptance Test-Driven Development as an Agile collaboration with stakeholders).
