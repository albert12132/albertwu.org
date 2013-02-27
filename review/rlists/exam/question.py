from utils.utils import p, pre
from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Recursive Lists'
level = 'exam'

references = [
    'Lecture: Sequences and Iterables',
    'Lab 5',
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
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

print_questions = [
    {'prompts': [
            ('r = rlist(1, rlist(rlist(2, empty_rlist), rlist(4, empty_rlist)))'),
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

    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    &gt;&gt;&gt; rlist_to_tup(alternate(r))
    (1, 3)
    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
    &gt;&gt;&gt; rlist_to_tup(alternate(r))
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

    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    &gt;&gt;&gt; rlist_to_tup(filter_rlist(lambda x: x % 2 == 1, r))
    (1, 3)
    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
    &gt;&gt;&gt; rlist_to_tup(filter_rlist(lambda x: x % 3 == 1, r))
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

attrs = globals()

