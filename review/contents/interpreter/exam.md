from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Interpreters'
level = 'exam'

references = [
    ('Lecture: Calculator',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/25-Calculator_1pps.pdf'),
    ('Lecture: Interpreters',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/26-Interpreters_1pps.pdf'),
    ('Lab 8',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab08/lab08.php'),
    ('Discussion 10',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion10.pdf'),
]

notes = ''

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
        'description': """Given the following Scheme expressions, what
        would <tt>scheme_read</tt> from Project 4 return? If the parser
        would raise an error, write ERROR. The first one is done for
        you.""",
        'code': """
scm> (+ 2 3)
Pair('+', Pair(2, Pair(3, nil)))
scm> '(1 2 3)
______
scm> (1 . 2)
______
scm> 3
______
scm> (1 . (3 2))
______
scm> ('hi . 3 4)
______""",
        'solution': prettify("""
scm> '(1 2 3)
Pair('quote', Pair(Pair(1, Pair(2, Pair(3, nil))), nil))
scm> (1 . 2)
Pair(1, 2)
scm> 3
3
scm> (1 . (3 2))
Pair(1, Pair(3, Pair(2, nil)))
scm> ('hi . 3 4)
ERROR"""),
    },
    {
        'description': """Given each of the following Pair objects,
        determine how many times <tt>scheme_eval</tt> and
        <tt>scheme_apply</tt> are called (not <tt>calc_eval</tt> and
        <tt>calc_apply</tt>!). Be sure to include the first
        <tt>scheme_eval</tt>. The first one has been done for you.</p>

        <p><b>Note</b>: assume that the following <tt>double</tt>
        function has been defined:""" + prettify("""
(define (double x) (+ x x))"""),
     'code': """
(+ 2 3)
; eval  4   (1 for whole expression, 1 for each element in list)
; apply 1   ('+' is primitive)

3
; eval  ________
; apply ________

(+ 3 (+ 5 2))
; eval  ________
; apply ________

(double 4)
; eval  ________
; apply ________

(double (double 4))
; eval  ________
; apply ________
""",
        'solution': prettify("""
3
; eval  <b>1</b>
; apply <b>0</b>

(+ 3 (+ 5 2))
; eval  <b>7</b>
; apply <b>2</b>

(double 4)
; eval  <b>7</b>
; apply <b>2</b>

(double (double 4))
; eval  <b>13</b>
; apply <b>4</b>"""),
    },
]

code_questions = [
    {
        'description': """Write a function <tt>is_pyramid</tt> that
        takes in a list of tokens, and checks if the list of tokens
        forms a pyramid. A <i>pyramid</i> is a list that is symmetric
        in <i>shape</i> (not necessarily the contents), and each list
        can only have one nested list at its level. The following are
        examples of valid pyramids:
        """ + prettify("""
(3 4 (5 (1) 3) 2 3)
(1 2 3 4)           # no nested lists is okay
(1 (2 () 3) 4)      # empty lists are okay
(1 (2) 3) )()       # junk, )(), after a valid pyramid is okay
(1 () 2) s d fs     # junk after a valid pyramid is okay""") + """The following are examples of invalid pyramids:""" + prettify("""
(2 (3) 4 5)     # too many elements on the right side
((3) (4))       # too many nested lists on the first level
(3 4            # missing closing parenthesis"""),
        'code': """
def is_pyramid(tokens):
    \"\"\"Returns true if the list of tokens begins with a valid
    pyramid. Junk at the end is okay.

    >>> t1 = ['(', 3, '(', 4, ')', 5, ')']  # (3 (4) 5)
    >>> is_pyramid(t1)
    True
    >>> t2 = ['(', '(', '(', ')', ')', ')'] # ((()))
    >>> is_pyramid(t2)
    True
    >>> t3 = ['(', 3, '(', 2, 3, ')', 4, ')', 3, 4] # (3 (2 3) 4) 3 4
    >>> is_pyramid(t3)
    True
    >>> f1 = ['(', 2, '(', 3, ')', 4, 5, ')'] # (2 (3) 4 5)
    >>> is_pyramid(f1)
    False
    >>> f2 = ['(', '(', 3, ')', '(', 4, ')', ')'] # ((3) (4))
    >>> is_pyramid(f2)
    False
    >>> f3 = ['(', 3, 4] # (3 4
    >>> is_pyramid(f3)
    False
    \"\"\"
    if not tokens or tokens[0] != '(':
        return False
    tokens.pop(0)
    "*** YOUR CODE HERE ***" """,

        'solution': """
def is_pyramid(tokens):
    if not tokens or tokens[0] != '(':
        return False
    tokens.pop(0)
    count, direction = 0, 1
    while tokens and tokens[0] != ')':
        if direction == -1 and count == 0:
            return False
        elif tokens[0] == '(':
            if direction == -1 or not is_pyramid(tokens):
                return False
            else:
                direction = -1
        else:
            tokens.pop(0)
            count += direction
    if not tokens:
        return False
    else:
        tokens.pop(0)
        return direction == 1 or count == 0""",
        'explanation': """The base case that is provided checks that
        the tokens begin with an '('. If it doesn't, then we
        immediately know that it is not a pyramid. We then remove the
        '('.</p>
        <p>First, let's write code that simply goes through each
        element and removes it from the list of tokens. The word
        <i>each</i> indicates that we need some looping structure, so
        we'll use a while look. Our while loop should stop if we reach
        the end of the list of tokens, or if we see a ')':""" + prettify("""
def is_pyramid(tokens):
    if not tokens or tokens[0] != '(':
        return False
    tokens.pop(0)
    while tokens and tokens[0] != ')':
        if tokens[0] == '(':
            # handle case for nested lists
        else:
            # handle case for numbers""") + """
        How do we handle a nested list? Simply make a recursive call;
        if the nested list is not a valid pyramid, the recursive call
        will return False. The recursive call has the additional
        benefit of removing the nested list, including its closing
        parenthesis:""" + prettify("""
...
if tokens[0] == '(':
    if not is_pyramid(tokens):
        return False
...""") + """How do we handle a number? Simply
        remove it from the list of tokens:""" + prettify("""
...
else:
    tokens.pop(0)
...""") + """What happens if we break out of
        our while loop? There are two scenarios: 1) if we run out of
        tokens, and 2) if the first token is a ')'. If we run out of
        tokens, we should return False, because that means we never
        saw the corresponding ')'. If the first token is a ')', then
        we successfully closed the list and we can just pop it off and
        return True:
        """ + prettify("""
...
while tokens and tokens[0] != ')':
    ...
if not tokens:
    return False
else:
    tokens.pop(0)
    return True""") + """At this point, our code
    looks like this:""" + prettify("""
def is_pyramid(tokens):
    if not tokens or tokens[0] != '(':
        return False
    tokens.pop(0)
    while tokens and tokens != ')':
        if tokens[0] == '(':
            if not is_pyramid(tokens):
                return False
        else:
            tokens.pop(0)
    if not tokens:
        return False
    else:
        return True""") + """This looks
    promising, but it doesn't account for the symmetry of the list.
    Here's the idea. We'll keep track of two variables: 1) a
    <tt>count</tt>, which counts the number of elements before the
    nested list, and then checks that the number of elements after the
    nested list matches; 2) a <tt>direction</tt>, that tells us whether
    we're before the nested list or after it:""" + prettify("""
...
tokens.pop(0)
count, direction = 0, 1
while tokens and tokens[0] != ')':
    ...""") + """We'll use the convention that,
    when direction is 1, we are incrementing our count, and when
    direction is -1, we are decrementing our count.</p>
    <p>Now, let's go in the while loop. If <tt>tokens[0] == '('</tt>
    (meaning we see a nested list), this tells us that we've reached
    our midpoint, and we should begin decrementing count after this:
    """ + prettify("""
if tokens[0] == '(':
    if not is_pyramid(tokens):
        return False
    else:
        direction = -1""") + """In addition,
    if our direction is already -1 (meaning we've already seen a nested
    list), and we see another nested list, this breaks our definition
    of a pyramid, so we should return False (e.g. the case
    <tt>((3) (4))</tt>):""" + prettify("""
if tokens[0] == '(':
    if direction == -1 or not is_pyramid(tokens):
        return False
    else:
        direction = -1""") + """What about the
        case of regular numbers? In addition to removing the token,
        we also need to update our <tt>count</tt>. If direction is 1,
        we should increment; if it is -1 (i.e. we've seen a nested
        list already), we should decrement:""" + prettify("""
else:
    tokens.pop(0)
    count += direction""") + """We need one
    other case inside the while loop; what happens if we see
    <tt>(3 (4) 5 6)</tt>? There are too many elements on the right
    side! Walk through the code we have right now, and you'll notice
    that when we reach the 6, <tt>count</tt> will be 0, and
    <tt>direction</tt> will be -1. This is the red flag we look for
    to tell us to return False:""" + prettify("""
while tokens and tokens[0] != ')':
    if direction == -1 and count == 0:
        return False
    if tokens[0] == '(':
        ...""") + """Almost done! At the end,
        we need to update the case where <tt>tokens</tt> is not empty.
        Consider this example: <tt>(3 4 () 3)</tt>. The right side
        contains too few elements. How can we tell? <tt>count</tt> will
        be nonzero! Instead of just returning True, we add the
        additional check on count:""" + prettify("""
if not tokens:
    return False
else:
    return direction == 1 or count == 0""") + """Overall,
    our code looks like this:""" + prettify("""
def is_pyramid(tokens):
    if not tokens or tokens[0] != '(':
        return False
    tokens.pop(0)
    count, direction = 0, 1
    while tokens and tokens[0] != ')':
        if direction == -1 and count == 0:
            return False
        elif tokens[0] == '(':
            if direction == -1 or not is_pyramid(tokens):
                return False
            else:
                direction = -1
        else:
            tokens.pop(0)
            count += direction
    if not tokens:
        return False
    else:
        tokens.pop(0)
        return direction == 1 or count == 0""")
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#
questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

