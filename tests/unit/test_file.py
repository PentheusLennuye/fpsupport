"""Testing the monad-wrapped file module."""

from unittest import TestCase
from unittest.mock import Mock, patch

from fpsupport import file
from fpsupport.monad import unwrap
from fpsupport.struct import IOType


class TestOpen(TestCase):
    """Testing the file.fopen function with unit and integration tests."""

    @patch("fpsupport.file.open")
    def test_nok(self, os_open):
        """file.fopen with a monad's ok cleared should not run os.open."""
        # given
        io = IOType("", "", False)
        # when
        result = file.fopen(io, "fake.txt", "r", encoding="utf-8")
        # then
        new_io = unwrap(result)
        assert not new_io.ok
        os_open.assert_not_called()

    @patch("fpsupport.file.open")
    def test_failed_open_clears_ok(self, os_open):
        """file.fopen with an OS Error clears ok."""
        # given
        io = IOType("")
        os_open.side_effect = OSError(1, "abcd", "fake.txt")
        # when
        result = file.fopen(io, "fake.txt", "r", encoding="utf-8")
        # then
        new_io = unwrap(result)
        assert not new_io.ok
        assert new_io.error_msg == "fake.txt: abcd"

    @patch("fpsupport.file.open")
    def test_open_sets_ok(self, os_open):
        """file.open without errors sets ok."""
        # given
        io = IOType("")
        os_open.return_value = "Another visitor!"
        # when
        result = file.fopen(io, "fake.txt", "r", encoding="utf-8")
        # then
        new_io = unwrap(result)
        assert new_io.ok
        assert new_io.outcome == "Another visitor!"
        os_open.assert_called_once_with("fake.txt", "r", encoding="utf-8")


class TestRead(TestCase):
    """Testing the file.fread function with unit and integration tests."""

    def test_nok(self):
        """file.fread with a monad's ok cleared should not run os.open."""
        # given
        file_object = Mock()
        io = IOType(file_object, "", False)

        # when
        result = file.fread(io)

        # then
        new_io = unwrap(result)
        assert not new_io.ok
        file_object.read.assert_not_called()

    def test_failed_read_clears_ok(self):
        """file.fread with an OS Error clears ok."""
        # given
        file_object = Mock()
        file_object.read.side_effect = OSError(1, "bad bits", "fake.txt")
        io = IOType(file_object)

        # when
        result = file.fread(io)

        # then
        new_io = unwrap(result)
        assert not new_io.ok
        assert new_io.error_msg == "fake.txt: bad bits"

    def test_read_sets_ok(self):
        """file.fread without any error sets ok."""
        # given
        file_object = Mock()
        file_object.read.return_value = "Another visitor!"
        io = IOType(file_object)

        # when
        result = file.fread(io)

        # then
        new_io = unwrap(result)
        assert new_io.ok
        assert new_io.outcome == "Another visitor!"
        file_object.read.assert_called_once_with()
