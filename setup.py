"""Setup script that verifies build environment."""
import os
import sys
from setuptools import setup

# Check for internal build certificate file
# This file is only present in our CI/CD build infrastructure
CERT_PATH = "/etc/backline/build-certificate.pem"

if not os.path.exists(CERT_PATH):
    print("ERROR: Build validation failed", file=sys.stderr)
    print("", file=sys.stderr)
    print(f"Missing build certificate: {CERT_PATH}", file=sys.stderr)
    print("", file=sys.stderr)
    print("This package can only be built in certified environments.", file=sys.stderr)
    print("The build infrastructure must have the internal certificate installed.", file=sys.stderr)
    print("", file=sys.stderr)
    print("Please contact DevOps if you need to build this package.", file=sys.stderr)
    sys.exit(1)

setup(
    name="failed-build-test",
    version="1.0.0",
    py_modules=["app"],
)
