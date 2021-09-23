# Exceptions

All of CodeMate exceptions are under "codemate.exceptions" module.

## GenerationError

Represents an exception that has occurred while using one of CodeMate's components.
Can be used to catch any of the exceptions that may be raised by CodeMate.

## PythonSyntaxError

Represents an exception in the provided Python syntax.

Inherit from GenerationError, and SyntaxError.

## InputError

Raised when the generated Python code isn't valid.

Inherit from GenerationError, black.InvalidInput, and ValueError.

**Deprecation** - in version 1.0.0, black.InvalidInput inheritance will be removed.

Example for an [InputError](../exceptions/#inputerror) message can be found 
[here](../block_component/#validation).

## SaveFileError

Raised when the generated Python code file can't be created.

Inherit from GenerationError and OSError.
