from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Dictionaries'
level = 'basic'

references = [
    'Lecture: Objects, Lists, and Dictionaries',
    'Discussion 6',
]

notes = ''

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
]

concept_questions = [
    {'description': """What type of objects can be used as keys for
        dictionaries? What type of objects can be used as values?""",
    'solution': """Any <b>immutable</b> object can be used as a key --
    this includes numbers, strings, and tuples. Mutable objects, such
    as lists and dictionaries, are not allowed to be used as keys.
    Anything can be used as a value, however."""
    },

    {'description': """How many objects can a single key map to?""",

    'solution': """A single key can only map on to one value. That
    value can, however, be a sequence like a tuple or a list, so you
    can effectively map to multiple things (but it still only counts
    as one value)."""
    },

    {'description': """Are dictionaries ordered?""",

    'solution': """Python dictionaries are not ordered. If you were to
    iterate through the dictionary, the order in which you iterate
    through them is not necessarily the ordre in which you added them.
    """
    },
]

print_questions = [
    {'prompts': [
        ("logins = {'albert': 'cs61a-tg'}",),
        ("logins['albert']", "'cs61a-tg'"),
        ("logins['cs61a-tg']", "KeyError"),
        ("logins['allen'] = None",),
        ("len(logins)", '2'),
        ("""for elem in logins:
...     print(elem)""", """allen
albert  # not necessarily in that order"""),
        ("""for key, value in logins.items():
...     print(key, value)""", """allen None
albert cs61a-tg # not necessarily in that order"""),
        ]},
]

code_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    }
]

env_questions = [
    {'code': """
def code(test):
    return test
""",
'solution': 'hi',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

