"""Testing the FileIO extra example

fpsupport/test_fileio.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import collections

from unittest import TestCase
from unittest.mock import Mock, patch

from fpsupport import IOMonad, IOType
from fpsupport.extra import fileio


# -----------------------------------------------------------------------------
# UNIT TESTING
# -----------------------------------------------------------------------------

class TestFileIOUnit(TestCase):
    """Ensuring the File IO example works.

    This demonstrates that we can simply set False as a result of a
    monadic IO function rather than go through a list of Exceptions.

    This also means we do not have to mock a built-in or third-party function
    for unit testing.
    """
    def setUp(self):
        Unwrap = collections.namedtuple("Unwrap", "ok contents")
        self.failure = Unwrap(ok=False, contents="")
        self.success = Unwrap(ok=True, contents="this is a success")

        self.fmonad_call = Mock()
        self.fmonad = Mock()
        self.fmonad.call.return_value = self.fmonad_call

        self.pmonad_call = Mock()
        self.pmonad = Mock()
        self.pmonad.call.return_value = self.pmonad_call

    def test_print_file_contents_fails_on_open(self):
        """Mock the injected monads to fail."""
        # given
        self.fmonad_call.unwrap.return_value = self.failure

        # then
        assert not fileio.print_file_contents(self.fmonad, self.pmonad)

    def test_print_file_contents_fails_on_print(self):
        """Mock the print monad to pass.

        This of course is silly because print() always succeeds.
        """
        # given
        self.fmonad_call.unwrap.return_value = self.success
        self.pmonad_call.unwrap.return_value = self.failure

        # then
        assert not fileio.print_file_contents(self.fmonad, self.pmonad)

    def test_print_file_contents_succeeds(self):
        """Mock the injected monads to pass."""
        # given
        self.fmonad_call.unwrap.return_value = self.success
        self.pmonad_call.unwrap.return_value = self.success

        # then
        assert fileio.print_file_contents(self.fmonad, self.pmonad)


# -----------------------------------------------------------------------------
# INTEGRATION TESTING
# -----------------------------------------------------------------------------

class TestFileIOIntegration(TestCase):
    """Demonstrate that one can still use integration testing with FP.

    This would be necessary to ensure that the wrapped "impure" functions work.
    It is also used by integration testers can monitor system calls.

    This requires bringing in the actual Monads rather than just mocking them.

    """
    @patch("fpsupport.extra.fileio.open")
    def test_open_text_file_handles_oserror(self, mock_open):
        """Ensure OS Error returns a false and message"""
        # given
        mock_open.side_effect = OSError(1, "file not found", "mkdocs.yml")

        # when
        res = fileio.open_text_file(fileio.FileType("mkdocs.yml"))

        # then
        assert not res.unwrap().ok

    @patch("fpsupport.extra.fileio.open")
    def test_print_file_contents_integration(self, mock_open):
        """This is an integration test: is open called?"""
        # given
        fp = Mock()
        fp.read.return_value = "this is a common string"
        mock_open.read.return_value = fp

        # when
        fileio.print_file_contents(
            IOMonad(fileio.FileType(fileio.open_text_file, "mkdocs.yml")),
            IOMonad(IOType((lambda x: print(x.contents) or IOMonad(x)), ""))
        )

        # then
        mock_open.assert_called_once_with("mkdocs.yml", "r", encoding="utf-8")
