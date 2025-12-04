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

import inspect

from fpsupport import exception

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
    def __init__(self, outer: Optional[T]) -> Self:
        """Initializes the object with internal attributes.

        Monads are meant to be called from unit().

        Args:
            outer: the wrapped type

        Returns:
            self

        Raises:
            MonadException if the class was instantiated directly and not from
            unit()
        """
        print(inspect.stack()[1].function)
        if inspect.stack()[1].function != "unit":
            raise exception.MonadException("monad instantiated outside unit()")
        self.outer: Optional[T] = outer

    @staticmethod
    def unit(outer: Optional[T]) -> Self:
        """Wraps the arguments into this Monad. a -> M a.

        Also known as the type converter. Also known as pure().

        If Monad is subclassed, then this function must also be overridden to
        return its own subclass.

        It may seem silly to return a new Monad (or subclass) rather than self,
        but one of the tenets of functional programming is immutable data.

        Args:
          outer: any object

        Returns:
          Monad
        """
        return Monad(outer)

    @property
    def identity(self) -> Self:
        """Returns the wrapped type. M a -> a """
        return self.outer

    def flat_map(self, f: Callable, *args, **kwargs) -> Self:
        """Execute _f_ with the wrapped values as the argument.

        Unwraps the original type, sends it to map for some pre-execution
        massaging, and then sends it through _f_ along with other arguments.

        M a -> (a -> M b) -> M b

        Also known as chain, join_map, select, then_apply and the bind
        operator. The bind operator in Python is represented with ">>", the
        __rshift__ operator.

        Args:
            f: a function
            *args: additional positional arguments
            **kwargs: additional keyword arguments

        Returns:
            A Monad

        Raises:
            MonadException if the function fails to return the same type as
            the original wrapped value. This is necessary in a duck-typed
            language.
        """
        outer_prime = self.map(self.identity)

        result = f(outer_prime, *args, **kwargs)
        if not isinstance(result, type(self.outer)):
            self._fail(f.__name__)
        return type(self).unit(result)

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
    def map(outer: Optional[T]) -> Optional[T]:
        """Massage the original variables through executing internal functions.

        This function is meant to be overridden by Monad's subclasses.

        Args:
            outer: the original type

        Returns:
            outer_prime: the original type, with possibly modified values
        """
        return deepcopy(outer)

    def final(self) -> Self:
        """Run the map by itself without calling any function.

        This is called optionally. For example, if the map() function calls
        a Writer, it will write out any remaining buffer.
        
        Returns:
            subclassed object
        """
        return type(self).unit(self.map(self.outer))

    # Aliases
    chain = flat_map
    flatMap = flat_map
    fmap = flat_map
    join_map = flat_map
    joinMap = flat_map
    pure = unit
    select = flat_map
    then_apply = flat_map
    unwrap = identity
    __rshift__ = flat_map
