from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Rlists as Classes'
level = 'exam'

references = [
    'Lecture: Memoization, Recursive Data, Sets',
    'Lab 4b',
    'Discussion 4b',
]

notes = """For this section, we will be using the <tt>Rlist</tt>
class implementation from lecture:""" + pre("""
class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __repr__(self):
        if self.rest is Rlist.empty:
            return 'Rlist({})'.format(repr(self.first))
        return 'Rlist({}, {})'.format(repr(self.first),
                                      repr(self.rest))""",
    classes='prettyprint')

contents = [
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

code_questions = [
    {
        'description': """Implement a function <tt>validate</tt>,
        which takes an Rlist and returns True if the Rlist is valid.
        """,
        'code': """
def validate(r):
    \"\"\"Returns True if R is a valid Rlist.

    >>> r = Rlist(1, Rlist(2, Rlist(3)))
    >>> validate(r)
    True
    >>> okay = Rlist(Rlist(1), Rlist(2))
    >>> validate(okay)
    True
    >>> bad = Rlist(1, 2)
    >>> validate(Rlist.empty)
    True
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def validate(r):
    if r is Rlist.empty:
        return True
    elif r.rest is not Rlist.empty and type(r.rest) != Rlist:
        return False
    else:
        return valdiate(r.rest)"""
    },
    {
        'description': """Implement a function <tt>count</tt>,
        which takes an Rlist and another value, and counts the number
        of times that <tt>value</tt> is found in the Rlist.""",
        'code': """
def count(r, value):
    \"\"\"Counts the number of times VALUE shows up in R.

    >>> r = Rlist(3, Rlist(3, Rlist(2, Rlist(3))))
    >>> count(r, 3)
    3
    >>> count(r, 2)
    1
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def count(r, value):
    if r is Rlist.empty:
        return 0
    elif r.first == value:
        return 1 + count(r.rest, value)
    else:
        return count(r.rest, value)"""

    },
    {
        'description': """Implement a function <tt>extend_rlist</tt>,
        which takes two Rlists, <tt>s1</tt> and <tt>s2</tt>, and
        mutates <tt>s1</tt> such that it contains the elements of
        <tt>s2</tt> at its tail. Do this mutatively -- don't return
        anything! Also, make sure <tt>s2</tt> itself does not get
        attached to <tt>s1</tt>. You may assume <tt>s1</tt> always
        has at least one element.""",
        'code': """
def extend_rlist(s1, s2):
    \"\"\"Extends s1 to include the elements of s2.

    >>> s1 = Rlist(1)
    >>> s2 = Rlist(2, Rlist(3))
    >>> extend_rlist(s1, s2)
    >>> s1
    Rlist(1, Rlist(2, Rlist(3)))
    >>> s1.rest is not s2
    True
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'hint': """This question is similar to the
        <tt>extend_rlist</tt> from lecture, except this version
        mutates the original Rlist and does not make <tt>s2</tt> part
        of <tt>s1</tt>.""",
        'solution': """
def extend_rlist(s1, s2):
    if s2 is Rlist.empty:
        return
    elif s1.rest is Rlist.empty:
        s1.rest = Rlist(s2.first)
        extend_rlist(s1.rest, s2.rest)
    else:
        extend_rlist(s1.rest, s2)"""

    },
    {
        'description': """Implement a function <tt>deep_map</tt>,
        which takes an (possibly nested) Rlist and a function
        <tt>fn</tt>, and applies <tt>fn</tt> to every element in the
        Rlist. If an element is itself an Rlist, recursively apply
        <tt>fn</tt> to each of the element's elements.""",
        'code': """
def deep_map(fn, r):
    \"\"\"Applies FN to every element in R.

    >>> normal = Rlist(1, Rlist(2, Rlist(3)))
    >>> deep_map(lambda x: x*x, normal)
    >>> normal
    Rlist(1, Rlist(4, Rlist(9)))
    >>> nested = Rlist(Rlist(1, Rlist(2)), Rlist(3, Rlist(4)))
    >>> deep_map(lambda x: x*x, nested)
    >>> nested
    Rlist(Rlist(1, Rlist(4)), Rlist(9, Rlist(16)))
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def deep_map(fn, r):
    if r is Rlist.empty:
        return
    if type(r.first) == Rlist:
        deep_map(fn, r.first)
    else:
        r.first = fn(r.first)
    deep_map(fn, r.rest)"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

