from expressions import Expression
from variables import Variable


def show_solve(exp: Expression, *variables: Variable):
    '''
    Prints Expression and all Variables to show how Expression is solved

    Input:
        exp: the Expression to solve
        variables: all Variables used in the Expression
    '''
    print(f'Expression: {exp}')
    print('Solve using:')
    for var in variables:
        print(f'  {var.name} = {var.value}')

    print(f'Solution: {exp.solve()}')
    print('-------------')


if __name__ == '__main__':
    # ===============================
    # Examples of Solving Expressions
    # ===============================

    # x + 1
    x = Variable('x', 4)
    exp = Expression(x, '+', 1)
    show_solve(exp, x)

    # 2 - y + 3x
    y = Variable('y', 5)
    exp = Expression(2, '-', Expression(y, '+', Expression(3, '*', x)))
    show_solve(exp, x, y)

    # 5 * a / b
    a = Variable('a', 8)
    b = Variable('b', 10)
    exp = Expression(Expression(5, '*', a), '/', b)
    show_solve(exp, a, b)

    # 3 * (x + 1)
    exp = Expression(3, '*', Expression(x, '+', 1))
    show_solve(exp, x)

    # ===============================
    # Examples of Solving Expressions
    #   & Using the Associative Property
    # ===============================

    # 2(x + 1) + 5y + z
    z = Variable('z', 7)
    exp_1 = Expression(2, '*', Expression(x, '+', 1))
    exp_2 = Expression(5, '*', y)
    exp_3 = Expression(Expression(exp_1, '+', exp_2), '+', z)
    exp_3_switched = exp_3.switch()
    exp_3_alt = Expression(exp_1, '+', Expression(exp_2, '+', z))
    exp_3_alt_switched = exp_3_alt.switch()

    print(f'Expression: {exp_3}')
    print(f'Switched using Associative Property: {exp_3_switched}')
    print('-------------')
    print(f'Expression (alternate): {exp_3_alt}')
    print(f'Switched using Associative Property: {exp_3_alt_switched}')
    print('-------------')
    show_solve(exp_3, x, y, z)
    print(f'Solution (switched) = {exp_3.solve()}')
    print(f'Solution (alt) = {exp_3.solve()}')
    print(f'Solution (alt switched) = {exp_3.solve()}')
    print('-------------')

    # switching Variable values
    x.value = 10
    y.value = 12
    z.value = 3
    show_solve(exp_3, x, y, z)

    # (((c + d) - e) * 2) - ((f * e) / (2 * g))
    c = Variable('c', 3)
    d = Variable('d', 180)
    e = Variable('e', 40)
    f = Variable('f', 42)
    g = Variable('g', 15)
    exp = Expression(Expression(Expression(Expression(c, '+', d), '-', e), '*', 2),
                     '-', Expression(Expression(f, '*', e), '/', Expression(2, '*', g)))
    show_solve(exp, c, d, e, f, g)

    exp_switched = exp.switch()
    print(f'Switched using Associative Property: {exp_switched}')
    print(f'Solved using switched: {exp_switched.solve()}')
