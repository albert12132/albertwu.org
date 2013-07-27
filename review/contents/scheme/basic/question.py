from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Scheme'
level = 'basic'

references = [
    'Lecture: Scheme',
    'Lab 5b',
    'Discussion 5b',
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
]

print_questions = [
    {
        'prompts': [
            ('(+ 4 3)', '7'),
            ('(4 + 3)', 'Error'),
            ('(+ 1 2 3 4)', '10'),
            ('(- 1 2 3 4)', '-8'),
            ('(/ 1 2 2)', '0.25'),
        ],
        'symbol': PROMPT
    },
    {
        'prompts': [
            ('(if #t (+ 2 3))', '5'),
            ('(if #f (+ 2 3))', 'okay   ; i.e. returns nothing'),
            ('(if #f (/ 1 0) 4)', '4'),
            ('(and #t #f #t)', '#f'),
            ('(and #t 0 #t)', '#t'),
            ('(and 3 5 2)', '2'),
            ('(or #t #f #t)', '#t'),
            ('(or #f 4 #t)', '4'),
        ],
        'symbol': PROMPT
    },
    {
        'prompts': [
            ('(define x 2)', 'x'),
            ('x', '2'),
            ('(define (f x) (* x x))', 'f'),
            ('(f 4)', '16'),
            ('(define (g x) (lambda (y) (* x y)))', 'g'),
            ('((g 4) 5)', '20'),
        ],
        'symbol': PROMPT},
    {
        'prompts': [
            ('(cons 1 (cons 2 nil))', '(1 2)'),
            ('(cons 1 2)', '(1 . 2)'),
            ('(car (cons 1 (cons 2 nil)))', '1'),
            ('(cdr (cons 1 (cons 2 nil)))', '(2)'),
            ('(cdr (cons 1 2))', '2'),
            ('(null? (cons 1 nil))', '#f'),
            ('(null? (cdr (cons 1 nil)))', '#t'),
            ('(list 1 2 3 4)', '(1 2 3 4)'),
            ('(cdr (list 1 2 3 4))', '(2 3 4)'),
        ],
        'symbol': PROMPT
    },
]

code_questions = [
    {
        'description': """Implement the function <tt>filter</tt>,
        which takes a predicate and a Scheme list as arguments.
        <tt>filter</tt> will return a new list that only contains
        elements of the original list that satisfy the predicate.""",

        'code': """
(define (filter pred lst)
    ; YOUR CODE HERE
    )

; Tests
STk> (define (less-3 x) (< x 3))
less-3
STk> (filter less-3 (list 1 2 3 4))
(1 2)""",
        'solution': """
(define (filter pred lst)
    (cond ((null? lst) nil)
          ((pred (car lst)) (cons (car lst)
                                  (filter pred (cdr lst))))
          (else (filter pred (cdr lst)))))"""
    },
    {
        'description': """Implement the function <tt>interleave</tt>,
        which takes a two lists as arguments. <tt>interleave</tt> will
        return a new list that interleaves the elements of the two
        lists, with <tt>list1</tt> starting first. Refer to the tests
        for sample input/output.""",

        'code': """
(define (interleave list1 list2)
    ; YOUR CODE HERE
    )

; Tests
STk> (interleave (list 1 3 5) (list 2 4 6))
(1 2 3 4 5 6)
STk> (interleave (list 1 3 5) nil)
(1 3 5)
STk> (interleave (list 1 3 5) (list 2 4))
(1 2 3 4 5)""",
        'solution': """
(define (interleave list1 ist2)
    (if (or (null? list1) (null? list2))
        (append list1 list2)
        (cons (car list1)
              (cons (car list2)
                    (interleave (cdr list1) (cdr list2))))))""",
    },
    {
        'description': """Implement the function 
        <tt>count-stairways</tt>, which takes a number (of steps).
        Assuming we can take 1 or 2 steps, return the number of ways
        we can climb up the stairs.""",

        'code': """
(define (count-stairways n)
    ; YOUR CODE HERE
    )

; Tests
STk> (count-stairways 4)
5
STk> (count-stairways 5)
8""",
        'solution': """
(define (count-stairways n)
    (cond ((= n 1) 1)
          ((= n 2) 2)
          (else (+ (count-stairways (- n 1))
                   (count-stairways (- n 2))))))""",
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

