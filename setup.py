"""Setup file for the test package."""
from setuptools import setup, find_packages

# This import will fail because broken_module.py has a syntax error
from broken_module import VERSION

setup(
    name="failed-build-test",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests==2.19.1",
        "urllib3==1.24.1",
        "pyyaml==5.3.1",
        "flask==0.12.2",
    ],
)
