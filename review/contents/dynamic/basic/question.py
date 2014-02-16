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
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker': make_env_question,
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

attrs = globals()

