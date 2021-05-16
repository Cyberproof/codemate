from typing import Collection, Optional

from codemate.structure import Function


class Method(Function):
    """
    Generates a python method syntax.

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
        super().__init__(
            name=name,
            arguments=("self", *arguments),
            is_async=is_async,
            return_value=return_value,
        )


class ClassMethod(Function):
    """
    Generates a python class method syntax.

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
        super().__init__(
            name=name,
            arguments=("cls", *arguments),
            is_async=is_async,
            return_value=return_value,
        )
        self.add_decorator("classmethod")


class StaticMethod(Function):
    """
    Generates a python method syntax.

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
        super().__init__(
            name=name, arguments=arguments, is_async=is_async, return_value=return_value
        )
        self.add_decorator("staticmethod")
