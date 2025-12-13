# Functional Programming Support

This project adds functional programming helpers up and beyond (and sometimes
parallels) official Python function programming tools.

There are, of course, many many quality Python projects doing the same thing. I
encourage Python developers to explore them as well and see if they suit their
needs.

## Training Materials

Functional programming holds the promise of easy-to-follow-and-maintain
software. OOP also holds that promise. Functional programming promises
correctness. So does OOP along with a metric ton of tests.

Either can be difficult to comprehend without painful experience. My notes
and other materials are posted here as well.

This will be published in PyPi, but expect this library to be in development as
I learn-while-I-earn.

## Installation

```sh
pip install fpsupport
```

## Examples

### Monads

This library includes monadic patterns such as State, Maybe and Writer monads.
In the case of the monad that I call _Pipeline_, it incorporates all three to
be used as a logged chain-of-responsibility[^1] pattern.

Of interest to a TDD[^2] enthusiast is the use of monads for side-effects, used
to hide not only system calls but any other side effect or
non-deterministic[^3] value that plays havoc with the proof of a function. It
is used in dependency injection[^4], so there would be no need to use
monkeypatching in unit tests.

#### Are monads Pythonic?

This will be debated in the training materials once written. The answer is,
quite frankly, up to the writer. They certainly seem to add complication at
first glance, violating _simple is better than complex_. However, it enforces
_explicit is better than implicit_ and, properly used, is the epitome of
_readability counts_.

See [The Zen of Python](https://peps.python.org/pep-0020/).

## Further Reading

See [docs](docs/index.md).

## Development

```bash
make setup
```

Now you can program away without messing up standards. For suggested VS Code
plugins, see [preferences](setup/preferences/examples/README.md).

[^1]: Refactoring.Guru. [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility), retrieved
Nov 26, 2025.

[^2]: Test-driven development, used to encourage technical correctness. It works
alongside BDD (Behaviour-Driven Development for system behaviour), and ATDD
(Acceptance Test-Driven Development as an Agile collaboration with
stakeholders).

[^3]: For example, a random number generator.

[^4]: That is to say, converting a system call made from inside a function to an
argument of that function.
