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

from collections import namedtuple

from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from fpsupport import IOMonad, IOType
from fpsupport.examples import file_and_print as fp


# -----------------------------------------------------------------------------
# UNIT TESTING
# -----------------------------------------------------------------------------

class TestFileAndPrint(TestCase):
    """Ensuring the FileAndPrint example function works.

    This demonstrates that we can simply set False as a result of a
    monadic IO function to test a function that uses monads as dependency
    injections. We do not need to mock the hidden system, third-party, or
    non-deterministic calls.

    Note that this library needs to use MagicMocks to mock the >> (rshift)
    operator in our monads.
    """
    def setUp(self):
        self.iotype = namedtuple("Unwrap", "ok")
        self.inner_monad = MagicMock()  # required for >> (rshift)
        self.fmonad = MagicMock()
        self.fmonad.flat_map.return_value = self.inner_monad

    def test_print_file_contents_fails_on_bad_open(self):
        """Mock the injected monads to fail."""
        self.inner_monad.unwrap.return_value = self.iotype(False)
        assert not fp.print_file_contents(self.fmonad)

    def test_print_file_contents_succeeds(self):
        """Mock the injected monads to pass."""
        self.inner_monad.unwrap.return_value = self.iotype(True)
        self.inner_monad.__rshift__.return_value = self.inner_monad
        assert fp.print_file_contents(self.fmonad)


# -----------------------------------------------------------------------------
# UNIT TESTING THE MONAD
# -----------------------------------------------------------------------------

class TestOpenTextFile(TestCase):
    """The monad itself, to get 100% coverage, will need to patch its call."""
    @patch("fpsupport.examples.file_and_print.open")
    def test_open_text_file_handles_oserror(self, mock_open):
        """Ensure OS Error returns a false and message."""
        # given
        mock_open.side_effect = OSError(1, "file not found", "mkdocs.yml")

        # then
        assert fp.print_file_contents(IOMonad(IOType(""))) is False

    @patch("fpsupport.examples.file_and_print.open")
    def test_open_text_file_succeeds(self, mock_open):
        """Ensure open text file succeeds when opening and reading succeed.

        Note that, since we are using context management "with open(x) as y:",
        need to set the Mock's __enter__ attribute.
        """
        # given
        file_pointer = Mock()
        file_pointer.read.return_value = ""
        mock_open.__enter__.return_value = file_pointer  # See docstyle

        # then
        assert fp.print_file_contents(IOMonad(IOType(""))) is True


# -----------------------------------------------------------------------------
# INTEGRATION TESTING
# -----------------------------------------------------------------------------

class TestPrintFileContents(TestCase):
    """Demonstrate that one can still use integration testing with FP.

    This would be necessary to ensure that the wrapped "impure" functions work.
    It is also used by integration testers so they can monitor system calls.

    This requires bringing in the actual Monads rather than just mocking them.

    """
    @patch("fpsupport.examples.file_and_print.open")
    def test_print_file_contents_integration(self, mock_open):
        """This is an integration test: is open called correctly?"""
        # given
        file_pointer = Mock()
        file_pointer.read.return_value = "this is a common string"
        mock_open.__enter__.return_value = file_pointer

        # when
        fp.print_file_contents(IOMonad(IOType("")))

        # then (this is the integration part)
        mock_open.assert_called_once_with("mkdocs.yml", "r", encoding="utf-8")
