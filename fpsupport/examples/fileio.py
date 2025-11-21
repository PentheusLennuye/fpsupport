"""fileio.py is an example of using an IO Monad.

This uses the functional programming principles of immutable code and "pure"
functions.
"""

from copy import deepcopy
from fpsupport import IOMonad, IOType


class FileType(IOType):
    """Adds filepath to the IOType"""
    def __init__(self, filepath: str = ""):
        super().__init__("")
        self.filepath: str = filepath


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


def do_stuff(io: IOMonad, filepath: str) -> str | None:
    """Just a function trying to do its thing, testably."""
    new_io = set_filepath(io, filepath)
    res = (new_io >> open_text_file).unwrap()
    if res.ok:
        return res.contents
    else:
        return None


if __name__ == "__main__":
    FILEPATH = "mkdocs.yml"
    print(do_stuff(IOMonad(FileType("")), FILEPATH))
