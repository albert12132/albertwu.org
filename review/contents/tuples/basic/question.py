from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Tuples'
level = 'basic'

references = [
    ('Lecture: Sequences, Iterables',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/11-Sequences_1pps.pdf'),
    'Lab 3a',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'What would Python print?',
         'id': 'print',
         'maker': make_print_question,
         'questions': lambda: print_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker': make_env_question,
         'questions': lambda: env_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

concept_questions = [
    {'description': """What does <i>immutability</i> mean? How does
        it relate to tuples?""",

    'solution': """An object that is <i>immutable</i> cannot be
    modified after it is created. For example, tuples and strings are
    immutable. Consider the following:""" + pre("""
x = (1, 2, 3, 4)
x[0] = 4""", classes='prettyprint') + """This will cause an error:
    since tuples are immutable, we cannot change its elements. The
    question then is, why does this work?""" + pre("""
x = (1, 2, 3, 4)
x += (5,)""", classes='prettyprint') + """The reason why this doesn't
    cause an error is because we <b>are not mutating the original
    tuple</b>. Instead we are creating a new tuple, and assigning it
    to <tt>x</tt>."""
    },
]

print_questions = [
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0]', '1'),
            ('x[3]', '4'),
            ('x[4]', 'IndexError'),
            ('x[-1]', '4'),
            ('x[-4]', '1'),
            ('x[-5]', 'IndexError'),
            ('x[5.0]', 'TypeError'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0:4]', '(1, 2, 3, 4)'),
            ('x[1:3]', '(2, 3)'),
            ('x[:3]', '(1, 2, 3)'),
            ('x[0:]', '(1, 2, 3, 4)'),
            ('x[:]', '(1, 2, 3, 4)'),
            ('x[:10000]', '(1, 2, 3, 4)'),
            ('x[100:10000]', '()'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0:3:2]', '(1, 3)'),
            ('x[:3:2]', '(1, 3)'),
            ('x[1::2]', '(2, 4)'),
            ('x[::2]', '(1, 3)'),
            ('x[::-1]', '(4, 3, 2, 1)'),
            ('x[0:4:-1]', '()'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0]', '1'),
            ('x[0:1]', '(1,)'),
            ('len(x)', '4'),
            ('1 in x', 'True'),
            ('10 not in x', 'True'),
            ('(1, 2) in x', 'False'),
            ("""if x:
...     print("hi")""", "hi"),
            ('y = ()',),
            ("""if y:
...     print("hi")""", "# nothing"),
        ]},
]

code_questions = [
    {'description': """Write a function <tt>reverse</tt> that reverses
        a given tuple.""",
     'code': """
def reverse(tup):
    \"\"\"Reverse the given tuple.

    >>> reverse((1, 2, 3, 4))
    (4, 3, 2, 1)
    >>> reverse(())
    ()""",
    'solution': """
def reverse(tup):
    if not tup:
        return ()
    return reverse(tup[1:]) + (tup[0],)"""
    },

    {'description': """Write a function <tt>map</tt> that applies a
    function to every element in a given tuple. The result should be
    a newly created tuple.""",
     'code': """
def map(f, tup):
    \"\"\"Applies F to every element in TUP, and returns the results
    as a new tuple.

    >>> map(lambda x: x*x, (1, 2, 3, 4))
    (1, 4, 9, 16)
    >>> map(lambda x: x*x, ())
    ()""",
    'solution': """
def map(fn, tup):
    if not tup:
        return ()
    return (fn(tup[0]),) + map(fn, tup[1:])"""
    },

    {'description': """Write a function <tt>filter</tt> that takes a
    predicate function <tt>cond</tt> and a tuple <tt>tup</tt>, and
    returns a new tuple that contains only the elements in <tt>tup</tt>
    that satisfy <tt>cond</tt>.""",
     'code': """
def filter(cond, tup):
    \"\"\"Filters out elements of TUP using the predicate COND.

    >>> filter(lambda x: x % 2 == 0, (1, 2, 3, 4, 5))
    (2, 4)
    >>> filter(lambda x: x % 2 == 0, ())
    ()""",
    'solution': """
def filter(cond, tup):
    if not tup:
        return ()
    elif cond(tup[0]):
        return (tup[0],) + filter(cond, tup[1:])
    else:
        return filter(cond, tup[1:])"""
    }
]

env_questions = [
    {'code': """
def draw(me):
    return me[2]

y = (4, 5, 6)
x = (1, 2, draw(y))""",
    },
    {'code': """
def draw(me, too):
    tup = (too,)
    return me + tup

y = (1, 2)
x = draw(y, 3)""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

