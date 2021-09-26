import re
from functools import partial
from typing import List, Set

import black
import isort

from codemate import validator
from codemate.exceptions import InputError, PythonSyntaxError
from codemate.utils import remove_indentation


class Block:
    """
     A generator of a Python block syntax.

     The block syntax structure:

     * Documentation - Order is kept, when using block parsing it will be striped.
     * Imports - Sorted and modified by isort - https://github.com/PyCQA/isort.
     * General syntax lines - Order is kept, when using block parsing it will be striped.

     The only way to control the structure is by using the following methods:

     * add_line
     * add_lines
     * add_syntax_block
     * add_variable
     * extend
     * insert
     * syntax

     Methods for adding documentation:

     * add_doc_line
     * add_doc_lines
     * add_doc_block

     Methods for adding imports:

     * add_import
     * add_imports
     * add_specific_import

     Methods for adding Python syntax:

     * add_syntax_line
     * add_syntax_lines
     * add_syntax_block
     * add_variable
     * extend
     * insert

     Methods for getting the generated syntax:

     * syntax
     * use_black

     Other Methods:

     * validate
     * parse_line

    Args:
        indentation (int): Determines how many spaces are used in the syntax indentation.
    """

    def __init__(
        self,
        indentation: int = 4,
    ) -> None:
        self._indentation = indentation * " "

        self._docs: List[str] = []
        self._imports: Set[str] = set()
        self._lines: List[str] = []

    def parse_block(self, block: str, new_line: int = 0, indent: int = 0) -> str:
        """
        Parsing a given block to be in the proper indentation and place.

        Args:
            block (str): A string that represents multiple line .
            new_line (int): How many empty new lines to insert before the block.
            indent (indent): How many indentations to insert before each line.

        Returns:
            str: The parsed line.
        """
        syntax = "\n" * new_line
        syntax += re.sub("(^|\n)(.)", f"\\1{self._indentation * indent}\\2", block)
        return syntax

    def add_doc_line(self, line: str, indent: int = 0) -> "Block":
        """
        Adds a documentation line to the Python block syntax.

        Args:
            line (str): Documentation line of the block.
            indent (int): How much to indent the syntax.

        Returns:
            Block: The block instance.
        """
        doc = self.parse_block(line, indent=indent)
        self._docs.append(doc)
        return self

    def add_doc_lines(self, *lines: str, indent: int = 0) -> "Block":
        """
        Adds documentation lines to the Python block syntax.

        Args:
            *lines (Collection[str]): Documentation lines of the block.
            indent (int): How much to indent the syntax.

        Returns:
            Block: The block instance.
        """
        add_doc_line = partial(self.add_doc_line, indent=indent)
        list(map(add_doc_line, lines))
        return self

    def add_doc_block(self, block: str, indent: int = 0) -> "Block":
        """
        Adds documentation block of lines to the Python block syntax.

        Args:
            block (str): Documentation block.
            indent (int): How much to indent the syntax.

        Returns:
            Block: The block instance.
        """
        lines = remove_indentation(block).strip().split("\n")
        self.add_doc_lines(*lines, indent=indent)
        return self

    def add_import(self, module: str) -> "Block":
        """
        Adds an import syntax line to the Python block syntax.

        Args:
            module (str): The module name that we want to import.

        Returns:
            Block: The block instance.
        """
        self._imports.add(f"import {module}")
        return self

    def add_imports(self, *modules: str) -> "Block":
        """
        Adds imports syntax lines to the Python block syntax,
        Ignores empty modules names.

        Args:
            modules (Collection[str]): The modules names that we want to import.

        Returns:
            Block: The block instance.
        """
        list(map(self.add_import, filter(bool, modules)))
        return self

    def add_specific_import(self, module: str, *components: str) -> "Block":
        """
        Adds a specific import syntax to the Python block syntax.

        Args:
            module (str): The module name that we want to import.
            *components (Tuple[str]): The components that we want to import directly from
                the given module.

        Returns:
            Block: The block instance.
        """
        if components:
            self._imports.add(f"from {module} import {', '.join(components)}")
        return self

    def add_syntax_line(self, line: str, indent: int = 0) -> "Block":
        """
         Adds a Python line syntax to the Python block syntax.

         Args:
             line (str): The Python line syntax that we want to insert.
             indent (int): How much to indent the line.

        Returns:
             Block: The block instance.
        """
        syntax = self.parse_block(line, indent=indent)
        self._lines.append(syntax)
        return self

    def add_syntax_lines(self, *lines: str, indent: int = 0) -> "Block":
        """
         Adds multiple Python lines syntax to the Python block syntax.

         Args:
             *lines (Collection[str]): The Python lines syntax that we want to insert.
             indent (int): How much to indent the lines.

        Returns:
             Block: The block instance.
        """
        add_syntax_line = partial(self.add_syntax_line, indent=indent)
        tuple(map(add_syntax_line, lines))
        return self

    def add_syntax_block(self, block: str, indent: int = 0) -> "Block":
        """
         Adds a block of Python lines syntax to the Python block syntax.

         Args:
             block (str): A Python syntax block.
             indent (int): How much to indent the lines.

        Returns:
             Block: The block instance.
        """
        lines = remove_indentation(block).strip().split("\n")
        self.add_syntax_lines(*lines, indent=indent)
        return self

    def add_variable(self, name: str, **kwargs: str) -> "Block":
        """
        Adds a variable Python syntax to the class.

        Args:
            name (str): The name of the variable.

        Keyword Args:
            type (:obj:`str`, optional): The type of the variable.
            value (:obj:`str`, optional): The value of the variable.

        Returns:
            Class: The class instance.
        """
        syntax = name
        if not (kwargs.get("type") or kwargs.get("value")):
            message = "Class variable must have at least 'type' or 'value'"
            raise PythonSyntaxError(message)
        if kwargs.get("type"):
            syntax += f": {kwargs['type']}"
        if kwargs.get("value"):
            syntax += f" = {kwargs['value']}"
        self.add_syntax_line(syntax)
        return self

    def extend(self, block: "Block") -> "Block":
        """
        Adds other Python block syntax to the current Python block syntax.
        Ignoring the other's docs, copying the imports and adding the syntax.

        Args:
            block (Block): The block that we want to add.

        Returns:
            Block: The block instance.
        """
        self._imports.update(block._imports)  # pylint: disable=protected-access
        self._lines.extend(block._lines)  # pylint: disable=protected-access
        return self

    def insert(self, block: "Block") -> "Block":
        """
        Inserts as is other Python block syntax to the current Python block syntax.
        Inserting the docs and syntax as is and copying the imports.

        Args:
            block (Block): The block that we want to add.

        Returns:
            Block: The block instance.
        """
        self._imports.update(block._imports)  # pylint: disable=protected-access
        self._lines.append(block.syntax(imports=False))
        return self

    def _format_docs(self, indent: int) -> str:
        format_line = partial(self.parse_block, new_line=1, indent=indent)
        syntax = self.parse_block('"""', indent=indent)
        syntax += "".join(format_line(doc) for doc in self._docs)
        syntax += format_line('"""')
        syntax += "\n"
        return syntax

    def _format_imports(self, indent: int) -> str:
        format_line = partial(self.parse_block, new_line=1, indent=indent)
        syntax = "".join(format_line(import_) for import_ in self._imports)
        return isort.code(syntax.strip("\n"))

    def syntax(self, indent: int = 0, imports: bool = True) -> str:
        """
        Convert the block structure to Python syntax.

        Args:
            indent (int): How much to indent the block syntax.
            imports (bool): Whether to add imports or not to the block syntax.

        Returns:
            str: The block syntax.
        """
        format_line = partial(self.parse_block, new_line=1, indent=indent)
        syntax = ""
        if self._docs:
            syntax += self._format_docs(indent)
        if imports and self._imports:
            if syntax:
                syntax += "\n"
            syntax += self._format_imports(indent)
        if self._lines:
            if syntax:
                syntax += "\n"
            syntax += "".join(format_line(str(line)) for line in self._lines).strip(
                "\n"
            )
        if syntax and syntax[-1] != "\n":
            return syntax + "\n"
        return syntax

    def use_black(self) -> str:
        """
        Convert the block structure to python syntax formatted by Black.

        References:
            * Black docs - https://github.com/psf/black
            * The solution - https://stackoverflow.com/a/57653302

        Returns:
            str: The block syntax.

        Raises:
            InputError: When the generated Python 3 code isn't valid.
        """
        self.validate()
        return black.format_str(self.syntax(), mode=black.Mode())

    def validate(self, raise_error: bool = True) -> bool:
        """
        Checks if the generated syntax is Python 3 valid.

        Args:
            raise_error (bool): When True and the syntax is invalid, an exception will be
                raised. When False and the syntax is invalid, False will be returned.

        Returns:
            bool: True when the syntax is valid, otherwise False.

        Raises:
            InputError: When the generated Python 3 code isn't valid.
        """
        try:
            validator.validate(self.syntax(), raise_error=True)
        except InputError as error:
            if raise_error:
                raise error from None
            return False
        return True

    def __repr__(self) -> str:
        class_name = getattr(type(self), "__name__", type(self))
        return f"{class_name}({vars(self)})"

    def __str__(self) -> str:
        return self.syntax()

    def __contains__(self, value: str) -> bool:
        """
        x.__contains__(y) <==> y in x.

        Raises:
            ValueError: When the provided input isn't instance of string.
        """
        if not isinstance(value, str):
            type_name = type(value).__name__
            error = f"Argument 'value' should be instance of 'str' not '{type_name}'"
            raise ValueError(error)
        return value in str(self)
