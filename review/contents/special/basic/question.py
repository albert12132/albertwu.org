from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Special Methods'
level = 'basic'

references = [
    ('Lecture: Multiple representations',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/20-Interfaces_1pps.pdf'),
]

notes = ''

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
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
    {
        'description': """Special methods provide a common interface
        across many different types of objects. List some special
        methods and the contexts in which they are used.""",

        'solution': """Here are some examples:</p>""" + ul((
            '<tt>__init__</tt>: used to create instances of a class.',
            """<tt>__len__</tt>: called by the built-in <tt>len</tt>
            to calculate the "length" of an object.""",
            """<tt>__getitem__</tt>: used with square brackets
            (<tt>[ ]</tt>) to retrieve an element at a certain index.
            """,
            """<tt>__repr__</tt>: returns a string representation
            of an object that is "Python readable" (could be typed
            into Python to replicate the same object).""",
            """<tt>__str__</tt>: returns a string representation of an
            object that is human readable"."""
            """<tt>__eq__</tt>: called when the <tt>==</tt> operator
            is used. Determines how to check if two objects are equal.
            """,
            """<tt>__add__</tt>: called when the <tt>+</tt> operator
            is used."""
        ))
    },
    {
        'description': """What do the underscores (e.g.
        <tt>__init__</tt>) in special method names do?""",

        'solution': """Functionally, the underscores don't do
        anything -- they are just part of the method name. However,
        when Python looks for a certain special method, it expects
        the name to have those underscores, so you can't leave them
        out!""",
    },
]

print_questions = [
    {
        'description': """For the following quesitons, assume the
        following class has been defined in the interpreter:
        </p>""" + pre("""
class Box(object):
    def __init__(self, item):
        self.item = item
        print('Created a box!')

    def __getitem__(self, index):
        item, self.item = self.item, None
        return item

    def __setitem__(self, index, item):
        self.item = item

    def __repr__(self):
        return 'Box(' + repr(self.item) + ')'

    def __str__(self):
        rep = self.item if self.item is not None else ''
        return '|_{}_|'.format(rep) """, classes='prettyprint'),

        'prompts': [
            ('d = Box(4)', 'Created a box!'),
            ('repr(d)', "'Box(4)'"),
            ('str(d)', "'|_4_|'"),
            ('d', "'Box(4)'"),
            ('d[0]', '4'),
            ('str(d)', "'|__|'"),
            ('d[1000] = 1',),
            ('str(d)', "'|_1_|'"),
        ]
    },
    {
        'description': """Use the <tt>Box</tt> class defined above.
        """,
        'prompts': [
            ('a = Box(Box(4))', 'Created a box!\nCreated a box!'),
            ('str(a)', "'|_|_4_|_|'"),
            ('a[0][0]', '4'),
            ('str(a)', '|__|'),
            ('a[0] = a',),
            ('repr(a)', 'RuntimeError: maximum recursion depth...'),
        ]
    },
]

code_questions = [
    {
        'description': """Implement a class called
        <tt>DoubleList</tt>, such that its doctest passes.""",
        'code': """
class DoubleList(object):
    \"\"\"See doctests for behavior.

    >>> d = DoubleList([1, 2, 3])
    >>> repr(d)
    'DoubleList([1, 2, 3])'
    >>> str(d)
    '[1, 1, 2, 2, 3, 3]'
    >>> d[2]
    2
    >>> d[3]
    2
    >>> d[4]
    3
    >>> len(d)
    6
    >>> d.append(4)
    >>> str(d)
    '[1, 1, 2, 2, 3, 3, 4, 4]'
    \"\"\" """,
        'solution': """
class DoubleList(object):
    def __init__(self, lst):
        self.lst = lst

    def append(self, item):
        self.lst.append(item)

    def __repr__(self):
        return 'DoubleList(' + repr(self.lst) + ')'

    def __str__(self):
        rep = '['
        for elem in self.lst:
            rep += '{0}, {0}, '.format(elem)
        return rep[:-2] + ']'

    def __len__(self):
        return 2 * len(self.lst)

    def __getitem__(self, index):
        return self.lst[index // 2]"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

