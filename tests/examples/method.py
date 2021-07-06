from copy import deepcopy
from functools import partial
from typing import List

from codemate import Block, ClassMethod, Function, Method, StaticMethod
from tests import utils

_API_STRUCTURE = [
    {"operation_name": "get_x", "return_value": "List[int]"},
    {"operation_name": "get_y", "return_value": "str"},
    {"operation_name": "post_x", "return_value": "bool"},
    {"operation_name": "post_y", "return_value": "bool"},
]

_METHODS: List[Function] = []

_INIT = Method("__init__", arguments=("logger:Logger=LOGGER",), return_value="None")
_INIT.add_specific_import("logging", "Logger")
_INIT.add_specific_import("typing", "List")
_INIT.add_variable("self._logger", value="logger")
_INIT.add_variable("self._size", value="0")

_METHODS.append(_INIT)

for _operation in _API_STRUCTURE:
    _name, _return_value = _operation.values()
    _method = Method(_name, arguments=("item_id:str",), return_value=_return_value)
    _method.add_decorator("timer")
    _method.add_syntax_line("pass")
    _METHODS.append(_method)

_LEN = Method("__len__", return_value="int")
_LEN.add_syntax_line("return self._size")

_METHODS.append(_LEN)

_CLASS_METHOD = ClassMethod("set_base", return_value="int")
_CLASS_METHOD.add_syntax_line("pass")

_METHODS.append(_CLASS_METHOD)

_STATIC_METHOD = StaticMethod(
    "calc",
    arguments=(
        "key:str",
        "value:int",
    ),
    return_value="int",
)
_STATIC_METHOD.add_decorator("timer")
_STATIC_METHOD.add_syntax_line("pass")

_METHODS.append(_STATIC_METHOD)

_BLOCK = Block()

for _item in _METHODS:
    _BLOCK.insert(_item)

_SYNTAX = """
from typing import List

from logging import Logger

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
""".lstrip()


def get_example() -> Block:
    """
    Factory class that returns a copy of an example of Class object for tests
        and POCs.

    Returns:
        Method: The copy of the Function object instance.
    """
    return deepcopy(_BLOCK)


get_syntax = partial(utils.get_syntax, postfix=_SYNTAX)
