from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Trees'
level = 'exam'

references = [
    'Lecture: Trees, memoization, and sets',
]

notes = 'We will be using the implementation of Trees from lecture:' + pre("""
class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right""", classes='prettyprint')

contents = [
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

code_questions = [
    {
        'description': """Implement a function <tt>equal</tt> which
        takes two trees and returns <tt>True</tt> if they satisfy all
        the following conditions:""" + utils.ul((
            'The data of both Trees are equal',
            'The Trees have the same number of children',
            """All corresponding pairs of sub-Trees are also
            <tt>equal</tt> (i.e. the left children of both trees are
            <tt>equal</tt>, and the right children of both trees are
            <tt>equal</tt>.)""",
        )),
        'code': """
def equal(t1, t2):
    \"\"\"Returns Tree if t1 and t2 are equal trees.

    >>> t1 = Tree(1,
    ...           Tree(2, Tree(4)),
    ...           Tree(3))
    >>> t2 = Tree(1,
    ...           Tree(2, Tree(4)),
    ...           Tree(3))
    >>> equal(t1, t2)
    True
    >>> t3 = Tree(1,
    ...           Tree(2),
    ...           Tree(3, Tree(4)))
    >>> equal(t1, t3)
    False
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def is_leaf(t):
    return t1.left is None and t2.left is None

def equal(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif is_leaf(t1) and is_leaf(t2):
        return t1.entry == t2.entry
    else:
        return equal(t1.left, t2.left) and equal(t1.right, t2.right)"""
    },
    {
        'description': """Implement a function <tt>size</tt> that
        returns the number of elements in a given Tree.""",
        'code': """
def size(t):
    \"\"\"Returns the number of elements in a tree.

    >>> t1 = Tree(1,
    ...           Tree(2, Tree(4)),
    ...           Tree(3))
    >>> size(t1)
    4
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def size(t):
    if t is None:
        return 0
    else:
        return 1 + size(t.left) + size(t.right)"""
    },
    {
        'description': """Implement a function <tt>height</tt>, which
        returns the height of a Tree. The <i>height</i> of a tree is
        defined as the number of branches from the <i>root</i> to the
        bottom-most leaf</i> of the Tree.""",
        'hint': """By definition, a leaf has a height of 0, since
        there are 0 branches from the root to the root.""",
        'code': """
def height(t):
    \"\"\"Returns the height of the tree.

    >>> leaf = Tree(1)
    >>> height(leaf)
    0
    >>> t1 = Tree(1,
    ...           Tree(2, Tree(4)),
    ...           Tree(3))
    >>> height(t1)
    2
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def height(t):
    if t is None or not t.left and not t.right:
        return 0
    else:
        return 1 + max(height(t.left), height(t.right))""",
    },
    {
        'description': """Implement the function <tt>contains</tt>,
        which takes a binary search tree and an item, and returns True
        if the binary search tree contains the item, and False if it
        doesn't.""",
        'code': """
def contains(b, item):
    \"\"\"Returns True if B contains ITEM.

    >>> b1 = Tree(2,
    ...           Tree(1),
    ...           Tree(4, Tree(3)))
    >>> contains(b1, 4)
    True
    >>> contains(b1, 8)
    False
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def contains(b, item):
    if b is None:
        return False
    elif b.entry == item:
        return True
    elif b.entry > item:
        return contains(b.left, item)
    elif b.entry < item:
        return contains(b.right, item)""",
    },
    {
        'description': """Implement a function <tt>nth_largest</tt>,
        which takes a <b>binary search tree</b> and a number
        <tt>n</tt> (greater than or equal to 1), and returns the
        <tt>nth</tt> largest item in the tree. For example,
        <tt>nth_largest(b, 1)</tt> should return the largest item in
        <tt>b</tt>. If <tt>n</tt> is greater than the number of items
        in the tree, return None.""",
        'hint': """You can assume there is a <tt>size</tt> function
        that returns the number of elements in a given tree.""",
         'code': """
def nth_largest(b, n):
    \"\"\"Returns the Nth largest item in T.

    >>> b1 = Tree(2,
    ...           Tree(1),
    ...           Tree(4, Tree(3)))
    >>> nth_largest(b1, 1)
    4
    >>> nth_largest(b1, 3)
    2
    >>> nth_largest(b1, 4)
    1
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def nth_largest(b, n):
    if b is None:
        return None
    right = size(b.right)
    if right == n - 1:
        return b.entry
    elif right > n - 1:
        return nth_largest(b.right, n)
    elif right < n - 1:
        return nth_largest(b.left, n - 1 - right)"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

