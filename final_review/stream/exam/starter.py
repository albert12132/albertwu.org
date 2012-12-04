"""Starter file for Streams"""

# Q1

# Call this function in the interactive interpreter if you want to
# know the answer to Q1
def stream1():
    def compute_rest():
        return add_streams(stream1(), stream1().rest)
    return Stream(0, lambda: Stream(1, compute_rest))
# Q2

# Call this function in the interactive interpreter if you want to
# know the answer to Q2
def stream2():
    def compute_rest():
        return add_streams(stream2(), stream2())
    return Stream(1, compute_rest)
        
####################
# STREAM UTILITIES #
####################

class Stream(object):
    """A lazily computed recursive list.

    >>> s = Stream(1, lambda: Stream(2+3, lambda: Stream(9)))
    >>> s.first
    1
    >>> s.rest.first
    5
    >>> s.rest
    Stream(5, <...>)
    >>> s.rest.rest.first
    9
    """
    class empty(object):
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
        self._rest = None
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def integer_stream(first=1):
    """Return a stream of consecutive integers, starting with first.

    >>> s = integer_stream(3)
    >>> s
    Stream(3, <...>)
    >>> m = map_stream(lambda x: x*x, s)
    >>> first_k_as_list(m, 5)
    [9, 16, 25, 36, 49]
    """
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)

def map_stream(fn, s):
    """Map a function fn over the elements of a stream s."""
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
    """Filter stream s with predicate function fn."""
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()

def first_k_as_list(s, k):
    """Return the first k elements of stream s as a list."""
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k

def fib_stream(a=0, b=1):
    """A stream of Fibonacci numbers.

    >>> first_k_as_list(fib_stream(), 8)
    [0, 1, 1, 2, 3, 5, 8, 13]
    """
    return Stream(a, lambda: fib_stream(b, a+b))

ones = Stream(1, lambda: ones)

def add_streams(s1, s2):
    """Return the sum of two streams as a stream.

    >>> ints = Stream(1, lambda: add_streams(ints, ones))
    >>> first_k_as_list(ints, 6)
    [1, 2, 3, 4, 5, 6]
    >>> fibs = Stream(0, lambda: Stream(1, lambda: add_streams(fibs, fibs.rest)))
    >>> first_k_as_list(fibs, 8)
    [0, 1, 1, 2, 3, 5, 8, 13]
    """
    def compute_rest():
        return add_streams(s1.rest, s2.rest)
    return Stream(s1.first + s2.first, compute_rest)

def primes(pos_stream):
    """Return a stream of primes, given a stream of consecutive integers.

    >>> ints = Stream(2, lambda: add_streams(ints, ones))
    >>> first_k_as_list(primes(ints), 8)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    def not_divisible(x):
        return x % pos_stream.first != 0
    def compute_rest():
        return primes(filter_stream(not_divisible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)

