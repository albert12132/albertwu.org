from utils import utils
from review.utils.utils import *

def make_env_question(num, question):
    assert 'code' in question, 'not a valid environment diagram'
    text = h(3, 'Q' + str(num), classes='question')
    text += p('For the following question, draw the diagram using <b>dynamic scoping</b>')
    text += prettify(question['code'])

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    text += div(a(question['solution'], 'Link to solution', internal=False),
            classes=['solution', tag])
    return text

#---------#
# CONTENT #
#---------#

title = 'Dynamic Scope'
level = 'exam'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker': make_env_question,
         'questions': lambda: env_questions},
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
lst = [1]
def outer(x):
    lst = [x]
    def inner(y):
        lst.append(y)
        return x
    return inner

x = outer(3)
x(4)(5)""",
    'solution': 'exam_1.jpg',
    },

    {'code': """
def study(x):
    return x*y

def final(y):
    return study(y)

y = 4
x = study(3)
z = final(x)""",
    'solution': 'exam_2.jpg',
    },

    {'code': """
def silly(x):
    if x == 0:
        return y
    return names(x - 1)

def names(y):
    if y == 0:
        return x
    return silly(y - 1)

silly(3)""",
    'solution': 'exam_3.jpg',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

