from copy import deepcopy
from functools import partial

from codemate import Class
from tests import utils

# Note:
# This generated code must be part of an upper block to pass the imports to greater level

_CLASS = Class(name="APIWrapper", inherit=("Sized",))
_CLASS.add_doc_line("A class that represents a raper for a defined API structure.")
_CLASS.add_specific_import("collections", "Sized")
_CLASS.add_specific_import("logging", "Logger")

_SYNTAX = """
class APIWrapper(Sized,):
    \"\"\"
    A class that represents a raper for a defined API structure.
    \"\"\"

    from collections import Sized
    from logging import Logger
""".lstrip()


def get_example() -> Class:
    """
    Factory class that returns a copy of an example of Class object for tests
        and POCs.

    Returns:
        Class: The copy of the Function object instance.
    """
    return deepcopy(_CLASS)


get_syntax = partial(utils.get_syntax, postfix=_SYNTAX)
