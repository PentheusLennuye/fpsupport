"""Testing the monad-wrapped file module."""

from unittest import TestCase

from pytest import raises

from fpsupport.struct import IOType


class TestIOType(TestCase):
    """Testing the IOType init."""

    def test_fail_bad_ok(self):
        """OK must be boolean or None."""
        with raises(TypeError):
            _ = IOType("", "", "this should fail.")  # type: ignore

    def test_fail_bad_error_msg(self):
        """Error_msg must be string or None."""
        with raises(TypeError):
            _ = IOType("", 5, None)  # type: ignore
