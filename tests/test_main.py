"""
    Here is my pytest test file.
    Poetry manages my environment, so pytest runs smoothly.
"""

import pytest
from awesome_fastapi_project.main import *

def test_mock():
    assert 1 == 1