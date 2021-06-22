from copy import deepcopy
from functools import partial

from codemate import Block
from tests import utils

_BLOCK = Block()
_BLOCK.add_doc_lines(
    " Example ".center(90, "-"),
    "This is an example of how to use this Python package to generate easily and safely",
    "Python syntax.",
)
_BLOCK.add_doc_line("")
_BLOCK.add_doc_block(
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
_BLOCK.add_doc_line("")
_BLOCK.add_doc_line("".center(90, "-"))
_BLOCK.add_specific_import("logging", "getLogger")
_BLOCK.add_specific_import("logging", "INFO, StreamHandler")
_BLOCK.add_specific_import("logging", "DEBUG", "Logger")
_BLOCK.add_variable("LOGGER", type="Logger", value="getLogger(__name__)")
_BLOCK.add_syntax_block(
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


_SYNTAX = """
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

import math
from logging import DEBUG, INFO, Logger, StreamHandler, getLogger

LOGGER: Logger = getLogger(__name__)
LOGGER.setLevel(DEBUG)
_channel = StreamHandler()
_channel.setLevel(INFO)
LOGGER.addHandler(_channel)
LOGGER.debug("✨So far so good✨")
""".lstrip()


def get_example() -> Block:
    """
    Factory function that returns a copy of an example of Block object for tests and POCs.

    Returns:
        Block: The copy of the Block object instance.
    """
    return deepcopy(_BLOCK)


get_syntax = partial(utils.get_syntax, postfix=_SYNTAX)
