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

notes = 'We will be using the implementation of sets from lecture, found ' + a('http://www-inst.eecs.berkeley.edu/~cs61a/sp13/slides/25.py', 'here', internal=False) + '.'

contents = [
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

code_questions = [
        {'description': """Implement a function <tt>equal</tt> which takes two trees and returns <tt>True</tt> if they satisfy all the following conditions:""" + utils.ul((
            'The data of both Trees are equal',
            'The Trees have the same number of children',
            'All corresponding pairs of sub-Trees are also <tt>equal</tt> (i.e. the left children of both trees are <tt>equal</tt>, and the right children of both trees are <tt>equal</tt>.)',
            )),
     'code': """
def equal(t1, t2):
    \"\"\"Returns Tree if t1 and t2 are equal trees.

    &gt;&gt;&gt; t1 = Tree(1,
    ...     Tree(2, Tree(4)),
    ...     Tree(3))
    &gt;&gt;&gt; t2 = Tree(1,
    ...     Tree(2, Tree(4)),
    ...     Tree(3))
    &gt;&gt;&gt; equal(t1, t2)
    True
    &gt;&gt;&gt; t3 = Tree(1,
    ...     Tree(2),
    ...     Tree(3, Tree(4)))
    &gt;&gt;&gt; equal(t1, t3)
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
        {'description': """Implement a function <tt>size</tt> that returns the number of elements in a given Tree.""",
     'code': """
def size(t):
    \"\"\"Returns the number of elements in a tree.

    &gt;&gt;&gt; t1 = Tree(1,
    ...     Tree(2, Tree(4)),
    ...     Tree(3))
    &gt;&gt;&gt; size(t1)
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
        {'description': """Implement a function <tt>height</tt>, which returns the height of a Tree. The <i>height</i> of a tree is defined as the number of branches from the <i>root</i> to the bottom-most leaf</i> of the Tree.""",
        'hint': 'by definition, a leaf has a height of 0, since there are 0 branches from the root to the root.',
     'code': """
def height(t):
    \"\"\"Returns the height of the tree.

    &gt;&gt;&gt; leaf = Tree(1)
    &gt;&gt;&gt; height(leaf)
    0
    &gt;&gt;&gt; t1 = Tree(1,
    ...     Tree(2, Tree(4)),
    ...     Tree(3))
    &gt;&gt;&gt; height(t1)
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
        {'description': """Implement the function <tt>contains</tt>, which takes a binary search tree and an item, and returns True if the binary search tree contains the item, and False if it doesn't.""",
     'code': """
def contains(b, item):
    \"\"\"Returns True if B contains ITEM.

    &gt;&gt;&gt; b1 = Tree(2,
    ...     Tree(1),
    ...     Tree(4, Tree(3)))
    &gt;&gt;&gt; contains(b1, 4)
    True
    &gt;&gt;&gt; contains(b1, 8)
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
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

