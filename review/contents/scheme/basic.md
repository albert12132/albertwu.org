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
    STk> (+ 4 3)
    7
    STk> (4 + 3)
    Error
    STk> (+ 1 2 3 4)
    10
    STk> (- 1 2 3 4)
    -8
</prompt>

<question>

<prompt>
    STk> (if #t (+ 2 3))
    5
    STk> (if #f (+ 2 3))
    okay   ; i.e. returns nothing
    STk> (if #f (/ 1 0) 4)
    4
    STk> (and #t #f #t)
    #f
    STk> (and #t 0 #t)
    #t
    STk> (and 3 5 2)
    2
    STk> (or #t #f #t)
    #t
    STk> (or #f 4 #t)
    4
</prompt>

<question>

<prompt>
    STk> (define x 2)
    x
    STk> x
    2
    STk> (define (f x) (* x x))
    f
    STk> (f 4)
    16
    STk> (define (g x) (lambda (y) (* x y)))
    g
    STk> ((g 4) 5)
    20
</prompt>

<question>

<prompt>
    STk> (cons 1 (cons 2 nil))
    (1 2)
    STk> (cons 1 2)
    (1 . 2)
    STk> (car (cons 1 (cons 2 nil)))
    1
    STk> (cdr (cons 1 (cons 2 nil)))
    (2)
    STk> (cdr (cons 1 2))
    2
    STk> (null? (cons 1 nil))
    #f
    STk> (null? (cdr (cons 1 nil)))
    #t
    STk> (list 1 2 3 4)
    (1 2 3 4)
    STk> (cdr (list 1 2 3 4))
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
    STk> (define (less-3 x) (< x 3))
    less-3
    STk> (filter less-3 (list 1 2 3 4))
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
    STk> (interleave (list 1 3 5) (list 2 4 6))
    (1 2 3 4 5 6)
    STk> (interleave (list 1 3 5) nil)
    (1 3 5)
    STk> (interleave (list 1 3 5) (list 2 4))
    (1 2 3 4 5)

<solution>

    (define (interleave list1 ist2)
        (if (or (null? list1) (null? list2))
            (append list1 list2)
            (cons (car list1)
                  (cons (car list2)
                        (interleave (cdr list1) (cdr list2))))))""",

</solution>

<question>

Implement the function `count-stairways`, which takes a number (of
steps).  Assuming we can take 1 or 2 steps, return the number of ways
we can climb up the stairs.

    (define (count-stairways n)
        ; YOUR CODE HERE
        )

    ; Tests
    STk> (count-stairways 4)
    5
    STk> (count-stairways 5)
    8

<solution>

    (define (count-stairways n)
        (cond ((= n 1) 1)
              ((= n 2) 2)
              (else (+ (count-stairways (- n 1))
                       (count-stairways (- n 2))))))

</solution>

</block contents>
