#######################
# TREE IMPLEMENTATION #
#######################

class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry =entry 
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return self.right == None and self.left == None

################
# CODE WRITING #
################

def equal(t1, t2):
    """Returns True if t1 and t2 are equal trees.

    >>> t1 = Tree(1,
    ...             Tree(2,
    ...                    Tree(4)),
    ...             Tree(3))
    >>> t2 = Tree(1,
    ...             Tree(2,
    ...                    Tree(4)),
    ...             Tree(3))
    >>> equal(t1, t2)
    True
    >>> t3 = Tree(1, 
    ...             Tree(2),
    ...             Tree(3,
    ...                    Tree(4)))
    >>> equal(t1, t3)
    False
    """
    "*** YOUR CODE HERE ***"

def size(t):
    """Returns the number of elements in a tree.

    >>> t1 = Tree(1,
    ...             Tree(2,
    ...                    Tree(4)),
    ...             Tree(3))
    >>> size(t1)
    4
    """
    "*** YOUR CODE HERE ***"

def height(t):
    """Returns the height of the tree.

    >>> leaf = Tree(1)
    >>> height(leaf)
    0
    >>> t1 = Tree(1,
    ...             Tree(2,
    ...                    Tree(4)),
    ...             Tree(3))
    >>> height(t1)
    2
    """
    "*** YOUR CODE HERE ***"

def max_ree(b):
    """Retrusn the largest element in a binary search tree.

    >>> b1 = Tree(2,
    ...             Tree(1),
    ...             Tree(4,
    ...                    Tree(3)))
    >>> max_tree(b1)
    4
    """
    "*** YOUR CODE HERE ***"

