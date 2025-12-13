"""Ensure the Monad structures work as designed.

File: test/unit/test_monad.py

Every monad in the fpsupport/monad directory are tested here.
"""

from typing import Self
from unittest import TestCase

import pytest

from fpsupport.exception import MonadException
from fpsupport.monad import Monad, unwrap


class TestBaseClass(TestCase):
    """Test the Monad Base Class."""

    def test_identity(self):
        """Test that Monad.identity(M) returns M."""
        m = Monad(5)  # using __init__ instead of unit() for coverage.
        assert unwrap(m.identity) == 5

    def test_unit_and_unwrap(self):
        """Test that (M a).unwrap() returns a."""
        assert unwrap(Monad.unit(5)) == 5

    def test_flat_map(self):
        """Checks that a simple monadic function works with the base class."""

        # given
        def monadic_add_one(a: int) -> Monad:
            """A very simple working function."""
            print("monadic", a + 1)
            return Monad(a + 1)

        # when
        m = Monad.unit(1)

        # then
        assert unwrap((m >> monadic_add_one)) == 2

    def test_bind(self):
        """Test that the bind operator works while testing subclassing."""

        # given
        class MyMonad(Monad):
            """Demonstrate map and bind operator."""

            @staticmethod
            def unit(outer: int) -> Self:  # pyright: ignore[reportGeneralTypeIssues]
                return MyMonad(outer)

            def map(self) -> Self:
                return MyMonad(self.outer + 1)  # pyright: ignore[reportReturnType]

        def monadic_add_one(a: int) -> MyMonad:
            return MyMonad(a + 1)

        # when
        m = MyMonad.unit(5)

        # then
        result = (m >> monadic_add_one >> monadic_add_one).final()
        assert unwrap(result) == 10

    def test_bind_failure(self):
        """Test that the bind operator fails with an exception."""
        # given
        m = Monad.unit(5)

        # then
        with pytest.raises(MonadException):
            _ = m >> (lambda x: str(x + 1))
