from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Streams'
level = 'exam'

references = [
    'Lecture: Streams, Generators',
    'Discussion 7a',
]

notes = """You can find the source code that contains the Stream class """ + a('http://www-inst.eecs.berkeley.edu/~cs61a/sp13/slides/37.py', 'here', internal=False) + '.'

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

concept_questions = [
        {'description': """Given the following function, list the first 5 elements of the Stream that is returned by <tt>stream1()</tt>.""",
     'code': """
def stream1():
    def compute_rest():
        return add_streams(stream1(), stream1().rest)
    return Stream(0, lambda: Stream(1, compute_rest))""",
    'solution': '0, 1, 1, 2, 3 (the Fibonacci numbers)'
    },
        {'description': """Given the following function, list the first 5 elements of the Stream that is returned by <tt>stream2()</tt>.""",
     'code': """
def stream2():
    def compute_rest():
        return add_streams(stream2(), stream2())
    return Stream(1, compute_rest)""",
    'solution': '1, 2, 4, 8, 16 (the powers of 2)',
    },
]


code_questions = [
        {'description': 'This ' + a('http://www-inst.eecs.berkeley.edu/~cs61a/su12/lab/lab13/lab13.php', 'link', internal=False) + """ contains Stream problems (as well as iterator and generator problems) from the summer 2012 version of 61A. They are pretty tough (probably tougher than final material), so don't get discouraged if you get stuck!""",
            'solution': """Solutions are also included in the lab (in the form of toggle buttons). Don't worry about the Py section -- we didn't cover that this semester.""",}
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

