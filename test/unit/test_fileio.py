"""Testing the FileIO extra

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

from unittest import TestCase

import pytest

from fpsupport import exception, IOMonad, IOType

class TestFileIO(TestCase):
    """Ensuring the File IO example works."""
    def test_unit_fails_on_bad_arg(self):
        """unit() should only except IOType as its argument."""
        with pytest.raises(exception.MonadException):
            IOMonad.unit({"this": "should not work"})

    def test_unit_works_with_iotype(self):
        """unit() returns an IOMonad."""
        io = IOMonad.unit(IOType("stub content"))
        assert io.a.contents == "stub content"

    def test_unit_works_with_iotype_derivative(self):
        """unit() returns an IOMonad."""
        class FileType(IOType):
            """Adds filepath to the IOType"""
            def __init__(self, filepath: str = ""):
                super().__init__("")
                self.filepath: str = filepath

        io = IOMonad.unit(FileType("mkdocs.yml"))
        assert io.a.filepath == "mkdocs.yml"
