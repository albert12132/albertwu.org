####################
# FUNCTIONS BASICS #
####################

################
# CODE-WRITING #
################

# Q1
def map(f, seq):
    """Acts just like the built-in map function, but returns a tuple.

    >>> tup = (1, 2, 3, 4)
    >>> map(lambda x: x**2, tup)
    (1, 4, 9, 16)
    """
    "*** YOUR CODE HERE ***"

# Q2
def filter(pred, seq):
    """Acts just like the built-in filter function, but returns a 
    tuple.

    >>> seq = range(10)
    >>> filter(lambda x: x % 2 == 0, seq)
    (0, 2, 4, 6, 8)
    """
    "*** YOUR CODE HERE ***"

# Q3
def reduce(combiner, seq): 
    """Acts just like the buitl-in reduce function.

    >>> seq = [1, 2, 3, 4, 5, 6]
    >>> reduce(lambda x, y: x + y, seq)
    21
    >>> reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    """
    "*** YOUR CODE HERE ***"

