"""Basic Jinja Operations wrapped in I/O Monads."""

import pathlib

import jinja2

from .decorator import side_effect
from .struct import IOType
from .monad import Monad, unwrap


@side_effect
def load_template(io: IOType, file_path: str) -> Monad:  # pylint: disable=unused-argument
    """Load a Jinja2 template from disk.

    Args:
        io: an unwrapped monad with content, error_msg, ok
        file_path: the direct path to a template.

    Returns:
        a monad wrapped around IOType:
           contents: a jinja2 template, correctly formatted.
    """
    template_dir = pathlib.Path(file_path).resolve().parent
    filename = pathlib.Path(file_path).name
    try:
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
        return Monad(IOType(env.get_template(filename), "", True))
    except jinja2.TemplateNotFound as e:
        return Monad(IOType("", e.message, False))


def render(io: IOType, data: dict) -> Monad:  # pylint: disable=unused-argument
    """Pass data through a jinja2 template and returns its contents.

    Args:
        io: An IOType whose contents are a jinja template
        data: a dictionary of values to be merged with the template

    Returns:
        a monad wrapped around IOType:
           contents: a string combining the data with the template
    """
    if not isinstance(io.contents, jinja2.Template):
        return Monad(io)
    if not isinstance(data, dict):
        return Monad(IOType("", f"data invalid type {str(type(data))}", False))
    template = io.contents
    return Monad(IOType(template.render(data), "", True))


def render_from_file(io: Monad, template_filepath: str, data: dict) -> str | None:
    """Generate a message from a jinja2 template."""
    result = unwrap(io.flat_map(load_template, template_filepath).flat_map(render, data))
    return result.contents if result.ok else None
