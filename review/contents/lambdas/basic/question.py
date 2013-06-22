from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Lambda Expressions'
level = 'basic'

references = [
    'Lecture: Environments and Lambda',
    'Lab 3',
    'Discussion 3',
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
    {'description': """What are some differences between <tt>def</tt>
statements and <tt>lambda</tt> expressions?""",
    'solution': """Some differences between lambdas and def statements include:
<ul>
    <li>lambdas are expressions (they are a value), while defs are
    statements.</li>
    <li>lambdas can only be one liners</li>
    <li>lambdas are anonymous -- they have no intrinsic names</li>
</ul>"""},

    {'description': """What are the intrinsic names of the following functions?""",
     'code': """
def cube(x):
    return x * x * x

square = lambda x: x * x""",
    'solution': """The first function has an intrinsic name of <tt>cube</tt>. The second function does not have an intrinsic name, since it is a lambda. <b>Note</b> that the intrinsic name is the name you should write in your environment diagram frames!"""},
]

print_questions = [
    {'prompts': [
        ('lambda x: x * x', '<function <lambda > at ...>'),
        ('g = lambda x: x**2',),
        ('g(4)', '16'),
        ('(lambda x, y: x * y)(4, 5)', '20'),
    ]},
]

code_questions = [
    {'description': """Translate the following def statements into
lambda expressions.""",
     'code': """
# 1
def square(x):
    return x * x

# 2
def compose(f, g):
    def h(x):
        return f(g(x))
    return h""",
    'solution': """
# 1
square = lambda x: x * x

# 2
compose = lambda f, g: lambda x: f(g(x))""",
    },

    {'description': """Translate the following lambda expressions into
def statements.""",
     'code': """
# 1
pow = lambda x, y: x**y

# 2
foo = lambda x: lambda y: lambda z: x + y * z
""",
    'solution': """
# 1
def pow(x, y):
    return x**y

# 2
def foo(x):
    def f(y):
        def g(z):
            return x + y * z
        return g
    return f""",
    }
]

env_questions = [
    {'code': """
square = lambda x: x * x
higher = lambda f: lambda y: f(f(y))

higher(square)(5)
""",
    },

    {'code': """
a = (lambda f, a: f(a))(lambda b: b * b, 2)
""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

