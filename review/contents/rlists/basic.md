~ title: Recursive Lists
~ level: basic

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

Concept Questions
-----------------

<question>

What type of object can `first` be (e.g.  int, string, function, etc.)?
What type of object can `rest` be?

<solution>

`first` can be any type of object, even an rlist. `rest` can only be an
rlist.

</solution>

<question>

Which of the following are valid Rlist constructors?

1. `rlist(1, 3)`
2. `rlist(1, None)`
3. `rlist(1, rlist(4, empty_rlist))`
4. `rlist(1, empty_rlist)`
5. `rlist()`

<solution>

The correct answers are in bold:

1. `rlist(1, 3)`
2. `rlist(1, None)`
3. **`rlist(1, rlist(4, empty_rlist))`**
4. **`rlist(1, empty_rlist)`**
5. `rlist()`

</solution>

<question>

Construct an rlist that contains the following elements:

    1, 3, lambda x: x, 'hi'

<solution>

    rlist(1, rlist(3, rlist(lambda x: x, rlist('hi', empty_rlist))))

</solution>

<question>

What is the third element of the following rlist?

    rlist('this', rlist(rlist('is', rlist('a', empty_rlist)), rlist('question', empty_rlist)))

<solution>

`'question'`

</solution>

<question>

What is the length of the rlist in the previous question (i.e. how many
elements are in the rlist, not including the elements of nested rlists?

<solution>

3

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    >>> first(r)
    1
    >>> rest(r)
    (2, (3, None))
    >>> rest(rest(r))
    (3, None)
    >>> first(rest(r))
    2
    >>> first(rest(rest(r)))
    3
</prompt>

Code-Writing Questions
----------------------

<question>

Implement a function `rlist_to_tup` that takes an rlist as an argument, and
returns a tuple that contains the same elements as the rlist.

    def rlist_to_tup(lst):
        """Returns a tuple that contains the same elements as the
        rlist.

        >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
        >>> rlist_to_tup(r)
        (1, 2, 3)
        """
        "*** YOUR CODE HERE ***"

<solution>

A recursive version:

    def rlist_to_tup(lst):
        if lst == empty_rlist:
            return ()
        return (first(lst),) + rlist_to_tup(rest(lst))

An iterative version:

    def rlist_to_tup(lst):
        new = ()
        while lst != empty_rlist:
            new += (first(lst),)
            lst = rest(lst)
        return new

</solution>

<question>

Implement a function `map_rlist` that maps a function `f` onto each element of
an rlist.

    def map_rlist(lst, f):
        """Maps f onto each element in the rlist.

        >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
        >>> rlist_to_tup(map_rlist(r, lambda x: x**2))
        (1, 4, 9)
        """
        "*** YOUR CODE HERE ***"

<solution>

A recursive version:

    def map_rlist(lst, f):
        if lst == empty_rlist:
            return empty_rlist
        return rlist(f(first(lst)), map_rlist(rest(lst), f))

An iterative version:

    def map_rlist(lst, f):
        new = empty_rlist
        while lst != empty_rlist:
            new = rlist(f(first(lst)), new)
            lst = rest(lst)
        while new != empty_rlist:
            lst = rlist(first(new), lst)
            new = rest(new)
        return lst

</solution>
</block contents>
