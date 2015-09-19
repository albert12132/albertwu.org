~ title: Tail Recursion
~ level: exam

<block references>
[Lecture: Tail Calls](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/27-Tail_1pps.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

Which of the following Scheme functions are tail recursive?

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

<solution>

1. `one`: tail recursive
2. `two`: not tail recursive
3. `three`: tail recursive
4. `four`: technically tail recursive, but loops forever (so it's
   stuck, but efficiently so)

</solution>

Code-Writing questions
----------------------

<question>

Write a function `map` that is tail recursive. It should take in a list
`lst` and a function `fn`, and apply the function onto every element in
the list.

    (define (map fn lst)
        ; YOUR CODE HERE
        )

    scm> (map (lambda (x) (* x x)) '(1 2 3 4))
    (1 4 9 16)

You should use a helper function. Also, the built-in `append` function,
which concatenates two lists together, should prove useful.

<solution>

    (define (map fn lst)
        (define (map-help lst so-far)
            (if (null? lst)
                so-far
                (map-help (cdr lst)
                          (append so-far (list (fn (car lst)))))))
        (map-help lst nil))

</solution>

<question>

Write a function `filter` that is tail recursive. It should take in a
list `lst` and a function `pred`, and keep only the elements in the
list that satisfy the predicate.

    (define (filter pred lst)
        ; YOUR CODE HERE
        )

    scm> (filter even? '(1 2 3 4))
    (2 4)

**Hint**: You should use a helper. Also, the built-in `append`
function, which concatenates two lists together, should prove useful.

<solution>

    (define (filter pred lst)
        (define (filter-help lst so-far)
            (cond ((null? lst) so-far)
                  ((pred (car lst))
                        (filter-help (cdr lst)
                                     (append so-far (list (car lst)))))
                  (else (filter-help (cdr lst) so-far))))
        (filter-help lst nil))

</solution>

<question>

Write a function `insert` that is tail recursive. It should take in a
list `lst`, an `item`, and an `index`, and insert the `item` into the
list at the given `index`.

    (define (insert lst item index)
        ; YOUR CODE HERE
        )

    scm> (insert '(1 2 3 4) 100 2)
    (1 2 100 3 4)
    scm> (insert nil 10 4)
    (10)

You should use a helper. Also, the built-in `append` function, which
concatenates two lists together, should prove useful.

<solution>

    (define (insert lst item index)
        (define (insert-help lst index so-far)
            (if (or (null? lst) (= index 0))
                (append so-far
                        (cons item lst))
                (insert-help (cdr lst)
                             (- index 1)
                             (append so-far (list (car lst))))))
        (insert-help lst index nil))

</solution>

<question>

Write a function `remove` that is tail recursive. It should take in a
list `lst` and an `item`, and remove the first occurence of `item` in
the list.  If `item` item doesn't occur, just return the original list.

    (define (remove lst item)
        ; YOUR CODE HERE
        )

    scm> (remove '(1 2 3 4) 3))
    (1 2 4)
    scm> (remove '(1 3 5) 6)
    (1 3 5)
    scm> (remove nil 100)
    ()

**Hint**: You should use a helper. Also, the built-in `append`
function, which concatenates two lists together, should prove useful.

<solution>

    (define (remove lst item)
        (define (remove-help lst so-far)
            (cond ((null? lst) so-far)
                  ((eq? (car lst) item) (append so-far (cdr lst)))
                  (else (remove-help (cdr lst)
                                     (append so-far (list (car lst)))))))
        (remove-help lst nil))

</solution>

<question>

Write a function `pop` that is tail recursive. It should take in a list
`lst` and an `index`, and remove the item in the list at the given
`index`. If the index is out of bounds, just return the original list.

    (define (pop lst index)
        ; YOUR CODE HERE
        )

    scm> (pop '(1 2 3 4) 2))
    (1 2 4)
    scm> (pop '(1 3 5) 2)
    (1 3)
    scm> (pop nil 8)
    ()

**Hint**: You should use a helper. Also, the built-in `append`
function, which concatenates two lists together, should prove useful.

<solution>

    (define (pop lst index)
        (define (pop-help lst index so-far)
            (cond ((null? lst) so-far)
                  ((= index 0) (append so-far (cdr lst)))
                  (else (pop-help (cdr lst)
                                  (- index 1)
                                  (append so-far (list (car lst)))))))
        (pop-help lst index nil))

</solution>

</block contents>
