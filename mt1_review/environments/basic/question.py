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
""" },
    {'code': """
def mul(a, b):
    return a * b

def sum_of_squares(x, y):
    return mul(x, x) + mul(y, y)

result = sum_of_squares(3, 4)
""" },
    {'code': """
x = 4

def update_x(n):
    x = n
    return x

update_x(10)
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
    {'code': """
cats = True
dogs = cats

def bee(boots):
    x = 4
    if boots and cats:
        dogs = False
    return x

cats = bee(cats)
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
