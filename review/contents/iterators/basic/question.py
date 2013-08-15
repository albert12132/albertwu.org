from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Iterators and Generators'
level = 'basic'

references = [
    'Lecture: Tail Calls, Iterators',
    'Lecture: Streams, Generators',
    'Lab 7a',
    'Discussion 7a',
]

notes = ''

contents = [
        {'name': 'Iterators: Conceptual',
         'id': 'iter-conceptual',
         'maker': make_concept_question,
         'questions': lambda: iter_concept_questions},
        {'name': 'Iterators: Code Writing',
         'id': 'iter-code',
         'maker': make_code_question,
         'questions': lambda: iter_code_questions},
        {'name': 'Generators: Conceptual',
         'id': 'gen-conceptual',
         'maker': make_concept_question,
         'questions': lambda: gen_concept_questions},
        {'name': 'Generators: Code Writing',
         'id': 'gen-code',
         'maker': make_code_question,
         'questions': lambda: gen_code_questions},
]

iter_concept_questions = [
    {'description': """Given any object <tt>obj</tt>, what special method will <tt>iter(obj)</tt> call? What type of object will it return?""",
    'solution': """the built-in Python function <tt>iter</tt> will implicitly call <tt>obj.__iter__</tt>, a method. This method will return an <b>Iterator object</b>, which is any object that has a <tt>__next__</tt> method."""
    },
    {'description': """What is wrong with the following code?""",
     'code': """
>>> obj = SomeObj()
>>> i = iter(obj)
>>> next(obj)""",
    'solution': """<tt>obj</tt> is not necessarily an iterator, so you should not call <tt>next</tt> on it. <tt>next</tt> should be called on <tt>i</tt> instead.</p>

    <p><b>NOTE:</b> even if the <tt>__iter__</tt> method of <tt>SomeObj</tt> returns <tt>self</tt>, you still shoudl nto call <tt>iter</tt> on <tt>obj</tt>. This is to protect abstraction barriers."""
    },
]

iter_code_questions = [
    {'description': """Write an iterator for a Fibonacci class. The iterator should return the next Fibonacci number every time <tt>next</tt> is called on it.""",
     'code': """
class Fibonacci:
    \"\"\"Doctests

    >>> f = Fibonacci()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
class Fibonacci:
    def __init__(self):
        self.cur, self.next = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.cur
        self.cur, self.next = self.next, self.next + self.cur
        return tmp"""
    },
]

gen_concept_questions = [
    {'description': """Given the following generator function, what will the call to <tt>gen()</tt> return?""",
     'code': """
def gen():
    start = 0
    while start != 10:
        yield start
        start += 1""",
    'solution': """<tt>gen()</tt> will return a generator object, NOT the number 0. None of the code inside the generator function will be executed."""
    },
    {'description': """When does a generator raise a <tt>StopIteration</tt> exception?""",
    'solution': """when the end of the generator function is reached.""",
    },
]

gen_code_questions = [
    {'description': """Write a generator function <tt>map_gen</tt> that takes a one-argument function and an iterator as arguments. The return result should be a generator whose elements are the elements of the iterator, but with the function mapped onto them.""",
     'code': """
def map_gen(fn, iter1):
    \"\"\"Doctests

    >>> i = iter([1, 2, 3, 4])
    >>> fn = lambda x: x**2
    >>> m = map_gen(fn, i)
    >>> next(m)
    1
    >>> next(m)
    4
    >>> next(m)
    9
    >>> next(m)
    16
    >>> next(m)
    Traceback (most recent call last):
      ...
    StopIteration
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def map_gen(fn, iter1):
    for elem in iter1:
        yield fn(elem)""",
    'explanation': """
Since <tt>iter1</tt> is an iterator, we can iterate over it in a for loop."""
    },
    {'description': """Write another iterator for a Fibonacci class. Like before, the iterator shoudl return the nxt Fibonacci number every time <tt>next</tt> is called on it. This time, write the iterator using a generator function.""",
     'code': """
class Fibonacci:
    \"\"\"Doctests

    >>> f = Fibonacci()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
class Fibonacci:
    def __iter__(self):
        cur, next = 0, 1
        while True:
            yield cur
            curn, next = next, cur + next""",
    'explanation': """The generator in the <tt>__iter__</tt> method can keep track of state, so we don't need to initialize anything. We also don't need to write a <tt>__next__</tt> method, since the <tt>__iter__</tt> method is not returning <tt>self</tt>."""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

