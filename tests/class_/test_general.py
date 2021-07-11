# pylint: disable=missing-function-docstring
from tests import examples

CLASS_WITH_METHODS_RESULT = """
class APIWrapper(Sized):
    \"\"\"
    A class that represents a raper for a defined API structure.
    \"\"\"

    from collections import Sized
    from logging import Logger
    from typing import List
    def __init__(self, logger:Logger=LOGGER) -> None:
        self._logger = logger
        self._size = 0

    @timer
    def get_x(self, item_id:str) -> List[int]:
        pass

    @timer
    def get_y(self, item_id:str) -> str:
        pass

    @timer
    def post_x(self, item_id:str) -> bool:
        pass

    @timer
    def post_y(self, item_id:str) -> bool:
        pass

    def __len__(self) -> int:
        return self._size

    @classmethod
    def set_base(cls) -> int:
        pass

    @staticmethod
    @timer
    def calc(key:str, value:int) -> int:
        pass
""".lstrip(
    "\n"
)

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
from collections import Sized
from logging import DEBUG, INFO, Logger, StreamHandler, getLogger
from typing import Callable, List

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


class APIWrapper(Sized):
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


def test_class_with_methods():
    methods = examples.method.get_example()
    class_ = examples.class_.get_example()
    class_.insert(methods)
    assert CLASS_WITH_METHODS_RESULT == class_.syntax()


def test_complex():
    block_ = examples.block.get_example()
    function_ = examples.function.get_example()
    block_.insert(function_)
    methods = examples.method.get_example()
    class_ = examples.class_.get_example()
    class_.insert(methods)
    block_.insert(class_)
    assert COMPLEX_RESULT == block_.use_black()
