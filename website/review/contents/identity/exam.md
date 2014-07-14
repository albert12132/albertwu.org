~ title: Identity vs. Equality
~ level: exam

<block references>
* [Lecture: Objects](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/15-Objects_1pps.pdf)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<prompt>
    >>> def outer():
    ...     def inner():
    ...         return 42
    ...     return inner
    >>> outer is outer
    True   # referring to the function outer
    >>> outer() is outer()
    False  # referring to the return value of outer; draw an environment diagram to see why it is False
    >>> outer() == outer()
    False  # == for functions behaves like is
    >>> [1, 2, (3, 4)] == [1, 2, (3, 4)]
    True
    >>> [1, 2, outer()] == [1, 2, outer()]
    False  # == for list checks if each pair of elements satisfies ==
</prompt>

<question>

<prompt>
    >>> a = [1, 2, 3, 4]
    >>> a[0] = a
    >>> a is a[0]
    True
    >>> a = {'hi': 3}
    >>> b = {'hi': 3}
    >>> a is b
    False
    >>> a == b
    True
    >>> a['hi'] = 10
    >>> a == b
    False  # keys AND values must be equivalent
</prompt>

</block contents>
