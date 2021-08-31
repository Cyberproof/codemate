# Function component

The Function generates a python function syntax, moreover this is the base of the methods
objects.

## Initialization

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

## Decorators

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