"""FPSupport provides libraries to assist in fp programming."""

from .monad import Monad
from .io_monad import IOMonad, IOType

__all__ = ["Monad", "IOMonad", "IOType"]
