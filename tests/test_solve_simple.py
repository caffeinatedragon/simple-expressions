import pytest

from expressions import Expression
from variables import Variable


x = Variable('x', 5)
y = Variable('y', 2)
z = Variable('z', -10)


@pytest.mark.parametrize('exp,expected', [
    (Expression(5, '+', 8), 13),
    (Expression(x, '+', 8), 13),
    (Expression(8, '+', x), 13),
    (Expression(x, '+', y), 7),
    (Expression(y, '+', x), 7),
    (Expression(y, '+', z), -8)
])
def test_simple_add(exp, expected):
    assert exp.solve() == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(5, '-', 8), -3),
    (Expression(x, '-', 8), -3),
    (Expression(8, '-', x), 3),
    (Expression(x, '-', y), 3),
    (Expression(y, '-', x), -3),
    (Expression(y, '-', z), 12)
])
def test_simple_subtract(exp, expected):
    assert exp.solve() == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(5, '*', 8), 40),
    (Expression(x, '*', 8), 40),
    (Expression(8, '*', x), 40),
    (Expression(x, '*', y), 10),
    (Expression(y, '*', x), 10),
    (Expression(y, '*', z), -20)
])
def test_simple_multiply(exp, expected):
    assert exp.solve() == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(5, '/', 8), 0.625),
    (Expression(x, '/', 8), 0.625),
    (Expression(8, '/', x), 1.6),
    (Expression(x, '/', y), 2.5),
    (Expression(y, '/', x), 0.4),
    (Expression(y, '/', z), -0.2)
])
def test_simple_divide(exp, expected):
    assert exp.solve() == expected
