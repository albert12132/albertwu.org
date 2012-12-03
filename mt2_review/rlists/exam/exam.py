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
def alternate(rlist):
    """Returns a new Rlist that conains every other element of the
    original.

    >>> r = Rlist(1, Rlist(2, Rlist(3)))
    >>> alternate(r)
    Rlist(1, Rlist(3))
    >>> r = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> alternate(r)
    Rlist(1, Rlist(3))
    """
    "*** YOUR CODE HERE ***"

# Q2
def reverse(rlist):
    """Returns a list with the same elements as the Rlist.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> reverse(rlist)
    Rlist(3, Rlist(2, Rlist(1)))
    >>> rlist = Rlist(Rlist(1, Rlist(2)), Rlist(3))
    >>> reverse(rlist)
    Rlist(3, Rlist(Rlist(1, Rlist(2))))
    """
    "*** YOUR CODE HERE ***"
    
# Q3
def deep_map(rlist, f):
    """Apply f onto each element in rlist -- if an element is an rlist,
    apply f onto each of its elements as well.

    >>> r = Rlist(1, Rlist(Rlist(2, Rlist(3)), Rlist(4)))
    >>> deep_map(r, lambda x: x**2)
    >>> r
    Rlist(1, Rlist(Rlist(4, Rlist(9)), Rlist(16)))
    """
    "*** YOUR CODE HERE ***"

# Q4
def deep_max(rlist):
    """Find the largest element in an Rlist and any of its nested 
    Rlists.

    >>> r = Rlist(1, Rlist(Rlist(4, Rlist(3)), Rlist(2)))
    >>> deep_max(r)
    4
    """
    "*** YOUR CODE HERE ***"

