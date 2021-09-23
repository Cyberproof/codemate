import ast

from codemate.exceptions import InputError

ERROR_CONTEXT_PADDING = 2
ERROR_POST_FIX = "   <-- 🔍 seems the error is around here"


def _format_error(syntax: str, error: SyntaxError) -> InputError:
    if error.lineno is None:
        raise ValueError("SyntaxError.lineno can not contain None")
    lines = syntax.split("\n")
    start = max(error.lineno - ERROR_CONTEXT_PADDING - 1, 0)
    end = min(error.lineno + ERROR_CONTEXT_PADDING, len(lines))
    for i, line_number in enumerate(range(start, end), start=start):
        lines[i] = f"{str(line_number + 1).ljust(len(str(end)) + 1, ' ')}|{lines[i]}"
    exc_index = error.lineno - 1
    lines[exc_index] = lines[exc_index] + ERROR_POST_FIX
    err_lines = "\n".join(lines[start:end])
    exc_name = getattr(type(error), "__name__", "SyntaxError")
    return InputError(
        f"Caused by {exc_name} in line-{error.lineno} column-{error.offset}:"
        f"\n{err_lines}"
    )


def validate(syntax: str, raise_error: bool = False) -> bool:
    """
    Checks if a given Python 3 syntax is valid.

    See Also:
        * https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    Args:
        syntax (str): Python 3 syntax.
        raise_error (bool): When True and the syntax is invalid, an exception will be
            raised. When False and the syntax is invalid, False will be returned.

    Returns:
        bool: True when the syntax is valid, otherwise False.

    Raises:
        InputError: When the given Python 3 syntax isn't valid.
    """
    try:
        ast.parse(syntax)
    except SyntaxError as exception:
        if raise_error is False:
            return False
        if not exception.lineno:
            raise InputError(
                "The syntax structure is not Python 3 valid"
            ) from exception
        error = _format_error(syntax, exception)
        if raise_error:
            raise error from None
    return True
