from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Dictionaries'
level = 'exam'

references = [
    'Lecture: Objects, Lists, Dictionaries, Mutable Data',
    'Discussion 3a',
]

notes = ''

contents = [
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

code_questions = [
    {
        'description': """Implement a function <tt>stem_and_leaf</tt>,
        which takes a sorted list of integers and a multiple of 10
        called <tt>leaf_max</tt>.  <tt>stem_and_leaf</tt> will create
        a <a href='http://en.wikipedia.org/wiki/Stem-and-leaf_display'>stem-and-leaf plot</a>,
        where the leaves are numbers less than the <tt>leaf_max</tt>
        (e.g. if <tt>leaf_max == 100</tt>, the leaves must all be less
        than 100: 34, 1, and 99 are valid leaves, but 100 and 101 are
        not). <tt>stem_and_leaf</tt> should return a dictionary,
        where the keys are stems and values are lists of leaves. For
        example:
        </p>""" + pre("""
stem_and_leaf([7, 31, 365, 365, 3650], 100)""", classes='prettyprint') + """
        <p>would create the following dictionary:</p>""" + pre("""
{
    0: [7, 31],
    3: [65, 65],
    36: [50],
}""", classes='prettyprint'),

        'code': """
def stem_and_leaf(lst, leaf_max):
    \"\"\"Returns a dictionary representing a stem-and-leaf plot.
    \"\"\"
    "*** YOUR CODE HERE ***" """,

        'solution': """
def stem_and_leaf(lst, leaf_unit):
    plot = {}
    for num in lst:
        stem, leaf = num // leaf_unit, num % leaf_unit
        if stem not in plot:
            plot[stem] = []
        plot[stem].append(leaf)
    return plot"""
    },
    {
        'description': """Implement a function <tt>one_to_one</tt>,
        which takes a dictionary <tt>d</tt> and returns True if every
        value in <tt>d</tt> only has one corresponding key. See the
        doctests for more details.""",

        'code': """
def one_to_one(d):
    \"\"\"Returns True if D represents a one-to-one mapping of keys
    to values.

    >>> d = {'a': 4, 'b': 5, 'c': 3}
    >>> one_to_one(d)
    True
    >>> fail = {'a': 2, 'b': 4, 'c': 2}
    >>> one_to_one(fail)
    False
    \"\"\"
    "*** YOUR CODE HERE ***" """,

        'solution': """
def one_to_one(d):
    seen = set()
    for value in d.values():
        if value in seen:
            return False
        seen.add(value)
    return True"""
    },
    {
        'description': """The TAs have started a social networking
        site called Bookface. Bookface users are recorded in a
        Python dictionary, where the keys are usernames and values
        are lists of friends. Here is an example:</p>""" + pre("""
users = {
    'Robert': ['Brian', 'Mark'],
    'Mark': ['Eric', 'Brian', 'Robert'],
    'Brian': ['Eric', 'Mark', 'Robert'],
    'Eric': ['Mark', 'Brian'],
    'Albert': []
}""", classes='prettyprint') + """<p>One of the features of Bookface
        calculates the <a href='https://en.wikipedia.org/wiki/Six_degrees_of_separation'>degrees of separation</a>
        between two users. For example, there is one (1) degree of
        separation between Robert and Mark, because they are direct
        friends; there are two (2) degrees of separation between
        Robert and Eric (Robert - Mark - Eric); and there is an
        infinite degree of separation between Albert and
        everyone else, since he has no friends.</p>

        <p>Help the TAs implement the function <tt>degrees</tt>,
        which calculates the degree of separation between two
        users. See the docstring for more details.""" ,

        'code': """
def degrees(users, start, end, visited):
    \"\"\"Finds the degree of separation between START and END. If
    START and END are not connected, return infinity: float('inf').

    PARAMETERS:
    users   -- dictionary; keys are users, values are friends lists
    start   -- starting user
    end     -- ending user
    visited -- a Python set of users we've already checked
    \"\"\"
    if ______:
        return 0
    smallest = float('inf')     # infinity
    for friend in ______:
        if ______:
            visited.add(friend)
            friend_degree = degrees(______)
            smallest = _______
    return smallest""",

        'solution': """
def degrees(users, start, end, visited):
    if start == end:
        return 0
    smallest = float('inf')     # infinity
    for friend in users[start]:
        if friend not in visited:
            visited.add(friend)
            friend_degree = degrees(users, friend, end, visited)
            smallest = min(smallest, friend_degree + 1)
    return smallest"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

