from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'exam'

references = [
    'Lecture: Names, Environment diagrams',
    'Lecture: Environment diagrams 2',
    'Discussion 1a',
    'Discussion 1b',
]

notes = ''

contents = [
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker': make_env_question,
         'questions': lambda: env_questions},
]

env_questions = [
    {'code': """
def funny(joke):
    hoax = joke + 1
    return funny(hoax)

def sad(joke):
    hoax = joke - 1
    return hoax + hoax

funny, sad = sad, funny
result = funny(sad(1))

# pay special attention to the names of
# the frames!""",
    },

    {'code': """
def double(x):
    return double(x + x)

first = double

def double(y):
    return y + y

result = first(10)"""
    },

    {'code': """
def fun(fun):
    def time(time):
        return fun(x)
    x = 4
    return time

def boo(x):
    return x**2
    x = 5

result = fun(boo)(10)""",
    },

    {'code': """
from operator import sub
def trick(me, you):
    sub = treat
    return sub

def treat(me, you):
    return sub(me, 1)

treat = trick
trick(3, 4)""",
    },

    {'code': """
def easy(x):
    def peasy(y):
        def ironic(name):
            return name(x, y)
        return y
    return peasy

result = easy(4)(easy)(2)""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

