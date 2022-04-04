import pytest

from expressions import Expression
from variables import Variable

x = Variable('x', 5)
y = Expression(3, '+', 6)


@pytest.mark.parametrize('left', [
    5, x, y, 0.25, 'bad value'
])
@pytest.mark.parametrize('operand', [
    '+', 'bad value', '**', 0
])
@pytest.mark.parametrize('right', [
    5, x, y, 0.25, 'bad value'
])
def test_expression_constructor(left, operand, right):
    if type(left) in {int, float, Variable, Expression} and \
       type(right) in {int, float, Variable, Expression} and \
       type(operand) == str and operand in {'+', '-', '*', '/'}:
        z = Expression(left, operand, right)
        assert type(z) == Expression

    else:
        with pytest.raises((TypeError, ValueError)) as ex:
            z = Expression(left, operand, right)

        if type(left) in {int, float, Variable, Expression} and \
                type(right) in {int, float, Variable, Expression} and \
                type(operand) == str:
            assert ex.type == ValueError
        else:
            assert ex.type == TypeError


@pytest.mark.parametrize('name', [
    'x', 'value', 0
])
@pytest.mark.parametrize('value', [
    5, 0.25, x, 'bad value'
])
def test_variable_constructor(name, value):
    if type(name) == str and type(value) in {int, float}:
        z = Variable(name, value)
        assert type(z) == Variable

    else:
        with pytest.raises(TypeError) as ex:
            z = Variable(name, value)
