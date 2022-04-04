import pytest

from expressions import Expression
from variables import Variable


x = Variable('x', 5)
y = Variable('y', 2)
z = Variable('z', 10)
test_var = Variable('a', 100)


@pytest.mark.parametrize('var,name', [
    (x, 'x'), (y, 'y'), (z, 'z'), (test_var, 'a')
])
def test_variable_str(var, name):
    assert str(var) == name


@pytest.mark.parametrize('exp,expected', [
    (Expression(2, '+', 5), '2 + 5'),
    (Expression(x, '+', 2), 'x + 2'),
    (Expression(y, '+', 20), 'y + 20'),
    (Expression(3, '+', y), '3 + y'),
    (Expression(x, '+', z), 'x + z'),
    (Expression(Expression(x, '+', y), '+', z), '(x + y) + z'),
    (Expression(x, '+', Expression(y, '+', 2)), 'x + (y + 2)'),
    (Expression(Expression(x, '+', y), '+', Expression(2, '+', z)), '(x + y) + (2 + z)'),
    (Expression(Expression(Expression(x, '+', y),
     '+', test_var), '+', 2), '((x + y) + a) + 2'),
    (Expression(Expression(Expression(Expression(x, '+', y),
                                      '+', z), '+', 2), '+', Expression(Expression(x, '+', y), '+', Expression(2, '+', z))),
     '(((x + y) + z) + 2) + ((x + y) + (2 + z))')

])
def test_expression_add(exp, expected):
    assert str(exp) == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(2, '-', 5), '2 - 5'),
    (Expression(x, '-', 2), 'x - 2'),
    (Expression(y, '-', 20), 'y - 20'),
    (Expression(3, '-', y), '3 - y'),
    (Expression(x, '-', z), 'x - z'),
    (Expression(Expression(x, '-', y), '-', z), '(x - y) - z'),
    (Expression(x, '-', Expression(y, '-', 2)), 'x - (y - 2)'),
    (Expression(Expression(x, '-', y), '-', Expression(2, '-', z)), '(x - y) - (2 - z)'),
    (Expression(Expression(Expression(x, '-', y),
     '-', test_var), '-', 2), '((x - y) - a) - 2'),
    (Expression(Expression(Expression(Expression(x, '-', y), '-', z), '-', 2), '-', Expression(Expression(x, '-', y), '-', Expression(2, '-', z))),
     '(((x - y) - z) - 2) - ((x - y) - (2 - z))')
])
def test_expression_subtract(exp, expected):
    assert str(exp) == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(2, '/', 5), '2 / 5'),
    (Expression(x, '/', 2), 'x / 2'),
    (Expression(y, '/', 20), 'y / 20'),
    (Expression(3, '/', y), '3 / y'),
    (Expression(x, '/', z), 'x / z'),
    (Expression(Expression(x, '/', y), '/', z), '(x / y) / z'),
    (Expression(x, '/', Expression(y, '/', 2)), 'x / (y / 2)'),
    (Expression(Expression(x, '/', y), '/', Expression(2, '/', z)), '(x / y) / (2 / z)'),
    (Expression(Expression(Expression(x, '/', y),
     '/', test_var), '/', 2), '((x / y) / a) / 2'),
    (Expression(Expression(Expression(Expression(x, '/', y), '/', z), '/', 2), '/', Expression(Expression(x, '/', y), '/', Expression(2, '/', z))),
        '(((x / y) / z) / 2) / ((x / y) / (2 / z))')
])
def test_expression_divide(exp, expected):
    assert str(exp) == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(2, '*', 5), '2 * 5'),
    (Expression(x, '*', 2), 'x * 2'),
    (Expression(y, '*', 20), 'y * 20'),
    (Expression(3, '*', y), '3 * y'),
    (Expression(x, '*', z), 'x * z'),
    (Expression(Expression(x, '*', y), '*', z), '(x * y) * z'),
    (Expression(x, '*', Expression(y, '*', 2)), 'x * (y * 2)'),
    (Expression(Expression(x, '*', y), '*', Expression(2, '*', z)), '(x * y) * (2 * z)'),
    (Expression(Expression(Expression(x, '*', y),
     '*', test_var), '*', 2), '((x * y) * a) * 2'),
    (Expression(Expression(Expression(Expression(x, '*', y), '*', z), '*', 2), '*', Expression(Expression(x, '*', y), '*', Expression(2, '*', z))),
     '(((x * y) * z) * 2) * ((x * y) * (2 * z))')
])
def test_expression_multiply(exp, expected):
    assert str(exp) == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(Expression(x, '+', y), '*', z), '(x + y) * z'),
    (Expression(x, '*', Expression(y, '-', 2)), 'x * (y - 2)'),
    (Expression(Expression(x, '/', y), '*', Expression(2, '-', z)), '(x / y) * (2 - z)'),
    (Expression(Expression(Expression(x, '/', y),
     '-', test_var), '/', 2), '((x / y) - a) / 2')
])
def test_expression_mixed(exp, expected):
    assert str(exp) == expected


@pytest.mark.parametrize('exp,expected', [
    (Expression(-2, '*', -5), '(-2) * (-5)'),
    (Expression(x, '-', -2), 'x - (-2)'),
    (Expression(-20, '/', y), '(-20) / y'),
    (Expression(x, '*', Expression(y, '-', -2)), 'x * (y - (-2))')
])
def test_expression_negative(exp, expected):
    assert str(exp) == expected
