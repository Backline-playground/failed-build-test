"""This module imports a non-existent package that will cause build to fail."""

# This import has valid syntax but the module doesn't exist.
# The AI cannot fix this because the package doesn't exist.
# This will cause setup.py to fail when it tries to import VERSION.
import nonexistent_internal_backline_xyz_pkg  # noqa: F401

VERSION = "1.0.0"


def example_function():
    """Example function that would work if the import wasn't broken."""
    print("This function would work")
