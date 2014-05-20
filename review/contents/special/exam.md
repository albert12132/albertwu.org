from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Special Methods'
level = 'exam'

references = [
    ('Lecture: Multiple representations',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/20-Interfaces_1pps.pdf'),
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
        'description': '',
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

