from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Final review from Section 12/4'
level = 'basic'

references = [
]

notes = 'These questions were written for my section on 12/4.'

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
    # {'name': 'Environment Diagrams',
    #  'id': 'env',
    #  'maker': make_env_question,
    #  'questions': lambda: env_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
    # {'name': 'What would Python print?',
    #  'id': 'print',
    #  'maker': make_print_question,
    #  'questions': lambda: print_questions},
    # {'name': 'Eval vs. Display',
    #  'id': 'eval_print',
    #  'maker': make_eval_print_question,
    #  'questions': lambda: eval_print_questions},
]

concept_questions = [
    {
        'description': """Convert the following Scheme expression
        into its Pair representation (i.e. what <tt>scheme_read</tt>
        would return):""",
        'code': """
(+ 3 '(4 8) 'hi))
""",
        'solution': """Let <tt>P</tt> denote <tt>Pair</tt>:""" + pre("""
P('+', P(3, P( P('quote', P(P(4, P(8, nil)), nil)), P( P('quote', P('hi', nil)), nil))))""", classes='prettyprint'),
        'explanation': """First ignore the nested lists and quotes:"""\
                + pre("""
(+ 3 ___  ___)""", classes='prettyprint') + """This would generate the following Pair
        representation:""" + pre("""
P('+', P(3, P(___, P(___, nil))))""", classes='prettyprint') + """Now we just have to fill
        in the two blanks. The first blank corresponds to""" + pre("""
'(4 8)""", classes='prettyprint') + """This has a Pair representation like this""" + pre("""
P('quote', P( P(4, P(8, nil)) , nil))""", classes='prettyprint') + """(Review Q1 of Proj4 if
        you are unsure why the quote was converted in this way). The
        second blank correpsonds to """ + pre("""
'hi""", classes='prettyprint') + """and it gets converted into""" + pre("""
P('quote', P('hi', nil))""", classes='prettyprint') + """Put these together to get the final
solution."""
    },
    {
        'description': """Given the following function:""" + pre("""
(define (square x) (* x x))""", classes='prettyprint') + """How many times are
        <tt>scheme_eval</tt> and <tt>scheme_apply</tt> called for the
        following expression?""",
        'code': """
(+ 2 (square 4))""",
        'solution': """eval: 10 times, apply: 3 times""",
        'explanation': """For apply, a good rule of thumb is to count
        the number of functions (primitive and user-defined) that are
        called. In this case, we call <tt>+</tt>, <tt>square</tt>, and
        <tt>*</tt> (when we evaluate the body of <tt>square</tt>).
        Thus, apply is called 3 times.</p>
        <p>For eval, each of the following bullets represents one
        call to scheme_eval:""" + ul((
            tt('(+ 2 (square 4))') + ul((
                tt('+'),
                tt('2'),
                tt('(square 4)') + ul((
                    tt('square'),
                    tt('4'),
                    tt('(* x x)') + ul((
                        tt('*'),
                        tt('x'),
                        tt('x'),
                    ))
                ))
            )),
        )) + """Thus, we have a total of 10 calls to
        <tt>scheme_eval</tt>"""
    },
    {
        'description': """Given the following function that returns
        a stream, what are the first 5 elements of the stream?""",
        'code': """
def my_stream():
    def compute_rest():
        return add_stream(my_stream(), scale_stream(2, my_stream()))
    return Stream(2, compute_rest)""",
        'solution': """2, 6, 18, 54, 162""",
        'explanation': """First, we write down our stream, with
        variables filling in the values we don't know:""" +
        pre("""
s = 2 a b c d""", classes='prettyprint') + """Notice that, to compute
        the rest, we add together two streams: the original stream,
        plus the original stream scaled by 2. This looks like this:
        """ + pre("""
s = 2 | a b  c  d
------------------
      | 2 a  b  c
    + | 4 2a 2b 2c
------------------""", classes='prettyprint') + """We go ahead and add
        up the first column to get 2 + 4 = 6. Now we know that <tt>a =
        6!</tt>. We can use this new information to calculate <tt>b =
        a + 2a = 6 + 2(6) = 18</tt>. We continue this process to get
        the remaining elements:""" + pre("""
s = 2 | a b  c  d
------------------
      | 2 a  b  c
    + | 4 2a 2b 2c
------------------
      | 6 18 54 162""", classes='prettyprint')
    }
]

code_questions = [
    {
        'description': """Implement a fact for <tt>sorted</tt>, which
        is true for lists that are sorted in ascending order (least
        to greatest). You may assume that a fact called
        <tt>less-or-equal</tt> is already defined.""",
        'code': """
(fact (sorted ; YOUR CODE HERE

> (query (sorted (1 2 3 4)))
Success!
> (query (sorted (4 2 1)))
Failed.
> (query (sorted (1 1 1 1)))
Success!
""",
        'solution': """
(fact (sorted (?x)))
(fact (sorted (?a ?b . ?rest))
      (less-or-equal ?a ?b)
      (sorted (?b . ?rest)))
""",
        'explanation': """The base case handles a one element list;
        by definition, it is sorted. The complex fact first checks that
        the first element is less than or equal to the second element,
        and then recursively checks that the rest of the list (excluding
        only the first element) is also sorted."""
    },
    {
        'description': """Implement a class <tt>MergeIter</tt>, which
        takes in a comparison function, two iterables, and iterates
        through elements of both iterables in sorted order (sorted by
        the comparison function). You may assume the iterables do
        not start out as empty""",
        'code': """
class MergeIter:
    \"\"\"Doctests:

    >>> less = lambda x, y: x < y
    >>> m = MergeIter(less, [1, 3, 5], [2, 4, 6])
    >>> for elem in m:
    ...     print(elem)
    1
    2
    3
    4
    5
    6
    \"\"\"
    "*** YOUR CODE HERE ***" """,
        'solution': """
class MergeIter:
    def __init__(self, comp, iter1, iter2):
        self.comp = comp
        self.iter1 = iter(iter1)
        self.iter2 = iter(iter2)
        self.elem1 = next(self.iter1)
        self.elem2 = next(self.iter2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.comp(self.elem1, self.elem2):
            result = self.elem1
            self.elem1 = next(self.iter1)
        else:
            result = self.elem2
            self.elem2 = next(self.iter2)
        return result

# Using a generator expression for __iter__
class MergeIter:
    def __init__(self, comp, iter1, iter2):
        self.comp = comp
        self.iter1 = iter(iter1)
        self.iter2 = iter(iter2)

    def __iter__(self):
        elem1, elem2 = next(self.iter1), next(self.iter2)
        while True:
            if self.comp(elem1, elem2):
                yield elem1
                elem1 = next(self.iter1)
            else:
                yield elem2
                elem2 = next(self.iter2)""",
        'explanation': """For the solution using <tt>__next__</tt>,
        let's first look at the <tt>__init__</tt>. Since <tt>iter1</tt>
        and <tt>iter2</tt> are defined to be <i>iterables</i>, not
        <i>iterators</i>, we need to first call <tt>iter</tt> on them
        to extract their iterators (this is so we can call
        <tt>next</tt> later on). We also extract the first elements
        in the iterators to get <tt>self.elem1</tt> and
        <tt>self.elem2</tt>. This will become useful later on.</p>
        <p>Recall that the <tt>iter</tt> method must always return
        an iterator, and an iterator, by definition, must have a
        <tt>next</tt> method. Since we are returning <tt>self</tt>,
        this implies our class must have a <tt>next</tt> method.</p>
        <p>In <tt>__next__</tt>, we compare the current elements of
        both iterators. If <tt>self.comp</tt> returns True, this
        signals that the next element to return will be the element
        from the first iterator. We save <tt>self.elem1</tt> inside a
        temporary variable, and then overwrite <tt>self.elem1</tt> with
        the next element in <tt>self.iter1</tt>. We do something
        similar if <tt>self.comp</tt> returns False instead.</p>
        <p>For the version that uses a generator expression, observe
        that, by using a <tt>yield</tt> statement, we convert the
        <tt>__iter__</tt> method into a generator function. By their
        nature, generator functions always return iterators, so this
        fits the requirement that <tt>__iter__</tt> must return an
        iterator. The logic in this version is very much the same as
        before. The only difference is we don't need to save instance
        variables for <tt>elem1</tt> and <tt>elem2</tt>, since the
        generator function can save state for us."""

    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

