~ title: Scheme
~ level: basic

<block references>
* [Lecture: Functional Programming](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/23-Scheme_1pps.pdf)
* [Lab 8](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab08/lab8-scheme.html)
* [Discussion 9](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion09_sol.pdf)
</block references>

<block notes>
</block notes>

<block contents>

What would Scheme print
-----------------------

<question>

<prompt>
    scm> (+ 4 3)
    7
    scm> (4 + 3)
    Error
    scm> (+ 1 2 3 4)
    10
    scm> (- 1 2 3 4)
    -8
</prompt>

<question>

<prompt>
    scm> (if True (+ 2 3))
    5
    scm> (if False (+ 2 3))
    okay   ; i.e. returns nothing
    scm> (if False (/ 1 0) 4)
    4
    scm> (and True False True)
    False
    scm> (and True 0 True)
    True
    scm> (and 3 5 2)
    2
    scm> (or True False True)
    True
    scm> (or False 4 True)
    4
</prompt>

<question>

<prompt>
    scm> (define x 2)
    x
    scm> x
    2
    scm> (define (f x) (* x x))
    f
    scm> (f 4)
    16
    scm> (define (g x) (lambda (y) (* x y)))
    g
    scm> ((g 4) 5)
    20
</prompt>

<question>

<prompt>
    scm> (cons 1 (cons 2 nil))
    (1 2)
    scm> (cons 1 2)
    (1 . 2)
    scm> (car (cons 1 (cons 2 nil)))
    1
    scm> (cdr (cons 1 (cons 2 nil)))
    (2)
    scm> (cdr (cons 1 2))
    2
    scm> (null? (cons 1 nil))
    False
    scm> (null? (cdr (cons 1 nil)))
    True
    scm> (list 1 2 3 4)
    (1 2 3 4)
    scm> (cdr (list 1 2 3 4))
    (2 3 4)
</prompt>

Code-Writing Questions
----------------------

<question>

Implement the function `filter`, which takes a predicate and a Scheme
list as arguments.  `filter` will return a new list that only contains
elements of the original list that satisfy the predicate.

    (define (filter pred lst)
        ; YOUR CODE HERE
        )

    ; Tests
    scm> (define (less-3 x) (< x 3))
    less-3
    scm> (filter less-3 (list 1 2 3 4))
    (1 2)

<solution>

    (define (filter pred lst)
        (cond ((null? lst) nil)
              ((pred (car lst)) (cons (car lst)
                                      (filter pred (cdr lst))))
              (else (filter pred (cdr lst)))))

</solution>

<question>

Implement the function `interleave`, which takes a two lists as
arguments.  `interleave` will return a new list that interleaves the
elements of the two lists, with `list1` starting first. Refer to the
tests for sample input/output.

    (define (interleave list1 list2)
        ; YOUR CODE HERE
        )

    ; Tests
    scm> (interleave (list 1 3 5) (list 2 4 6))
    (1 2 3 4 5 6)
    scm> (interleave (list 1 3 5) nil)
    (1 3 5)
    scm> (interleave (list 1 3 5) (list 2 4))
    (1 2 3 4 5)

<solution>

    (define (interleave list1 ist2)
        (if (or (null? list1) (null? list2))
            (append list1 list2)
            (cons (car list1)
                  (cons (car list2)
                        (interleave (cdr list1) (cdr list2))))))

</solution>

<question>

Implement the function `count-stairways`, which takes a number (of
steps).  Assuming we can take 1 or 2 steps, return the number of ways
we can climb up the stairs.

    (define (count-stairways n)
        ; YOUR CODE HERE
        )

    ; Tests
    scm> (count-stairways 4)
    5
    scm> (count-stairways 5)
    8

<solution>

    (define (count-stairways n)
        (cond ((= n 1) 1)
              ((= n 2) 2)
              (else (+ (count-stairways (- n 1))
                       (count-stairways (- n 2))))))

</solution>

</block contents>
