from utils import utils
from review.utils.utils import *

def make_env_question(num, question):
    assert 'code' in question, 'not a valid environment diagram'
    text = h(3, 'Q' + str(num), classes='question')
    text += p('For the following question, draw the diagram using <b>dynamic scoping</b>')
    text += pre(question['code'], classes='prettyprint')
    return text

def make_env_solution(num, question):
    assert 'solution' in question, 'Not a valid solution'
    text = h(3, 'Q' + str(num), classes='question')
    text += a(question['solution'], 'Solution', internal=False)
    return text

#---------#
# CONTENT #
#---------#

title = 'Dynamic Scope'
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker q': make_env_question,
         'maker s': make_env_solution,
         'questions': lambda: env_questions},
]

concept_questions = [
    {'description': """What is the difference between lexical scope and dynamic scope?""",
    'solution': """The difference is in the way they do lookup. In <b>lexical scope</b>, a function's parent is the frame in which it was <i>defined</i>. In <b>dynamic scope</b>, a function's parent is the frame in which it was <i>called</i>.""",
    },

    {'description': """What type of scoping does Python use?""",
    'solution': """Python uses lexical scoping.""",
    },
]

code_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    }
]


env_questions = [
    {'code': """
x = 4
def f1(a):
    x = 2*a
    def f2(b):
        b = x + b
        return b
    return f2

f1(x)(3)""",
'solution': 'basic_1.jpg',
    },

    {'code': """
lst = [3]
def outer(x):
    def inner(y):
        lst.append(y)
        return x
    return inner

outer(3)(4)""",
    'solution': 'basic_2.jpg',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

