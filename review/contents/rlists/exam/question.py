from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Recursive Lists'
level = 'exam'

references = [
    'Lecture: Sequences, Iterables',
    'Lab 3a ',
]

notes = p("""
We will be using the following implementation of immutable recursive
lists. Keep in mind that your code should not depend on the assumption
that rlists are implemented as tuples -- preserve data abstraction!
""") + pre("""
empty_rlist = None

def rlist(first, rest=empty_rlist):
    return (first, rest)

def first(s):
    return s[0]

def rest(s):
    return s[1]
""", classes='prettyprint')

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
    {'prompts': [
            ('r = rlist(1, rlist(rlist(2, empty_rlist), rlist(4, empty_rlist)))',),
            ('first(r)', '1'),
            ('first(rest(rest(r)))', '4'),
            ('first(first(rest(r)))', '2'),
        ]},
    {'prompts': [
            ('r = rlist(rlist(1, rlist(2, empty_rlist)), rlist(3, rlist(4, empty_rlist)))',),
            ('first(rest(r))', '3'),
            ('first(rest(first(r)))', '2'),
            ('first(first(rest(r)))', 'IndexError'),
        ]},
]

code_questions = [
    {'description': """Implement a function <tt>alternate</tt> which
        takes an rlist and returns a new rlist that contains
        <i>every other</i> element in the original rlist.""",
     'code': """
def alternate(lst):
    \"\"\"Returns a new rlist that contains every other element of the
    original.

    >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    >>> rlist_to_tup(alternate(r))
    (1, 3)
    >>> r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
    >>> rlist_to_tup(alternate(r))
    (1, 3)
""",
    'solution': """
def alternate(r):
    if r == empty_rlist:
        return empty_rlist
    elif rest(r) == empty_rlist:
        return r
    else:
        return rlist(first(r), alternate(rest(rest(r)))"""
    },

    {'description': """Implement a function <tt>filter_rlist</tt> which
        takes an rlist and returns a new rlist that contains
        only elements that satisfy the given predicate.""",
     'code': """
def filter(pred, lst):
    \"\"\"Returns a new rlist that contains elements of lst that
    satisfy the predicate.

    >>> r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    >>> rlist_to_tup(filter_rlist(lambda x: x % 2 == 1, r))
    (1, 3)
    >>> r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
    >>> rlist_to_tup(filter_rlist(lambda x: x % 3 == 1, r))
    (1, 4)
""",
    'solution': """
def filter(pred, lst):
    if r == empty_rlist:
        return empty_rlist
    elif pred(first(lst)):
        return rlist(first(lst), filter(pred, rest(lst)))
    else:
        return filter(pred, rest(lst))"""
    },

]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

