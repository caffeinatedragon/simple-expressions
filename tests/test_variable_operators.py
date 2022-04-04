import pytest

from variables import Variable

x = Variable('x', 5)
y = Variable('y', 2)


@pytest.mark.parametrize('a,b,expected', [
    (x, 5, 10),
    (5, x, 10),
    (x, y, 7),
    (y, x, 7),
    (x, -10, -5),
    (-10, x, -5)
])
def test_add(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize('a,b,expected', [
    (x, 5, 0),
    (5, x, 0),
    (x, y, 3),
    (y, x, -3),
    (x, -10, 15),
    (-10, x, -15)
])
def test_subtract(a, b, expected):
    assert a - b == expected


@pytest.mark.parametrize('a,b,expected', [
    (x, 5, 25),
    (5, x, 25),
    (x, y, 10),
    (y, x, 10),
    (x, -10, -50),
    (-10, x, -50)
])
def test_multiply(a, b, expected):
    assert a * b == expected


@pytest.mark.parametrize('a,b,expected', [
    (x, 5, 1),
    (5, x, 1),
    (x, y, 2.5),
    (y, x, 0.4),
    (x, -10, -0.5),
    (-10, x, -2)
])
def test_divide(a, b, expected):
    assert a / b == expected


@pytest.mark.parametrize('a,b', [
    (x, 1.0),
    (4.2, y),
    (y, 'a'),
    ('a', x)
])
def test_invalid_operation(a, b):
    with pytest.raises(TypeError) as ex:
        a + b

    with pytest.raises(TypeError) as ex:
        a - b

    with pytest.raises(TypeError) as ex:
        a * b

    with pytest.raises(TypeError) as ex:
        a / b
