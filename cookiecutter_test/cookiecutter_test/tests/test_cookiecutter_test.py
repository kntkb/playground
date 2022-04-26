"""
Unit and regression test for the cookiecutter_test package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import cookiecutter_test


def test_cookiecutter_test_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "cookiecutter_test" in sys.modules
