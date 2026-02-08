"""This module has a syntax error that will cause build to fail."""

VERSION = "1.0.0"

# Intentional syntax error - missing closing parenthesis
def broken_function(
    print("This will never work")
