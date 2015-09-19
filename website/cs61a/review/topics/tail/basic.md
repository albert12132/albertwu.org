~ title: Tail Recursion
~ level: basic

<block references>
[Lecture: Tail Calls](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/27-Tail_1pps.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What is tail call optimization? What is the benefit to using it?

<solution>

Tail call optimization is a compiler/interpreter optimization that
makes memory usage more efficient for recursion. Normally, each
recursive call requires a new frame, and each frame needs to stick
around until all of the recursive calls are done. With tail call
optimization, once we move on to the next recursive call, the old
frame gets discarded, leaving only one frame in memory at a time.

</solution>

<question>

What is a tail context, in terms of Scheme?  Why are tail contexts
important for tail call optimization?

<solution>

A tail context is a location in a Scheme function that the interpreter
can identify as tail recursive.  A Scheme function needs to be written
in a particular way in order for the interpreter to realize that it
should perform tail call optimization. The following are tail contexts:

* The last sub-expression in the body of a `lambda`
* The 2nd and 3rd sub-expression in an `if`
* All non-predicate sub-expressions in a `cond`
* The last sub-expression in `and` or `or`
* The last sub-expression in a `begin`

</solution>

<question>

Which of the following Scheme functions are tail recursive?

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
            (and (four fn (cdr x)) (fn x))))

<solution>

1. `one`: not tail recursive
2. `two`: tail recursive
3. `three`: tail recursive
4. `four`: not tail recursive

</solution>

Code-Writing question
---------------------

<question>

Write a function `reverse` that is tail recursive. It should take a
list `lst` and return the reverse of that list.

    (define (reverse lst)
        ; YOUR CODE HERE
        )

    scm> (reverse '(1 2 3 4))
    (4 3 2 1)
    scm> (reverse nil)
    ()

**Hint**: You should use a helper function.

<solution>

    (define (reverse lst)
        (define (reverse-help lst so-far)
            (if (null? lst)
                so-far
                (reverse-help (cdr lst) (cons (car lst) so-far))))
        (reverse-help lst nil))

</solution>

<question>

Write a function `reduce` that is tail recursive. It should take a list
`lst`, `combiner` function, and a `start` value, and reduce all the
elements in the list using the `combiner`, beginnning at `start`.

    (define (reduce combiner lst start)
        ; YOUR CODE HERE
        )

    scm> (reduce + '(1 2 3 4) 0)
    10
    scm> (reduce - '(1 2 3 4) 0)
    -10
    scm> (reduce + '(1 2 3 4) 10)
    20
    scm> (reduce * '(1 2 3 4) 1)
    24

<solution>

    (define (reduce combiner lst start)
        (if (null? lst)
            start
            (reduce combiner (cdr lst) (combiner start (car lst)))))

</solution>

<question>

Write a function `all` that is tail recursive. It should take a list
`lst` and a function `pred`, and return true (`#t`) only if all the
elements in the list satisfy the predicate.

    (define (all lst pred)
        ; YOUR CODE HERE
        )

    scm> (all '(1 2 3 4) even?)
    #f
    scm> (all '(1 3 5) odd?)
    #t

<solution>

    (define (all lst pred)
        (if (null? lst)
            #t
            (and (pred (car lst)) (all (cdr lst) pred))))

</solution>

<question>

Write a function `count` that is tail recursive. It should take a list
`lst` and an `item`, and return the number of times that `item` occurs
in the list.

    (define (count lst item)
        ; YOUR CODE HERE
        )

    scm> (count '(1 2 3 4) 3)
    1
    scm> (count '(2 3) 5)
    0
    scm> (count '(2 2 4 2 3) 2)
    3

<solution>

    (define (count lst item)
        (define (count-help lst num)
            (cond ((null? lst) num)
                  ((eq? (car lst) item) (count-help (cdr lst) (+ num 1)))
                  (else (count-help (cdr lst) num))))
        (count-help lst 0))

</solution>

</block contents>
