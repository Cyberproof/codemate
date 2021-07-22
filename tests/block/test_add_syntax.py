# pylint: disable=missing-function-docstring

from codemate import Block

SYNTAX_LINE = "print('hello world')"

SYNTAX_LINE_RESULT = f"{SYNTAX_LINE}\n"

SYNTAX_LINES = (
    "greet = True",
    "if greet:",
    "    print('hello world')",
    "else:",
    "    pass",
)

SYNTAX_LINES_RESULT = "\n".join(SYNTAX_LINES) + "\n"

SYNTAX_BLOCK = """
multi = lambda: x: x*9
number = multi(9)
print(number)
""".strip(
    "\n"
)

SYNTAX_BLOCK_RESULT = SYNTAX_BLOCK + "\n"

SINGLE_VARIABLE = dict(name="round", type="int", value="50")

SINGLE_VARIABLE_RESULT = "round: int = 50\n"

SYNTAX_COMPLEX_RESULT = """
    round: int = 50
    multi = lambda: x: x*9
    number = multi(9)
    print(number)
    greet = True
    if greet:
        print('hello world')
    else:
        pass
    round: int = 50
    print('hello world')
""".lstrip(
    "\n"
)
SYNTAX_COMPLEX_REMOVE_RESULT = """
    multi = lambda: x: x*9
    number = multi(9)
    print(number)
    greet = True
    if greet:
        print('hello world')
    else:
        pass
    round: int = 50
""".lstrip(
    "\n"
)
EMPTY_RESULT = ""


def test_single_line():
    block = Block()
    block.add_syntax_line(SYNTAX_LINE)
    assert SYNTAX_LINE_RESULT == block.syntax()


def test_remove_single_line():
    block = Block()
    block.add_syntax_line(SYNTAX_LINE)
    block.remove_syntax_line(SYNTAX_LINE)
    assert EMPTY_RESULT == block.syntax()


def test_multiple_lines():
    block = Block()
    block.add_syntax_lines(*SYNTAX_LINES)
    assert SYNTAX_LINES_RESULT == block.syntax()


def test_remove_multiple_lines():
    block = Block()
    block.add_syntax_lines(*SYNTAX_LINES)
    block.remove_syntax_lines(*SYNTAX_LINES)
    assert EMPTY_RESULT == block.syntax()


def test_single_block():
    block = Block()
    block.add_syntax_block(SYNTAX_BLOCK)
    assert SYNTAX_BLOCK_RESULT == block.syntax()


def test_remove_single_block():
    block = Block()
    block.add_syntax_block(SYNTAX_BLOCK)
    block.remove_syntax_block(SYNTAX_BLOCK)
    assert EMPTY_RESULT == block.syntax()


def test_single_variable():
    block = Block()
    block.add_variable(**SINGLE_VARIABLE)
    assert SINGLE_VARIABLE_RESULT == block.syntax()


def test_remove_single_variable():
    block = Block()
    block.add_variable(**SINGLE_VARIABLE)
    block.remove_variable(**SINGLE_VARIABLE)
    assert EMPTY_RESULT == block.syntax()


def test_complex():
    block = Block()
    block.add_variable(**SINGLE_VARIABLE)
    block.add_syntax_block(SYNTAX_BLOCK)
    block.add_syntax_lines(*SYNTAX_LINES)
    block.add_variable(**SINGLE_VARIABLE)
    block.add_syntax_line(SYNTAX_LINE)
    assert SYNTAX_COMPLEX_RESULT == block.syntax(indent=1)


def test_remove_complex():
    block = Block()
    block.add_variable(**SINGLE_VARIABLE)
    block.add_syntax_block(SYNTAX_BLOCK)
    block.add_syntax_lines(*SYNTAX_LINES)
    block.add_variable(**SINGLE_VARIABLE)
    block.add_syntax_line(SYNTAX_LINE)
    block.remove_variable(**SINGLE_VARIABLE)
    block.remove_syntax_line(SYNTAX_LINE)
    assert SYNTAX_COMPLEX_REMOVE_RESULT == block.syntax(indent=1)
