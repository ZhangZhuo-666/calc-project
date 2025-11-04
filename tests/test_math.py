from utils.math_tools import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 1) == 4

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
