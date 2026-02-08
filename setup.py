"""Setup script with C extension requiring unavailable system library."""
from setuptools import setup, Extension

# This extension requires libbackline-crypto which is a proprietary
# internal library not available in public package managers.
# The build will fail because the header file doesn't exist.
crypto_extension = Extension(
    'backline_crypto',
    sources=['crypto_module.c'],
    libraries=['backline-crypto'],
    include_dirs=['/usr/include/backline'],
)

setup(
    ext_modules=[crypto_extension],
)
