~ title: Tuples
~ level: basic

<block references>
* [Lecture: Recursion](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/07_1pp.pdf)
* [Lecture: Function Examples](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/09_1pp.pdf)
* [Lab 3](http://inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab03/lab03.php)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What does *immutability* mean? How does it relate to tuples?

<solution>

An object that is *immutable* cannot be modified after it is created.
For example, tuples and strings are immutable. Consider the following:

    x = (1, 2, 3, 4)
    x[0] = 4

This will cause an error: since tuples are immutable, we cannot change
its elements. The question then is, why does this work?

    x = (1, 2, 3, 4)
    x += (5,)

The reason why this doesn't cause an error is because we **are not
mutating the original tuple**. Instead we are creating a new tuple, and
assigning it to `x`.

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> x = (1, 2, 3, 4)
    >>> x[0]
    1
    >>> x[3]
    4
    >>> x[4]
    IndexError
    >>> x[-1]
    4
    >>> x[-4]
    1
    >>> x[-5]
    IndexError
    >>> x[5.0]
    TypeError
</prompt>

<question>

<prompt>
    >>> x = (1, 2, 3, 4)
    >>> x[0:4]
    (1, 2, 3, 4)
    >>> x[1:3]
    (2, 3)
    >>> x[:3]
    (1, 2, 3)
    >>> x[0:]
    (1, 2, 3, 4)
    >>> x[:]
    (1, 2, 3, 4)
    >>> x[:10000]
    (1, 2, 3, 4)
    >>> x[100:10000]
    ()
</prompt>

<question>

<prompt>
    >>> x = (1, 2, 3, 4)
    >>> x[0:3:2]
    (1, 3)
    >>> x[:3:2]
    (1, 3)
    >>> x[1::2]
    (2, 4)
    >>> x[::2]
    (1, 3)
    >>> x[::-1]
    (4, 3, 2, 1)
    >>> x[0:4:-1]
    ()
</prompt>

<question>

<prompt>
    >>> x = (1, 2, 3, 4)
    >>> x[0]
    1
    >>> x[0:1]
    (1,)
    >>> len(x)
    4
    >>> 1 in x
    True
    >>> 10 not in x
    True
    >>> (1, 2) in x
    False
    >>> if x:
    ...     print("hi")
    hi
    >>> y = ()
    >>> if y:
    ...     print("hi")
    # nothing
</prompt>

Code-Writing questions
----------------------

<question>

Write a function `reverse` that reverses a given tuple.

    def reverse(tup):
        """Reverse the given tuple.

        >>> reverse((1, 2, 3, 4))
        (4, 3, 2, 1)
        >>> reverse(())
        ()
        """

<solution>

    def reverse(tup):
        if not tup:
            return ()
        return reverse(tup[1:]) + (tup[0],)

</solution>

<question>

Write a function `map` that applies a function to every element in a
given tuple. The result should be a newly created tuple.

    def map(f, tup):
        """Applies F to every element in TUP, and returns the results
        as a new tuple.

        >>> map(lambda x: x*x, (1, 2, 3, 4))
        (1, 4, 9, 16)
        >>> map(lambda x: x*x, ())
        ()
        """

<solution>

    def map(fn, tup):
        if not tup:
            return ()
        return (fn(tup[0]),) + map(fn, tup[1:])

</solution>

<question>

Write a function `filter` that takes a predicate function `cond` and a
tuple `tup`, and returns a new tuple that contains only the elements in
`tup` that satisfy `cond`.

    def filter(cond, tup):
        """Filters out elements of TUP using the predicate COND.

        >>> filter(lambda x: x % 2 == 0, (1, 2, 3, 4, 5))
        (2, 4)
        >>> filter(lambda x: x % 2 == 0, ())
        ()
        """

<solution>

    def filter(cond, tup):
        if not tup:
            return ()
        elif cond(tup[0]):
            return (tup[0],) + filter(cond, tup[1:])
        else:
            return filter(cond, tup[1:])

</solution>

Environment Diagrams
--------------------

<question>

<env>
    def draw(me):
        return me[2]

    y = (4, 5, 6)
    x = (1, 2, draw(y))
</env>

<question>

<env>
    def draw(me, too):
        tup = (too,)
        return me + tup

    y = (1, 2)
    x = draw(y, 3)
</env>

</block contents>
