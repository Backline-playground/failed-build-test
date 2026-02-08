"""Setup script for the package."""
from setuptools import setup

# Try to import the build configuration module
# This import will fail because build_config.py has an error
try:
    from build_config import get_build_options
    options = get_build_options()
except ImportError:
    # Fallback - but this also fails because we need build_config
    raise RuntimeError(
        "Build configuration error: Cannot import 'get_build_options' from build_config. "
        "Please ensure build_config.py defines the get_build_options() function correctly."
    )

setup(**options)
