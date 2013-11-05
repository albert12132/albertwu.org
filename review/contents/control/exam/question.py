from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Conrol Structures'
level = 'exam'

references = [
    ('Lecture: Control',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/03-Control_1pps.pdf'),
    ('Lab 2',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab02/lab02.php'),
    ('Discussion 2',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion02.pdf'),
]

notes = ''

contents = [
    # {'name': 'Conceptual',
    #  'id': 'conceptual',
    #  'maker': make_concept_question,
    #  'questions': lambda: concept_questions},
    # {'name': 'Environment Diagrams',
    #  'id': 'env',
    #  'maker': make_env_question,
    #  'questions': lambda: env_questions},
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
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

print_questions = [
    {
        'description': """The following code is loaded into the Python
        interpreter:""" + pre("""
def is_even(x):
    if x % 2 == 0:
        print('even')
    print('odd')
    return x - 1

def branch(x):
    if x > 5:
        print('one')
    elif x > 0:
        print('two')
    if x > 10:
        print('three')
    else:
        print('four')
    return x + 5""", classes='prettyprint'),
         'prompts': [
            ('a = is_even(4)', 'even\nodd'),
            ('b = branch(20)', 'one\nthree'),
            ('c = branch(3)', 'two\nfour'),
            ('d = is_even(is_even(5))', 'odd\neven\nodd'),
            ('e = branch(branch(3))', 'two\nfour\none\nfour'),
        ]
    },
]

code_questions = [
    {
        'description': """Implement a function <tt>is_ascending</tt>,
        which takes in a number <tt>n</tt>. <tt>is_ascending</tt>
        returns <tt>True</tt> if the one's digit of <tt>n</tt> is less
        than or equal to the ten's digit, and the ten's digit is less
        than or equal to the hundred's digit, and so on. In other
        words, the digits of the number going from right to left must
        be in ascending order.""",
        'code': """
def is_ascending(n):
    \"\"\"Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    \"\"\"
    "*** YOUR CODE HERE ***"
""",
        'solution': """
def is_ascending(n):
    largest = 0
    while n > 0:
        ones = n % 10
        if ones < largest:
            return False
        largest = ones
        n = n // 10
    return True"""
    },
    {
        'description': """Implement a function <tt>count_one</tt>,
        which takes in a number <tt>n</tt>, and returns the number of
        ones in the digits of <tt>n</tt>.""",
        'code': """
def count_one(n):
    \"\"\"Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    \"\"\"
    "*** YOUR CODE HERE ***"
""",
        'solution': """
def count_one(n):
    count = 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        n = n // 10
    return count""",
    },
    {
        'description': """Implement a function <tt>total_one</tt>,
        which takes in a number <tt>n</tt>, and returns the number of
        ones in the digits of all numbers from 1 to <tt>n</tt>.""",
        'hint': """You can use the <tt>count_one</tt> function from
        above.""",
        'code': """
def total_ones(n):
    \"\"\"Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    \"\"\"
    "*** YOUR CODE HERE ***"
""",
        'solution': """
def total_ones(n):
    i, total = 1, 0
    while i <= n:
        total += count_one(i)
        i += 1
    return total""",
    }
]

env_questions = [
    {'code': """
def code(test):
    return test
""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

