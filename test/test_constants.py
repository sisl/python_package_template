#!/usr/local/bin/python3

# Test Modules
import sys
import pytest
from   pytest import approx
from   os import path

# Import module under test
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from python_package_template.constants import *

# Other imports
import math

def test_constants():
    assert MY_DUMMY_CONSTANT == 42

if __name__ == '__main__':
    test_constants()