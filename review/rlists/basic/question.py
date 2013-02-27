from utils.utils import p, pre, ol
from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Recursive Lists'
level = 'basic'

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
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
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

concept_questions = [
    {'description': """What type of object can <tt>first</tt> be (e.g.
        int, string, function, etc.)? What type of object can
        <tt>rest</tt> be?""",
     'solution': """<tt>first</tt> can be any type of object, even an
     rlist. <tt>rest</tt> can only be an rlist."""
    },

    {'description': """Which of the following are valid Rlist constructors?""",
     'code': """
rlist(1, 3)
rlist(1, None)
rlist(1, rlist(4, empty_rlist))
rlist(1, empty_rlist)
rlist()""",
    'solution': """The correct answers are in bold:""" + pre("""
rlist(1, 3)
rlist(1, None)
<b>rlist(1, rlist(4, empty_rlist))</b>
<b>rlist(1, empty_rlist)</b>
rlist()""", classes='prettyprint'),
    },

    {'description': """Construct an rlist that contains the following
    elements:""",
     'code': """
1, 3, lambda x: x, 'hi'""",
    'solution':  pre("""
rlist(1, rlist(3, rlist(lambda x: x, rlist('hi', empty_rlist))))""",
classes='prettyprint'),
    },

    {'description': """What is the element at index 2 of the following
    rlist?""",
     'code': """
rlist('this', rlist(rlist('is', rlist('a', empty_rlist)), rlist('question', empty_rlist)))""",
    'solution': "<tt>'question'</tt>",
    },

    {'description': """What is the length of the rlist in the previous
    question?""",
    'solution': '3',
    },
]

print_questions = [
    {'prompts': [
            ('r = rlist(1, rlist(2, rlist(3, empty_rlist)))',),
            ('first(r)', '1'),
            ('rest(r)', '(2, (3, none))'),
            ('rest(rest(r))', '(3, none)'),
            ('first(rest(r))', '2'),
            ('first(rest(rest(r)))', '3'),
        ]},
]

code_questions = [
    {'description': """Implement a function <tt>tup_to_rlist</tt> that
        takes a tuple as an argument, and returns an rlist that
        contains the same elements as the tuple.""",
     'code': """
def rlist_to_tup(lst):
    \"\"\"Returns an rlist with the same elements as the tuple.

    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    &gt;&gt;&gt; tup_to_rlist(r)
    (1, 2, 3)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
# recursive
def rlist_to_tup(lst):
    if lst == empty_rlist:
        return ()
    return (first(lst),) + rlist_to_tup(rest(lst))

# iterative
def rlist_to_tup(lst):
    new = ()
    while lst != empty_rlist:
        new += (first(lst),)
        lst = rest(lst)
    return new"""
    },

    {'description': """Implement a function <tt>map_rlist</tt> that
    maps a function <tt>f</tt> onto each element of an rlist.""",
     'code': """
def map_rlist(lst, f):
    \"\"\"Maps f onto each element in the rlist.

    &gt;&gt;&gt; r = rlist(1, rlist(2, rlist(3, empty_rlist)))
    &gt;&gt;&gt; rlist_to_tup(map_rlist(r, lambda x: x**2))
    (1, 4, 9)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
# recursive
def map_rlist(lst, f):
    if lst == empty_rlist:
        return empty_rlist
    return rlist(f(first(lst)), map_rlist(rest(lst, f)))

# iterative
def map_rlist(lst, f):
    new = empty_rlist
    while lst != empty_rlist:
        new = rlist(f(first(lst)), new)
        lst = rest(lst)
    while new != empty_rlist:
        lst = rlist(first(lst), lst)
        new = rest(new)
    return lst"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

