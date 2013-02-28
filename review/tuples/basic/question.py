from utils.utils import p, pre
from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Tuples'
level = 'basic'

references = [
    'Lab 5',
    'Lecture: Sequences',
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
    {'description': """What does <i>immutability</i> mean? How does
        it relate to tuples?""",

    'solution': """An object that is <i>immutable</i> cannot be
    modified after it is created. For example, tuples and strings are
    immutable. Consider the following:""" + pre("""
x = (1, 2, 3, 4)
x[0] = 4""", classes='prettyprint') + """This will cause an error:
    since tuples are immutable, we cannot change its elements. The
    question then is, why does this work?""" + pre("""
x = (1, 2, 3, 4)
x += (5,)""", classes='prettyprint') + """The reason why this doesn't
    cause an error is because we <b>are not mutating the original
    tuple</b>. Instead we are creating a new tuple, and assigning it
    to <tt>x</tt>."""
    },
]

print_questions = [
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0]', '1'),
            ('x[3]', '4'),
            ('x[4]', 'IndexError'),
            ('x[-1]', '4'),
            ('x[-4]', '1'),
            ('x[-5]', 'IndexError'),
            ('x[5.0]', 'TypeError'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0:4]', '(1, 2, 3, 4)'),
            ('x[1:3]', '(2, 3)'),
            ('x[:3]', '(1, 2, 3)'),
            ('x[0:]', '(1, 2, 3, 4)'),
            ('x[:]', '(1, 2, 3, 4)'),
            ('x[:10000]', '(1, 2, 3, 4)'),
            ('x[100:10000]', '()'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0:3:2]', '(1, 3)'),
            ('x[:3:2]', '(1, 3)'),
            ('x[1::2]', '(2, 4)'),
            ('x[::2]', '(1, 3)'),
            ('x[::-1]', '(4, 3, 2, 1)'),
            ('x[0:4:-1]', '()'),
        ]},
    {'prompts': [
            ('x = (1, 2, 3, 4)',),
            ('x[0]', '1'),
            ('x[0:1]', '(1,)'),
            ('len(x)', '4'),
            ('1 in x', 'True'),
            ('10 not in x', 'True'),
            ('(1, 2) in x', 'False'),
            ("""if x:
...     print("hi")""", "hi"),
            ('y = ()',),
            ("""if y:
...     print("hi")""", "# nothing"),
        ]},
]

code_questions = [
    {'description': """Write a function <tt>reverse</tt> that reverses
        a given tuple.""",
     'code': """
def reverse(tup):
    \"\"\"Reverse the given tuple.

    &gt;&gt;&gt; reverse((1, 2, 3, 4))
    (4, 3, 2, 1)
    &gt;&gt;&gt; reverse(())
    ()""",
    'solution': """
def reverse(tup):
    if not tup:
        return ()
    return reverse(tup[1:]) + (tup[0],)"""
    }
]

env_questions = [
    {'code': """
def draw(me):
    return me[2]

y = (4, 5, 6)
x = (1, 2, draw(y))""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+draw(me)%3A%0A++++return+me%5B2%5D%0A%0Ay+%3D+(4,+5,+6)%0Ax+%3D+(1,+2,+draw(y))&mode=display&cumulative=true&py=3&curInstr=5",
    },
    {'code': """
def draw(me, too):
    tup = (too,)
    return me + tup

y = (1, 2)
x = draw(y, 3)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+draw(me,+too)%3A%0A++++tup+%3D+(too,)%0A++++return+me+%2B+tup%0A%0Ay+%3D+(1,+2)%0Ax+%3D+draw(y,+3)&mode=display&cumulative=true&py=3&curInstr=6"
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

