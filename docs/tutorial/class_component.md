# Class component

The Class generates a python class syntax.

## Initialization

```python
from codemate import Class

# Simple class
simple_class = Class(name="Simple")
simple_class.add_syntax_line("pass")

# Class with metaclass
with_meta_class = Class(name="WithMeta", metaclass="Simple", inherit=("str",))
with_meta_class.add_syntax_line("pass")

# Class with inheritance
with_inheritance_class = Class(name="WithInheritance", inherit=("str", "WithMeta"))
with_inheritance_class.add_syntax_line("pass")

```

Generating the syntax using `print({class instance}.syntax())`, we will receive:
   
```python
class Simple:
    pass

# --------------------------------------------
class WithMeta(str, metaclass=Simple):
    pass

# --------------------------------------------
class WithInheritance(str, WithMeta):
    pass

```

## Decorators

```python
from codemate import Class, Function, Block

block = Block()

decorator = Function(name="class_decorator", arguments=("cls",))
decorator.add_syntax_line("pass")
block.insert(decorator)

class_ = Class(name="Bar")
class_.add_syntax_line("pass")
class_.add_decorator("class_decorator")
block.insert(class_)

```

Generating the syntax using `print(block.syntax())`, we will receive:
   
```python
def class_decorator(cls):
    pass

@class_decorator
class Bar:
    pass

```
