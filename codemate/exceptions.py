import black


class GenerationError(Exception):
    """Represents an exception while generating the Python syntax"""


class PythonSyntaxError(GenerationError, SyntaxError):
    """Represents an exception in the Python syntax"""


class InputError(GenerationError, black.InvalidInput, ValueError):
    """
    Raised when the generated Python code isn't valid.
    Deprecation - in version 1.0.0, black.InvalidInput inheritance will be removed.
    """


class SaveFileError(GenerationError, OSError):
    """Raised when the generated Python code file can't be created"""
