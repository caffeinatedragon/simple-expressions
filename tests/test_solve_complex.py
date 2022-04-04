import pytest

from math import isclose

from expressions import Expression
from variables import Variable


x = Variable('x', 5)
y = Variable('y', 2)
a = Variable('a', 10)
z = Expression(x, '+', y)
b = Variable('b', 0.25)
c = Variable('c', 3.89)
d = Variable('d', 12.09)


@pytest.mark.parametrize('exp,expected', [
    (z, 7),
    (Expression(z, '*', 2), 14),
    (Expression(3, '*', z), 21),
    (Expression(z, '/', x), 1.4),
    (Expression(y, '+', z), 9),
    (Expression(Expression(x, '+', y), '+', Expression(2, '+', z)), 16),
    (Expression(Expression(Expression(Expression(x, '+', y), '-', a), '*', 2),
     '+', Expression(Expression(x, '*', a), '/', Expression(2, '*', x))), -1)
])
def test_solve(exp, expected):
    assert exp.solve() == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(0.5, '*', 2), 1.0),
    (Expression(Expression(2, '/', 5), '*', 10), 4.0),
    (Expression(Expression(y, '/', x), '*', z), 2.8),
    (Expression(Expression(0.25, '-', x), '/', Expression(0.125, '*', y)), -19),
    (Expression(Expression(Expression(Expression(b, '*', c), '*', d), '*', -0.23),
     '*', Expression(Expression(b, '*', c), '*', Expression(2.3, '*', d))), -73.12863949)
])
def test_solve_float(exp, expected):
    # since we're comparing floats, check for almost-equality
    assert isclose(exp.solve(), expected)
