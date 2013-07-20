from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
#     {'name': 'Conceptual',
#      'id': 'conceptual',
#      'maker': make_concept_question,
#      'questions': lambda: concept_questions},
#     {'name': 'Environment Diagrams',
#      'id': 'env',
#      'maker': make_env_question,
#      'questions': lambda: env_questions},
#     {'name': 'Code Writing',
#      'id': 'code',
#      'maker': make_code_question,
#      'questions': lambda: code_questions},
#     {'name': 'What would Python print?',
#      'id': 'print',
#      'maker': make_print_question,
#      'questions': lambda: print_questions},
    {'name': 'Eval vs. Display',
     'id': 'eval-print',
     'maker': make_eval_print_question,
     'questions': lambda: eval_print_questions},
]

concept_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    },
]

print_questions = [
    {'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
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

eval_print_questions = [
    {'prompts': [
        ('print(2 + 3)', 'None', '5'),
    ],
     'description': 'this is a description'}
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

