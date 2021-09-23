# Block component

The Block component is the base of all of the components, it generates a python syntax
in a new context block.

The Block structure (each section is optional):

1. Docs
2. Imports
3. General Syntax

## Initialization

In the initiation of the Block, the default indentation may be changed, it will set how many
spaces to add before each line multiplied by the indentation.

Each method that inserts/parse lines support indentation as input.

```python
from codemate import Block

block = Block(indentation=4)

```

To generate the code use the following line:

`print(block.syntax())`

## Adding syntax

Syntax lines are referred as general Python code lines, they are inserted as is,
in the given order.

```python
from codemate import Block

block = Block()

# Adding multiple line as block
block.add_syntax_block("""
import math

x = math.sqrt(9)
if x > 3:
""")

# Adding a single line
block.add_syntax_line("print(x)", indent=1)

# Adding a variable
block.add_variable(
    name="y",
    type="float",
    value="x * 3"
)

# Adding multiple lines
block.add_syntax_lines(
    "z = x * y",
    "print(z)"
)

```
   
Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
import math

x = math.sqrt(9)
if x > 3:
    print(x)
y: float = x * 3
z = x * y
print(z)

```

## Adding imports

Specifying syntax lines as imports line provide syntax typo safety, sorting with isort
and inserting after the docs section and before the syntax. Order and content
are modified.

```python
from codemate import Block

block = Block()

# Adding a single import
block.add_import("codemate")

# Adding specific import from a module
block.add_specific_import(
    "codemate",
    "Block",
    "Function",
    "Method",
    "ClassMethod",
    "StaticMethod",
    "Class",
    "File",
)

# Adding multiple imports
block.add_imports(
    "typing",
    "codemate",
    "typing"
)

```
   
Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
import typing

import codemate
from codemate import (Block, Class, ClassMethod, File, Function, Method,
                      StaticMethod)


```

## Adding docs

Specifying syntax lines as doc line inserts it before the imports section and the syntax 
section.

```python
from codemate import Block

block = Block()

# Adding a doc line
block.add_doc_line("Adding a single documentation line to the block")

# Adding multiple doc lines
block.add_doc_lines(
    "",
    "Adding multiple,",
    "documentation lines,",
    "each one of them is in a new line.",
    "",
)

# Adding multiple imports
block.add_doc_block("""
    Adding a block of documentation,
    for adding paragraphs easily.
""")

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Adding a single documentation line to the block

Adding multiple,
documentation lines,
each one of them is in a new line.

Adding a block of documentation,
for adding paragraphs easily.
"""

```

## Extension

Adds other Python block syntax to the current Python block syntax. Ignoring the 
other's docs, copying the imports and adding the syntax.

```python
from codemate import Block

other = Block()

other.add_import("math")

other.add_doc_line("Other doc")

other.add_syntax_block("""
# other syntax
x = math.sqrt(9)
if x > 3:
""")

other.add_syntax_line("print(x)")

block = Block()

block.add_doc_line("Extend example")

block.add_syntax_line("pass")

block.extend(other)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Extend example
"""

import math

pass
# other syntax
x = math.sqrt(9)
if x > 3:
print(x)

```

## Insertion

Inserts as is other Python block syntax to the current Python block syntax. Inserting 
the docs and syntax as is and copying the imports.

```python
from codemate import Block

other = Block()

other.add_import("math")

other.add_doc_line("Other doc")

other.add_syntax_block("""
# other syntax
x = math.sqrt(9)
if x > 3:
""")

other.add_syntax_line("print(x)")

block = Block()

block.add_doc_line("Insert example")

block.add_syntax_line("pass")

block.insert(other)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
"""
Insert example
"""

import math

pass
"""
Other doc
"""

# other syntax
x = math.sqrt(9)
if x > 3:
print(x)

```

## Using Black

Will use the [black](https://github.com/psf/black) linter to format the Python syntax.
 
** Note it modifies the content.

```python
from codemate import Block

block = Block()

# complex syntax
block.add_syntax_block("""
    data = [{'userId':'3998e9a3dsdsa', 'related': {'tmp':'example'},
            'emails':['gopo@fake.com', 'tmp@tmp.io', 'ab@ab.io']}]
    print(data)
""")

```

Generating the syntax using `print(block.use_black())`, we will receive:
   
```python
data = [
    {
        "userId": "3998e9a3dsdsa",
        "related": {"tmp": "example"},
        "emails": ["gopo@fake.com", "tmp@tmp.io", "ab@ab.io"],
    }
]
print(data)

```

## Validation

Checks if the generated syntax structure is valid in Python 3.

```python
from codemate import Block

block = Block()

# complex syntax
block.add_syntax_block("""
    configuration = {}
    data = ["structure error here -> missing ']'"
    configuration.get("setting")
    print(data)
    print(configuration)
""")

# Will return False, the reason is that ']' is missing in the 'data' variable set.
block.validate(raise_error=False)

# Will raise an exception, the reason is that ']' is missing in the 'data' variable set.
block.validate()

```

Executing the code will raise an [InputError](../exceptions/#inputerror) with the 
following message:

```text
...

codemate.exceptions.InputError: Caused by SyntaxError in line-3 column-13:
1 |configuration = {}
2 |data = ["structure error here -> missing ']'"
3 |configuration.get("setting")   <-- 🔍 seems the error is around here
4 |print(data)
5 |print(configuration)

```
