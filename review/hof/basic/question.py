from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'basic'

references = [
    'Lecture: Higher-Order Functions',
    'Discussion 2',
    'Discussion 3',
    'Lab 3',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
        {'name': 'What would Python print?',
         'id': 'print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker q': make_env_question,
         'maker s': make_env_solution,
         'questions': lambda: env_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

concept_questions = [
    {'description': """What is the definition of a higher-order function?""",
    'solution': """A function is a higher-order function if it satisfies at least one of the following:
<li>It takes at least one function as an argument</li>
<li>It returns a function</li>
"""
    },

    {'description': """In the following code, what type of object (number, boolean, string, function) does <tt>foo</tt> return? What type of object should <tt>x</tt> be for this function to work?""",
     'code': """
def foo(x):
    def inner(y):
        return x(y)
    return inner
""",
    'solution': """<tt>foo</tt> should return a <b>function</b>object (in particular, the function <tt>inner</tt>). <tt>x</tt> should also be a <b>function</b>, or else calling <tt>inner</tt> will result in an error (because it will try <tt>x(y)</tt>)."""
    },
]

print_questions = [
    {'prompts': [
        ("""def silly():
...     def rabbit(y):
...         return 'Tricks are for kids!'
...     print('Lucky Charms?')
...     return False""",),
        ('a = silly()', 'Lucky Charms?'),
        ('a', 'False'),
        ('a(5)', 'TypeError'),
    ]},

    {'prompts': [
        ("""def func1(fn):
...     def inner():
...         return fn(2)
...     return inner""",),
        ("""def func2(fn):
...     def inner():
...         return fn(2)
...     return inner()""",),
        ('func1(lambda x: x * x)', '&lt;function inner at ...&gt;'),
        ('func2(lambda x: x * x)', '4'),
    ]},

    {'prompts': [
        ("""def dream1(totem):
...     def dream2(totem_guess):
...         print('I think my totem is a', totem_guess)
...         return totem_guess == totem
...     return dream2""",),
        ("inception = dream1('top')",),
        ('inception', '&lt;function dream2 at ...&gt;'),
        ("inception('spinning top')", """I think my totem is a spinning top
False"""),
    ]},
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
# name of the functions""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+my_strat(score)%3A%0A++++return+score+%2B+2%0A%0Adef+play(strat)%3A%0A++++i,+roll+%3D+0,+strat(0)%0A++++while+i+%3C+roll%3A%0A++++++++result+%3D+my_strat(i)%0A++++++++i+%2B%3D+1%0A++++return+i%0A%0Aresult+%3D+play(my_strat)%0A%0A%23+How+many+times+do+we+call+my_strat%3F%0A%23+Remember+to+label+the+frames+with+the+intrinsic%0A%23+name+of+the+functions&mode=display&cumulative=true&py=3&curInstr=0",
    },

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
# What type of object is a?""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+fun(x)%3A%0A++++return+x**2%0A%0Adef+time(y)%3A%0A++++y,+x+%3D+4,+5%0A++++def+fun(y)%3A%0A++++++++return+y+%2B+x%0A++++return+fun%0A%0Aa+%3D+time(10)%0Ab+%3D+a(2)%0A%0A%23+Which+fun+is+called%3F%0A%23+Which+y+is+used%3F%0A%23+What+type+of+object+is+a%3F&mode=display&cumulative=true&py=3&curInstr=0",
    },

    {'code': """
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
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+square(x)%3A%0A++++return+x+*+x%0A%0Adef+boom(fn)%3A%0A++++def+bam(x)%3A%0A++++++++print(x)%0A++++++++return+fn(x)%0A++++return+bam%0A%0Aboom(square)%0Aa+%3D+boom(square)%0Aa(4)&mode=display&cumulative=true&py=3&curInstr=16",
    },

    {'code': """
x = 4

def outer(f):
    def inner(g):
        return f(g(x))
    return inner

def square(x):
    return x**2

c = outer(square)(square)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=x+%3D+4%0A%0Adef+outer(f)%3A%0A++++def+inner(g)%3A%0A++++++++return+f(g(x))%0A++++return+inner%0A%0Adef+square(x)%3A%0A++++return+x**2%0A%0Ac+%3D+outer(square)(square)&mode=display&cumulative=true&py=3&curInstr=0",
    },

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
# What are the parents of each frame?""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+one(f)%3A%0A++++a+%3D+1%0A++++def+two(g)%3A%0A++++++++b+%3D+2%0A++++++++def+three(h)%3A%0A++++++++++++c+%3D+3%0A++++++++++++return+f(a)+%2B+g(b)+%2B+h(c)%0A++++++++return+three%0A++++return+one%0A%0Adef+identity(x)%3A%0A++++return+x%0A%0Adef+square(x)%3A%0A++++return+x**2%0A%0Adef+cube(x)%3A%0A++++return+x**3%0A%0Amiddle+%3D+one(identity)(square)%0Aresult+%3D+middle(cube)&mode=display&cumulative=true&py=3&curInstr=0",
    },
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
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

