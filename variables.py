class Variable:
    '''
    Representation of a Mathematical Variable
        ex: x = 5

    Parameters:
        name:  str          : name of the Variable ("x")
        value: int or float : value of the Variable (5)
    '''

    def __init__(self, name: str, value: int or float):
        if type(name) != str:
            return TypeError(
                f'Unsupported type {type(name)} for Variable.name. Should be str.')
        if type(value) != int and type(value) != float:
            return TypeError(
                f'Unsupported type {type(name)} for Variable.value. Should be int or float.')

        self.name = name
        self.value = value

    def __str__(self):
        return self.name

    # ================
    # Operator Overloads
    # ================

    def __add__(self, other):
        if type(other) == Variable:
            return self.value + other.value
        elif type(other) == int:
            return self.value + other
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Variable:
            return self.value - other.value
        elif type(other) == int:
            return self.value - other
        else:
            return NotImplemented

    def __rsub__(self, other):
        if type(other) == int:
            return other - self.value
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) == Variable:
            return self.value * other.value
        elif type(other) == int:
            return self.value * other
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == Variable:
            return self.value / other.value
        elif type(other) == int:
            return self.value / other
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if type(other) == int:
            return other / self.value
        else:
            return NotImplemented
