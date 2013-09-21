from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = "Newton's method and Iterative Improvement"
level = 'exam'

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
#         {'name': 'Conceptual',
#          'id': 'conceptual',
#          'maker': make_concept_question,
#          'questions': lambda: concept_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

concept_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    },
]

code_questions = [
        {'description': """Using Newton's method, write a function
        <tt>fourth_root</tt> that calculates the fourth root of a
        number <tt>x</tt>. <i>Note</i>: this is not quite the same as
        finding the root of the fourth root (since that's just <tt>x =
        0</tt>).
        """,
     'code': """
def fourth_root(x):
    "*** YOUR CODE HERE ***" """,
    'solution': """
def fourth_root(x):
    f = lambda y: y**4 - x
    return find_root(f)"""
    },
        {'description': """An elementary exercise in calculus is to
        find a critical point of a function. The <a href='http://en.wikipedia.org/wiki/Critical_point_(mathematics)'>critical point</a>
        of a mathematical function <i>f</i> is a value <i>x</i> such
        that the <i>derivative of f</i> at <i>x</i> is equal to 0 (i.e.
        f'(x) = 0). For example, the critical point of
        <i>f(x) = (x - 1)<super>2</super></i> is <i>x = 1</i>.</p>

        <p>Write a function <tt>critical_point</tt> that takes a
        function <tt>f</tt> and returns a critical point for that
        function.""",
     'code': """
def critical_point(f):
    \"\"\"Returns a single critical point for the function F.\"\"\"
    "*** YOUR CODE HERE ***" """,
    'solution': """
def critical_point(f):
    f_prime = lambda x: approx_derivative(f, x)
    return find_root(f_prime)"""
    },
        {'description': """In economics, <i><a href='http://en.wikipedia.org/wiki/Walrasian_auction'>t&acirc;tonnement</a></i> is an iterative process for finding price equilibria in a market. The price
        of a good is adjusted depending on the amount of excess
        demand until demand is equal to supply. The price at which
        this happens is called the equilibrium price. Here is one
        such recurrence for finding the equilibrium price:</p>

        <img src='tatonnement.png'>

        <p>where <i>p<sub>i</sub></i> is the price at iteration
        <i>i</i>, and <i>z<sub>i</sub></i> is the excess demand
        (demand minus supply) at iteration <i>i</i>.</p>

        <p>Write a function <tt>equilibrium</tt>, which takes
        in a supply and demand function (both functions that take in
        a price as an argument and output a quantity), and returns
        an approximation of the equilibrium price. See the docstring
        for more details.""",
     'code': """
def equilibrium(supply, demand, tolerance=1e-2):
    \"\"\"Calculates the equilibrium price for the given SUPPLY and
    DEMAND functions.

    You need to figure out two things: the UPDATE function and the
    ISCLOSE function. UPDATE should follow the equation described
    above. ISCLOSE should return True when demand minus supply is less
    than certain TOLERANCE level.

    PARAMETERS:
    supply    -- a function that takes a price and outputs
    demand    -- a function that takes a price and outputs
    tolerance -- how far from 0 the excess demand can vary
    \"\"\"
    initial_guess = 1

    def update(p):
        "*** YOUR CODE HERE ***"

    def isclose(p):
        "*** YOUR CODE HERE ***"

    return improve(update, isclose, initial_guess)
""",
    'solution': """
def equilibrium(supply, demand, tolerance=1e-2):
    initial_guess = 1

    def update(p):
        return p * (1 + demand(p) - supply(p))

    def isclose(p):
        return abs(demand(p) - supply(p)) <= tolerance

    return improve(update, isclose, initial_guess)"""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

