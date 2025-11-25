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
"pure" functions. It may seem silly at first, but this is a toy problem
Think again on the principle of dependency injection: instead of "print()",
think of DB calls requiring input validation.
"""

from copy import deepcopy
from typing import Callable

from fpsupport import IOMonad, IOType


class FileType(IOType):
    """Adds filepath to the IOType"""
    def __init__(self, fn: Callable, filepath: str = ""):
        super().__init__(fn, "")
        self.filepath: str = filepath


def open_text_file(a: FileType) -> IOMonad:
    """Open a utf-8 file and returns its contents as one long string.

    This is a demonstration of a bound function.

    Args:
        a: a structure filepath, error, error_msg, contents

    Returns:
        a new IOMonad
    """
    b = deepcopy(a)  # immutable
    try:
        with open(b.filepath, "r", encoding="utf-8") as fp:
            b.contents = fp.read()
            b.ok = True
            b.error_msg = ""
    except OSError as e:
        b.contents = None
        b.ok = False
        b.error_msg = f"opening '{e.filename}' failed with '{e.strerror}'"
    return IOMonad(b)


# Testing ------------------------------------------------------------------

def print_file_contents(fmonad: IOMonad, pmonad: IOMonad) -> bool:
    """Just a simple function trying to do its thing, testably.

    Note how we use immutable data, even in such a simple function.

    Although this function uses monads, it itself does not belong to the
    IOMonad realm and cannot be bound to them.

    It *is*, however, an example of fp programming, as functions are first-
    class objects, immutability is maintained, and this can be tested as
    given inputs will always return the same outputs. In this case,
    print_file_contents is merely an AND gate.
    """
    res = fmonad.call().unwrap()
    if not res.ok:
        return False

    printer = deepcopy(pmonad)  # immutability
    printer.a.contents = res.contents

    # Looking for ok is silly, because print() is not going to fail.
    return printer.call().unwrap().ok


if __name__ == "__main__":  # pragma: no cover
    print_file_contents(
        IOMonad(FileType(open_text_file, "mkdocs.yml")),
        IOMonad(IOType((lambda x: print(x.contents) or IOMonad(x)), ""))
    )
