~ title: Links as Classes
~ level: basic

<block references>
* [Recursive Objects](http://cs61a.org/assets/slides/20-Composition_1pps.pdf)
* [Lab 6](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab06/lab06.php)
</block references>

<block notes>
For this section, we will be using the `Link` class implementation
from lecture:

    class Link(object):
        empty = ()

        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest

        def__len__(self):
            return 1 + len(self.rest)

        def __getitem__(self, i):
            if i == 0:
                return self.first
            return self.rest[i - 1]

        def __repr__(self):
            if self.rest is empty:
                return 'Link({})'.format(repr(self.first))
            return 'Link({}, {})'.format(repr(self.first),
                                          repr(self.rest))
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What type of object can `self.first` be? What type of object can
`self.rest` be?

<solution>

`self.first` can be any type of object, including a `Link`.
`self.rest` can only be a `Link` or `Link.empty`.

</solution>

<question>

How is the `Link` class different the `link` abstract data type we
saw earlier in the course?

<solution>

The `Link` class is mutable, meaning we can modify its contents. On
the other hand, the `link` abstract data type is immutable, so it can
not be mutated after it is created.

</solution>

Code-Writing questions
----------------------

<question>

Implement a function `seq_to_link`, which takes any type of sequence
(e.g. tuple, list) and converts it to a `Link`.

    def seq_to_link(seq):
        """Converts SEQ into an Link.

        >>> seq = [1, 2, 3, 4]
        >>> seq_to_link(seq)
        Link(1, Link(2, Link(3, Link(4))))
        >>> null = ()
        >>> seq_to_rlist(null) is Link.empty
        True
        """

<solution>

    # recursive
    def seq_to_link(seq):
        if not seq:
            return Link.empty
        return Link(seq[0], seq_to_rlist(seq[1:]))

    # iterative
    def seq_to_link(seq):
        new = Link.empty
        for elem in seq[::-1]:
            new = Link(elem, new)
        return new

</solution>

<question>

Implement a function `map_link`, which takes a Link and a function
`fn`, and applies `fn` to every element in the Link. `map_rlist`
should **mutate** the Link -- do not return a new one!

    def map_link(fn, lst):
        """Maps FN onto every element of the Link lst.

        >>> r = Link(1, Link(2, Link(3)))
        >>> map_link(lambda x: x*x, r)
        >>> r
        Link(1, Link(4, Link(9)))
        """
        "*** YOUR CODE HERE ***"

<solution>

    # recursive
    def map_link(fn, lst):
        if lst is not Link.empty:
            lst.first = fn(lst.first)
            map_rlist(fn, lst.rest)

    # iterative
    def map_rlist(fn, lst):
        while lst is not Link.empty:
            lst.first = fn(lst.first)
            lst = lst.rest

</solution>

</block contents>
