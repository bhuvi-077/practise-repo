from calculator import add
from calculator import divide
import pytest

def test_add():
    result = add(2,3)
    assert result == 5

def test_add_positive():
    assert add(2,3) == 5

def test_add_negative():
    assert add(-1,-1) == -2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)