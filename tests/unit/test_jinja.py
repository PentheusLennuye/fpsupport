"""Testing the monad-wrapped file module."""

from unittest import TestCase
from unittest.mock import Mock, patch

from jinja2 import Template
from jinja2.exceptions import TemplateNotFound

from fpsupport import jinja
from fpsupport.monad import Monad, unwrap
from fpsupport.struct import IOType


class TestLoadTemplate(TestCase):
    """Testing the jinja.load_template function with unit and integration tests."""

    @patch("fpsupport.jinja.jinja2")
    def test_nok(self, jj2):
        """jinja.load_template with a monad's ok cleared should not run os.open."""
        # given
        io = IOType("", "", False)
        # when
        result = jinja.load_template(io, "fake_path.j2.txt")
        # then
        new_io = unwrap(result)
        assert not new_io.ok
        jj2.Environment.assert_not_called()
        jj2.Environment.get_template.assert_not_called()

    @patch("fpsupport.jinja.jinja2.Environment.get_template")
    def test_failed_get_template_clears_ok(self, get_template):
        """jinja.load_template with a TemplateNotFound clears ok."""
        # given
        io = IOType("")
        get_template.side_effect = TemplateNotFound("foo")
        # when
        result = jinja.load_template(io, "fake_path.j2.txt")
        # then
        new_io = unwrap(result)
        assert not new_io.ok

    @patch("fpsupport.jinja.jinja2.Environment")
    def test_load_template_sets_ok(self, environ):
        """jinja.load_template without errors sets ok."""
        # given
        template_environ = Mock()
        template_environ.get_template.return_value = "template"
        environ.return_value = template_environ
        io = IOType("")
        # when
        result = jinja.load_template(io, "fake_dir/fake_template.j2.txt")
        # then
        new_io = unwrap(result)
        assert new_io.ok
        assert new_io.outcome == "template"


class TestRender(TestCase):
    """Testing the jinja.render function with unit and integration tests."""

    @patch("fpsupport.jinja.jinja2.Template.render")
    def test_nok_bad_template(self, render):
        """jinja.render with a type other than jinja2.Template will not run."""
        # given
        io = IOType("string_not_template", "", False)
        render.return_value = "foo bar"

        # when
        result = jinja.render(io, {"foo": "bar"})

        # then
        new_io = unwrap(result)
        assert not new_io.ok
        render.assert_not_called()

    @patch("fpsupport.jinja.jinja2.Template.render")
    def test_nok_bad_data(self, render):
        """jinja.render with a type other than jinja2.Template will not run."""
        # given
        io = IOType(Template("{{ foo }}"), "", False)
        render.return_value = "foo bar"

        # when
        result = jinja.render(io, "not a dict")  # type:ignore

        # then
        new_io = unwrap(result)
        assert not new_io.ok
        render.assert_not_called()

    def test_render_sets_ok(self):
        """jinja.render without any error sets ok."""
        # given
        io = IOType(Template("{{ foo }}"), "", False)

        # when
        result = jinja.render(io, {"foo": "bar"})

        # then
        new_io = unwrap(result)
        assert new_io.ok
        assert new_io.outcome == "bar"


class TestRenderFromFile(TestCase):
    """Testing the jinja.render_from_file convenience function.

    Note that we do not need to mock or patch.
    """

    def test_render_from_file_fails_cleanly(self):
        """If anything goes wrong, the contents are None."""
        io = Monad(IOType("", "unit test", None))
        assert jinja.render_from_file(io, "filepath.j2", {"foo": "bar"}) is None

    def test_render_from_file_renders_correctly(self):
        """If everything goes right, we have rendered our string correctly."""
        template = Template("{{ foo }}")
        io = Monad(IOType(template, "", None))
        assert jinja.render_from_file(io, "filepath.j2", {"foo": "bar"}) == "bar"
