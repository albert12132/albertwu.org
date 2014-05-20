~ title: Rlists as Classes
~ level: basic

<block references>
* [Recursive Objects](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/17-Structure_1pps.pdf)
* [Lab 6](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab06/lab06.php)
</block references>

<block notes>
For this section, we will be using the `Rlist` class implementation
from lecture:

    class Rlist(object):
        class EmptyList(object):
            def __len__(self):
                return 0
        empty = EmptyList()

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
                return 'Rlist({})'.format(repr(self.first))
            return 'Rlist({}, {})'.format(repr(self.first),
                                          repr(self.rest))
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What type of object can `self.first` be? What type of object can
`self.rest` be?

<solution>

`self.first` can be any type of object, including an `Rlist`.
`self.rest` can only be an `Rlist` or an `EmptyList`.

</solution>

<question>

How is the `Rlist` class different the `rlist` abstract data type we
saw earlier in the course?

<solution>

The `Rlist` class is mutable, meaning we can modify its contents. On
the other hand, the `rlist` abstract data type is immutable, so it can
not be mutated after it is created.

</solution>

Code-Writing questions
----------------------

<question>

Implement a function `seq_to_rlist`, which takes any type of sequence
(e.g. tuple, list) and converts it to an `Rlist`.

    def seq_to_rlist(seq):
        """Converts SEQ into an Rlist.

        >>> seq = [1, 2, 3, 4]
        >>> seq_to_rlist(seq)
        Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
        >>> null = ()
        >>> seq_to_rlist(null) is Rlist.empty
        True
        """

<solution>

    # recursive
    def seq_to_rlist(seq):
        if not seq:
            return Rlist.empty
        return Rlist(seq[0], seq_to_rlist(seq[1:]))

    # iterative
    def seq_to_rlist(seq):
        new = Rlist.empty
        for elem in seq[::-1]:
            new = Rlist(elem, new)
        return new

</solution>

<question>

Implement a function `map_rlist`, which takes an Rlist and a function
`fn`, and applies `fn` to every element in the Rlist. `map_rlist`
should **mutate** the Rlist -- do not return a new one!

    def map_rlist(fn, r):
        """Maps FN onto every element of the Rlist R.

        >>> r = Rlist(1, Rlist(2, Rlist(3)))
        >>> map_rlist(lambda x: x*x, r)
        >>> r
        Rlist(1, Rlist(4, Rlist(9)))
        """
        "*** YOUR CODE HERE ***"

<solution>

    # recursive
    def map_rlist(fn, r):
        if r is not Rlist.empty:
            r.first = fn(r.first)
            map_rlist(fn, r.rest)

    # iterative
    def map_rlist(fn, r):
        while r is not Rlist.empty:
            r.first = fn(r.first)
            r = r.rest

</solution>

</block contents>
