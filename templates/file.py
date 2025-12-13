"""A one-line summary of the module or program, ended with a period.

[Module Name] Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Description:

This is an overall description of the module. If any classes or functions are
meant for export, list them.

Typical usage example:

  import fpsupport as fp

  m = fp.Maybe(Some(None))
  m >> f >> g >> None
"""

from typing import Any


class X:
    """Summary of class.

    Longer class information

    Attributes:
        thing_a:
        thing_b:
    """

    def __init__(self):
        """Initiate an X object.

        Args:
            thing_a: description of thing_a
            thing_b: description of thing_b

        Returns:
            object X

        Raises:
            Fizzbuzz error
        """
        self.thing_a: Any = None
        self.thing_b: Any = None

    def public_function(self, my_var: Any) -> int:
        """The summary of the function ended with a period.

        A deeper description if necessary so long as the information is useful.
        One should not need to describe easy-to-understand algorithms but
        perhaps the reason for it.

        Args:
            my_var: the denominator of the fizzbuzz.

        Returns:
            The fizzbuzz algorithm major version as an integer.

        Raises:
            FizzBuzzError if fizzbuzz cannot blog.

        """
        return int(my_var)
