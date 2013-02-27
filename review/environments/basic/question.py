from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'basic'

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
def square1(x):
    return x * x

def square2(x):
    print(x * x)

a = square1(3)
b = square2(3)

# How does return behave differently than print?""",
    'solution': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+square1(x)%3A%0A++++return+x+*+x%0A%0Adef+square2(x)%3A%0A++++print(x+*+x)%0A%0Aa+%3D+square1(3)%0Ab+%3D+square2(3)%0A%0A%23+How+does+return+behave+differently+than+print%3F&mode=display&cumulative=true&py=3&curInstr=0',},

    {'code': """
def mul(a, b):
    return a * b

def sum_of_squares(x, y):
    return mul(x, x) + mul(y, y)

result = sum_of_squares(3, 4)

# How many times do we call mul?
# How many frames do we draw for mul?""",
    'solution': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+mul(a,+b)%3A%0A++++return+a+*+b%0A%0Adef+sum_of_squares(x,+y)%3A%0A++++return+mul(x,+x)+%2B+mul(y,+y)%0A%0Aresult+%3D+sum_of_squares(3,+4)%0A%0A%23+How+many+times+do+we+call+mul%3F%0A%23+How+many+frames+do+we+draw+for+mul%3F&mode=display&cumulative=true&py=3&curInstr=0',},

    {'code': """
from operator import add
first = add(3, 4)

def add(a, b):
    return a + b

second = add(3, 4)

# What changes between the first time we call add and the
# second time? How does this affect our diagram?""",
    'solution': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+add%0Afirst+%3D+add(3,+4)%0A%0Adef+add(a,+b)%3A%0A++++return+a+%2B+b%0A%0Asecond+%3D+add(3,+4)%0A%0A%23+What+changes+between+the+first+time+we+call+add+and+the%0A%23+second+time%3F+How+does+this+affect+our+diagram%3F&mode=display&cumulative=true&py=3&curInstr=0',},

    {'code': """
score, opp_score = 0, 0

def assign(arg0, arg1):
    score = arg0
    opp_score = arg1
    return True

success = assign(3, 9001)

# But did we really succeed?
# Did the global values of score and opp_score change?""",
    'solution': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=score,+opp_score+%3D+0,+0%0A%0Adef+assign(arg0,+arg1)%3A%0A++++score+%3D+arg0%0A++++opp_score+%3D+arg1%0A++++return+True%0A%0Asuccess+%3D+assign(3,+9001)%0A%0A%23+But+did+we+really+succeed%3F%0A%23+Did+the+global+values+of+score+and+opp_score+change%3F&mode=display&cumulative=true&py=3&curInstr=0',},

    {'code': """
goal = 100

def foo(x):
    y = x + goal
    return b

result = foo(4)

# What's the lookup procedure for goal?
# Does result every show up in the diagram?""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=goal+%3D+100%0A%0Adef+foo(x)%3A%0A++++y+%3D+x+%2B+goal%0A++++return+b%0A%0Aresult+%3D+foo(4)%0A%0A%23+What's+the+lookup+procedure+for+goal%3F%0A%23+Does+result+every+show+up+in+the+diagram%3F&mode=display&cumulative=true&py=3&curInstr=0",},

    {'code': """
from operator import add, sub
def a_plus_abs_b(a, b):
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

result = a_plus_abs_b(4, -4)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+add,+sub%0Adef+a_plus_abs_b(a,+b)%3A%0A++++if+b+%3C+0%3A%0A++++++++op+%3D+sub%0A++++else%3A%0A++++++++op+%3D+add%0A++++return+op(a,+b)%0A%0Aresult+%3D+a_plus_abs_b(4,+-4)&mode=display&cumulative=true&py=3&curInstr=0",},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

