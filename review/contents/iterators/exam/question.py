from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Iterators and Generators'
level = 'exam'

references = [
        'Lecture: Iterators',
        'Lab 11',
]

notes = ''

contents = [
        {'name': 'Iterators: Cross out the errors',
         'id': 'iter-cross',
         'maker': make_code_question,
         'questions': lambda: iter_cross_questions},
        {'name': 'Iterators: Fill in the blank',
         'id': 'iter-fill',
         'maker': make_code_question,
         'questions': lambda: iter_fill_questions},
        {'name': 'Generators: Code-writing',
         'id': 'gen-code',
         'maker': make_code_question,
         'questions': lambda: gen_code_questions},
        {'name': 'Generators: Fill in the blank',
         'id': 'gen-fill',
         'maker': make_code_question,
         'questions': lambda: gen_fill_questions},
]

iter_cross_questions = [
    {'description': """Cross out any incorrect or unnecessary lines. You should not need to write any new lines to make the code work. Do not cross out any doctests.""",
     'code': """
class Naturals:
    \"\"\"Doctests.

    >>> n = Naturals()
    >>> i = iter(n)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    2
    \"\"\"
    def __init__(self):
        self.cur = 0

    def __iter__(self):
    def __iter__(self, start):
        self.cur = start
        while True:
            self.cur += 1
            return self.cur
        return NatIter(self.cur)

    def __next__(self):
        tmp = self.cur
        self.cur += 1
        return tmp

class NatIter(Iterator)
class NatIter:
    def __init__(self):
    def __init__(self, start):
        self.cur = start

    def __iter__(Self):
        return self

    def __next__(self):
        tmp = self.cur
        self.cur += 1
        return tmp""",
     'solution': """
class Naturals:
    \"\"\"Doctests.

    >>> n = Naturals()
    >>> i = iter(n)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    2
    \"\"\"
    def __init__(self):
        self.cur = 0

    def __iter__(self):
    <b class='cross'>def __iter__(self, start):</b>
        <b class='cross'>self.cur = start</b>
        <b class='cross'>while True:</b>
            <b class='cross'>self.cur += 1</b>
            <b class='cross'>return self.cur</b>
        return NatIter(self.cur)

    <b class='cross'>def __next__(self):</b>
        <b class='cross'>tmp = self.cur</b>
        <b class='cross'>self.cur += 1</b>
        <b class='cross'>return tmp</b>

<b class='cross'>class NatIter(Iterator)</b>
class NatIter:
    <b class='cross'>def __init__(self):</b>
    def __init__(self, start):
        self.cur = start

    def __iter__(Self):
        return self

    def __next__(self):
        tmp = self.cur
        self.cur += 1
        return tmp""",
    }
]

iter_fill_questions = [
    {'description': """Fill in the implementation of the iterator for the Rlist class.""",
     'code': """
class Rlist:
    \"\"\"Doctests

    >>> r = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> for item in r:
    ...     print(item)
    1
    2
    3
    \"\"\"
    class EmptyList:
        pass

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
        self.cur = self

    def __iter__(self):
        return ______

    def __next__(self):
        if self.cur == ______:
            raise ______
        else:
            result = ______
            ______ = self.cur.rest
            return result""",
    'solution': """
class Rlist:
    class EmptyList:
        pass

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
        self.curr = self

    def __iter__(self):
        return <b class='fill'>self</b>

    def __next__(self):
        if self.curr == <b class='fill'>Rlist.empty</b>:
            raise <b class='fill'>StopIteration</b>
        else:
            result = <b class='fill'>self.curr.first</b>
            <b class='fill'>self.curr</b> = self.curr.rest
            return result""",
    'explanation':"""Since we are writing a <tt>__next__</tt> method for the <tt>Rlist</tt> class, the <tt>Rlist</tt> class is technically an iterator. As such, its <tt>__iter__</tt> method can just return <tt>self</tt>. In the <tt>__next__</tt> method, if the current Rlist is empty, we must raise a <tt>StopIteration</tt> exception. Otherwise, we will return the <i>element</i> (<tt>self.curr.first</tt>) at the current node, and change our point (<tt>self.curr</tt>) to the next node in the Rlist (<tt>self.cur.rest</tt>)."""
    },
]

gen_code_questions = [
    {'description': """Write a generator function <tt>zip</tt> that takes two iterators and yields elements of thsoe iterators in pairs (see the doctests for clarification). <tt>zip</tt> will stop once one of the input iterators stops.""",
     'code': """
def zip(iter1, iter2):
    \"\"\"Doctests

    >>> i1 = iter([1, 2, 3, 4])
    >>> i2 = iter([5, 6, 7])
    >>> gen = zip(i1, i2)
    >>> for elem in gen:
    ...     print(item)
    (1, 5)
    (2, 6)
    (3, 7)
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def zip(iter1, iter2):
    while True:
        try:
            yield (next(iter1), next(iter2))
        except StopIteration:
            break""",
    },
]

gen_fill_questions = [
    {'description': """fill in the implementation of <tt>pascals</tt>, a generator function that yields successive lines of Pascal's triangle every time <tt>next</tt> is called. Each line should be represented as a Python list.""",
        'hint': "a description of Pascal's triangle can be found " + a("http://en.wikipedia.org/wiki/Pascal's_triangle", 'here', internal=False) + '.',
     'code': """
def pascals():
    \"\"\"Doctests

    >>> p = pascals()
    >>> next(p)
    [1]
    >>> next(p)
    [1, 1]
    >>> next(p)
    [1, 2, 1]
    >>> next(p)
    [1, 3, 3, 1]
    >>> next(p)
    [1, 4, 6, 4, 1]
    \"\"\"
    curr = ______
    while True:
        yield curr
        i, new = 1, [1]
        while ______:
            new.append(______ + ______)
            i += 1
        new.append(1)
        curr = new""",
    'solution': """
def pascals():
    curr = <b class='fill'>[1]</b>
    while True:
        yeild curr
        i, new = 1, [1]
        while <b class='fill'>i < len(curr)</b>:
            new.append(<b class='fill'>curr[i-1]</b> + <b class='fill'>curr[i]</b>)
            i += 1
        new.append(1)
        curr = new""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

