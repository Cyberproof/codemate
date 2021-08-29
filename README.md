<h1 align="center">CodeMate</h1>

<p align="center">
    <em>Python syntax generator based on Object-Oriented Programing, type hints, and simplicity.</em>
</p>

<p align="center">
    <a href="https://github.com/Cyberproof/codemate/actions?query=workflow%3ATest" target="_blank">
        <img src="https://github.com/Cyberproof/codemate/workflows/Test/badge.svg" alt="Test">
    </a>
    <a href="https://pypi.org/project/codemate/" target="_blank">
        <img src="https://img.shields.io/pypi/v/codemate?color=%2334D058&label=pypi" alt="Version">
    </a>
    <a href="https://pypi.org/project/codemate/" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/codemate.svg?color=%2334D058&label=python" alt="Support">
    </a>
    <a href="https://pypi.org/project/codemate/" target="_blank">
        <img src="https://img.shields.io/pypi/l/codemate?color=%2334D058&label=license" alt="Support">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

## Goals

Easily generating python code without the need to care for styling and typo's.

## Use Cases

The use cases for using this pack may be one of the following:

* Generate Python clients by protocols:

    * OpenAPI

    * AsyncAPI

    * ProtoBuf

* Generate adapters between the code to services I/O.

## Set Up

`pip install codemate`

## Versioning

This project is based on [Semantic Versioning 2.0.0](https://semver.org/#semantic-versioning-200) 
methodology.

## Use case example

An example of how to use the components in this Python package to generate a client by 
API.

```python
from typing import Tuple

from codemate import Class, ClassMethod, File, Function, Method, StaticMethod

DECORATOR_NAME = "timer"

API_STRUCTURE = [
    {"operation_name": "get_x", "return_value": "List[int]"},
    {"operation_name": "get_y", "return_value": "str"},
    {"operation_name": "post_x", "return_value": "bool"},
    {"operation_name": "post_y", "return_value": "bool"},
]


def _set_file_docs(file: File) -> None:
    file.add_doc_lines(
        " Example ".center(90, "-"),
        "This is an example of how to use this Python package to generate easily and safely",
        "Python syntax.",
    )
    file.add_doc_line("")
    file.add_doc_block(
        """
        The use cases for using this pack may be one of the following:
        * Generate Python clients by protocols:
            * OpenAPI
            * AsyncAPI
            * ProtoBuf
        * Generate adapters between the code to systems I/O.

        Easily generating python code without the need to care for styling and indentation.
    """.strip(
            "\n"
        )
    )
    file.add_doc_line("")
    file.add_doc_line("".center(90, "-"))


def _create_file_base() -> File:
    file = File()
    _set_file_docs(file)
    file.add_specific_import("logging", "getLogger")
    file.add_specific_import("logging", "INFO, StreamHandler")
    file.add_specific_import("logging", "DEBUG", "Logger")
    file.add_variable("LOGGER", type="Logger", value="getLogger(__name__)")
    file.add_syntax_block(
        """
        LOGGER.setLevel(DEBUG)
        _channel = StreamHandler()
        _channel.setLevel(INFO)
        LOGGER.addHandler(_channel)
        LOGGER.debug("✨So far so good✨")
    """.strip(
            "\n"
        )
    )
    return file


def _create_inner_function() -> Function:
    function = Function(name="decorator", arguments=("*args", "**kwargs"))
    function.add_import("time")
    function.add_syntax_block(
        """
        start = time.perf_counter()
        return_value = func(*args, **kwargs)
        end = time.perf_counter()
        name = getattr(func, "__name__", "UnKnown")
        LOGGER.info(f"The execution of '{name}' took {end - start:0.4f} seconds")
        return return_value
    """.strip(
            "\n"
        )
    )
    return function


def _create_decorator():
    function = Function(
        name=DECORATOR_NAME, arguments=("func:Callable",), return_value="Callable"
    )
    function.add_doc_block(
        """
        A decorator that times the execution of the wrapped function.

        Args:
            func (Callable): The wrapped function.
    """.strip(
            "\n"
        )
    )
    function.add_specific_import("typing", "Callable")
    inner_function = _create_inner_function()
    function.insert(inner_function)
    function.add_syntax_line("return decorator")
    return function


def _create_init() -> Method:
    method = Method(
        "__init__", arguments=("logger:Logger=LOGGER",), return_value="None"
    )
    method.add_specific_import("logging", "Logger")
    method.add_specific_import("typing", "List")
    method.add_variable("self._logger", value="logger")
    method.add_variable("self._size", value="0")
    return method


def _create_operations() -> Tuple[Method, ...]:
    methods = []
    for _operation in API_STRUCTURE:
        _name, _return_value = _operation.values()
        _method = Method(_name, arguments=("item_id:str",), return_value=_return_value)
        _method.add_decorator("timer")
        _method.add_syntax_line("pass")
        methods.append(_method)
    return tuple(methods)


def _create_calc_method() -> StaticMethod:
    method = StaticMethod(
        "calc",
        arguments=(
            "key:str",
            "value:int",
        ),
        return_value="int",
    )
    method.add_decorator("timer")
    method.add_syntax_line("pass")
    return method


def _create_methods() -> Tuple[Function, ...]:
    methods = []
    methods.append(_create_init())
    methods.extend(_create_operations())
    len_ = Method("__len__", return_value="int")
    len_.add_syntax_line("return self._size")
    methods.append(len_)
    set_base_method = ClassMethod("set_base", return_value="int")
    set_base_method.add_syntax_line("pass")
    methods.append(set_base_method)
    methods.append(_create_calc_method())
    return tuple(methods)


def _create_class() -> Class:
    class_ = Class(name="APIWrapper", inherit=("Sized",))
    class_.add_doc_line("A class that represents a generated client for a defined API structure.")
    class_.add_specific_import("collections", "Sized")
    class_.add_specific_import("logging", "Logger")
    for method in _create_methods():
        class_.insert(method)
    return class_


def main():
    """
    An example of how to use the components in this Python package to generate a client
    by API.
    """
    file = _create_file_base()
    file.insert(_create_decorator())
    file.insert(_create_class())
    return file

```

Generating the syntax using `print(block.use_black())`, we will receive:
   
```python
"""
--------------------------------- Warning generated file ---------------------------------
Generated at: 2021-07-11T13:10:57.071246
------------------------------------------------------------------------------------------
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
"""

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
    """
    A decorator that times the execution of the wrapped function.

    Args:
        func (Callable): The wrapped function.
    """

    def decorator(*args, **kwargs):
        start = time.perf_counter()
        return_value = func(*args, **kwargs)
        end = time.perf_counter()
        name = getattr(func, "__name__", "UnKnown")
        LOGGER.info(f"The execution of '{name}' took {end - start:0.4f} seconds")
        return return_value

    return decorator


class APIWrapper(Sized):
    """
    A class that represents a generated client for a defined API structure.
    """

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

```
