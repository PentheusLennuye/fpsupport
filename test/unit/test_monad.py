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
        m = monad.Monad(5)  # using __init__ instead of unit() for coverage.
        assert m.identity() == 5

    def test_unit_and_unwrap(self):
        """Test that (M a).unwrap() returns a."""
        assert monad.Monad.unit(5).unwrap() == 5

    def test_flat_map(self):
        """Checks that a simple monadic function works with the base class."""
        # given
        def monadic_add_one(a: int) -> monad.Monad:
            """A very simple working function."""
            print("monadic", a + 1)
            return monad.Monad(a + 1)

        # when
        m = monad.Monad(1)

        # then
        assert (m >> monadic_add_one).unwrap() == 2

    def test_bind(self):
        """Test that the bind operator works while testing subclassing."""
        # given
        class MyMonad(monad.Monad):
            """Demonstrate map and bind operator."""
            @staticmethod
            def unit(a: int) -> Self:
                return MyMonad(a)

            @staticmethod
            def outer(a: int) -> int:
                return a + 1

            final = unit

        def monadic_add_one(a: int) -> monad.Monad:
            return MyMonad(a + 1)

        # when
        m = MyMonad.unit(5)

        # then
        assert (
            m >> monadic_add_one >> monadic_add_one >> MyMonad.final
        ).unwrap() == 10

    def test_bind_failure(self):
        """Test that the bind operator fails with an exception."""
        # given
        class MyMonad(monad.Monad):
            """Demonstrates how to subclass Monads."""
            @staticmethod
            def unit(a: int) -> Self:
                return MyMonad(a)

            @staticmethod
            def outer(a: int) -> int:
                """This will change the type to string. Bad!"""
                print("mapped", a + 1)
                return a + 1

            final = unit

        # when
        m = MyMonad.unit(5)

        # then
        with pytest.raises(exception.MonadException):
            m >> (lambda x: x + 1)  # pylint: disable=pointless-statement
