"""
Python syntax generator based on Object-Oriented Programing, type hints, and simplicity.
"""
from codemate._version import __version__
from codemate.block import Block
from codemate.file import File
from codemate.method import ClassMethod, Method, StaticMethod
from codemate.structure import Class, Function

# Package version
__version__ = ".".join(str(i) for i in __version__)  # type: ignore
