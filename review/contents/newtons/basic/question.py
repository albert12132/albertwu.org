from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = "Newton's method and Iterative Improvement"
level = 'basic'

references = [
    "Lecture: Newton's method",
]

notes = """We will be using the implementation of Newton's method and
iterative improvement from lecture:""" + \
pre("""
# iterative improvement framework

def improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

# Newton's method

def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def find_root(f, initial_guess=10):
    def close_to_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f), close_to_zero, initial_guess)""",
classes='prettyprint')




contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
]

concept_questions = [
    {'description': """Describe what iterative improvement is and how
        it works.""",
    'solution': """Iterative improvement is a programming technique
    that involves updating an initial guess until it comes close enough
    to the correct solution. Iterative improvement algorithms have two
    major components: an <tt>update</tt> function; and an
    <tt>isclose</tt> function (which tells you when you can stop).
    """
    },
    {'description': """Conceptually, what is the <tt>update</tt>
    function for Newton's method? What is the <tt>isclose</tt> function
    for Newton's method?""",
     'code': """
def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def close_to_zero(x):
    return approx_eq(f(x), 0)
""",
    'solution': """<tt>newton_update</tt> is not the actual update
    function -- instead, depending on what <tt>f</tt> is given, it
    will create an <tt>update</tt> function that follows the
    mathematical equation for Newton's Method.
    <tt>close_to_zero</tt> is the <tt>isclose</tt> function, and
    returns True when <tt>f(x)</tt> is approximately equal to 0 --
    this is the goal of Newton's method."""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

