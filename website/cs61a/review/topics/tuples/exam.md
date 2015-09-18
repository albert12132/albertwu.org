~ title: Tuples
~ level: exam

<block references>
* [Lecture: Recursion](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/07_1pp.pdf)
* [Lecture: Function Examples](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/09_1pp.pdf)
* [Lab 3](http://inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab03/lab03.php)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<prompt>
    >>> x = (1, (2, (3, (4,))))
    >>> len(x)
    2
    >>> x[1][0]
    2
    >>> 2 in x
    False
    >>> y = (1, (2, (3,), 4), 5)
    >>> len(y)
    3
    >>> len(y[1])
    3
    >>> y[2] = 50
    TypeError
    >>> z = (2, (1, (2,), 1), 1)
    >>> z[z[z[0]]]
    (1, (2,), 1)
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `is_palindrome` if the given tuple is a
palindrome. A palindrome is a sequence that is the same backwards.

    def is_palindrome(tup):
        """Returns True if tup is a palindrome.

        >>> x = (1, 2, 3, 4)
        >>> is_palindrome(x)
        False
        >>> y = (1, 2, 3, 2, 1)
        >>> is_palindrome(y)
        True
        >>> is_palindrome(())
        True
        """
        "*** YOUR CODE HERE ***"

<solution>

    # simple version
    def is_palindrome(tup):
        return tup == tup[::-1]

    # recursive
    def is_palindrome(tup):
        if len(tup) == 0 or len(tup) == 1:
            return True
        return tup[0] == tup[-1] and is_palindrome(tup[1:-1])

    # iterative
    def is_palindrome(tup):
        for i in range(len(tup)//2):
            if tup[i] != tup[-i-1]:
                return False
        return True

</solution>

<question>

Implement a function `flatten` that takes a (possibly deep) tuple and
returns a new tuple that has no nested tuples. See the doctests for
behavior specifics.

    def flatten(tup):
        """Flattens a possibly deep tuples.

        >>> x = (1, (2, (3,), 4), 5)
        >>> flatten(x)
        (1, 2, 3, 4, 5)
        >>> y = (1, 2, 3, 4)
        >>> flatten(y)
        (1, 2, 3, 4)
        """
        "*** YOUR CODE HERE ***"

<solution>

    # recursive
    def flatten(tup):
        if not tup:
            return ()
        elif type(tup[0]) == tuple:
            return flatten(tup[0]) + flatten(tup[1:])
        else:
            return (tup[0],) + flatten(tup[1:])

    # iterative
    def flatten(tup):
        total = ()
        for elem in tup:
            if type(elem) == tuple:
                total += flatten(elem)
            else:
                total += (elem,)
        return total

</solution>

<question>

Implement a function `deep_reverse` that takes a (possibly deep) tuple
and reverses it. If the tuple has elements that are themselves tuples,
those elements will be reversed too. See the doctests for behavior
specifics.

    def deep_reverse(tup):
        """Reverses a possibly deep tuples.

        >>> tup = (1, (2, (3,), 4), 5)
        >>> deep_reverse(tup)
        (5, (4, (3,) 2), 1)
        >>> y = (1, 2, 3, 4)
        >>> deep_reverse(y)
        (4, 3, 2, 1)
        """
        "*** YOUR CODE HERE ***"

<solution>

    # recursive
    def deep_reverse(tup):
        if not tup:
            return ()
        elif type(tup[0]) == tuple:
            return deep_reverse(tup[1:]) + (deep_reverse(tup[0]),)
        else:
            return deep_reverse(tup[1:]) + (tup[0],)

    # iterative
    def deep_reverse(tup):
        total = ()
        for elem in tup:
            if type(elem) == tuple:
                total = (deep_reverse(elem),) + total
            else:
                total += (elem,) + total
        return total

</solution>

</block contents>
