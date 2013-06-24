from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Trees'
level = 'basic'

references = [
        'Lecture: Trees, memoization, and sets',
]

notes = 'We will be using the implementation of sets from lecture, found ' + a('http://www-inst.eecs.berkeley.edu/~cs61a/sp13/slides/25.py', 'here', internal=False) + '.'

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
]

concept_questions = [
    {'description': """Define each of the following terms:""" + utils.ul((
        'entry/datum',
        'node',
        'child',
        'parent,'
        'leaf',
        'forest',
        'binary search tree')),
    'solution': utils.ul((
        'entry/datum: an item contained inside of a node',
        'node: a single "circle" or vertex in a tree that contains an item (the node is the container, the datum is the item inside that container).',
        'child: a node that has a parent (i.e. a node that branches off from another node)',
        'parent: a node that has at least one child (i.e. a node that has other nodes branching off from it',
        'leaf: a node that has no children (has no other nodes branching off underneath it).'
        'forest: one or more trees',
        'binary search tree: a type of tree that staisfies the followign conditions: 1) each node can have at most 2 children, called a left and a right; 2) every element in the subtree to the left of the node must be smaller than the element in the node.',)),
    },
    {'description': """Which of the following are valid <tt>Tree</tt> constructors?""" + utils.ol(list(map(utils.tt, (
        'Tree()',
        'Tree(3)',
        'Tree(5, Tree(1), Tree(5))',
        'Tree(4, Tree(2))',
        'Tree(2, Tree(2, 4, 5))',
        )))),
    'solution': utils.ol((
        'Invalid: trees must contain at least one element',
        'Valid: this constructs a leaf with 3 as its entry',
        'Valid: this constructs a tree whose datum is 5, and has two children whose elements are 1 and 5',
        'Valid: this is a Tree that does not have a right child',
        'Invalid: the 2nd and 3rd argument to a Tree constructor must be other Trees',
        ))
    },
    {'description': """Draw a graphical representation of the following tree and answer these three questions:""" + utils.ol((
        'What number is contained in the root of this tree?',
        'Which numbers are contained in leaves?',
        'How many children does the node containing 14 have?',
        )),
        'code': """
Tree(25,
     Tree(14,
          Tree(9),
          Tree(20)),
     Tree(30,
          Tree(27)))""",
      'solution': '</p><p><img src="tree.png"></p>' + utils.ol((
        '25',
        '9, 20, 27',
        '2 children',
        ))
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

