"""An opinionated version of The Monad.

fpsupport/monad.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

-----

Description:

This Base Class is only useful to derived classes.

Before defining a Monad, I will define "type." A "type" is any construct. For
example a type could be a scalar, a function, an object, or an object composed
of scalars, functions, and other objects.

A Monad is a monoid in the class of endofunctors.

- An endofunctor is a function that returns the same type as it takes in. Using
  python typing, the signature of an integer endofunctor would be
  "def my_function(x: int) -> int". A dict endofunctor would be
  "def my_function(x: dict) -> dict".

- A monoid is a collection of three functions:
    - A _unit_ function that encapsulates a type, call it type "a"
    - Any number of "bind" functions that call an outside function and expect
      type "a" back
    - An _identity_ function, which returns type "a" with its current values.

- A monoid has some mathematic rules. We will skip them here and just get on
  with it working as an object that hides data and does hidden operations on
  that hidden data, while keeping its type.

A monad is a monoid, but being in the class of endofunctors, its functions must
accept and return the same type. This file provides the basics, but to be
useful, it needs to be subclassed.

-----

Typical usage example:

  from typing import Callable, Self
  from fpsupport import monad

  class MyMonad(monad.Monad):
      def __init__(self, t: int) -> Self:
          '''Initialize the MyMonad with internal and wrapped attributes.'''

          #Define the Monad internal attributes
          self.odd_check : bool = False

          # Wrap the type
          self.t : int = t

      @staticmethod
      def unit(self, t: int) -> Self:
          return MyMonad(t)

      @staticmethod
      def map(t: int) -> int:
          '''Execute this automatically before each bind.'''
          self.odd_check = t & 1
          return t

      final = unit

  m = MyMonad(2)
  m_prime = (
      m >>
      (lamda x: MyMonad.unit(x.unwrap() + 1)) >>
      MyMonad.final
  )

  print(m_prime.odd_check)  # returns True
  print(m_prime.t))  # returns 3
"""

from copy import deepcopy
from typing import Callable, Self, Optional, TypeVar

from . import exception

T = TypeVar("T")


class Monad:
    """The Monad Base Class

    An interface to the base class. It contains the three mandatory functions,
    and it also creates aliases for the different names for those functions.

    Note that this monad has an inherent "Maybe" component: if a derived
    subclass's map() returns None, then bound execution is stopped.

    Attributes:
        There are no attributes. Any attribute will be defined by a derived
        class __init()__, and populated by the class unit() function.
    """
    def __init__(self, a: Optional[T]) -> Self:
        """Initializes the object with internal attributes.

        This is meant to be overridden by subclasses, ensuring super() is
        called.

        Monads are meant to be called from unit() so type checking can be
        implemented.
        """
        self.a: Optional[T] = a

    @staticmethod
    def unit(a: Optional[T]) -> Self:
        """Wraps the arguments into this Monad. a -> M a.

        Also known as the type converter. Also known as pure().

        This must be overridden by base classes to implement type checking on
        the wrapped type 'a'. It may seem silly to return a new Monad (or
        subclass) rather than self, but one of the tenets of functional
        programming is immutable data.
        """
        return Monad(a)

    def identity(self) -> Self:
        """Returns a. Also known as 'unwrap'."""
        return self.a

    def flat_map(self, f: Callable, *args, **kwargs) -> Self:
        """Execute _f_ with the wrapped type as the first argument.

        Unwraps the original type, sends it to map for some pre-execution
        massaging, and then sends it through _f_.

        Also known as chain, join_map, select, then_apply and the bind
        operator. The bind operator in Python is represented with ">>", the
        __rshift__ operator.

        Args:
            f: a function

        Returns:
            A Monad

        Raises:
            MonadException if the function fails to return the same type of
            Monad.
        """
        a_prime = self.outer(self.unwrap())  # Permits a set of repeatable ops.

        result = f(a_prime, *args, **kwargs)
        if not isinstance(result, type(self)):
            self._fail(f.__name__)
        return result

    def _fail(self, fn_name: str) -> None:
        """Throws an exception with an explanation.

        Args:
            fn_name: the name of the function that triggered the failure.

        Raises:
            MonadException
        """
        me = str(type(self)).split("'")[1]
        raise exception.MonadException(
            f"bound function \"{fn_name}\" did not return type {me}"
        )

    @staticmethod
    def outer(a: Optional[T]) -> Optional[T]:
        """A function that is run just prior to the flat_map's bound function.

        This function is not required for the definition of a monad. However,
        it allows for a defined set of repeatable operations.

        outer() is meant to be overridden, so its base here is just identity().

        Args:
            a: the original type, or

        Returns:
            a_prime: the original type, possibly modified
        """
        return deepcopy(a)

    # Aliases

    chain = flat_map
    final = unit  # Used to ensure the map is run one last time if necessary
    flatMap = flat_map
    fmap = flat_map
    join_map = flat_map
    joinMap = flat_map
    pure = unit
    select = flat_map
    then_apply = flat_map
    unwrap = identity
    __rshift__ = flat_map
