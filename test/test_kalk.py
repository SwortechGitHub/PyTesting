import random
from ..main import add, subtract, multiply, divide
import pytest

def test_add():
    for _ in range(999999999):
        a = round(random.uniform(-10, 10), 2)
        b = round(random.uniform(-10, 10), 2)
        assert add(a, b) == a + b

def test_subtract():
    for _ in range(999999999):
        a = round(random.uniform(-10, 10), 2)
        b = round(random.uniform(-10, 10), 2)
        assert subtract(a, b) == a - b

def test_multiply():
    for _ in range(999999999):
        a = round(random.uniform(-10, 10), 2)
        b = round(random.uniform(-10, 10), 2)
        assert multiply(a, b) == a * b

def test_divide():
    for _ in range(999999999):
        a = round(random.uniform(1, 10), 2)
        b = round(random.uniform(1, 10), 2)
        assert divide(a, b) == a / b
        assert divide(-a, b) == -a / b
        assert divide(a, -b) == -a / b
    with pytest.raises(ValueError):
        divide(4, 0)
