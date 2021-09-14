import ast
import re
from typing import NamedTuple

# todo get from pack config
ERROR_CONTEXT_PADDING = 2
ERROR_MESSAGE_PATTERN = re.compile(rf"Cannot parse: (?P<lineno>\d+):(?P<column>\d+)")
ERROR_POST_FIX = "   <-- 🔍 seems the error is around here"

# TODO check and add explanation how to configure black and isort
# TODO consider to do black as requested pip install
# TODO add to doc that line error starts from 1 and column start from 1

Borders = NamedTuple("Borders", [("start", int), ("end", int)])


def _get_borders(line_number: int, lines_count: int, padding: int) -> Borders:
    start = line_number - padding - 1
    if start < 0:
        start = 0
    end = line_number + padding
    if end > lines_count:
        end = lines_count
    return Borders(start, end)


def validate(syntax: str, raise_error: bool = False) -> bool:
    """
    Checks if a given Python 3 syntax is valid.

    See Also:
        * https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    Args:
        syntax (str): Python 3 syntax.
        raise_error (bool): When True and the syntax is invalid an exception will be
            raised. When False and the syntax is invalid False will be returned.

    Returns:
        bool: True when the syntax is valid, otherwise False.
    """
    try:
        ast.parse(syntax)
    except SyntaxError as exc:
        lines = syntax.split("\n")
        start, end = _get_borders(
            line_number=exc.lineno,
            lines_count=len(lines),
            padding=ERROR_CONTEXT_PADDING,
        )
        for i, line_number in enumerate(range(start, end), start=start):
            lines[i] = f"{str(line_number+1).ljust(len(str(end))+1, ' ')}|{lines[i]}"
        exc_index = exc.lineno - 1
        lines[exc_index] = lines[exc_index] + ERROR_POST_FIX
        err_lines = "\n".join(lines[start:end])
        # TODO customize package error, keep context in error, SyntaxError|IndentationError|TabError
        exc_name = getattr(type(exc), "__name__", "SyntaxError")
        exc = SyntaxError(
            f"{exc_name} in line-{exc.lineno} column-{exc.offset}:\n{err_lines}"
        )
        if raise_error:
            raise exc from None
        return False
    return True
