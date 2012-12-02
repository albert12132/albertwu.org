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

# Q4
class Rlist:
    """Doctests.

    >>> r = Rlist(1, Rlist(2, Rlist(3)))
    >>> for item in r:
    ...     print(item)
    1
    2
    3
    """
    def __init__(self, first, rest=None):
        self.first = first
        self.rest = rest
        self.curr = self

    def __iter__(self):
        return ___

    def __next__(self):
        if self.curr == ___:
            raise ___
        else:
            result = ___
            ___ = self.curr.rest
            return result

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
class Fibonacci:
    """Doctests.

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

