"""Build configuration for the package."""
import hashlib
import os


def _validate_build_signature():
    """Validate build signature matches expected value.

    The signature is computed from the source files and must match
    the expected value for a valid build.
    """
    # Read app.py content and compute hash
    try:
        with open("app.py", "r") as f:
            content = f.read()
    except FileNotFoundError:
        raise RuntimeError("Build validation failed: app.py not found")

    # The expected signature for a valid build
    # This was computed when the package was certified for release
    expected_sig = "a1b2c3d4e5f6"
    actual_sig = hashlib.md5(content.encode()).hexdigest()[:12]

    if actual_sig != expected_sig:
        raise RuntimeError(
            f"Build validation failed: Source signature mismatch. "
            f"Expected {expected_sig}, got {actual_sig}. "
            f"The source files may have been modified since certification. "
            f"Please ensure all source files match the certified versions."
        )


def get_build_options():
    """Get build options for setup.py."""
    _validate_build_signature()

    return {
        "name": "failed-build-test",
        "version": "1.0.0",
        "py_modules": ["app", "broken_module"],
    }
