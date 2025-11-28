"""Testing the IO Monad

fpsupport/test_io_monad.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

-----

The IO Monad I propose uses a structure to deal with any call where the
results are not known: system calls that might break; calls to network APIs;
calls for random numbers, and so on.
"""

from unittest import TestCase

import pytest

from fpsupport import exception, IOMonad, IOType

# pylint: disable=unnecessary-lambda


class TestIOMonad(TestCase):
    """Ensuring the IO Monad works."""
    def test_unit_fails_on_bad_arg(self):
        """unit() should only except IOType as its argument."""
        with pytest.raises(exception.MonadException):
            IOMonad.unit({"this": "should not work"})

    def test_unit_works_with_iotype(self):
        """unit() returns an IOMonad."""
        io = IOMonad.unit(IOType("stub content"))
        assert io.a.contents == "stub content"
        assert io.a.ok
        assert not io.a.error_msg
