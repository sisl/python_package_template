#!/usr/local/bin/python3

# Test Modules
import sys
import pytest
from   pytest import approx
from   os import path

# Import module under test
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from python_package_template.ducks import *

# Other imports
import math

def test_ducks_in_earth():
    assert ducks_in_earth(1) == 1086781292542889164800

if __name__ == '__main__':
    test_ducks_in_earth()