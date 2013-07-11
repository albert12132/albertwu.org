from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Lambda Expressions'
level = 'exam'

references = [
    "Lecture: Lambda, Newton's method",
    'Lab 1a',
]

notes = ''

contents = [
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker': make_env_question,
         'questions': lambda: env_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

code_questions = [
    {'description': """Fill in the blanks for the following expression
        so that <tt>result</tt> is a list.""",
     'code': """
x = lambda x, y: lambda: [x, y]
result = (lambda ____, game: fun(_____)_____)(x, (3, 2))""",
    'solution': """
result = (lambda fun, game: fun(game[0], game[1])())(x, (3, 2))"""
    },
    {'description': """Fill in the blanks for the following expression
        so that <tt>result</tt> is the number 3.""",
     'code': """
f = lambda: lambda x: x[0]
result = (lambda _____: f(_____)(_____))(lambda: [3])""",
    'solution': """
result = (lambda var: f()(var()))(lambda: [3])"""
    },
]

env_questions = [
    {'code': """
f = lambda x: lambda y: lambda z: g(x + y + z)

g = f(3)
f(4)(5)(6)""",
    },
    {'code': """
fn = lambda f, a: f(f(2*a))

result = fn(lambda x: x*x, 2)""",
    },
    {'code': """
fn = lambda: lambda: print('hi')

def example(x):
    print('example')
    return x

result = example(fn())()""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

