from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'exam'

references = [
    'Discussion 2',
    'Lecture: Names',
    'Lecture: Control and Higher-Order Functions',
    'Lecture: Higher-Order Functions',
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
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+funny(joke)%3A%0A++++hoax+%3D+joke+%2B+1%0A++++return+funny(hoax)%0A%0Adef+sad(joke)%3A%0A++++hoax+%3D+joke+-+1%0A++++return+hoax+%2B+hoax%0A%0Afunny,+sad+%3D+sad,+funny%0Aresult+%3D+funny(sad(1))&mode=display&cumulative=true&py=3&curInstr=13",},

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
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+fun(fun)%3A%0A++++def+time(time)%3A%0A++++++++return+fun(x)%0A++++x+%3D+4%0A++++return+time%0A%0Adef+boo(x)%3A%0A++++return+x**2%0A++++x+%3D+5%0A%0Aresult+%3D+fun(boo)(10)&mode=display&cumulative=true&py=3&curInstr=11",},

    {'code': """
from operator import sub
def trick(me, you):
    sub = treat
    return sub

def treat(me, you):
    return sub(me, 1)

treat = trick
trick(3, 4)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+sub%0Adef+trick(me,+you)%3A%0A++++sub+%3D+treat%0A++++return+sub%0A%0Adef+treat(me,+you)%3A%0A++++return+sub(me,+1)%0A%0Atreat+%3D+trick%0Atrick(3,+4)&mode=display&cumulative=true&py=3&curInstr=8",},

    {'code': """
def easy(x):
    def peasy(y):
        def ironic(name):
            return name(x, y)
        return y
    return peasy

result = easy(4)(easy)(2)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+easy(x)%3A%0A++++def+peasy(y)%3A%0A++++++++def+ironic(name)%3A%0A++++++++++++return+name(x,+y)%0A++++++++return+y%0A++++return+peasy%0A%0Aresult+%3D+easy(4)(easy)(2)&mode=display&cumulative=true&py=3&curInstr=11",},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

