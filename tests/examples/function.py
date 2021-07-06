from copy import deepcopy
from functools import partial

from codemate import Function
from tests import utils

# Note:
# This generated code must be part of an upper block to pass the imports to greater level

_FUNCTION = Function(
    name="timer", arguments=("func:Callable",), return_value="Callable"
)
_FUNCTION.add_doc_block(
    """
    A decorator that times the execution of the wrapped function.

    Args:
        func (Callable): The wrapped function.
""".strip(
        "\n"
    )
)
_FUNCTION.add_specific_import("typing", "Callable")
_INNER_DECORATOR = Function(name="decorator", arguments=("*args", "**kwargs"))
_INNER_DECORATOR.add_import("time")
_INNER_DECORATOR.add_syntax_block(
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
_FUNCTION.insert(_INNER_DECORATOR)
_FUNCTION.add_syntax_line("return decorator")

_SYNTAX = """
def timer(func:Callable) -> Callable:
    \"\"\"
    A decorator that times the execution of the wrapped function.

    Args:
        func (Callable): The wrapped function.
    \"\"\"

    import time
    from typing import Callable
    def decorator(*args, **kwargs):
        start = time.perf_counter()
        return_value = func(*args, **kwargs)
        end = time.perf_counter()
        name = getattr(func, "__name__", "UnKnown")
        LOGGER.info(f"The execution of '{name}' took {end - start:0.4f} seconds")
        return return_value

    return decorator
""".lstrip()


def get_example() -> Function:
    """
    Factory function that returns a copy of an example of Function object for tests
        and POCs.

    Returns:
        Function: The copy of the Function object instance.
    """
    return deepcopy(_FUNCTION)


get_syntax = partial(utils.get_syntax, postfix=_SYNTAX)
