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
        'solution': pre("""
scm> '(1 2 3)
Pair('quote', Pair(Pair(1, Pair(2, Pair(3, nil))), nil))
scm> (1 . 2)
Pair(1, 2)
scm> 3
3
scm> (1 . (3 2))
Pair(1, Pair(3, Pair(2, nil)))
scm> ('hi . 3 4)
ERROR""", classes='prettyprint'),
    },
    {
        'description': """Given each of the following Pair objects,
        determine how many times <tt>scheme_eval</tt> and
        <tt>scheme_apply</tt> are called (not <tt>calc_eval</tt> and
        <tt>calc_apply</tt>!). Be sure to include the first
        <tt>scheme_eval</tt>. The first one has been done for you.</p>

        <p><b>Note</b>: assume that the following <tt>double</tt>
        function has been defined:""" + pre("""
(define (double x) (+ x x))""", classes='prettyprint'),
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
        'solution': pre("""
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
; apply <b>4</b>""", classes='prettyprint'),
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#
questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

