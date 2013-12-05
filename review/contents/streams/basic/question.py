from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Streams'
level = 'basic'

references = [
    ('Lecture: Streams', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30-Streams_1pps.pdf'),
    ('Lab 10:', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab10/lab10.php'),
]

notes = """You can find the source code that contains the Stream class
""" + a('http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30.py', 'here', internal=False) + '.'

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
        'description': """What are the advantages to using a stream as
        opposed to a regular list?""",
        'solution': """A stream can be used to "store" infinite
        amounts of data. Because the data is not computed until you
        need it, you can use memory more efficiently.""",
    },
    {
        'description': """The signature of the Stream constructor is
        <tt>Stream(item, compute_rest)</tt> --  <tt>compute_rest</tt>
        will be a function that computes the rest of the Stream. How
        many arguments can <tt>compute_rest</tt> take? What type of
        object must it return?""",
        'solution': """<tt>compute_rest</tt> must take zero arguments,
        or else the <tt>Stream.rest</tt> property method will not
        work. <tt>compute_rest</tt> must return another Stream
        object.""",
    },
    {
        'description': """Given the following function, list the first
        5 numbers in the Stream that <tt>my_stream()</tt> returns.""",
        'code': """
def my_stream():
    def compute_rest():
        return add_streams(integer_stream(),
                           map_stream(lambda x: 3*x,
                                      integer_stream()))
    return Stream(0, compute_rest)
""",
        'solution': '0, 4, 8, 12, 16'
    },
]

code_questions = [
    {
        'description': """Write a function <tt>odd_stream()</tt> that
        returns a stream of odd-numbered integers, start from 1.""",
        'code': """
def odd_stream():
    \"\"\"Returns a Stream of odd numbers starting at 1.

    >>> s = odd_stream()
    >>> first_k_as_list(s, 5)
    [1, 3, 5, 7, 9]
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def odd_stream():
    def compute_rest():
        return map_stream(lambda x: x + 2, odd_stream())
    return Stream(1, compute_rest)""",
        'explanation': """Let <tt>s</tt> be the result of
        odd_Stream():""" + pre("""
s = 1,    3,        5,      7,    ...
  = 1, (1 + 2), (3 + 2), (5 + 2), ...""") + """The rest of <tt>s</tt>
        is just the elements of <tt>s</tt>, but with 2 added to each
        element."""
    },
    {
        'description': """Write a function <tt>reduce_first_k()</tt>
        that reduces the first <i>k</i> elements in a given Stream,
        using a given combiner. If the stream has fewer than <i>k</i>
        elements, reduce all the elements in the stream.""",
        'code': """
def reduce_first_k(s, k, combiner):
    \"\"\"Reduces the first k elements in s with combiner.

    >>> s = integer_stream()
    >>> reduce_first_k(s, 4, lambda x, y: x + y)
    10
    >>> s1 = Stream(1, lambda: Stream(2))
    >>> reduce_first_k(s1, 4, lambda x, y: x + y)
    3
    \"*** YOUR CODE HERE ***\" """,
        'solution': """
def reduce_first_k(s, k, combiner):
    total, s = s.first, s.rest
    while k > 1 and s != Stream.empty:
        total = combiner(total, s.first)
        s = s.rest
        k -= 1
    return total""",
        'explanation': """We start the total with the first element of
        <tt>s</tt>. We keep iterating until <tt>k</tt> is equal to 1,
        because we've already visited the first element of <tt>s</tt>
        (so we only need to iterate <tt>k - 1</tt> times.""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

