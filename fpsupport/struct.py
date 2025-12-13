"""Structures that can be passed into base monads."""

from typing import Any
from dataclasses import dataclass


@dataclass
class IOType:
    """A type used in a Monad to capture IO side effects: contents, errors, and error messages."""

    def __init__(self, contents: Any = None, error_msg: str | None = None, ok: bool | None = True):
        """Initialize IOType, ensuring values are of type."""
        self.contents: Any = contents
        if not isinstance(error_msg, str | None):
            raise TypeError("IOType attribute 'error_msg' must be of type str or None")

        self.error_msg: str | None = error_msg

        if not isinstance(ok, bool | None):
            raise TypeError("IOType attribute 'ok' must be of type bool or None")
        self.ok: bool | None = ok
