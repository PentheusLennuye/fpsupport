"""Ensure unit tests work.

File: test/unit/test_identity.py

The pre-commit script will not work if there is no unit tests at all. This
simple file takes care of that.
"""


def test_test():
    """Ensure pytest works at the simplest level."""
    assert True
