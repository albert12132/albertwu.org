from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Recursion'
level = 'basic'

references = [
    ('Lecture: Recursion',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/07-Recursion_1pps.pdf'),
    ('Lecture: Tree Recursion',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf'),
    ('Lab 3',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab03/lab03.php'),
    ('Discussion 3',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion03.pdf'),
]

notes = ''

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
        'description': """What is a recursive function?""",
        'solution': """A <b>recursive function</b> is a function that
        calls itself one or more times. The call to itself is called
        a <b>recursive call</b>.""",
    },
    {
        'description': """Explain what base cases and recursive
        cases are. How do they interact with each other?""",
        'solution': """A <b>base case</b> is an input that requires no
        recursive calls to compute; the output for that input is
        "immediately" known. A <b>recursive case</b> is an input that
        requires one or more recursive calls to compute an output.
        Since each recursive case makes a call to the function again,
        it eventually needs a stopping point: that stopping point is
        the base case."""
    },
    {
        'description': """What is a tree recursive function? How is it
        different from a linearly recursive function?""",
        'solution': """A <b>tree recursive</b> function is a function
        that makes two more recursive calls to itself (for example,
        the <tt>fibonacci</tt> function). This is different from
        linearly recursive functions (such as <tt>factorial</tt>),
        because linearly recursive functions make exactly one
        recursive call."""
    },
    {
        'description': """Describe what is wrong with the following
        function and find a way to fix it:""",
        'code': """
def factorial(n):
    return n * factorial(n)
""",
        'solution': """There are two problems with <tt>factorial</tt>.
        """ + ol((
            """First, the recursive call is made on the exact same
            input <tt>n</tt>. Since the input never gets smaller, the
            function will loop forever. To fix it, change the argument
            to the recursive call from <tt>n</tt> to <tt>n-1</tt>.""",
            """There is no base case. There's no stopping point, so
            it will run forever. To fix it, add a base case for
            <tt>n == 0</tt>"""
        )) + """Notice that you need to fix both of these problems
        for it to work, otherwise the function will still loop
        forever!""" + pre("""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)""", classes='prettyprint')
    },

]

code_questions = [
    {
        'description': """A geometric series is a series whose first
        element is some number <i>a</i>; each element is equal to
        the previous element multiplied by some other number <i>r</i>.
        For example, the series</p>""" +
        "<img src='geo-series.png'>" + """<p>is a geometric series with
        the first element <i>a = 1</i> and ratio <i>r = 1/2</i>.</p>
        <p>Implement a function <tt>geo_sum</tt> that takes three
        numbers <tt>a</tt> and <tt>r</tt> (as defined above) and
        <tt>n</tt>, and calculates the sum of the first <tt>n</tt>
        elements of the geometric series defined by <tt>a</tt> and
        <tt>r</tt>. <b>Use recursion!</b>""",
        'code': """
def geo_sum(a, r, n):
    \"\"\"Returns the first n elements of a geometric series.

    >>> geo_sum(1, 1/2, 4)  # 1 + 1/2 + 1/4 + 1/8
    1.875
    >>> geo_sum(2, 2, 3)  # 2 + 4 + 8
    14
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def geo_sum(a, r, n):
    if n == 1:
        return a
    else:
        return a + geo_sum(a*r, r, n-1)"""
    },
    {
        'description': """Implement a function <tt>num_primes</tt>
        which takes a number <tt>n</tt> and returns the number of
        prime numbers less than <i>or equal to</i> <tt>n</tt>. You
        can assume there is already a function <tt>is_prime</tt>
        that takes in a number <i>i</i> and returns <tt>True</tt>
        if <i>i</i> is prime, and <tt>False</tt> otherwise.
        <b>Use recursion!</b>""",
        'code': """
def num_primes(n):
    \"\"\"Returns the number of primes less than or equal to n.

    >>> num_primes(6)   # 2, 3, 5
    3
    >>> num_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    \"\"\"
    "*** YOUR CODE HERE ***"

def is_prime(i):
    m = 2
    while m * m <= i:
        if i % m == 0:
            return False
        m += 1
    return True""",
        'solution': """
def num_primes(n):
    if n < 2:
        return 0
    elif is_prime(n):
        return 1 + num_primes(n - 1)
    else:
        return num_primes(n - 1)"""
    },
    {
        'description': """Implement a function <tt>any</tt>
        which takes two numbers <tt>a</tt> and <tt>b</tt> and a
        predicate function <tt>pred</tt>, and returns <tt>True</tt> if
        any number from <tt>a</tt> to <tt>b</tt> inclusive satisfies
        <tt>pred</tt> (i.e. return <tt>True</tt> if there exists some
        number <i>i</i> such that <tt>a</tt> &le; <i>i</i> &le;
        <tt>b</tt> and <tt>pred(i)</tt> returns <tt>True</tt>). You
        may assume <tt>a</tt> &le; <tt>b</tt>.
        <b>Use recursion!</b>""",
        'code': """
def any(a, b, pred):
    \"\"\"Returns the number of primes less than or equal to n.

    >>> any(1, 4, lambda x: x % 2 == 0)
    True
    >>> any(-5, 2, lambda x: x * x == -3 * x)   # -3 satisfies pred
    True
    >>> any(1, 6, lambda x: x % 7 == 0)
    False
    >>> any(0, 6, lambda x: x % 7 == 0)
    True
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def any(a, b, pred):
    if a == b:
        return pred(a)
    else:
        return pred(b) or any(a, b - 1, pred)"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

