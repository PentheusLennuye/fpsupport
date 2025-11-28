"""The Base Monad Class

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

A Monad is a monoid in the class of endofunctors. Casting category theory to
the side, all this means is that Monad is a collection of functions. The
functions are:
    - A single function that encapsulates the type into the Monad
    - Any number of "bind" functions that accept only the Monad as its argument
      and returns only the Monad
    - One of those functions is called the _identity_ function, which only
      returns itself.

Note that functions do not have to be in the Monad class to be considered part
of the Monad's collection. In fact, I have found that most functions are not in
the Monad class but spread throughout a programme that uses the Monad object as
its argument.

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

        Monads are meant to be called from unit().
        """
        self.a: Optional[T] = a

    @staticmethod
    def unit(a: Optional[T]) -> Self:
        """Wraps the arguments into this Monad. a -> M a.

        Also known as the type converter. Also known as pure().

        This must be overridden by base classes. It may seem silly to return
        a new Monad (or subclass) rather than self, but one of the tenets of
        functional programming is immutable data.
        """
        return Monad(a)

    def identity(self) -> Self:
        """Returns myself."""
        return self

    def flat_map(self, f: Callable, *args, **kwargs) -> Self:
        """Execute _f_ with the wrapped values as the argument.

        Unwraps the original type, sends it to map for some pre-execution
        massaging, and then sends it through _f_.

        Also known as chain, join_map, select, then_apply and the bind
        operator. The bind operator in Python is represented with ">>", the
        __rshift__ operator.

        Note that this monad has an inherent "Maybe" component: if a derived
        subclass's map() returns None, then bound execution is stopped.

        Args:
            f: a function

        Returns:
            A Monad

        Raises:
            MonadException if the function fails to return the same type of
            Monad.
        """
        a_prime = self.map(self.unwrap())

        result = f(a_prime, *args, **kwargs)
        if not isinstance(result, type(self)):
            self._fail(f.__name__)
        return result

    def _fail(self, fn_name: str) -> None:
        """Fails the Monad.

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
    def map(a: Optional[T]) -> Optional[T]:
        """Massage the original variables while executing internal functions.

        This function is meant to be overridden.

        Args:
            a: the original type, or
            None: do not execute the bound function.

        Returns:
            a_prime: the original type, possibly modified
        """
        return deepcopy(a)

    def unwrap(self) -> Optional[T]:
        """Return the original type."""
        return self.a

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
    __rshift__ = flat_map
