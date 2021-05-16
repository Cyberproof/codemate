import re


def remove_indentation(content: str) -> str:
    """
    Removes indentation from a given string that contains multiple lines.
    It removes spaces before new lines by the first line spaces at the beginning.

    Args:
        content(str): The sting that we want to clean from the indentation.

    Returns:
         str: The unindented content.
    """
    indentation = next(iter(re.findall("^\n*( *)", content) or []), "")
    unindented = re.subn(f"(\n){indentation}", r"\1", content)[0].strip()
    return unindented
