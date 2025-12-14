"""This provides an example of jinja2 templates through monad.

fpsupport/examples/jinja2_templating.py Copyright 2025 George Cummings

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing permissions and limitations under the
License.

---

Description:

Although it adds seemingly needless complication, wrapping Jinja in a monad permits better
proof. Additionally, the _load_template()_ and _render()_ code is very, very reusable. Perhaps the
one-liner on line 54 is all you need in your own program.

"""

import pathlib
import jinja2

from fpsupport.jinja import load_template, render
from fpsupport.monad import Monad, unwrap
from fpsupport.struct import IOType


def render_from_file(io: Monad, template_filepath: str, data: dict) -> str | None:
    """Generate a message from a jinja2 template."""
    result = unwrap(io.flat_map(load_template, template_filepath).flat_map(render, data))
    return result.contents if result.ok else None


if __name__ == "__main__":
    SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
    TEMPLATE = f"{SCRIPT_DIR}/templates/sample.txt.j2"
    m = Monad(IOType())
    render_from_file(m, TEMPLATE, {"holiday": "Birthday", "to": "Mum", "from": "Gus"})


# -- Testing the use of those Jinja 2 operations -------------------------------------------------


def test_render_from_file_fails():
    """Ensure that the message is None on failure."""
    io = Monad(IOType("", "unit test", False))  # "False" means simulate the IO failing.
    assert render_from_file(io, "no_path", {"x": "1", "y": "2", "z": "5"}) is None


def test_render_from_file_renders_correctly():
    """Ensure that the message generates correctly."""
    # given
    template = jinja2.Template("{{ x }}{{ y }}{{ z }}")
    io = Monad(IOType(template, "", None))  # "None" means simulate the IO passing

    # when
    result = render_from_file(io, "no_path", {"x": "1", "y": "2", "z": "5"})

    # then
    assert result == "125"
