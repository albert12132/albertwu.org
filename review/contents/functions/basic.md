~ title: Map, filter, and friends
~ level: basic

<block references>
* [Lecture: Strings and Sequence Processing](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/13-Strings_1pps.pdf)
* [Lab 5](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab05/lab05.php)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<wwpp>
    >>> tup = (1, 2, 3, 4, 5)
    >>> map(lambda x: x*2, tup)
    <map object ...>
    >>> tuple(map(lambda x: x*2, tup))
    (2, 4, 6, 8, 10)
    >>> tup
    (1, 2, 3, 4, 5)
    >>> tuple(map(lambda x: 3, tup))
    (3, 3, 3, 3, 3)
</wwpp>

<question>

<wwpp>
    >>> tup = (1, 2, 3, 4, 5)
    >>> filter(lambda x: x % 2 == 0, tup)
    <filter object>
    >>> tuple(filter(lambda x: x % 2 == 0, tup))
    (2, 4)
    >>> tup
    (1, 2, 3, 4, 5)
    >>> tuple(filter(lambda x: False, tup))
    ()
</wwpp>

<question>

<wwpp>
    >>> from functools import reduce
    >>> tup = (1, 2, 3, 4, 5)
    >>> reduce(lambda x, y: x + y, tup)
    15
    >>> reduce(lambda x: x**2, tup)
    TypeError
</wwpp>

Code-Writing questions
----------------------

<question>

Implement a function `map` that acts just like the built-in `map`,
except that it returns a tuple instead of a map object.

    def map(f, seq):
        """Acts just like the built-in map function, but returns a
        tuple.

        >>> tup = (1, 2, 3, 4)
        >>> map(lambda x: x**2, tup)
        (1, 4, 9, 16)
        """
        "*** YOUR CODE HERE ***"

<solution>

    def map(f, seq):
        tup = ()
        for elem in seq:
            tup += (f(elem),)
        return tup

</solution>

<question>

Implement a function `filter` that acts just like the built-in
`filter`, except that it returns a tuple instead of a filter object.

    def filter(pred, seq):
        """Acts just like the built-in filter function, but returns a
        tuple.

        >>> seq = range(10)
        >>> filter(lambda x: x % 2 == 0, seq)
        (0, 2, 4, 6, 8)
        """
        "*** YOUR CODE HERE ***"

<solution>

    def filter(pred, seq):
        tup = ()
        for elem in seq:
            if pred(elem):
                tup += (elem,)
        return tup

</solution>

<question>

Implement a function `reduce` that acts just like the built-in
`reduce`.

    def reduce(combiner, seq):
        """Acts just like the built-in reduce function.

        >>> seq = (1, 2, 3, 4, 5, 6)
        >>> reduce(lambda x, y: x + y, seq)
        21
        >>> reduce(lambda x, y: x * y, (1, 2, 3, 4))
        24
        """
        "*** YOUR CODE HERE ***"

<solution>

    def reduce(combiner, seq):
        total = seq[0]
        for elem in seq[1:]:
            total = combiner(total, elem)
        return total

</block contents>
