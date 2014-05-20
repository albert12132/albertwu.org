from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Recursion'
level = 'exam'

references = [
    ('Lecture: Recursion',
        'http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/07_1pp.pdf'),
    ('Lecture: Tree Recursion',
        'http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/08_1pp.pdf'),
    ('Lab 3',
     'http://www-inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab03/lab03.php'),
    ('Discussion 3',
     'http://www-inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion03.pdf'),
]

notes = ''

contents = [
    # {'name': 'What would Python print?',
    #  'id': 'print',
    #  'maker': make_print_question,
    #  'questions': lambda: print_questions},
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
        'description': 'This is a description',
        'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
        ]
    },
]

code_questions = [
    {
        'description': """In game theory, a <i>subtraction game</i> is
         a simple game with two players, player 0 and player 1.  At the
         beginning, there is a pile of <i>n</i> cookies. The players
         alternate turns; each turn, a player can take anywhere from 1
         to 3 cookies. The player who takes the last cookie wins.  Fill
         in the function <tt>can_win</tt>, which returns <tt>True</tt>
         if it is possible to win starting at the given number of
         cookies. It uses the following ideas:""" + ul((
            """if the number of cookies is negative, it is impossible
             to win.""",
            """otherwise, the current player can choose to take either
             1, 2, or 3 cookies.""",
            """evaluate each action: if that action forces the opponent
            to lose, then return True (since we can win)""",
            """if none of the actions can force a win, then we
            can't guarantee a win.""",
        )),
        'code': """
def can_win(number):
    \"\"\"Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game from
    an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
def can_win(number):
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win ( new_state ):
            return True
        action += 1
    return False"""
    },
]

env_questions = [
    {
        'code': """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

ans = factorial(2)
"""
    },
    {
        'code': """
def foo(n):
    i = 0
    if n == 0:
        return 0
    result = foo(n - 2)
    i += 1
    return i + result

result = foo(4)
"""
    },
    {
        'code': """
def bar(f):
    def g(x):
        if x == 1:
            return f(x)
        else:
            return f(x) + g(x - 1)
    return g

f = 4
bar(lambda x: x + f)(2)
"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

