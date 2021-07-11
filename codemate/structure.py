from abc import abstractmethod
from collections import Counter
from functools import partial
from typing import Collection, List, Optional

from codemate.block import Block


class Structure(Block):
    """
    Creates an abstract Python structure syntax.

    Args:
        name(str): The name of the structure.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        super().__init__()
        self._name = name
        self._decorators: List[str] = []

    def add_decorator(self, line: str) -> "Structure":
        """
        Adds a line that represent a Python decorator syntax to the structure,
        in FIFO order.

        Args:
            line (str): The syntax line that should be inserted as a decorator.

        Returns:
            Class: The class instance.
        """
        self._decorators.append(f"@{line}")
        return self

    def _format_decorators(self, indent: int) -> str:
        format_line = partial(self.parse_block, new_line=1, indent=indent)
        syntax = "".join(format_line(line) for line in self._decorators)
        return syntax.strip()

    @abstractmethod
    def _format_signature(self, indent: int) -> str:
        raise NotImplementedError

    def syntax(self, indent: int = 0, imports: bool = True) -> str:
        """
        Convert the structure to Python syntax.

        Args:
            indent (int): How much to indent the class content.
            imports (bool): Whether to add imports or not.

        Returns:
            str: The structure Python syntax.
        """
        syntax = ""
        if self._decorators:
            syntax += self._format_decorators(indent)
            syntax += "\n"
        syntax += self._format_signature(indent)
        block_content = super().syntax(indent + 1, imports)
        syntax += "\n"
        syntax += self.parse_block(block_content)
        return syntax


class Function(Structure):
    """
    Generates a Python function syntax.

    Args:
        name (str): The name of the function.
        arguments (Collection[str]): The inputs of the function.
        is_async (bool): Represents whether async keyword should be added.
        return_value (Optional[str]): The type of the function return value.
    """

    def __init__(
        self,
        name: str,
        arguments: Collection[str] = (),
        is_async: bool = False,
        return_value: Optional[str] = None,
    ) -> None:
        super().__init__(name)
        self._arguments = arguments
        self._is_async = is_async
        self._return_value = return_value

    def _format_signature(self, indent: int) -> str:
        # Counter is used to remove duplications of arguments
        args_syntax = ", ".join(Counter(self._arguments))
        async_prefix = "async " if self._is_async else ""
        return_value = f" -> {self._return_value}" if self._return_value else ""
        signature = f"{async_prefix}def {self._name}({args_syntax}){return_value}:"
        return self.parse_block(signature, indent=indent)


class Class(Structure):
    """
    Creates a python class syntax.

    Args:
        name(str): The name of the class.
        inherit (Collection[str]): The classes that this class inherits from.
    """

    def __init__(
        self,
        name: str,
        metaclass: Optional[str] = None,
        inherit: Collection[str] = (),
    ) -> None:
        super().__init__(name)
        self._metaclass = metaclass
        self._inherit = inherit

    def _format_signature(self, indent: int) -> str:
        signature = f"class {self._name}"
        # Counter is used to remove duplications of arguments
        inheritance = ", ".join(Counter(self._inherit))
        metaclass = f"metaclass={self._metaclass}" if self._metaclass else ""
        if inheritance and metaclass:
            inheritance += ","
        if inheritance or metaclass:
            signature += f"({inheritance}{metaclass})"
        signature += ":"
        return self.parse_block(signature, indent=indent)
