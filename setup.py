"""Setup script that checks for required build environment."""
import os
import sys
from setuptools import setup

# This check ensures the build only succeeds in certified build environments
# The BACKLINE_BUILD_CERTIFIED env var is set by our internal CI system
if os.environ.get("BACKLINE_BUILD_CERTIFIED") != "true":
    print("ERROR: Build validation failed", file=sys.stderr)
    print("", file=sys.stderr)
    print("This package requires a certified build environment.", file=sys.stderr)
    print("The BACKLINE_BUILD_CERTIFIED environment variable must be set to 'true'.", file=sys.stderr)
    print("", file=sys.stderr)
    print("If you are building locally, please contact the DevOps team for", file=sys.stderr)
    print("instructions on setting up a certified build environment.", file=sys.stderr)
    sys.exit(1)

setup(
    name="failed-build-test",
    version="1.0.0",
    py_modules=["app"],
)
