from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Identity vs. Equality'
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
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
    {'description': """What condition must be satisfied for the
        expression <tt>a is b</tt> to be <tt>True</tt>?""",
    'solution': """<tt>a</tt> and <tt>b</tt> must reference the same
    physical object in memory."""
    },

    {'description': """What special method determines if
    <tt>a == b</tt> to be <tt>True</tt>?""",
    'solution': """In each class, the <tt>__eq__</tt> determines if
    two objects are equivalent (but not identical). For user-defined
    types (i.e. classes), you can implement your own <tt>__eq__</tt>
    method! Otherwise, the default <tt>__eq__</tt> for user-defined
    types behaves the same way as <tt>is</tt>."""
    },

    {'description': """For built-in types, if <tt>a is b</tt> is
    <tt>True</tt>, is <tt>a == b</tt> guaranteed to be <tt>True</tt>?
    """,
    'solution': """Yes. in other words, a built-in object is, by
    definition, equivalent with itself. However, for user-defined
    types, you are able to break this property!"""
    },
]

print_questions = [
    {'prompts': [
            ('s = [1, 2, 3, 4]',),
            ('s == [1, 2, 3, 4]', 'True'),
            ('s is [1, 2, 3, 4]', 'False'),
            ('[1, 2, 3, 4] is [1, 2, 3, 4]', 'False  # 2 separate objects in memory!'),
            ('a = s',),
            ('a is s', 'True'),
            ('a[1:] is s[1:]', 'False  # slicing always creates new objects in memory'),
        ]},
    {'prompts': [
            ('s = (1, 2, 3, 4)',),
            ('s is (1, 2, 3, 4)', 'False  # Immutability has nothing to do with identity'),
            ('s == [1, 2, 3, 4]', 'False  # a tuple cannot be equivalent to a list'),
            ("'hello' == 'hello'", 'True'),
            ("'hello' is 'hello'", 'True   # strings are special -- Python only creates one copy of a string literal in memory'),
        ]},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#
questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

