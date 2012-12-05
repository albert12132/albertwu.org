"""Starter file for Iterators and Generators"""

# Q3
class Fibonacci:
    """Doctests

    >>> f = Fibonacci()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    """
    "*** YOUR CODE HERE ***"


# Q7
def map_gen(fn, iter1):
    """Doctests

    >>> i = iter([1, 2, 3, 4])
    >>> fn = lambda x: x**2
    >>> m = map_gen(fn, i)
    >>> next(m)
    1
    >>> next(m)
    4
    >>> next(m)
    9
    >>> next(m)
    16
    >>> next(m)
    Traceback (most recent call last):
      ...
    StopIteration
    """
    "*** YOUR CODE HERE ***"


# Q8
class Fibonacci1:
    """Doctests.

    >>> f = Fibonacci1()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    """
    "*** YOUR CODE HERE ***"

