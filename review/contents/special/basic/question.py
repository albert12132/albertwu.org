from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Special Methods'
level = 'basic'

references = [
    'Lecture: Generic functions',
    'Lecture: Multiple representations, Coercion',
    'Lab 4b',
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
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
]

concept_questions = [
    {
        'description': """Special methods provide a common interface
        across many different types of objects. List some special
        methods and the contexts in which they are used.""",

        'solution': """Here are some examples:</p>""" + ul((
            '<tt>__init__</tt>: used to create instances of a class.',
            """<tt>__len__</tt>: called by the built-in <tt>len</tt>
            to calculate the "length" of an object.""",
            """<tt>__getitem__</tt>: used with square brackets
            (<tt>[ ]</tt>) to retrieve an element at a certain index.
            """,
            """<tt>__repr__</tt>: returns a string representation
            of an object that is "Python readable" (could be typed
            into Python to replicate the same object).""",
            """<tt>__str__</tt>: returns a string representation of an
            object that is human readable"."""
            """<tt>__eq__</tt>: called when the <tt>==</tt> operator
            is used. Determines how to check if two objects are equal.
            """,
            """<tt>__add__</tt>: called when the <tt>+</tt> operator
            is used."""
        ))
    },
    {
        'description': """What do the underscores (e.g.
        <tt>__init__</tt>) in special method names do?""",

        'solution': """Functionally, the underscores don't do
        anything -- they are just part of the method name. However,
        when Python looks for a certain special method, it expects
        the name to have those underscores, so you can't leave them
        out!""",
    },
]

print_questions = [
    {
        'description': 'This is a description',
        'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
        ]
    },
]

code_questions = [
    {
        'description': """Question Description.""",
        'code': """
def foo(test):
    return 'this is a test'
""",
        'hint': 'This is a hint',
        'solution': 'hi'
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

