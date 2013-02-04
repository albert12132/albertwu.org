from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_env_question

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'basic'

references = [
    ('Discussion 2',),
    ('Lecture: Names',),
    ('Lecture: Control and Higher-Order Functions',),
    ('Lecture: Higher-Order Functions',),
]

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_question,
        lambda: env_questions),
]

env_questions = [
    {'code': """
def square1(x):
    return x * x

def square2(x):
    print(x * x)

a = square1(3)
b = square2(3)

# How does return behave differently than print?
""" },
    {'code': """
def mul(a, b):
    return a * b

def sum_of_squares(x, y):
    return mul(x, x) + mul(y, y)

result = sum_of_squares(3, 4)

# How many times do we call mul?
# How many frames do we draw for mul?
""" },
    {'code': """
from operator import add
first = add(3, 4)

def add(a, b):
    return a + b

second = add(3, 4)

# What changes between the first time we call add and the
# second time? How does this affect our diagram?
""" },
    {'code': """
score, opp_score = 0, 0

def assign(arg0, arg1):
    score = arg0
    opp_score = arg1
    return True

success = assign(3, 9001)

# But did we really succeed?
# Did the global values of score and opp_score change?
""" },
    {'code': """
goal = 100

def foo(x):
    y = x + goal
    return b

result = foo(4)

# What's the lookup procedure for goal?
# Does result every show up in the diagram?
""" },
    {'code': """
from operator import add, sub
def a_plus_abs_b(a, b):
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

result = a_plus_abs_b(4, -4)
""" },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

contents_str = make_list(contents_li, contents)
references_str = make_list(references_li, references)
questions_str = '\n'.join(map(make_section, contents))

tag_names = {
    'title': title,               # title here
    'level': level,
    'references': references_str, # references
    'contents': contents_str,     # table of contents
    'questions': questions_str,
}
