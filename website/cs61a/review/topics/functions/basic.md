~ title: Map, filter, and friends
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1skXespdgvJRzwUmW1oSxHP54_bKkJPGkF1-N9poNRt4/edit#slide=id.ga2e4b373c_0_10)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<prompt>
    >>> tup = (1, 2, 3, 4, 5)
    >>> map(lambda x: x*2, tup)
    <map object ...>
    >>> tuple(map(lambda x: x*2, tup))
    (2, 4, 6, 8, 10)
    >>> tup
    (1, 2, 3, 4, 5)
    >>> tuple(map(lambda x: 3, tup))
    (3, 3, 3, 3, 3)
</prompt>

<question>

<prompt>
    >>> tup = (1, 2, 3, 4, 5)
    >>> filter(lambda x: x % 2 == 0, tup)
    <filter object>
    >>> tuple(filter(lambda x: x % 2 == 0, tup))
    (2, 4)
    >>> tup
    (1, 2, 3, 4, 5)
    >>> tuple(filter(lambda x: False, tup))
    ()
</prompt>

<question>

<prompt>
    >>> from functools import reduce
    >>> tup = (1, 2, 3, 4, 5)
    >>> reduce(lambda x, y: x + y, tup)
    15
    >>> reduce(lambda x: x**2, tup)
    TypeError
</prompt>

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
