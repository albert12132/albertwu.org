from template.utils import make_list, references_li, contents_li,\
        make_section, \
        make_concept_question, make_env_question

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'basic'

references = [
        ('Lecture: Higher-Order Functions',),
    ('Discussion 2',),
    ('Discussion 3',),
    ('Lab 3',),
]

contents = [
    ('Conceptual', 'conceptual',
        lambda: make_concept_question,
        lambda: concept_questions),
    ('Environment Diagrams', 'env',
        lambda: make_env_question,
        lambda: env_questions),
    ('Code Writing', 'code',
        lambda: make_concept_question,
        lambda: code_questions),
]

concept_questions = [
    {'description': """What is the definition of a higher-order function?""",
     'code': None,
     'hint': None,
    },
]

env_questions = [
    {'code': """
def my_strat(score):
    return score + 2

def play(strat):
    i, roll = 0, strat(0)
    while i < roll:
        result = my_strat(i)
        i += 1
    return i

result = play(my_strat)

# How many times do we call my_strat?
# Remember to label the frames with the intrinsic
# name of the functions
""" },
    {'code': """
def fun(x):
    return x**2

def time(y):
    y, x = 4, 5
    def fun(y):
        return y + x
    return fun

a = time(10)
b = a(2)

# Which fun is called?
# Which y is used?
# What type of object is a?
""" },
    {'code': """
x = 4

def outer(f):
    def inner(g):
        return f(g(x))
    return inner

def square(x):
    return x**2

c = outer(square)(square)
""" },
    {'code': """
def one(f):
    a = 1
    def two(g):
        b = 2
        def three(h):
            c = 3
            return f(a) + g(b) + h(c)
        return three
    return one

def identity(x):
    return x

def square(x):
    return x**2

def cube(x):
    return x**3

middle = one(identity)(square)
result = middle(cube)

# what function is middle?
# What are the parents of each frame?
""" },
]

code_questions = [
    {'description': """Write a function <tt>make_mod</tt> that takes a number, <tt>n</tt>, as an argument, and returns a new function. The new function should take a single argument, <tt>x</tt>, and return the result of <tt>x</tt> modulo <tt>n</tt>.""",
     'code': """
def make_mod(n):
    \"\"\"Returns a function that takes an argument x.
    That function will return x modulo n.

    &gt;&gt;&gt; mod_7 = make_mod(7)
    &gt;&gt;&gt; mod_7(3)
    3
    &gt;&gt;&gt; mod_7(41)
    6
    \"\"\"
    "*** YOUR CODE HERE ***"
""",
     'hint': None,
    },
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
