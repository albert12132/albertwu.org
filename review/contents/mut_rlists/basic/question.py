from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Rlists as Classes'
level = 'basic'

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

    def__len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __repr__(self):
        if self.rest is empty:
            return 'Rlist({})'.format(repr(self.first))
        return 'Rlist({}, {})'.format(repr(self.first),
                                      repr(self.rest))""",
    classes='prettyprint')

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
    {
        'description': """What type of object can <tt>self.first</tt>
        be? What type of object can <tt>self.rest</tt> be?""",
        'solution': """<tt>self.first</tt> can be any type of object,
        including an <tt>Rlist</tt>. <tt>self.rest</tt> can only be
        an <tt>Rlist</tt> or an <tt>EmptyList</tt>."""
    },
    {
        'description': """How is the <tt>Rlist</tt> class different
        the <tt>rlist</tt> abstract data type we saw earlier in the
        course?""",
        'solution': """The <tt>Rlist</tt> class is mutable, meaning
        we can modify its contents. On the other hand, the
        <tt>rlist</tt> abstract data type is immutable, so it can not
        be mutated after it is created."""
    },
]

code_questions = [
    {
        'description': """Implement a function <tt>seq_to_rlist</tt>,
        which takes any type of sequence (e.g. tuple, list) and
        converts it to an <tt>Rlist</tt>.""",
        'code': """
def seq_to_rlist(seq):
    \"\"\"Converts SEQ into an Rlist.

    >>> seq = [1, 2, 3, 4]
    >>> seq_to_rlist(seq)
    Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> null = ()
    >>> seq_to_rlist(null) is Rlist.empty
    True
    \"\"\" """,
        'solution': """
# recursive
def seq_to_rlist(seq):
    if not seq:
        return Rlist.empty
    return Rlist(seq[0], seq_to_rlist(seq[1:]))

# iterative
def seq_to_rlist(seq):
    new = Rlist.empty
    for elem in seq[::-1]:
        new = Rlist(elem, new)
    return new"""
    },
    {
        'description': """Implement a function <tt>map_rlist</tt>,
        which takes an Rlist and a function <tt>fn</tt>, and applies
        <tt>fn</tt> to every element in the Rlist. <tt>map_rlist</tt>
        should <b>mutate</b> the Rlist -- do not return a new one!""",
        'code': """
def map_rlist(fn, r):
    \"\"\"Maps FN onto every element of the Rlist R.

    >>> r = Rlist(1, Rlist(2, Rlist(3)))
    >>> map_rlist(lambda x: x*x, r)
    >>> r
    Rlist(1, Rlist(4, Rlist(9)))
    \"\"\" """,
        'solution': """
# recursive
def map_rlist(fn, r):
    if r is not Rlist.empty:
        r.first = fn(r.first)
        map_rlist(fn, r.rest)

# iterative
def map_rlist(fn, r):
    while r is not Rlist.empty:
        r.first = fn(r.first)
        r = r.rest"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

