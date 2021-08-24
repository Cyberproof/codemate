<h1 align="center">CodeMate</h1>

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

Python package, syntax generator, easy to use, OOP API

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

## Documentation

Here will be described the usage of the pack features to generate Python code, 
by a simple and convenient API:

* Block
* Function
* Class
* Method
* File

All of the components inherit from the Block component,
from that we receive the simplicity of the API.

## Block component

The Block component is the base of all of the components, it generates a python syntax
in a new context block.

The Block structure (each section is optional):

1. Docs
2. Imports
3. General Syntax

### Initialization

In the initiation of the Block, the default indentation may be changed, it will set how many
spaces to add before each line multiplied by the indentation.

Each method that inserts/parse lines support indentation as input.

```python
from codemate import Block

block = Block(indentation=4)

```

To generate the code use the following line:

`print(block.syntax())`

### Adding syntax

Syntax lines are referred as general Python code lines, they are inserted as is,
in the given order.

```python
from codemate import Block

block = Block()

# Adding multiple line as block
block.add_syntax_block("""
import math

x = math.sqrt(9)
if x > 3:
""")

# Adding a single line
block.add_syntax_line("print(x)", indent=1)

# Adding a variable
block.add_variable(
    name="y",
    type="float",
    value="x * 3"
)

# Adding multiple lines
block.add_syntax_lines(
    "z = x * y",
    "print(z)"
)

```
   
Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
import math

x = math.sqrt(9)
if x > 3:
    print(x)
y: float = x * 3
z = x * y
print(z)

```

### Adding imports

Specifying syntax lines as imports line provide syntax typo safety, sorting with isort
and inserting after the docs section and before the syntax. Order and content
are modified.

```python
from codemate import Block

block = Block()

# Adding a single import
block.add_import("codemate")

# Adding specific import from a module
block.add_specific_import(
    "codemate",
    "Block",
    "Function",
    "Method",
    "ClassMethod",
    "StaticMethod",
    "Class",
    "File",
)

# Adding multiple imports
block.add_imports(
    "typing",
    "codemate",
    "typing"
)

```
   
Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
import typing

import codemate
from codemate import (Block, Class, ClassMethod, File, Function, Method,
                      StaticMethod)


```

### Adding docs

Specifying syntax lines as doc line inserts it before the imports section and the syntax 
section.

```python
from codemate import Block

block = Block()

# Adding a doc line
block.add_doc_line("Adding a single documentation line to the block")

# Adding multiple doc lines
block.add_doc_lines(
    "",
    "Adding multiple,",
    "documentation lines,",
    "each one of them is in a new line.",
    "",
)

# Adding multiple imports
block.add_doc_block("""
    Adding a block of documentation,
    for adding paragraphs easily.
""")

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Adding a single documentation line to the block

Adding multiple,
documentation lines,
each one of them is in a new line.

Adding a block of documentation,
for adding paragraphs easily.
"""

```

### Extension

Adds other Python block syntax to the current Python block syntax. Ignoring the 
other's docs, copying the imports and adding the syntax.

```python
from codemate import Block

other = Block()

other.add_import("math")

other.add_doc_line("Other doc")

other.add_syntax_block("""
# other syntax
x = math.sqrt(9)
if x > 3:
""")

other.add_syntax_line("print(x)")

block = Block()

block.add_doc_line("Extend example")

block.add_syntax_line("pass")

block.extend(other)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Extend example
"""

import math

pass
# other syntax
x = math.sqrt(9)
if x > 3:
print(x)

```

### Insertion

Inserts as is other Python block syntax to the current Python block syntax. Inserting 
the docs and syntax as is and copying the imports.

```python
from codemate import Block

other = Block()

other.add_import("math")

other.add_doc_line("Other doc")

other.add_syntax_block("""
# other syntax
x = math.sqrt(9)
if x > 3:
""")

other.add_syntax_line("print(x)")

block = Block()

block.add_doc_line("Insert example")

block.add_syntax_line("pass")

block.insert(other)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Insert example
"""

import math

pass
"""
Other doc
"""

# other syntax
x = math.sqrt(9)
if x > 3:
print(x)

```

### Using Black

Will use the [black](https://github.com/psf/black) linter to format the Python syntax.
 
** Note it modifies the content.

```python
from codemate import Block

block = Block()

# complex syntax
block.add_syntax_block("""
    data = [{'userId':'3998e9a3dsdsa', 'related': {'tmp':'example'},
            'emails':['gopo@fake.com', 'tmp@tmp.io', 'ab@ab.io']}]
    print(data)
""")

```

Generating the syntax using `print(block.use_black())`, we will receive:
   
```python
data = [
    {
        "userId": "3998e9a3dsdsa",
        "related": {"tmp": "example"},
        "emails": ["gopo@fake.com", "tmp@tmp.io", "ab@ab.io"],
    }
]
print(data)

```

### Validation

Checks if the generated syntax structure is valid.

```python
from codemate import Block

block = Block()

# complex syntax
block.add_syntax_block("""
    data = ["structure error here -> missing ']'"
    print(data)
""")

# Will raise an exception, the reason is that ']' is missing in the 'data' variable set.
block.validate()

```

## Function component

The Function generates a python function syntax, moreover this is the base of the methods
objects.

### Initialization

```python
from codemate import Function

# Simple function
simple_func = Function(name="simple")
simple_func.add_syntax_line("pass")

# Function with arguments
with_arguments_func = Function(name="with_arguments", arguments=("foo:int", "bar"))
with_arguments_func.add_syntax_line("pass")

# Async function
async_func = Function(name="async", arguments=("foo:int", "bar"))
async_func.add_syntax_line("pass")

# Function with return value type hint
with_rv_func = Function(name="with_rv", return_value="str")
with_rv_func.add_syntax_line("pass")

```

Generating the syntax using `print({function instance}.syntax())`, we will receive:
   
```python
def simple():
    pass

# --------------------------------------------
def with_arguments(foo:int, bar):
    pass

# --------------------------------------------
def async(foo:int, bar):
    pass

# --------------------------------------------
def with_rv() -> str:
    pass

```

### Decorators

```python
from codemate import Function, Block

block = Block()
block.add_specific_import("functools", "lru_cache")

function = Function(name="foo")
function.add_syntax_line("pass")
function.add_decorator("lru_cache()")

block.insert(function)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
from functools import lru_cache

@lru_cache()
def foo():
    pass

```

## Class component

The Class generates a python class syntax.

### Initialization

```python
from codemate import Class

# Simple class
simple_class = Class(name="Simple")
simple_class.add_syntax_line("pass")

# Class with metaclass
with_meta_class = Class(name="WithMeta", metaclass="Simple", inherit=("str",))
with_meta_class.add_syntax_line("pass")

# Class with inheritance
with_inheritance_class = Class(name="WithInheritance", inherit=("str", "WithMeta"))
with_inheritance_class.add_syntax_line("pass")

```

Generating the syntax using `print({class instance}.syntax())`, we will receive:
   
```python
class Simple:
    pass

# --------------------------------------------
class WithMeta(str, metaclass=Simple):
    pass

# --------------------------------------------
class WithInheritance(str, WithMeta):
    pass

```

### Decorators

```python
from codemate import Class, Function, Block

block = Block()

decorator = Function(name="class_decorator", arguments=("cls",))
decorator.add_syntax_line("pass")
block.insert(decorator)

class_ = Class(name="Bar")
class_.add_syntax_line("pass")
class_.add_decorator("class_decorator")
block.insert(class_)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
def class_decorator(cls):
    pass

@class_decorator
class Bar:
    pass

```

## Method component

The Method, ClassMethod, and StaticMethod components inherit from Function and already
contain the relevant adaptation.

## File component

File component is a Block component with relevant capabilities to make Python files 
generation simple.

### Initialization

```python
from codemate import File

# A file with default header
default = File()

# A file with customized header
customized = File(header="-------- Customized Header --------")

```

Generating the syntax using `print({file instance}.syntax())`, we will receive:
   
```python
"""
--------------------------------- Warning generated file ---------------------------------
Generated at: 2021-06-22T15:30:42.222423
------------------------------------------------------------------------------------------
"""

# --------------------------------------------
"""
-------- Customized Header --------
"""

```

### Saving the file

We can save the generated file and specific whether to use black linter on the content 
or not.

```python
from codemate import File

file = File()

# Without black linter
file.save(path="without_black.py")

# With black linter
file.save(path="with_black.py", use_black=True)

```

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
    class_.add_doc_line("A class that represents a raper for a defined API structure.")
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
    A class that represents a raper for a defined API structure.
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

## Development

Use the following command to execute the linters and the unit tests.

Make sure that the linters and the unit tests pass and that the unit tests coverage
is above 90%:

`scripts/test.sh`

Use "pytest-cov" to only execute the unit tests:

`pytest --cov=codemate --cov=tests`

Use the following command to make sure that the linters are passing:

`scripts/lint.sh`

Use "pre-commit" to run the active and passive linters:

* `pre-commit install` - run on every commit.
* `pre-commit run --all-files` - run manually on the repository.
