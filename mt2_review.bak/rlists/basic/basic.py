################
# RLIST BASICS #
################

empty = None

class Rlist:
    """Implementation of Rlists. This implementation may or may not
    be used in the exam."""

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        """A particular way to represent an Rlist as a string."""
        if self.rest == empty:
            return 'Rlist({})'.format(self.first)
        return 'Rlist({}, {})'.format(self.first, repr(self.rest))

################
# CODE-WRITING #
################

# Q1
def tup_to_rlist(tup):
    """Returns an Rlist with the same elements as the tuple.

    >>> tup = (1, 2, 3, 4)
    >>> tup_to_rlist(tup)
    Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    """
    "*** YOUR CODE HERE ***"

# Q2
def rlist_to_list(rlist):
    """Returns a list with the same elements as the Rlist.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> rlist_to_list(rlist)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"

# Q3
def map_rlist(rlist, f):
    """Maps f onto each element in the Rlist. Mutate the Rlist -- do
    not return a new Rlist.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> map_rlist(rlist, lambda x: x**2)
    >>> rlist
    Rlist(1, Rlist(4, Rlist(9)))
    """
    "*** YOUR CODE HERE ***"

