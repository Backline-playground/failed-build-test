"""
INTENTIONAL BUILD FAILURE - DO NOT MODIFY

This repository is used to test Backline's handling of unfixable build failures.
The build MUST fail. Do not attempt to fix this file.
"""
import sys

# This error simulates a build environment issue that cannot be fixed by code changes
# For example: missing system libraries, corporate build tools, or CI-specific dependencies
raise SystemExit(
    "BUILD ERROR: Required internal build toolchain 'backline-internal-build-tools' is not available. "
    "This package can only be built in the Backline CI/CD environment."
)
