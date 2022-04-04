# Simple Math Expression Solver

## What is This Project?
This project shows how to solve simple algebraic expressions using Python.

The Variable class defined in [variables.py](./variables.py) contains methods for defining variables such as `x = 5` and performing addition, subtraction, multiplication, and division on their values.

The Expression class defined in [expressions.py](./expressions.py) contains methods for defining algebraic expressions such as `2x + 8`, solving them using the Variables' values, and switching the order of terms using the Commutative Property.

An Expression is an operation on two terms. A term can be a number, a Variable, or another Expression. An operation can be addition (`+`), subtraction (`-`), multiplication (`*`), or division (`/`).

When combining multiple Expressions, each nested Expression will be in parentheses. For example, in order to create the Expression `2x + 8`, you would define it as `(2 * x) + 8`.

```python
x = Variable('x', 3)
exp = Expression(Expression(2, '*', x), '+', 8)
print(exp) # should print: (2 * x) + 8
```

To solve the Expression using the current value of all Variables, use the `Expression.solve()` method.

```python
print(exp.solve()) # should print: 14
```

If you change the value of any Variable in the Expression, solving the Expression will use the new value.

```python
x.value = 10
print(exp.solve()) # should print: 28
```

To switch the order of terms using the Commutative Property, use the `Expression.switch()` method.

```python
switched = exp.switch()
print(switched) # should print: 8 + (2 * x)
```

The `Expression.switch()` method will work for any supported operand. If you solve the switched Expression, it will equal the same value as the original Expression.

```python
y = Variable('y', 2)

# addition
exp = Expression(10, '+', y)
print(f'{exp} = {exp.solve()}')  # should print: 10 + y = 12
switched = exp.switch()
print(f'{switched} = {switched.solve()}')  # should print: y + 10 = 12

# subtraction
exp = Expression(10, '-', y)
print(f'{exp} = {exp.solve()}')  # should print: 10 - y = 8
switched = exp.switch()
print(f'{switched} = {switched.solve()}')  # should print: ((-1) * y) + 10 = 8

# multiplication
exp = Expression(10, '*', y)
print(f'{exp} = {exp.solve()}')  # should print: 10 * y = 20
switched = exp.switch()
print(f'{switched} = {switched.solve()}')  # should print: y * 10 = 20

# division
exp = Expression(10, '/', y)
print(f'{exp} = {exp.solve()}')  # should print: 10 / y = 5
switched = exp.switch()
print(f'{switched} = {switched.solve()}')  # should print: (1 / y) * 10 = 5
```


## Getting Started
This project was developed using [Python 3.10.3](https://www.python.org/downloads/release/python-3103/).

It is highly recommended to use a Python virtual environment to manage the project and its dependencies to avoid version conflicts with any other projects on your computer. I recommend using [conda](https://docs.conda.io/en/latest/), although [venv](https://docs.python.org/3/library/venv.html) or any other Python package management solution should work just as well.

The instructions in this README will use conda.


## How to Run the Example File
This project includes [example.py](./example.py), an example file showing how to form simple Expressions, solve them, and use the Commutative Property to switch term order.

1. Create a new virtual environment using Python 3.10:
    ```bash
    $ conda create -n math python=3.10
    $ conda activate math
    ```

2. To check that you're using the correct version of Python, use this command:
    ```bash
    $ python --version
    ```
    Expected Output:
    ```
    Python 3.10.3
    ```

3. Run the example code:
    ```bash
    $ python example.py
    ```

The result of running the example file should be identical to the results saved in [example-output.txt](./example-output.txt).

### Troubleshooting
* Make sure you've activated the virtual environment.
    ```bash
    $ conda activate math
    ```
* Make sure you're using Python 3.10.
    * To check your Python version:
        ```bash
        $ python --version
        ```
* Make sure you've installed the `pytest` and `coverage` packages before running the pytests.
    * To list all installed packages:
        ```bash
        $ conda list
        ```
    * To check specifically for pytest and coverage:
        ```bash
        $ conda list | grep 'pytest\|coverage'
        ```
* Make sure your working directory is the project folder. If you try to run the code from another folder, Python's import statements will not work properly.
    ```bash
    $ pwd
    ```
    Expected Output:
    ```
    (some path here)/simple-expressions
    ```


## How to Test the Project
Tests for this project are written using the [pytest](https://docs.pytest.org/en/stable/) package.

1. Activate the virtual environment (if not already active):
    ```bash
    $ conda activate math
    ```

2. Install the pytest package:
    ```bash
    $ conda install pytest
    ```

3. Run the test suite:
    ```bash
    $ python -m pytest tests/
    ```

Expected Output:
```
============================= test session starts ==============================
platform darwin -- Python 3.10.3, pytest-6.2.4, py-1.11.0, pluggy-0.13.1
rootdir: ~/math-expression
collected 273 items                                                            

tests/test_constructors.py ............................................. [ 16%]
...................................................................      [ 41%]
tests/test_print.py .................................................... [ 60%]
                                                                         [ 60%]
tests/test_solve_complex.py ............                                 [ 64%]
tests/test_solve_simple.py ........................                      [ 73%]
tests/test_switch.py .............................................       [ 89%]
tests/test_variable_operators.py ............................            [100%]

============================= 273 passed in 0.75s ==============================
```
**Note:** Your runtime may vary.

### Test Coverage
To verify test coverage, I am using the [coverage](https://coverage.readthedocs.io/en/6.3.2/) package.

#### To Check Coverage
1. Install the coverage package
    ```bash
    $ conda install coverage
    ```

2. Run pytests using coverage
    ```bash
    $ coverage run -m pytest tests/
    ```

3. View results (in Terminal)
    ```bash
    $ coverage report
    ```

4. View results (as HTML)
    ```bash
    $ coverage html
    $ open htmlcov/index.html
    ```

#### Current Coverage
Current Coverage is: **100%**.

Result of running `$ coverage report`:
```
Name             Stmts   Miss Branch BrPart  Cover
--------------------------------------------------
expressions.py      49      0     28      0   100%
variables.py        46      0     26      0   100%
--------------------------------------------------
TOTAL               95      0     54      0   100%
```
