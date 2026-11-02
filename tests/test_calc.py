import pytest

from app.calc import add, divide, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
