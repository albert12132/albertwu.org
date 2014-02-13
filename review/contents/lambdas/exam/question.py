from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Lambda Expressions'
level = 'exam'

references = [
    ('Lecture: Functions and Expressions',
        'http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/02_1pp.pdf'),
    ('Lecture: Environments',
        'http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/05_1pp.pdf'),
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
    {
        'description': """Fill in the blanks for the following
        expression so that <tt>result</tt> is the number 42.""",
        'code': """
x = lambda x, y: lambda: x - y
result = (lambda ____, question: one(__________)(x, 4)""",
    'solution': """
result = (lambda one, question: one(46, question)())(x, 4)"""
    },
    {
        'description': """Fill in the blanks for the following
        expression so that <tt>result</tt> is the boolean True.""",
        'code': """
x = lambda x: lambda y: x(y)
result = (lambda ______: x(fair)(dice))(lambda fair: fair == 3, 3)""",
    'solution': """
result = (lambda fair, dice: x(fair)(dice))(lambda fair: fair == 3, 3)"""
    },
#     {
#         'description': """Fill in the blanks for the following
#         expression so that <tt>result</tt> is a list.""",
#         'code': """
# x = lambda x, y: lambda: [x, y]
# result = (lambda ____, game: fun(_____)_____)(x, (3, 2))""",
#     'solution': """
# result = (lambda fun, game: fun(game[0], game[1])())(x, (3, 2))"""
#     },
#     {
#         'description': """Fill in the blanks for the following
#         expression so that <tt>result</tt> is the number 3.""",
#         'code': """
# f = lambda: lambda x: x[0]
# result = (lambda _____: f(_____)(_____))(lambda: [3])""",
#     'solution': """
# result = (lambda var: f()(var()))(lambda: [3])"""
#     },
    {
        'description': """Fill in the blanks for the following
        expression so that each call to <tt>mapper</tt> prints the
        output displayed below:""",
        'code': """
>>> def mapper(fn, num):
...     i = 0
...     while i < num:
...         print(fn(i))
...         i = i + 1
>>> mapper(lambda x: ______, 4)
1
3
5
7
>>> mapper(lambda x: ______, 5)
-2
-1
0
1
2
>>> mapper(lambda x: ______, 5)
0
-1
1
-2
2""",
    'solution': """
mapper(lambda x: 2 * x + 1, 4)
mapper(lambda x: x - 2, 5)
mapper(lambda x: (-1 ** x) * (x + 1) // 2, 5)"""
    },
]

env_questions = [
    {
        'code': """
f = lambda x: lambda y: lambda z: g(x + y + z)

g = f(3)
f(4)(5)(6)""",
    },
    {
        'code': """
fn = lambda f, a: f(f(2*a))

result = fn(lambda x: x*x, 2)""",
    },
    {
        'code': """
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

