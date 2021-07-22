# pylint: disable=missing-function-docstring
from copy import deepcopy

from codemate import Block
from codemate.exceptions import InputError
from tests import examples

OTHER_BLOCK = Block()
OTHER_BLOCK.add_import("math")
OTHER_BLOCK.add_doc_line("Testing two blocks features")
OTHER_BLOCK.add_syntax_lines("x = math.log2(8) ** 9", "LOGGER.debug(x)")

BLACK_OTHER_BLOCK = deepcopy(OTHER_BLOCK)
BLACK_OTHER_BLOCK.add_syntax_line(
    "result = "
    "{num:num2 for num in range(100) if num * 10 + 10 < 1000 for num2 in range(num)}"
)  # complex line

VALIDATE_OTHER_BLOCK = deepcopy(OTHER_BLOCK)
VALIDATE_OTHER_BLOCK.add_syntax_line("bk45jhb123h5jb13hjvb 4h12das")  # invalid line

EXTEND_RESULT = (
    examples.block.get_syntax()
    + """
x = math.log2(8) ** 9
LOGGER.debug(x)
""".lstrip()
)

INSERT_RESULT = (
    examples.block.get_syntax()
    + """
\"\"\"
Testing two blocks features
\"\"\"

x = math.log2(8) ** 9
LOGGER.debug(x)
""".lstrip()
)

REMOVE_RESULT = (
    examples.block.get_syntax()
    + """
\"\"\"
Testing two blocks features
\"\"\"

x = math.log2(8) ** 9
LOGGER.debug(x)
""".lstrip()
)

BLACK_RESULT = (
    examples.block.get_syntax()
    + """
\"\"\"
Testing two blocks features
\"\"\"

x = math.log2(8) ** 9
LOGGER.debug(x)
result = {
    num: num2 for num in range(100) if num * 10 + 10 < 1000 for num2 in range(num)
}
""".lstrip()
)


TO_STRING_RESULT = """
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

from logging import DEBUG, INFO, Logger, StreamHandler, getLogger

LOGGER: Logger = getLogger(__name__)
LOGGER.setLevel(DEBUG)
_channel = StreamHandler()
_channel.setLevel(INFO)
LOGGER.addHandler(_channel)
LOGGER.debug("✨So far so good✨")
""".lstrip()

CONTAINS_VALUE_TEST = """
The use cases for using this pack may be one of the following:
* Generate Python clients by protocols:
    * OpenAPI
    * AsyncAPI
    * ProtoBuf
* Generate adapters between the code to systems I/O.
""".strip()


def test_extend():
    block = examples.block.get_example()
    block.extend(OTHER_BLOCK)
    assert EXTEND_RESULT == block.syntax()


def test_insert():
    block = examples.block.get_example()
    block.insert(OTHER_BLOCK)
    assert INSERT_RESULT == block.syntax()


def test_remove():
    block = examples.block.get_example()
    block.insert(OTHER_BLOCK)
    block.remove(OTHER_BLOCK)
    assert str(examples.block.get_example()) == block.syntax()


def test_black():
    block = examples.block.get_example()
    block.insert(BLACK_OTHER_BLOCK)
    assert BLACK_RESULT == block.use_black()


# noinspection PyBroadException
def test_validate():
    block = examples.block.get_example()
    block.insert(BLACK_OTHER_BLOCK)
    assert block.validate()
    block = examples.block.get_example()
    block.insert(VALIDATE_OTHER_BLOCK)
    try:
        block.validate()
    except InputError:
        pass
    except Exception:  # pylint: disable=broad-except
        assert False, "Should raise InputError"
    else:
        assert False, "Should raise InputError"


def test_repr():
    block = examples.block.get_example()
    # The content is based on hash functions, therefore it is modified every iteration.
    # We will test only the stable wrapper of the representation.
    representation = repr(block)
    assert representation[0:6] == "Block(" and representation[-1] == ")"


def test_to_string():
    block = examples.block.get_example()
    assert TO_STRING_RESULT == str(block)


def test_contains():
    block = examples.block.get_example()
    assert CONTAINS_VALUE_TEST in block
