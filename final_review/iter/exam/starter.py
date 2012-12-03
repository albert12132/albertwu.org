"""Starter file for Iterators and Generators"""

# Q2
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

# Q3
def zip(iter1, iter2):
    """Doctest

    >>> i1 = iter([1, 2, 3, 4])
    >>> i2 = iter([5, 6, 7])
    >>> gen = zip(i1, i2)
    >>> for elem in gen:
    ...     print(elem)
    (1, 5)
    (2, 6)
    (3, 7)
    """
    "*** YOUR CODE HERE ***"


# Q4
def pascals():
    """
    >>> p = pascals()
    >>> next(p)
    [1]
    >>> next(p)
    [1, 1]
    >>> next(p)
    [1, 2, 1]
    >>> next(p)
    [1, 3, 3, 1]
    >>> next(p)
    [1, 4, 6, 4, 1]
    """
    curr = _____
    while True:
        yield curr 
        i, new = 1, [1]
        while ____:
            new.append(____ + ____)
            i += 1
        new.append(1)
        curr = new
