from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'basic'

references = [
    'Lecture: Higher-Order Functions',
    'Lab 2',
    'Discussion 2',
]

notes = ''

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
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

concept_questions = [
    {
        'description': """What is the definition of a higher-order
        function?""",
        'solution': """A function is a higher-order function if it
        satisfies at least one of the following:
<li>It takes at least one function as an argument</li>
<li>It returns a function</li>
"""
    },

    {
        'description': """In the following code, what type of object
        (number, boolean, string, function) does <tt>foo</tt> return?
        What type of object should <tt>x</tt> be for this function to
        work?""",
        'code': """
def foo(x):
    def inner(y):
        return x(y)
    return inner
""",
        'solution': """<tt>foo</tt> should return a <b>function</b>
        object (in particular, the function <tt>inner</tt>).
        <tt>x</tt> should also be a <b>function</b>, or else calling
        <tt>inner</tt> will result in an error (because it will try
        <tt>x(y)</tt>)."""
    },
]

print_questions = [
    {
        'prompts': [
            ("""def silly():
...     def rabbit(y):
...         return 'Tricks are for kids!'
...     print('Lucky Charms?')
...     return False""",),
            ('a = silly()', 'Lucky Charms?'),
            ('a', 'False'),
            ('a(5)', 'TypeError'),
        ]
    },
    {
        'prompts': [
            ("""def func1(fn):
...     def inner():
...         return fn(2)
...     return inner""",),
            ("""def func2(fn):
...     def inner():
...         return fn(2)
...     return inner()""",),
            ('func1(lambda x: x * x)', '<function inner at ...>'),
            ('func2(lambda x: x * x)', '4'),
        ]
    },
    {
        'prompts': [
            ("""def dream1(totem):
...     def dream2(totem_guess):
...         print('I think my totem is a', totem_guess)
...         return totem_guess == totem
...     return dream2""",),
            ("inception = dream1('top')",),
            ('inception', '<function dream2 at ...>'),
            ("inception('spinning top')", """I think my totem is a spinning top
False"""),
        ]
    },
]

env_questions = [
    {
        'code': """
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
# name of the functions""",
    },
    {
        'code': """
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
# What type of object is a?""",
    },
    {
        'code': """
def square(x):
    return x * x

def boom(fn):
    def bam(x):
        print(x)
        return fn(x)
    return bam

boom(square)
a = boom(square)
a(4)""",
    },
    {
        'code': """
x = 4

def outer(f):
    def inner(g):
        return f(g(x))
    return inner

def square(x):
    return x**2

c = outer(square)(square)""",
    },
    {
        'code': """
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
# What are the parents of each frame?""",
    },
]

code_questions = [
    {
        'description': """Write a function <tt>make_mod</tt> that
        takes a number, <tt>n</tt>, as an argument, and returns a new
        function. The new function should take a single argument,
        <tt>x</tt>, and return the result of <tt>x</tt> modulo
        <tt>n</tt>.""",
        'code': """
def make_mod(n):
    \"\"\"Returns a function that takes an argument x.
    That function will return x modulo n.

    >>> mod_7 = make_mod(7)
    >>> mod_7(3)
    3
    >>> mod_7(41)
    6
    \"\"\"
    "*** YOUR CODE HERE ***"
""",
        'solution': """
def make_mod(n):
    def mod_n(x):
        return x % n
    return mod_n
"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

