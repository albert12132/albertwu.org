~ title: Recursive Lists
~ level: exam

<block references>
* [Lecture: Sequences](http://cs61a.org/assets/slides/13-Sequences_1pps.pdf)
</block references>

<block notes>
We will be using the following implementation of immutable linked
lists. Keep in mind that your code should not depend on the assumption
that links are implemented as lists -- preserve data abstraction!

    empty = None

    def link(first, rest=empty):
        return [first, rest]

    def first(s):
        return s[0]

    def rest(s):
        return s[1]
</block notes>

<block contents>
What would Python print?
------------------------

<question>

<prompt>
    >>> r = link(1, link(link(2, empty), link(4, empty)))
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    4
    >>> first(first(rest(r)))
    2
</prompt>

<question>

<prompt>
    >>> r = link(1, link(link(2, empty), link(4, empty)))
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    4
    >>> first(first(rest(r)))
    2
</prompt>

<question>

<prompt>
    >>> r = link(link(1, link(2, empty)), link(3, link(4, empty)))
    >>> first(rest(r))
    3
    >>> first(rest(first(r)))
    2
    >>> first(first(rest(r)))
    IndexError
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `alternate` which takes a linked list and returns
a new linked list that contains *every other* element in the original
linked list.

    def alternate(lst):
        """Returns a new linked list that contains every other element
        of the original.

        >>> r = link(1, link(2, link(3, empty)))
        >>> link_to_list(alternate(r))
        [1, 3]
        >>> r = link(1, link(2, link(3, link(4, empty))))
        >>> link_to_list(alternate(r))
        [1, 3]
        """
        "*** YOUR CODE HERE ***"

<solution>
    def alternate(r):
        if r == empty:
            return empty
        elif rest(r) == empty:
            return r
        else:
            return link(first(r), alternate(rest(rest(r)))
</solution>

<question>

Implement a function `filter_link` which takes a linked list and
returns a new linked list that contains only elements that satisfy the
given predicate.

    def filter(pred, lst):
        """Returns a new link that contains elements of lst that
        satisfy the predicate.

        >>> r = link(1, link(2, link(3, empty)))
        >>> link_to_list(filter_link(lambda x: x % 2 == 1, r))
        [1, 3]
        >>> r = link(1, link(2, link(3, link(4, empty))))
        >>> link_to_list(filter_link(lambda x: x % 3 == 1, r))
        [1, 4]
        """
        "*** YOUR CODE HERE ***"

<solution>
    def filter(pred, lst):
        if r == empty:
            return empty
        elif pred(first(lst)):
            return link(first(lst), filter(pred, rest(lst)))
        else:
            return filter(pred, rest(lst))
</solution>
</block contents>
