from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Scheme'
level = 'exam'

references = [
    ('Lecture: Functional Programming',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/23-Scheme_1pps.pdf'),
    ('Lab 8',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab08/lab8-scheme.html'),
    ('Discussion 9',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion09_sol.pdf'),
]

notes = ''

PROMPT = 'STk> '

contents = [
    {'name': 'What would Scheme print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
#     {'name': 'Fill in the blank',
#      'id': 'fill',
#      'maker': make_concept_question,
#      'questions': lambda: fill_questions},
]

print_questions = [
    {
        'description': """For the following questions, write the value
        that the expression evaluates to if you type it into
        <tt>STk</tt>. If the expression contains a function (or
        multiple), write "FUNCTION" in place of that function. If the
        expression causes an error, write "ERROR".""",

        'prompts': [
            ('(cons 1 (cons 2 (cons 3 (cons 4 nil))))', '(1 2 3 4)'),
            ('(cons (cons (cons 3 2) 1) (cons 4 nil))', '(((3 . 2) . 1) 4'),
            ('(cdr (cons (cdr (list 1 2)) (cons 3 (cons 4 nil))))', '(3 4)'),
            ('(define lst (cons (lambda (x) (cons x x)) nil))',),
            ('((car lst) lst)', '((FUNCTION) FUNCTION)',),
            ('(define (x) (lambda (x) (list x x)))',),
            ('(((car ((x) x))) 4)', '(4 4)',),
        ],
        'symbol': PROMPT
    },
]

code_questions = [
    {
        'description': """Implement a function
        <tt>count-stairways</tt>, which takes a number <tt>n</tt> as
        an argument. Assuming you can only take 2 or 3 steps at a
        time, return the number of ways you can reach the top of a
        staircase with <tt>n</tt> stairs.""",

        'hint': """This is different than the usual
        <tt>count-stairways</tt> -- notice that this time, we can
        only take 2 or 3 steps, rather than 1 or 2.""",

        'code': """
(define (count-stairways n)
    ; YOUR CODE HERE
    )

; Tests
STk> (count-stairways 1)
0
STk> (count-stairways 4)
1
STk> (count-stairways 5)
2
STk> (count-stairways 8)
4""",
        'solution': """
(define (count-stairways n)
    (cond ((= n 1) 0)
          ((or (= n 2) (= n 3)) 1)
          (else (+ (count-stairways (- n 2))
                   (count-stairways (- n 3))))))""",
    },
    {
        'description': """Implement a function
        <tt>count-serpinski</tt>, which takes a numbero
        <tt>depth</tt> as an argument. The function calculates how
        many triangles are contained in a Serpinski's triangle with
        the given depth. See the tests for examples.<br/>
        <a href='http://en.wikipedia.org/wiki/File:Sierpinski_triangle_evolution.svg'>Picture</a>""",

        'hint': """You should count triangles of all sizes.""",

        'code': """
(define (count-serpinski depth)
    ; YOUR CODE HERE
    )

; Tests
STk> (count-serpinski 1)
1
STk> (count-serpinski 2)
5
STk> (count-stairways 3)
17
STk> (count-stairways 4)
53""",
        'solution': """
(define (count-serpinski n)
    (if (= n 1)
        1
        (+ 2 (* 3 (count-serpinski (- n 1))))))""",
        'explanation': """The recursive call can be derived as follows:
        """ + ol((
            """There are three smaller <i>n-1</i> serpinski triangles
            at each of the corners""",
            """There are two additional triangles drawn -- the triangle
            in the center, and the overall triangle."""
        )),
    },
]

fill_questions = [
    {
        'description': """Fill in the blanks for the
        <tt>construct</tt> function. It takes a value and a list of
        lists as arguments. It returns a new list of lists, where each
        element is a list from the old list, but with the value added
        to the front.""",
        'code': """
(define (construct value lists)
    (if ______
        ______
        (cons _____________
              _____________)))
    )

; Tests
STk> (define lists '((10) () (4 3) (2 5 3)))
lists
STk> (construct 6 lists)
((6 1) (6) (6 4 3) (6 2 5 3))
STk> (construct 6 '())
()""",
        'solution': """
(define (construct value lists)
    (if (null? lists)
        nil
        (cons (cons value (car lists))
              (construct value (cdr lists)))))""",
    },
    {
        'description': """Fill in the blanks for the
        <tt>list-change</tt> function. It returns a list of
        combinations of coins needed to make a certain amount of
        change (i.e. it returns a list of lists, where the elements of
        each list sum up to a specified value).""",

        'hint': """The implementation of this function uses the
        <tt>construct</tt> function defined in Q4.""",

        'code': """
(define (list-change total denoms)
    (cond ((= total 0) ______)
          ((or (< total 0) (null? denoms)) ______)
          (else (append (construct (car denoms)
                                   (list-change ______
                                                ______))
                        (list-change ______
                                     ______)))))

; Tests
STk> (define denoms '(10 5 1))
denoms
STk> (list-change 5 denoms)
((5) (1 1 1 1 1))
STk> (list-change 10 denoms)
((10) (5 5) (5 1 1 1 1 1) (1 1 1 1 1 1 1 1 1 1))""",
        'solution': """
(define (list-change total denoms)
    (cond ((= total 0) (list nil))
          ((or (< total 0) (null? denomes)) nil)
          (else (append (construct (car denoms)
                                   (list-change (- total (car denoms))
                                                denoms))
                        (list-change total
                                     (cdr denoms))))))""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

