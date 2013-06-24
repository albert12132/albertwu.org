from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

concept_questions = [
    {'description': """What is a <b>constructor</b>? What is a <b>selector</b>?""",
    'solution': """A <b>constructor</b> is a function that creates an abstract object.
    A <b>selector</b> is a function that retrieves information from a specified object."""
    },

    {'description': """The following is the <tt>rlist</tt> abstract data type from
        lecture. Which functions are constructors? Which functions are selectors?""",
     'code': """
empty_rlist = ()

def rlist(first, rest):
    return (first, rest)

def first(r):
    return r[0]

def rest(r):
    return r[1]
""",
    'solution': """There is one constructor: <tt>rlist</tt>. There are two selectors:
        <tt>first</tt> and <tt>rest</tt>."""
    },
]


code_questions = [
    {'description': """Implement a function <tt>midpoint</tt> that calculates the
    midpoint of two points <tt>p1</tt> and <tt>p2</tt>. These two "point objects"
    are represented by an abstract data type, shown below.
        works:""",
     'code': """
def point(x, y):
    return (x, y)

def x_coord(p):
    return p[0]

def y_coord(p):
    return p[1]

def midpoint(p1, p2):
    \"\"\"Doctests:

    >>> p1, p2 = point(1, 1), point(3, 3)
    >>> p3 = midpoint(p1, p2)
    >>> x_coord(p3)
    2
    >>> y_coord(p3)
    2
    \"\"\"
    "*** YOUR CODE HERE ***" """,

    'solution': """
def midpoint(p1, p2):
    mid_x = (x_coord(p1) + x_coord(p2)) / 2
    mid_y = (y_coord(p1) + y_coord(p2)) / 2
    return point(mid_x, mid_y)"""
    },

    {'description': """Rewrite the follow
    midpoint of two points <tt>p1</tt> and <tt>p2</tt>. These two "point objects"
    are represented by an abstract data type, shown below.
        works:""",
     'code': """
def point(x, y):
    return (x, y)

def x_coord(p):
    return p[0]

def y_coord(p):
    return p[1]

def midpoint(p1, p2):
    \"\"\"Doctests:

    >>> p1, p2 = point(1, 1), point(3, 3)
    >>> p3 = midpoint(p1, p2)
    >>> x_coord(p3)
    2
    >>> y_coord(p3)
    2
    \"\"\"
    "*** YOUR CODE HERE ***" """,

    'solution': """
def midpoint(p1, p2):
    mid_x = (x_coord(p1) + x_coord(p2)) / 2
    mid_y = (y_coord(p1) + y_coord(p2)) / 2
    return point(mid_x, mid_y)"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

