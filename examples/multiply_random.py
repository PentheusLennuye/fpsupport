#!/usr/bin/env python
"""An example of using a monad for a provable function using side effects.

fpsupport/examples/multiply_random.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing permissions and limitations under the
License.

---

Description: a rather silly example of using a monad to hide a non-deterministic function.
"""


import random

from fpsupport import monad


def randint(x: int | None, lower_bound: int, upper_bound: int) -> monad.Monad:
    """A wrapped random.randint function meant to be called by an unwrapped monad.

    If x is None, then we return a monad(random integer). Otherwise, we return x.

    Args:
        x is any class with attribute 'value'

    Returns:
        A monad containing a RandomInteger
    """
    if x is not None:
        return monad.Monad(x)
    return monad.Monad(random.randint(lower_bound, upper_bound))


def multiply_random(M: monad.Monad, value: float) -> float:  # pylint: disable=invalid-name
    """Demonstrate with a test a provable function even if using a random variable."""
    return monad.unwrap(M.flat_map(randint, 0, 100)) * value


if __name__ == "__main__":
    m = monad.Monad.unit()
    print(multiply_random(m, 3))  # Could be anything, really


# Testing. Ensures that the function says what it does -----------------


def test_multiply_random() -> None:
    """Prove that multiply_random will multiply a random value.

    The tester supplies the "random" number.

    Usage: python -m pytest examples/multiply_random.py
    """
    assert multiply_random(monad.Monad.unit(3), 3) == 9
