import black


class GenerationError(Exception):
    """Represents an exception while generating the Python syntax"""


class PythonSyntaxError(GenerationError):
    """Represents an exception in the python syntax"""


class InputError(GenerationError, black.InvalidInput):
    """Raised when the generated Python code isn't valid by black"""


class SaveFileError(GenerationError, OSError):
    """Raised when the generated Python code file can't be created"""
