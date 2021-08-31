# pylint: disable=missing-function-docstring
import os
import tempfile

from codemate import File
from tests import examples


def test_save_file():
    # If an exception has not been raised, the test has passed
    with tempfile.TemporaryDirectory() as tmp_dirname:
        file = File()
        path = os.path.join(tmp_dirname, "tmp.py")
        file.save(path)
        path = os.path.join(tmp_dirname, "tmp.py")
        file.save(path, use_black=False)


def test_complex_file():
    file = examples.file.get_example()
    assert examples.file.get_syntax() == file.use_black()
