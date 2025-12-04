"""Ensure the Monad structures work as designed.

File: test/unit/test_monad.py

Every monad in the fpsupport/monad directory are tested here.
"""

from typing import Self
from unittest import TestCase

import pytest

from fpsupport import exception, monad


class TestBaseClass(TestCase):
    """Test the Monad Base Class."""

    def test_identity(self):
        """Test that Monad.identity(M) returns M."""
        assert monad.Monad.unit(5).identity == 5

    def test_flat_map(self):
        """Checks that a simple monadic function works with the base class."""
        # given
        def monadic_add_one(a: int) -> int:
            """A very simple working function."""
            print("monadic", a + 1)
            return a + 1

        # when
        m = monad.Monad.unit(1)

        # then
        assert (m >> monadic_add_one).identity == 2

    def test_bind(self):
        """Test that the bind operator works while testing subclassing."""
        # given
        class MyMonad(monad.Monad):
            """Demonstrate map and bind operator."""
            @staticmethod
            def unit(outer: int) -> Self:
                return MyMonad(outer)

            @staticmethod
            def map(outer: int) -> int:
                print("map", outer + 1)
                return outer + 1

        def monadic_add_one(a: int) -> int:
            print("monadic", a + 1)
            return a + 1

        # when
        m = MyMonad.unit(5)

        # then
        result = (m >> monadic_add_one >> monadic_add_one).final()
        assert result.identity == 10

#    def test_bind_failure(self):
#        """Test that the bind operator fails with an exception.""""
#        # given
#        class MyMonad(monad.Monad):
#            """Demonstrates how to subclass Monads."""
#            @staticmethod
#            def unit(outer: int) -> Self:
#                return MyMonad(outer)
#
#            @staticmethod
#            def map(outer: int) -> int:
#                print("mapped", outer + 1)
#                return outer + 1
#
#            final = unit
#
#        # when
#        m = MyMonad.unit(5)
#
#        # then
#        with pytest.raises(exception.MonadException):
#            m >> (lambda x: x + 1)  # pylint: disable=pointless-statement
#