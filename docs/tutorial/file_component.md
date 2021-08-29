## File component

File component is a Block component with relevant capabilities to make Python files
generation simple.

### Initialization

```python
from codemate import File

# A file with default header
default = File()

# A file with customized header
customized = File(header="-------- Customized Header --------")

```

Generating the syntax using `print({file instance}.syntax())`, we will receive:

```python
"""
--------------------------------- Warning generated file ---------------------------------
Generated at: 2021-06-22T15:30:42.222423
------------------------------------------------------------------------------------------
"""

# --------------------------------------------
"""
-------- Customized Header --------
"""

```

### Saving the file

We can save the generated file and specific whether to use black linter on the content
or not.

```python
from codemate import File

file = File()

# Without black linter
file.save(path="without_black.py")

# With black linter
file.save(path="with_black.py", use_black=True)

```
