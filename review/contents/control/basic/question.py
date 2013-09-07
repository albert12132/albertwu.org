from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Control Structures'
level = 'basic'

references = [
    'Lecture: Control',
    'Lab 2',
    'Discussion 2',
]

notes = ''

contents = [
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Environment Diagrams',
     'id': 'env',
     'maker': make_env_question,
     'questions': lambda: env_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

print_questions = [
    {
        'prompts': [
            ('x = 4',),
            ('x > 2 and x < 6', 'True'),
            ('True and not True    # a.k.a. a contradiciton', 'False'),
            ('True and True        # a.k.a. a tautology', 'True'),
            ('False and True or True', 'True'),
            ('False and (True or True)', 'False'),
            ('False or True or 1 / 0', 'True'),
            ('False and 1 / 0', 'False'),
            ('3 and 4', '4'),
            ('3 or 4', '3'),
        ]
    },
    {
        'prompts': [
            ("""if True:
...     print('True!')
... else:
...     print('False!')""", 'True!'),

            ("""if 4:
...     print('True!')
... else:
...     print('False!')""", 'True!'),

            ("""if 0:
...     print('True!')
... else:
...     print('False!')""", 'False!'),

            ("""x = 42
>>> if x < 0:
...     print('negative')
... elif x == 42:
...     print('The answer to everthing')
... else:
...     print('Boring number')""", 'The answer to everything'),
        ]
    },
    {
        'prompts': [
            ("""x = 0
>>> while x < 5:
...     x += 1
...     print(x)""", """1
2
3
4
5"""),

            ("""while False:
...     print('hi!')""", '# nothing happens'),

            ("""while True:
...     print('hi!')
...     # press Control C to get out of this""", """hi!
hi!
hi!
# forever"""),
            ("""def foo(n):
...     while n > 0:
...         if n * n == 8 * n - 16:
...             return True
...         n -= 1
...     return False
>>> foo(3)""", 'False'),
            ('foo(9)', 'True'),
        ]
    },
]

env_questions = [
    {
        'code': """
def branch(x):
    if x > 10:
        x -= 5
    elif x > 7:
        x -= 2
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

a = branch(12)
b = branch(8)""",
    },
    {
        'code': """
def uhoh(x):
    if x:
        y = 5
    return y

a = uhoh(True)
b = uhoh(False)""",
    },
    {
        'code': """
def is_even(x):
    return x % 2 == 0

i = 0
while i < 2:
    if is_even(i):
        print(i)
    i += 1""",
    },
]

code_questions = [
    {
        'description': """For each of the following functions, try to
        make the code more concise.""",
     'code': """
def one(x):
    if x == True:
        return 'input is true'
    else:
        return 'input is false'

def two(x):
    if x == 100:
        return True
    else:
        return False

def three(x):
    if x % 6 == 0:
        x += x // 6
        return x
    else:
        return x

def four(ones_win):
    if ones_win == True:
        result = 6
    elif ones_win == False:
        result = 4
""",
        'solution': """
def one(x):
    if x:
        return 'input is true'
    return 'input is false'

def two(x):
    return x == 100

def three(x):
    if x % 6 == 0:
        x += x // 6
    return x

def four(ones_win):
    result = 6 if ones_win else 4
"""
    },
    {
        'description': """Write a function <tt>summation</tt> that
        adds the first <tt>n</tt> elements in a sequence. The
        <tt>k</tt>th element in the sequence can be computed by
        evaluating <tt>term(k)</tt>.""",
        'code': """
def summation(n, term):
    \"\"\"Computes the summation of the first n numbers in the sequence
    defined by the function term.

    >>> square = lambda x: x * x
    >>> summation(5, square)
    55
    \"\"\"
    \"*** YOUR CODE HERE ***\"
""",
        'solution': """
def summation(n, term):
    k, total = 1, 0
    while k <= n:
        total += term(k)
        k += 1
    return total
"""
    },
    {
        'description': """Write a function <tt>is_fib</tt> that
        returns <tt>True</tt> if its input is a fibonacci number, and
        False otherwise.""",
        'code': """
def is_fib(n):
    \"\"\"Returns True if n is a fibonacci number,
    else False

    >>> is_fib(8)
    True
    >>> is_fib(9)
    False
    \"\"\"
    \"*** YOUR CODE HERE ***\"
""",
        'solution': """
def is_fib(n):
    cur, next = 0, 1
    while cur < n:
        cur, next = next, cur + next
    return cur == n
"""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

