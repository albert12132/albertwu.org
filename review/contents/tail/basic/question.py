from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Tail Recursion'
level = 'basic'

references = [
    'Lecture: Tail Calls, Iterators',
    'Lab 7a',
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
        'description': """What is tail call optimization? What is the
        benefit to using it?""",
        'solution': """Tail call optimization is a
        compiler/interpreter optimization that makes memory usage
        more efficient for recursion. Normally, each recursive call
        requires a new frame, and each frame needs to stick around
        until all of the recursive calls are done. With tail call
        optimization, once we move on to the next recursive call, the
        old frame gets discarded, leaving only one frame in memory
        at a time."""
    },
    {
        'description': """What is a tail context, in terms of Scheme?
        Why are tail contexts important for tail call optimization?
        """,
        'solution': """A tail context is a location in a Scheme
        function that the interpreter can identify as tail recursive.
        A Scheme function needs to be written in a particular way
        in order for the interpreter to realize that it should perform
        tail call optimization. The following are tail contexts:
        """ + ul((
            'The last sub-expression in the body of a '+ tt('lambda'),
            'The 2nd and 3rd sub-expression in an '+ tt('if'),
            'All non-predicate sub-expressions in a '+ tt('cond'),
            'The last sub-expression in '+tt('and')+' or '+tt('or'),
            'The last sub-expression in a '+tt('begin'),
        ))
    },
    {
        'description': """Which of the following Scheme functions
        are tail recursive?""",
        'code': """
(define (one x)
    (if (= x 0)
        1
        (* x (one (- x 1)))))

(define (two x so-far)
    (if (= x 0)
        so-far
        (two (- x 1) (* so-far x))))

(define (three fn x)
    (cond ((null? x) #t)
          ((not (fn (car x))) #f)
          (else (three fn (cdr x)))))

(define (four fn x)
    (if (null? x)
        #t
        (and (four fn (cdr x)) (fn x))))""",
        'solution': ul((
            tt('one') + ': not tail recursive',
            tt('two') + ': tail recursive',
            tt('three') + ': tail recursive',
            tt('four') + ': not tail recursive',
        ))
    },
]

code_questions = [
    {
        'description': """Write a function <tt>reverse</tt> that is
        tail recursive. It should take a list <tt>lst</tt> and return
        the reverse of that list.""",
        'code': """
(define (reverse lst)
    ; YOUR CODE HERE
    )

STk> (reverse '(1 2 3 4))
(4 3 2 1)
STk> (reverse nil)
()
""",
        'hint': 'You should use a helper function',
        'solution': """
(define (reverse lst)
    (define (reverse-help lst so-far)
        (if (null? lst)
            so-far
            (reverse-help (cdr lst) (cons (car lst) so-far))))
    (reverse-help lst nil))"""
    },
    {
        'description': """Write a function <tt>reduce</tt> that is
        tail recursive. It should take a list <tt>lst</tt>,
        <tt>combiner</tt> function, and a <tt>start</tt> value, and
        reduce all the elements in the list using the
        <tt>combiner</tt>, beginnning at <tt>start</tt>.""",
        'code': """
(define (reduce combiner lst start)
    ; YOUR CODE HERE
    )

STk> (reduce + '(1 2 3 4) 0)
10
STk> (reduce - '(1 2 3 4) 0)
-10
STk> (reduce + '(1 2 3 4) 10)
20
STk> (reduce * '(1 2 3 4) 1)
24
""",
        'solution': """
(define (reduce combiner lst start)
    (if (null? lst)
        start
        (reduce combiner (cdr lst) (combiner start (car lst)))))"""
    },
    {
        'description': """Write a function <tt>all</tt> that is
        tail recursive. It should take a list <tt>lst</tt> and a
        function <tt>pred</tt>, and return true (<tt>#t</tt>) only if
        all the elements in the list satisfy the predicate.""",
        'code': """
(define (all lst pred)
    ; YOUR CODE HERE
    )

STk> (all '(1 2 3 4) even?)
#f
STk> (all '(1 3 5) odd?)
#t""",
        'solution': """
(define (all lst pred)
    (if (null? lst)
        #t
        (and (pred (car lst)) (all (cdr lst) pred))))"""
    },
    {
        'description': """Write a function <tt>count</tt> that is
        tail recursive. It should take a list <tt>lst</tt> and an
        <tt>item</tt>, and return the number of times that
        <tt>item</tt> occurs in the list.""",
        'code': """
(define (count lst item)
    ; YOUR CODE HERE
    )

STk> (count '(1 2 3 4) 3)
1
STk> (count '(2 3) 5)
0
STk> (count '(2 2 4 2 3) 2)
3""",
        'solution': """
(define (count lst item)
    (define (count-help lst num)
        (cond ((null? lst) num)
              ((eq? (car lst) item) (count-help (cdr lst) (+ num 1)))
              (else (count-help (cdr lst) num))))
    (count-help lst 0))"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

