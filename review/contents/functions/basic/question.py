from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Map, filter, and friends'
level = 'basic'

references = [
    ('Lecture: Strings and Sequence Processing',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/13-Strings_1pps.pdf'),
    ('Lab 5',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab05/lab05.php'),
]

notes = ''

contents = [
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

print_questions = [
    {
        'prompts': [
            ('tup = (1, 2, 3, 4, 5)',),
            ('map(lambda x: x*2, tup)', '<map object ...>'),
            ('tuple(map(lambda x: x*2, tup))', '(2, 4, 6, 8, 10)'),
            ('tup', '(1, 2, 3, 4, 5)'),
            ('tuple(map(lambda x: 3, tup))', '(3, 3, 3, 3, 3)'),
        ]
    },
    {
        'prompts': [
            ('tup = (1, 2, 3, 4, 5)',),
            ('filter(lambda x: x % 2 == 0, tup)', '<filter object>'),
            ('tuple(filter(lambda x: x % 2 == 0, tup))', '(2, 4)'),
            ('tup', '(1, 2, 3, 4, 5)'),
            ('tuple(filter(lambda x: False, tup))', '()'),
        ]
    },
    {
        'prompts': [
            ('from functools import reduce',),
            ('tup = (1, 2, 3, 4, 5)',),
            ('reduce(lambda x, y: x + y, tup)', '15'),
            ('reduce(lambda x: x**2, tup)', 'TypeError'),
        ]
    },
]

code_questions = [
    {
        'description': """Implement a function <tt>map</tt> that acts
        just like the built-in <tt>map</tt>, except that it returns a
        tuple instead of a map object.""",
        'code': """
def map(f, seq):
    \"\"\"Acts just like the built-in map function, but returns a
    tuple.

    >>> tup = (1, 2, 3, 4)
    >>> map(lambda x: x**2, tup)
    (1, 4, 9, 16)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def map(f, seq):
    tup = ()
    for elem in seq:
        tup += (f(elem),)
    return tup"""
    },
    {
        'description': """Implement a function <tt>filter</tt> that acts
        just like the built-in <tt>filter</tt>, except that it returns
        a tuple instead of a filter object.""",
        'code': """
def filter(pred, seq):
    \"\"\"Acts just like the built-in filter function, but returns a
    tuple.

    >>> seq = range(10)
    >>> map(lambda x: x % 2 == 0, seq)
    (0, 2, 4, 6, 8)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def filter(pred, seq):
    tup = ()
    for elem in seq:
        if pred(elem):
            tup += (elem,)
    return tup"""
    },
    {
        'description': """Implement a function <tt>reduce</tt> that acts
        just like the built-in <tt>reduce</tt>.""",
        'code': """
def reduce(combiner, seq):
    \"\"\"Acts just like the built-in reduce function.

    >>> seq = (1, 2, 3, 4, 5, 6)
    >>> reduce(lambda x, y: x + y, seq)
    21
    >>> reduce(lambda x, y: x * y, (1, 2, 3, 4))
    24
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def reduce(combiner, seq):
    total = seq[0]
    for elem in seq[1:]:
        total = combiner(total, elem)
    return total""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

