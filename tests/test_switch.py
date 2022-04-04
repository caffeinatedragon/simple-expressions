import pytest

from expressions import Expression
from variables import Variable


x = Variable('x', 5)
y = Variable('y', 2)
z = Variable('z', 10)


@pytest.mark.parametrize('exp,expected,switched', [
    (Expression(2, '+', 5), '2 + 5', '5 + 2'),
    (Expression(x, '+', 2), 'x + 2', '2 + x'),
    (Expression(y, '+', 20), 'y + 20', '20 + y'),
    (Expression(3, '+', y), '3 + y', 'y + 3'),
    (Expression(x, '+', z), 'x + z', 'z + x'),
    (Expression(Expression(x, '+', y), '+', z), '(x + y) + z', 'z + (x + y)'),
    (Expression(x, '+', Expression(y, '+', 2)), 'x + (y + 2)', '(y + 2) + x'),
    (Expression(Expression(x, '+', y), '+', Expression(2, '+', z)),
     '(x + y) + (2 + z)', '(2 + z) + (x + y)'),
    (Expression(Expression(Expression(x, '+', y),
     '+', z), '+', 2), '((x + y) + z) + 2', '2 + ((x + y) + z)'),
    (Expression(Expression(Expression(Expression(x, '+', y), '+', z), '+', 2), '+', Expression(Expression(x, '+', y), '+', Expression(2, '+', z))),
     '(((x + y) + z) + 2) + ((x + y) + (2 + z))', '((x + y) + (2 + z)) + (((x + y) + z) + 2)')
])
def test_add(exp, expected, switched):
    assert str(exp) == expected
    switch = exp.switch()
    assert str(switch) == switched
    assert str(exp) != str(switch)
    assert switch.solve() == exp.solve()


@pytest.mark.parametrize('exp,expected,switched', [
    (Expression(2, '-', 5), '2 - 5', '((-1) * 5) + 2'),
    (Expression(x, '-', 2), 'x - 2', '((-1) * 2) + x'),
    (Expression(y, '-', 20), 'y - 20', '((-1) * 20) + y'),
    (Expression(3, '-', y), '3 - y', '((-1) * y) + 3'),
    (Expression(x, '-', z), 'x - z', '((-1) * z) + x'),
    (Expression(Expression(x, '-', y), '-', z),
     '(x - y) - z', '((-1) * z) + (x - y)'),
    (Expression(x, '-', Expression(y, '-', 2)),
     'x - (y - 2)', '((-1) * (y - 2)) + x'),
    (Expression(Expression(x, '-', y), '-', Expression(2, '-', z)),
     '(x - y) - (2 - z)', '((-1) * (2 - z)) + (x - y)'),
    (Expression(Expression(Expression(x, '-', y),
     '-', z), '-', 2), '((x - y) - z) - 2', '((-1) * 2) + ((x - y) - z)'),
    (Expression(Expression(Expression(Expression(x, '-', y), '-', z), '-', 2), '-', Expression(Expression(x, '-', y), '-', Expression(2, '-', z))),
     '(((x - y) - z) - 2) - ((x - y) - (2 - z))', '((-1) * ((x - y) - (2 - z))) + (((x - y) - z) - 2)')
])
def test_subtract(exp, expected, switched):
    assert str(exp) == expected
    switch = exp.switch()
    assert str(switch) == switched
    assert str(exp) != str(switch)
    assert switch.solve() == exp.solve()


@pytest.mark.parametrize('exp,expected,switched', [
    (Expression(2, '/', 5), '2 / 5', '(1 / 5) * 2'),
    (Expression(x, '/', 2), 'x / 2', '(1 / 2) * x'),
    (Expression(y, '/', 20), 'y / 20', '(1 / 20) * y'),
    (Expression(3, '/', y), '3 / y', '(1 / y) * 3'),
    (Expression(x, '/', z), 'x / z', '(1 / z) * x'),
    (Expression(Expression(x, '/', y), '/', z),
     '(x / y) / z', '(1 / z) * (x / y)'),
    (Expression(x, '/', Expression(y, '/', 2)), 'x / (y / 2)', '(1 / (y / 2)) * x'),
    (Expression(Expression(x, '/', y), '/', Expression(2, '/', z)),
     '(x / y) / (2 / z)', '(1 / (2 / z)) * (x / y)'),
    (Expression(Expression(Expression(x, '/', y),
     '/', z), '/', 2), '((x / y) / z) / 2', '(1 / 2) * ((x / y) / z)'),
    (Expression(Expression(Expression(Expression(x, '/', y), '/', z), '/', 2), '/', Expression(Expression(x, '/', y), '/', Expression(2, '/', z))),
     '(((x / y) / z) / 2) / ((x / y) / (2 / z))', '(1 / ((x / y) / (2 / z))) * (((x / y) / z) / 2)')

])
def test_divide(exp, expected, switched):
    assert str(exp) == expected
    switch = exp.switch()
    assert str(switch) == switched
    assert str(exp) != str(switch)
    assert switch.solve() == exp.solve()


@pytest.mark.parametrize('exp,expected,switched', [
    (Expression(2, '*', 5), '2 * 5', '5 * 2'),
    (Expression(x, '*', 2), 'x * 2', '2 * x'),
    (Expression(y, '*', 20), 'y * 20', '20 * y'),
    (Expression(3, '*', y), '3 * y', 'y * 3'),
    (Expression(x, '*', z), 'x * z', 'z * x'),
    (Expression(Expression(x, '*', y), '*', z), '(x * y) * z', 'z * (x * y)'),
    (Expression(x, '*', Expression(y, '*', 2)), 'x * (y * 2)', '(y * 2) * x'),
    (Expression(Expression(x, '*', y), '*', Expression(2, '*', z)),
     '(x * y) * (2 * z)', '(2 * z) * (x * y)'),
    (Expression(Expression(Expression(x, '*', y),
     '*', z), '*', 2), '((x * y) * z) * 2', '2 * ((x * y) * z)'),
    (Expression(Expression(Expression(Expression(x, '*', y), '*', z), '*', 2), '*', Expression(Expression(x, '*', y), '*', Expression(2, '*', z))),
     '(((x * y) * z) * 2) * ((x * y) * (2 * z))', '((x * y) * (2 * z)) * (((x * y) * z) * 2)')

])
def test_multiply(exp, expected, switched):
    assert str(exp) == expected
    switch = exp.switch()
    assert str(switch) == switched
    assert str(exp) != str(switch)
    assert switch.solve() == exp.solve()


@pytest.mark.parametrize('exp,expected,switched', [
    (Expression(Expression(x, '+', y), '*', z), '(x + y) * z', 'z * (x + y)'),
    (Expression(x, '*', Expression(y, '-', 2)), 'x * (y - 2)', '(y - 2) * x'),
    (Expression(Expression(x, '+', y), '*', Expression(2, '-', z)),
     '(x + y) * (2 - z)', '(2 - z) * (x + y)'),
    (Expression(Expression(Expression(x, '+', y),
     '-', z), '/', 2), '((x + y) - z) / 2', '(1 / 2) * ((x + y) - z)'),
    (Expression(Expression(Expression(x, '*', y), '+', z), '-', 2),
     '((x * y) + z) - 2', '((-1) * 2) + ((x * y) + z)'),
])
def test_mixed(exp, expected, switched):
    assert str(exp) == expected
    switch = exp.switch()
    assert str(switch) == switched
    assert str(exp) != str(switch)
    assert switch.solve() == exp.solve()
