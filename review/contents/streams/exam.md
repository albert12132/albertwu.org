from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Streams'
level = 'exam'

references = [
    ('Lecture: Streams', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30-Streams_1pps.pdf'),
    ('Lab 10:', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab10/lab10.php'),
]

notes = """You can find the source code that contains the Stream class
""" + a('http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30.py', 'here', internal=False) + '.'

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
    {
        'description': """Given the following function, list the first 5 elements of the Stream that is returned by <tt>stream1()</tt>.""",
        'code': """
def stream1():
    def compute_rest():
        return add_streams(stream1(), stream1().rest)
    return Stream(0, lambda: Stream(1, compute_rest))""",
        'solution': '0, 1, 1, 2, 3 (the Fibonacci numbers)'
    },
    {
        'description': """Given the following function, list the first 5 elements of the Stream that is returned by <tt>stream2()</tt>.""",
        'code': """
def stream2():
    def compute_rest():
        return add_streams(stream2(), stream2())
    return Stream(1, compute_rest)""",
        'solution': '1, 2, 4, 8, 16 (the powers of 2)',
    },
]


code_questions = [
    {
        'description': """Create a function <tt>make_fact_stream</tt>,
        which returns a Stream whose <i>n</i>th element is <i>n</i>!
        (factorial of <i>n</i>).""",
        'code': """
def make_fact_stream():
    \"\"\"Returns a Stream of factorials.

    >>> s = make_fact_stream()
    >>> s.first      # 0!
    1
    >>> s.rest.first # 1!
    1
    >>> s.rest.rest.first   # 2!
    2
    >>> s.rest.rest.rest.first  # 3!
    6
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'hint': """This is similar to the <tt>make_fib_stream()</tt>
        function from discussion. Try writing an iterative factorial
        function first, then convert it into the Stream function.
        You should also use a helper function.""",
        'solution': """
def make_fact_stream():
    return fact_help(0, 1)

def fact_help(n, total)
    def rest():
        return fact_help(n + 1, total * (n + 1))
    return Stream(total, rest)

# here's the iterative factorial we use to convert
def infinite_fact():
    n, total = 0, 1
    while True:
        print(total)
        n, total = n + 1, total * n """,
    },
    {
        'description': 'This ' + a('http://www-inst.eecs.berkeley.edu/~cs61a/su12/lab/lab13/lab13.php', 'link', internal=False) + """
        contains Stream problems (as well as iterator and generator
        problems) from the summer 2012 version of 61A. They are pretty
        tough (probably tougher than final material), so don't get
        discouraged if you get stuck!""",
        'solution': """Solutions are also included in the lab (in the
        form of toggle buttons). Don't worry about the Py section --
        we didn't cover that this semester.""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

