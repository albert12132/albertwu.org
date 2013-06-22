from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Tuples'
level = 'exam'

references = [
    'Lab 5',
    'Lecture: Sequences',
]

notes = ''

contents = [
        {'name': 'What would Python print?',
         'id': 'print',
         'maker': make_print_question,
         'questions': lambda: print_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_concept_question,
         'questions': lambda: code_questions},
]

print_questions = [
    {'prompts': [
            ('x = (1, (2, (3, (4,))))',),
            ('len(x)', '2'),
            ('x[1][0]', '2'),
            ('2 in x', 'False'),
            ('y = (1, (2, (3,), 4), 5)',),
            ('len(y)', '3'),
            ('len(y[1])', '3'),
            ('y[2] = 50', 'TypeError'),
            ('z = (2, (1, (2,), 1), 1)',),
            ('z[z[z[0]]]', '(1, (2,), 1)'),
        ]},
]

code_questions = [
    {'description': """Implement a function <tt>is_palindrome</tt> if
        the given tuple is a palindrome. A palindrome is a sequence
        that is the same backwards.""",
     'code': """
def is_palindrome(tup):
    \"\"\"Returns True if tup is a palindrome.

    &gt;&gt;&gt; x = (1, 2, 3, 4)
    &gt;&gt;&gt; is_palindrome(x)
    False
    &gt;&gt;&gt; y = (1, 2, 3, 2, 1)
    &gt;&gt;&gt; is_palindrome(y)
    True
    &gt;&gt;&gt; is_palindrome(())
    True
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
# simple version
def is_palindrome(tup):
    return tup == tup[::-1]

# recursive
def is_palindrome(tup):
    if len(tup) == 0 or len(tup) == 1:
        return True
    return tup[0] == tup[-1] and is_palindrome(tup[1:-1])

# iterative
def is_palindrome(tup):
    for i in range(len(tup)//2):
        if tup[i] != tup[-i-1]:
            return False
    return True"""
    },
    {'description': """Implement a function <tt>flatten</tt> that
        takes a (possibly deep) tuple and returns a new tuple that has
        no nested tuples. See the doctests for behavior specifics.""",
     'code': """
def flatten(tup):
    \"\"\"Flattens a possibly deep tuples.

    &gt;&gt;&gt; x = (1, (2, (3,), 4), 5)
    &gt;&gt;&gt; flatten(x)
    (1, 2, 3, 4, 5)
    &gt;&gt;&gt; y = (1, 2, 3, 4)
    &gt;&gt;&gt; flatten(y)
    (1, 2, 3, 4)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
# recursive
def flatten(tup):
    if not tup:
        return ()
    elif type(tup[0]) == tuple:
        return flatten(tup[0]) + flatten(tup[1:])
    else:
        return (tup[0],) + flatten(tup[1:])

# iterative
def flatten(tup):
    total = ()
    for elem in tup:
        if type(elem) == tuple:
            total += flatten(elem)
        else:
            total += (elem,)"""
    },
    {'description': """Implement a function <tt>deep_reverse</tt> that
        takes a (possibly deep) tuple and reverses it. If the tuple has        elements that are themselves tuples, those elements will be
        reversed too. See the doctests for behavior specifics.""",
     'code': """
def deep_reverse(tup):
    \"\"\"Reverses a possibly deep tuples.

    &gt;&gt;&gt; tup = (1, (2, (3,), 4), 5)
    &gt;&gt;&gt; deep_reverse(tup)
    (5, (4, (3,) 2), 1)
    &gt;&gt;&gt; y = (1, 2, 3, 4)
    &gt;&gt;&gt; deep_reverse(y)
    (4, 3, 2, 1)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
# recursive
def deep_reverse(tup):
    if not tup:
        return ()
    elif type(tup) == tuple:
        return deep_reverse(tup[1:]) + (deep_reverse(tup[0]),)
    else:
        return deep_reverse(tup[1:]) + (tup[0],)

# iterative
def deep_reverse(tup):
    total = ()
    for elem in tup:
        if type(elem) == tuple:
            total = (deep_reverse(elem),) + total
        else:
            total += (elem,) + total
    return total"""
    }
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

