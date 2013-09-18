from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Recursion'
level = 'exam'

references = [
    'Lecture: Recursion',
    'Lecture: Tree Recursion',
    'Lab 3',
    'Discussion 3',
]

notes = ''

contents = [
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Environment Diagrams',
     'id': 'env',
     'maker': make_env_question,
     'questions': lambda: env_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
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

env_questions = [
    {
        'code': """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

ans = factorial(2)
"""
    },
    {
        'code': """
def foo(n):
    i = 0
    if n == 0:
        return 0
    result = foo(n - 2)
    i += 1
    return i + result

result = foo(4)
"""
    },
    {
        'code': """
def bar(f):
    def g(x):
        if x == 1:
            return f(x)
        else:
            return f(x) + g(x - 1)
    return g

f = 4
bar(lambda x: x + f)(2)
"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

