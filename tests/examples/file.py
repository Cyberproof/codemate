from copy import deepcopy
from functools import partial

from codemate import File
from tests import utils
from tests.examples.block import get_example as get_block_example
from tests.examples.class_ import get_example as get_class_example
from tests.examples.function import get_example as get_function_example
from tests.examples.method import get_example as get_method_example

_HEADER = """
--------------------------------- Warning generated file ---------------------------------
Generated by: foo
------------------------------------------------------------------------------------------
""".strip()

_File = File(header=_HEADER)
_File.insert(get_block_example())
_File.insert(get_function_example())
_METHODS = get_method_example()
_CLASS = get_class_example()
_CLASS.insert(_METHODS)
_File.insert(_CLASS)

_SYNTAX = """
\"\"\"
--------------------------------- Warning generated file ---------------------------------
Generated by: foo
------------------------------------------------------------------------------------------
\"\"\"

import time
from collections import Sized
from logging import DEBUG, INFO, Logger, StreamHandler, getLogger
from typing import Callable, List

\"\"\"
---------------------------------------- Example -----------------------------------------
This is an example of how to use this Python package to generate easily and safely
Python syntax.

The use cases for using this pack may be one of the following:
* Generate Python clients by protocols:
    * OpenAPI
    * AsyncAPI
    * ProtoBuf
* Generate adapters between the code to systems I/O.

Easily generating python code without the need to care for styling and indentation.

------------------------------------------------------------------------------------------
\"\"\"

LOGGER: Logger = getLogger(__name__)
LOGGER.setLevel(DEBUG)
_channel = StreamHandler()
_channel.setLevel(INFO)
LOGGER.addHandler(_channel)
LOGGER.debug("✨So far so good✨")


def timer(func: Callable) -> Callable:
    \"\"\"
    A decorator that times the execution of the wrapped function.

    Args:
        func (Callable): The wrapped function.
    \"\"\"

    def decorator(*args, **kwargs):
        start = time.perf_counter()
        return_value = func(*args, **kwargs)
        end = time.perf_counter()
        name = getattr(func, "__name__", "UnKnown")
        LOGGER.info(f"The execution of '{name}' took {end - start:0.4f} seconds")
        return return_value

    return decorator


class APIWrapper(
    Sized,
):
    \"\"\"
    A class that represents a raper for a defined API structure.
    \"\"\"

    def __init__(self, logger: Logger = LOGGER) -> None:
        self._logger = logger
        self._size = 0

    @timer
    def get_x(self, item_id: str) -> List[int]:
        pass

    @timer
    def get_y(self, item_id: str) -> str:
        pass

    @timer
    def post_x(self, item_id: str) -> bool:
        pass

    @timer
    def post_y(self, item_id: str) -> bool:
        pass

    def __len__(self) -> int:
        return self._size

    @classmethod
    def set_base(cls) -> int:
        pass

    @staticmethod
    @timer
    def calc(key: str, value: int) -> int:
        pass
""".lstrip()


def get_example() -> File:
    """
    Factory function that returns a copy of an example of Function object for tests
        and POCs.

    Returns:
        Function: The copy of the Function object instance.
    """
    return deepcopy(_File)


get_syntax = partial(utils.get_syntax, postfix=_SYNTAX)
