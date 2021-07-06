from datetime import datetime
from typing import Optional

from codemate.block import Block
from codemate.exceptions import SaveFileError


def generate_header() -> str:
    """
    Generates a file header.

    Returns:
        str: The generated header of a file.
    """
    syntax = " Warning generated file ".center(90, "-")
    date = datetime.now().isoformat()
    syntax += "\n"
    syntax += f"Generated at: {date}"
    syntax += "\n"
    syntax += "".center(90, "-")
    return syntax


class File(Block):
    """
    Creates a Python file syntax.

    Args:
        header (Optional[str]): A block string that represents the files header
    """

    def __init__(self, header: Optional[str] = generate_header()) -> None:
        super().__init__()
        if header:
            self.add_doc_block(block=header)

    def save(self, path: str, use_black: bool = True) -> None:
        """
        Save the generated Python file in a given location.

        Args:
            path (str): The path to the location that we want to save the file at.
            use_black (bool): When true black linter will be used to format the generated
                Python code.

        Raises:
            SaveFileError: When the generated Python code file can't be created.
        """
        try:
            with open(path, "w") as file:
                if use_black:
                    file.write(self.use_black())
                else:
                    file.write(self.syntax())
        except OSError as error:
            raise SaveFileError("Can't create the generated file") from error
