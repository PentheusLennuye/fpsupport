"""The IO Monad

fpsupport/io_monad.py Copyright 2025 George Cummings

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

A "side effect" is any transfer of data into and out of a function that does
not go through the function call or its return.

def my_impure_function(a: int) -> None:
    print(a)   # Side effect! A call to the system.

def my_second_impure_function(a: dict) -> None:
    a["wolf"] = "in the fold"  # Side effect!
                               # The function changed a memory location outside
                               # the function's scope.

A function that contains any side effect is called "impure." This sounds pretty
awful, but being "impure" is not a criticism, just a label. Any function that
prints to screen is impure. Any function that writes to disk, moves a robotic
arm, or merely sends information to the operating system is impure. Of course,
outside academics, a program is useless outside if it cannot change the outside
environment.

Nonetheless, there is a huge advantage to keeping side effects outside
functions as much as possible: provability without relying heavily on patching
and fixtures, and easy-to-understand structure.

To do this,

- use a monad to encapsulate a side-effect call
- ensure the monad has clearly defined, testable outcomes
- pass the monad to functions as one of its arguments.

The IO Monad I propose uses this structure to deal with any call where the
results are not known: system calls that might break; calls to network APIs;
calls for random numbers, and so on.

-----

Typical usage example. open_text_file() and FileType would be defined in a
user-defined library to the side of the main workflow.

# module_a: file IO -------------------

from copy import deepcopy
from fpsupport import IOMonad, IOType

class FileType(IOType):
    '''Adds filepath to the IOType'''
    def __init__(self, filepath: str = ""):
        super().__init__("")
        self.filepath: str = filepath


def open_text_file(a: FileType) -> IOMonad:
    '''A bound function'''
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


main workflow ------------

import module_a

def do_stuff(io: module_a.IOMonad) -> str:
    '''Just a function trying to do its thing, testably.'''
    #
    # ...
    #
    new_io = module_a.set_filepath(io, "mkdocs.yml")
    res = (io.set_filepath("mkdocs.yml") >> module_a.open_text_file).unwrap()
    if res.ok:
        return res.contents
    ... do something else

io = IOMonad(module_a.FileType())
print(do_stuff(io))
"""

from dataclasses import dataclass
from typing import Self, Optional, TypeVar

from fpsupport import Monad

T = TypeVar("T")


@dataclass
class IOType:
    """A structure that is passed to an IOMonad as its sole argument."""
    contents: Optional[T]
    ok: bool = True
    error_msg: str = ""


class IOMonad(Monad):
    """IOMonad encapsulates any call with an uncertain result.

    It is meant to be passed as an argument to a function with the uncertainty
    reduced to known attributes and types.
    """
    def __init__(self, a: IOType) -> Self:
        super().__init__(a)

    @staticmethod
    def unit(a: IOType) -> Self:
        """Type converter a -> M a."""
        return IOMonad(a)
