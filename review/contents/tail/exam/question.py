from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Tail Recursion'
level = 'exam'

references = [
    ('Lecture: Tail Calls',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/27-Tail_1pps.pdf'),
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
        'description': """Which of the following Scheme functions
        are tail recursive?""",
        'code': """
(define (one x y)
    (if (or (= x 0) (= y 0) (= x y))
        1
        (if (< x y)
            (one x (- y x))
            (if (> x y)
                (one (- x y) y)))))

(define (two x)
    (if (or (= x 0) (= x 1))
        x
        (+ (two (- x 1)) (two (- x 2)))))

(define (three n curr next)
    (if (= n 0)
        curr
        (three (- n 1) next (+ curr next))))

(define (four n total)
    (cond ((= n 0) 0)
          ((even? n) (four (- n 1) total))
          (else (four (- n 2) (+ total n)))))
""",
        'solution': ul((
            tt('one') + ': tail recursive',
            tt('two') + ': not tail recursive',
            tt('three') + ': tail recursive',
            tt('four') + """: technically tail recursive, but loops
            forever (so it's efficiently stuck)""",
        ))
    },
]

code_questions = [
    {
        'description': """Write a function <tt>map</tt> that is tail
        recursive. It should take in a list <tt>lst</tt> and a
        function <tt>fn</tt>, and apply the function onto every
        element in the list.""",
        'code': """
(define (map fn lst)
    ; YOUR CODE HERE
    )

STk> (map (lambda (x) (* x x)) '(1 2 3 4))
(1 4 9 16)
""",
        'hint': """You should use a helper. Also, the built-in
        <tt>append</tt> function, which concatenates two lists
        together, should prove useful.""",
        'solution': """
(define (map fn lst)
    (define (map-help lst so-far)
        (if (null? lst)
            so-far
            (map-help (cdr lst)
                      (append so-far (list (fn (car lst)))))))
    (map-help lst nil))"""
    },
    {
        'description': """Write a function <tt>filter</tt> that is
        tail recursive. It should take in a list <tt>lst</tt> and a
        function <tt>pred</tt>, and keep only the elements in the list
        that satisfy the predicate.""",
        'code': """
(define (filter pred lst)
    ; YOUR CODE HERE
    )

STk> (filter even? '(1 2 3 4))
(2 4)
""",
        'hint': """You should use a helper. Also, the built-in
        <tt>append</tt> function, which concatenates two lists
        together, should prove useful.""",
        'solution': """
(define (filter pred lst)
    (define (filter-help lst so-far)
        (cond ((null? lst) so-far)
              ((pred (car lst))
                    (filter-help (cdr lst)
                                 (append so-far (list (car lst)))))
              (else (filter-help (cdr lst) so-far))))
    (filter-help lst nil))""",
    },
    {
        'description': """Write a function <tt>insert</tt> that is
        tail recursive. It should take in a list <tt>lst</tt>, an
        <tt>item</tt>, and an <tt>index</tt>, and insert the
        <tt>item</tt> into the list at the given <tt>index</tt>.""",
        'code': """
(define (insert lst item index)
    ; YOUR CODE HERE
    )

STk> (insert '(1 2 3 4) 100 2)
(1 2 100 3 4)
STk> (insert nil 10 4)
(10)
""",
        'hint': """You should use a helper. Also, the built-in
        <tt>append</tt> function, which concatenates two lists
        together, should prove useful.""",
        'solution': """
(define (insert lst item index)
    (define (insert-help lst index so-far)
        (if (or (null? lst) (= index 0))
            (append so-far
                    (cons item lst))
            (insert-help (cdr lst)
                         (- index 1)
                         (append so-far (list (car lst))))))
    (insert-help lst index nil))"""
    },
    {
        'description': """Write a function <tt>remove</tt> that is
        tail recursive. It should take in a list <tt>lst</tt> and an
        <tt>item</tt>, and remove the first occurence of <tt>item</tt>
        in the list. If <tt>item</tt> item doesn't occur, just return
        the original list.""",
        'code': """
(define (remove lst item)
    ; YOUR CODE HERE
    )

STk> (remove '(1 2 3 4) 3))
(1 2 4)
STk> (remove '(1 3 5) 6)
(1 3 5)
STk> (remove nil 100)
()
""",
        'hint': """You should use a helper. Also, the built-in
        <tt>append</tt> function, which concatenates two lists
        together, should prove useful.""",
        'solution': """
(define (remove lst item)
    (define (remove-help lst so-far)
        (cond ((null? lst) so-far)
              ((eq? (car lst) item) (append so-far (cdr lst)))
              (else (remove-help (cdr lst)
                                 (append so-far (list (car lst)))))))
    (remove-help lst nil))"""
    },
    {
        'description': """Write a function <tt>pop</tt> that is
        tail recursive. It should take in a list <tt>lst</tt> and an
        <tt>index</tt>, and remove the item in the list at the given
        <tt>index</tt>. If the index is out of bounds, just return
        the original list.""",
        'code': """
(define (pop lst index)
    ; YOUR CODE HERE
    )

STk> (pop '(1 2 3 4) 2))
(1 2 4)
STk> (pop '(1 3 5) 2)
(1 3)
STk> (pop nil 8)
()
""",
        'hint': """You should use a helper. Also, the built-in
        <tt>append</tt> function, which concatenates two lists
        together, should prove useful.""",
        'solution': """
(define (pop lst index)
    (define (pop-help lst index so-far)
        (cond ((null? lst) so-far)
              ((= index 0) (append so-far (cdr lst)))
              (else (pop-help (cdr lst)
                              (- index 1)
                              (append so-far (list (car lst)))))))
    (pop-help lst nil))"""
    },
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

