from utils.utils import *
from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Interpreters'
level = 'exam'

references = [
        'Lecture: Calculator',
        'Lecture: Interpreters',
        'Lab 10',
        'Discussion 10',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
]

concept_questions = [
    {'description': """Given the following Scheme expressions, what would <tt>scheme_read</tt> from Project 4 return? If the parser would raise an error, write ERROR. The first one is done for you.""",
     'code': """
scm> (+ 2 3)
Pair('+', Pair(4, Pair(5, nil)))
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
    {'description': """Given each of the following Pair objects, determine how many times <tt>scheme_eval</tt> and <tt>scheme_apply</tt> are called (not <tt>calc_eval</tt> and <tt>calc_apply</tt>!). Be sure to include the first <tt>scheme_eval</tt>. The first one has been done for you.</p>

        <p><b>Note</b>: assume that the following <tt>double</tt> function has been defined:""" + pre("""
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

(and 2 #f 4)
; eval  ________
; apply ________
""",
    'solution': pre("""
4
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
; apply <b>4</b>

(and 2 #f 4)
; eval  <b>4</b>
; apply <b>0</b>""", classes='prettyprint'),
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

