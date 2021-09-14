import black


def get_syntax(use_black: bool = False, prefix: str = "", postfix: str = "") -> str:
    """
    Factory function that returns a copy of the example expected syntax.

    Args:
        use_black (bool): If sets to True, the black formatter is used on the syntax.
            Otherwise, the syntax return as is.
        prefix (str): The syntax prefix sting.
        postfix (str): The syntax postfix sting.

    Returns:
        str: The formatted syntax.
    """
    syntax = f"{prefix}{postfix}"
    if use_black:
        return black.format_str(syntax, mode=black.Mode())
    return syntax
