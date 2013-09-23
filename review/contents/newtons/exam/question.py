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
    # {'name': 'Conceptual',
    #  'id': 'conceptual',
    #  'maker': make_concept_question,
    #  'questions': lambda: concept_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

concept_questions = [
    {
        'description': """Question Description.""",
        'code': """
def foo(test):
    return 'this is a test'
""",
        'solution': 'hi'
    },
]

code_questions = [
    {
        'description': """Using Newton's method, write a function
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
    return find_zero(f, make_derivative(f))"""
    },
    {
        'description': """An elementary exercise in calculus is to
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
    df = make_derivative(f)
    ddf = make_derivative(df)
    return find_zero(df, ddf)"""
    },
    {
        'description': """If Newton's method reaches a guess that has
        a slope of 0 (also known as a <a href='http://en.wikipedia.org/wiki/Critical_point_(mathematics)'>critical point</a>), then
        <tt>newton_update</tt> will raise a ZeroDivisionError (i.e.
        the derivative of the function = 0). Rewrite
        <tt>newton_update</tt> to add a small <tt>offset</tt> to the
        derivative if it is equal to zero to avoid this problem.""",
        'code': """
def newton_update(f, df, offset=1e-5):
    "*** YOUR CODE HERE ***" """,
        'solution': """
def newton_update(f, df, offset=1e-5):
    def update(x):
        deriv = df(x)
        if deriv == 0:
            deriv += offset
        return x - f(x) / deriv
    return update
"""
    },
    {
        'description': """In economics, <i><a href='http://en.wikipedia.org/wiki/Walrasian_auction'>t&acirc;tonnement</a></i> is an iterative process for finding price equilibria in a market. The price
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

    def close(p):
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

