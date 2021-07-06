# pylint: disable=missing-function-docstring
from tests import examples

INITIATION_RESULT = examples.function.get_syntax()

COMPLEX_RESULT = """
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

import time
from logging import DEBUG, INFO, Logger, StreamHandler, getLogger
from typing import Callable

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
""".lstrip()


def test_initiation():
    function_ = examples.function.get_example()
    assert INITIATION_RESULT == function_.syntax()


def test_complex():
    block_ = examples.block.get_example()
    function_ = examples.function.get_example()
    block_.insert(function_)
    assert COMPLEX_RESULT == block_.use_black()
