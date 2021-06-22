# pylint: disable=missing-function-docstring
import isort

from codemate import Block

SINGLE_IMPORT = "math"

SINGLE_IMPORT_RESULT: str = isort.code("import math")

MULTIPLE_IMPORTS = ("math", "sys", "math", "datetime")

MULTIPLE_IMPORTS_RESULT: str = isort.code(
    """
import math
import sys
import datetime
""".strip()
)

SINGLE_SPECIFIC_IMPORT = ("math", "sin")

SINGLE_SPECIFIC_IMPORT_RESULT: str = isort.code("from math import sin")

IMPORTS_COMPLEX_RESULT = """
    import datetime
    import math
    import sys
    from math import sin
""".lstrip(
    "\n"
)


def test_single_import():
    block = Block()
    block.add_import(SINGLE_IMPORT)
    assert SINGLE_IMPORT_RESULT == block.syntax()


def test_multiple_imports():
    block = Block()
    block.add_imports(*MULTIPLE_IMPORTS)
    assert MULTIPLE_IMPORTS_RESULT == block.syntax()


def test_specific_import():
    block = Block()
    block.add_specific_import(*SINGLE_SPECIFIC_IMPORT)
    assert SINGLE_SPECIFIC_IMPORT_RESULT == block.syntax()


def test_complex():
    block = Block()
    block.add_imports(*MULTIPLE_IMPORTS)
    block.add_import(SINGLE_IMPORT)
    block.add_specific_import(*SINGLE_SPECIFIC_IMPORT)
    assert IMPORTS_COMPLEX_RESULT == block.syntax(indent=1)
