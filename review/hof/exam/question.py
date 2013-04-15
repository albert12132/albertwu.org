from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'exam'

references = [
    'Lecture: Higher-Order Functions',
    'Discussion 2',
    'Discussion 3',
]

notes = ''

contents = [
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker q': make_env_question,
         'maker s': make_env_solution,
         'questions': lambda: env_questions},
]

env_questions = [
    {'code': """
def f(x):
    return lambda y: x(y)

def g(x):
    return lambda : f(x) + f(y)

y = 2
result = f(g(f))""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+f(x)%3A%0A++++return+lambda+y%3A++x(y)%0A%0Adef+g(x)%3A%0A++++return+lambda+%3A+f(x)+%2B+f(y)%0A%0Ay+%3D+2%0Aresult+%3D+f(g(f))&mode=display&cumulative=true&py=3&curInstr=8",
    },

    {'code': """
def always_roll(n):
    return lambda s0, s1: n

def make_bad_strategy(p):
    def strategy(s0, s1):
        # next line is bad style!
        return always_roll(1 - p)(s0, s1)
    return strategy

num_rolls = make_bad_strategy(1)(50, 50)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+always_roll(n)%3A%0A++++return+lambda+s0,+s1%3A+n%0A%0Adef+make_bad_strategy(p)%3A%0A++++def+strategy(s0,+s1)%3A%0A++++++++%23+next+line+is+bad+style!%0A++++++++return+always_roll(1+-+p)(s0,+s1)%0A++++return+strategy%0A%0Anum_rolls+%3D+make_bad_strategy(1)(50,+50)&mode=display&cumulative=true&py=3&curInstr=12",
    },

    {'code': """
def dream1(f):
    kick = lambda x: mind()
    def dream2(secret):
        mind = f(secret)
        kick(2)
    return dream2

inception = lambda secret: lambda: secret
real = dream1(inception)(42)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+dream1(f)%3A%0A++++kick+%3D+lambda+x%3A+mind()%0A++++def+dream2(secret)%3A%0A++++++++mind+%3D+f(secret)%0A++++++++kick(2)%0A++++return+dream2%0A%0Ainception+%3D+lambda+secret%3A+lambda%3A+secret%0Areal+%3D+dream1(inception)(42)&mode=display&cumulative=true&py=3&curInstr=0",
    },

    {'code': """
def albert(albert):
    albert = albert()
    def albert():
        albert = lambda albert: albert
        return albert(albert)
    return albert

albert(lambda: albert)()""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+albert(albert)%3A%0A++++albert+%3D+albert()%0A++++def+albert()%3A%0A++++++++albert+%3D+lambda+albert%3A+albert%0A++++++++return+albert(albert)%0A++++return+albert%0A%0Aalbert(lambda%3A+albert)()&mode=display&cumulative=true&py=3&curInstr=13",
    },
]

eval_output_question = [
    {'code': """
def new(year):
    sign = 'snake'
    def red(env):
        if env == year:
            return sign
        else:
            return new
    return red

new, foo = lambda x: x * x, new
""",
    'prompts': [
        """foo(2013)""",
        """foo(new)""",
        """foo(new(4))(16)""",
        """foo(11)(11)""",
        """foo(2)(4)(2)""",
    ]},
]

eval_output_solutions = [
    {'prompts': [
        'foo(2013)',
        'foo(new)',
        'foo(new(4))(16)',
        'foo(11)(11)',
        'foo(2)(4)(2)',
    ], 'answers': [
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': '4',
         'output': '4'},
    ]},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

