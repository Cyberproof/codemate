# pylint: disable=missing-function-docstring

from codemate import Block

SYNTAX_BLOCK = """
def add(x: int, y:int):
    return x + y

print(add(1,1))
""".strip(
    "\n"
)

INDENTED_BLOCK = """
    def add(x: int, y:int):
        return x + y

    print(add(1,1))
""".strip(
    "\n"
)

NEW_LINE_BLOCK = """
def add(x: int, y:int):
    return x + y

print(add(1,1))
""".rstrip(
    "\n"
)

INDENTED_NEW_LINE_BLOCK = """
    def add(x: int, y:int):
        return x + y

    print(add(1,1))
""".rstrip(
    "\n"
)


def test_default():
    block = Block()
    assert SYNTAX_BLOCK == block.parse_block(SYNTAX_BLOCK)


def test_indented_block():
    block = Block()
    assert INDENTED_BLOCK == block.parse_block(INDENTED_BLOCK)
    assert INDENTED_BLOCK == block.parse_block(SYNTAX_BLOCK, indent=1)


def test_new_line_block():
    block = Block()
    assert NEW_LINE_BLOCK == block.parse_block(NEW_LINE_BLOCK)
    assert NEW_LINE_BLOCK == block.parse_block(SYNTAX_BLOCK, new_line=1)


def test_indented_new_line_block():
    block = Block()
    assert INDENTED_NEW_LINE_BLOCK == block.parse_block(INDENTED_NEW_LINE_BLOCK)
    result = block.parse_block(SYNTAX_BLOCK, indent=1, new_line=1)
    assert INDENTED_NEW_LINE_BLOCK == result
