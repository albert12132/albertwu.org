from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = "Newton's method"
level = 'basic'

references = [
    ("Lecture: Newton's method",
        'http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/06_1pp.pdf'),
]

notes = """We will be using the implementation of Newton's method and
iterative improvement from lecture:""" + \
pre("""
# iterative improvement framework

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

# Newton's method

def make_derivative(f, delta=1e-5):
    def derivative(x):
        df = f(x + delta) - f(x)
        return df / delta
    return derivative

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)""",
classes='prettyprint')



contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
]

concept_questions = [
    {
        'description': """Describe what iterative improvement is and
        how it works.""",
        'solution': """Iterative improvement is a programming
        technique that involves updating an initial guess until it
        comes close enough to the correct solution. Iterative
        improvement algorithms have two major components: an
        <tt>update</tt> function; and an <tt>close</tt> function
        (which tells you when you can stop)."""
    },
    {
        'description': """Conceptually, what is the <tt>update</tt>
        function for Newton's method? What is the <tt>close</tt>
        function for Newton's method?""",
        'code': """
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

# the following is defined inside find_zero
def near_zero(x):
    return approx_eq(f(x), 0)
""",
    'solution': """<tt>newton_update</tt> is not the actual update
    function -- instead, depending on what <tt>f</tt> is given, it
    will create an <tt>update</tt> function that follows the
    mathematical equation for Newton's Method.
    <tt>near_zero</tt> is the <tt>close</tt> function, and
    returns True when <tt>f(x)</tt> is approximately equal to 0 --
    this is the goal of Newton's method."""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

