from variables import Variable


class Expression:
    '''
    Representation of a Mathematical Expression
        ex: 5 + x

    Parameters:
        left:    one of (int, float, Variable, Expression)  : 5
        operand: one of ('+', '-', '*', '/')                : '+'
        right:   one of (int, float, Variable, Expression)  : Variable('x', 1)
    '''

    def __init__(self, left, operand, right):
        # validate input types
        if type(left) not in {Variable, Expression} and not self._is_number(left):
            raise TypeError(
                f'Unsupported type {type(left)} for Expression.left. Should be int, float, Variable, or Expression.')
        if type(right) not in {Variable, Expression} and not self._is_number(right):
            raise TypeError(
                f'Unsupported type {type(right)} for Expression.right. Should be int, float, Variable, or Expression.')
        if type(operand) != str:
            raise TypeError(
                f'Unsupported type {type(operand)} for Expression.operand. Should be str.')
        if operand not in {'+', '-', '*', '/'}:
            raise ValueError(
                'Expression.operand must be one of: {"+", "-", "*", "/"}')

        # assign attributes
        self._left = left
        self._operand = operand  # one of: ('+', '-', '*', '/')
        self._right = right

    def __str__(self):
        '''
        Returns the string representation of the Expression
            ex: "5 + x"
        '''
        left = self._left
        right = self._right

        # a nested expression should always have parentheses
        if type(left) == Expression:
            left = f'({left})'
        if type(right) == Expression:
            right = f'({right})'

        # a negative number should always have parentheses
        if self._is_number(left) and left < 0:
            left = f'({left})'
        if self._is_number(right) and right < 0:
            right = f'({right})'

        return f'{left} {self._operand} {right}'

    def _is_number(self, num) -> bool:
        return type(num) == int or type(num) == float

    def solve(self):
        '''
        Evaluates the Expression and returns result (public wrapper method)
        '''
        return self._solve(self)

    def _solve(self, to_solve):
        '''
        Evaluates the Expression and returns result (private method)
        '''
        left = to_solve._left
        operand = to_solve._operand
        right = to_solve._right

        while type(left) == Expression or type(right) == Expression:
            if type(left) == Expression:
                left = self._solve(left)

            if type(right) == Expression:
                right = self._solve(right)

        left_val = left.value if type(left) == Variable else left
        right_val = right.value if type(right) == Variable else right
        result = eval(f'{left_val} {operand} {right_val}')

        return result

    def switch(self) -> 'Expression':
        '''
        Use the Commutative Property to switch left & right values
        correctly so that the Expression's value remains equal

        Returns new Expression
        '''
        if self._operand in {'+', '*'}:
            # a + b = b + a || a * b = b * a
            return Expression(self._right, self._operand, self._left)
        elif self._operand == '-':
            # a - b = (-b) + a
            return Expression(Expression(-1, '*', self._right), '+', self._left)
        else:
            # a / b = (1/b) * a
            return Expression(Expression(1, '/', self._right), '*', self._left)
