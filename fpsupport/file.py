"""This module wraps file I/O functions in a monad.

They follow the same pattern: they accept an IOType and additional positional and keyword
arguments.

If IOType.ok is cleared (False), then the function will return immediately without changing the
IOType data. Otherwise, they execute a function and return a monad.

As Python is not a lazy-evaluation language, this will permit pure functions to test its
reaction to an IO error as a simple boolean without mocking.
"""

from typing import Callable


from .decorator import side_effect
from .monad import Monad
from .struct import IOType


@side_effect
def fopen(io: IOType, *args, **kwargs) -> Monad:  # pylint: disable=unused-argument
    """Open a file and send its results into the IOType.

    Args:
        IOType
        args and kwargs

    Returns:
        Monad(IOType) where IOType.contents holds a file pointer
    """
    return Monad(f_try(open, *args, **kwargs))


def f_try(function: Callable, *args, **kwargs) -> IOType:
    """Helper function that wraps a function with a reaction to an OSError."""
    try:
        return IOType(function(*args, **kwargs), "", True)
    except OSError as e:
        return IOType("", f"{e.filename}: {e.strerror}", False)


@side_effect
def fread(io: IOType, *args, **kwargs) -> Monad:
    """Read a file from a file pointer in a monad.

    Args:
        IOType

    Returns:
        Monad(IOType) where IOType.contents are the results of the file read.
    """
    return Monad(f_try(io.contents.read, *args, **kwargs))
