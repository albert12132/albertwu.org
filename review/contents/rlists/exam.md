~ title: Recursive Lists
~ level: exam

<block references>
* [Lecture: Sequences](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/11-Sequences_1pps.pdf)
</block references>

<block notes>
We will be using the following implementation of immutable recursive
lists. Keep in mind that your code should not depend on the assumption
that rlists are implemented as tuples -- preserve data abstraction!

    empty_rlist = None

    def rlist(first, rest=empty_rlist):
        return (first, rest)

    def first(s):
        return s[0]

    def rest(s):
        return s[1]
</block notes>

<block contents>
What would Python print?
------------------------

<question>
<wwpp>
    >>> r = rlist(1, rlist(rlist(2, empty_rlist), rlist(4, empty_rlist)))
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    4
    >>> first(first(rest(r)))
    2
</wwpp>

<question>
<wwpp>
    >>> r = rlist(1, rlist(rlist(2, empty_rlist), rlist(4, empty_rlist)))
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    4
    >>> first(first(rest(r)))
    2
</wwpp>

<question>
<wwpp>
    >>> r = rlist(rlist(1, rlist(2, empty_rlist)), rlist(3, rlist(4, empty_rlist)))
    >>> first(rest(r))
    3
    >>> first(rest(first(r)))
    2
    >>> first(first(rest(r)))
    IndexError
</wwpp>

Code-Writing questions
----------------------

<question>
Implement a function `alternate` which takes an rlist and returns a new
rlist that contains *every other* element in the original rlist.

    def alternate(lst):
        """Returns a new rlist that contains every other element of the
        original.

        >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
        >>> rlist_to_tup(alternate(r))
        (1, 3)
        >>> r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
        >>> rlist_to_tup(alternate(r))
        (1, 3)
        """
        "*** YOUR CODE HERE ***"

<solution>
    def alternate(r):
        if r == empty_rlist:
            return empty_rlist
        elif rest(r) == empty_rlist:
            return r
        else:
            return rlist(first(r), alternate(rest(rest(r)))
</solution>

<question>
Implement a function `filter_rlist` which takes an rlist and returns a
new rlist that contains only elements that satisfy the given predicate.

    def filter(pred, lst):
        """Returns a new rlist that contains elements of lst that
        satisfy the predicate.

        >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
        >>> rlist_to_tup(filter_rlist(lambda x: x % 2 == 1, r))
        (1, 3)
        >>> r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
        >>> rlist_to_tup(filter_rlist(lambda x: x % 3 == 1, r))
        (1, 4)
        """
        "*** YOUR CODE HERE ***"

<solution>
    def filter(pred, lst):
        if r == empty_rlist:
            return empty_rlist
        elif pred(first(lst)):
            return rlist(first(lst), filter(pred, rest(lst)))
        else:
            return filter(pred, rest(lst))
</solution>
</block contents>
