"""fileio.py is an example of using an IO Monad.

fpsupport/extra/fileio.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

-----

This example uses the functional programming principles of immutable code and
"pure" functions. It may seem silly at first, but think again on the principle
of dependency injection: instead of "print" and "fileopen," think of DB
and network API operations.
"""

from copy import deepcopy
from fpsupport import IOMonad, IOType


class FileType(IOType):
    """Adds filepath to the IOType"""
    def __init__(self, filepath: str = ""):
        super().__init__("")
        self.filepath: str = filepath


def mprint(a: IOType) -> IOMonad:
    """A simple, monadic print."""
    print(a.contents)
    return IOMonad(a)


def open_text_file(a: FileType) -> IOMonad:
    """Open a utf-8 file and returns its contents as one long string.

    This is a demonstration of a bound function.

    Args:
        a: a structure filepath, error, error_msg, contents

    Returns:
        a new IOMonad
    """
    b = deepcopy(a)
    try:
        with open(b.filepath, "r", encoding="utf-8") as fp:
            b.contents = fp.read()
            b.error = False
            b.error_msg = ""
    except OSError as e:
        b.contents = None
        b.error = True
        b.error_msg = f"opening '{e.filename}' failed with '{e.strerror}'"
    return IOMonad(b)


def set_filepath(io: IOMonad, filepath: str) -> IOMonad:
    '''Populate the Monad with a filepath.'''
    io_struct = io.unwrap()
    io_struct.filepath = filepath
    return IOMonad(io_struct)

# Testing ------------------------------------------------------------------


def print_file_contents(systemcall: IOMonad, filemonad: IOMonad) -> bool:
    """Just a simple function trying to do its thing, testably."""
    fopen = deepcopy(filemonad)
    fopen = set_filepath(fopen, "mkdocs.yml")
    res = (fopen >> open_text_file).unwrap()
    if not res.ok:
        return False
    return (systemcall >> mprint).unwrap().ok


if __name__ == "__main__":
    print_file_contents(IOMonad(IOType("")), IOMonad(FileType("")))
