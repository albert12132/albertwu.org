from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Scheme'
level = 'exam'

references = [
    'Lecture: Scheme',
    'Lab 9',
    'Discussion 9',
]

notes = ''

PROMPT = 'STk&gt; '

contents = [
        {'name': 'What would Scheme print?',
         'id': 'print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]
# add after the project
[
        {'name': 'Fill in the blank',
         'id': 'fill',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: fill_questions},
]

print_questions = [
    {'description': """For the following questions, write the value that the expression evaluates to if you type it into <tt>STk</tt>. If the expression contains a function (or multiple), write "FUNCTION" in place of that function. If the expression causes an error, write "ERROR".""",
    'prompts': [
        ('(cons 1 (cons 2 (cons 3 (cons 4 nil))))', '(1 2 3 4)'),
        ('(cons (cons (cons 3 2) 1) (cons 4 nil))', '(((3 . 2) . 1) 4'),
        ('(cdr (cons (cdr (list 1 2)) (cons 3 (cons 4 nil))))', '(3 4)'),
        ('(define lst (cons (lambda (x) (cons x x)) nil))',),
        ('((car lst) lst)', '((FUNCTION) FUNCTION)',),
        ('(define (x) (lambda (x) (list x x)))',),
        ('(((car ((x) x))) 4)', '(4 4)',),
    ],
    'symbol': PROMPT},
]

code_questions = [
    {'description': """Implement a function <tt>count-stairways</tt>, which takes a number <tt>n</tt> as an argument. Assuming you can only take 2 or 3 steps at a time, return the number of ways you can reach the top ofa staircase with <tt>n</tt> stairs.""",
     'hint': """This is different than the usual <tt>count-stairways</tt> -- notice that this time, we can only take 2 or 3 steps, rather than 1 or 2.""",
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
    {'description': """Implement a function <tt>count-serpinski</tt>, which takes a numbero <tt>depth</tt> as an argument. The function calculates how many triangles are contained in a Serpinski's triangle with the given depth. See the tests for examples.
    <br/>
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
    (cond ((= n 1) 1)
          ((= n 2) 5)
          (else (- (* 4 (count-serpinski (- n 1)))
                   (* 3 (count-serpinski (- n 2)))))))</pre>

<p>The recursive call can be derived as follows:</p>
<ol>
    <li>(# triangles for <i>n-1</i>) + (# triangles added for this depth)</li>
    <li>= count-serpinski(n-1) + (3/4)*4*(count-serpinski(n-2) - count-serpinski(n-2))</li>
    <ul>
        <li>count-serpinksi(n-1) - count-serpinski(n-2) triangles were added last time</li>
        <li>(3/4) of the old trangles will have nested triangles</li>
        <li>4 new triangles will be drawn in each of those (3/4) triangles</li>
    </ul>
    <li>= count-serpinski(n-1) + 3*count-serpinski(n-1) - 3*count-serpinski(n-2)</li>
</ol><pre>""",
    },
]

fill_questions = [
    {'description': """Fill in the blanks for the <tt>construct</tt> function. It takes a value and a list of lists as arguments. It returns a new list of lists, where each element is a list from the old list, but with the value added to the front.""",
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
    {'description': """Fill in the blanks for the <tt>list-change</tt> function. It returns a list of combinations of coins needed to make a certain amount of change (i.e. it returns a list of lists, where the elements of each list sum up to a specified value).""",
        'hint': """The implementation of this function uses the <tt>construct</tt> function defined in Q4.""",
     'code': """
(define (list-change total denoms)
    (cond ((= total 0) ______)
          ((or (&lt; total 0) (null? denoms)) ______)
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
          ((or (&lt; total 0) (null? denomes)) nil)
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
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()

