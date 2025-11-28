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

Description:

This example uses the functional programming principles of immutable code and
"pure" functions. It may seem silly at first, but this is a toy problem
Think again on the principle of dependency injection: instead of "print()",
think of DB calls requiring input validation.

See test/unit/example/file_and_print.py to see how to unit test the contents.
"""

from copy import deepcopy

from fpsupport import IOMonad, IOType


def open_text_file(a: IOType, *args, **kwargs) -> IOMonad:
    """Open a utf-8 file and returns its contents as one long string.

    This is a demonstration of a bound function. IOType -> IOMonad. It cannot
    guarantee the values, but it always guarantees the type of response.

    Args:
        a: an IOType structure: error, error_msg, contents

    Returns:
        a new IOMonad
    """
    b = deepcopy(a)  # immutable
    try:
        with open(*args, **kwargs) as fp:  # pylint: disable=w1514
            b.contents = fp.read()
            b.ok = True
            b.error_msg = ""
    except OSError as e:
        b.contents = None
        b.ok = False
        b.error_msg = f"opening '{e.filename}' failed with '{e.strerror}'"
    return IOMonad(b)


def print_text(a: IOType) -> IOMonad:
    """A simple print monad."""
    print(a.contents)
    return IOMonad(a)


# An example of using the "open_text_file" and "print_text" IOMonad
# endofunctions

def print_file_contents(fmonad: IOMonad) -> bool:
    """Just a simple function trying to do its thing, testably.

    Note how we use immutable data, even in such a simple function.

    Although this function uses monads, its signature is IOMonad -> bool and
    not IOType -> IOMonad. Therefore, this function does not belong to the
    IOMonad realm and cannot be bound to them.

    It *is*, however, an example of fp programming, as functions are first-
    class objects, immutability is maintained, and this can be tested as
    given inputs will always return the same outputs.
    """
    iomonad = fmonad.flat_map(
        open_text_file, "mkdocs.yml", "r", encoding="utf-8"
    )
    if not iomonad.unwrap().ok:
        return False

    return (iomonad >> print_text).unwrap().ok


if __name__ == "__main__":  # pragma: no cover
    print_file_contents(IOMonad(IOType("")))
