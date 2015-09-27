~ title: Scheme
~ level: exam

<block references>
* [Albert's and Robert's slides](https://docs.google.com/presentation/d/1abmDnKjrq1tcjGvvRNAKhOiSTSE2lyagtcEPal07Gbo/edit)
</block references>

<block notes>
</block notes>

<block contents>

What would Scheme print
-----------------------

<question>

For the following questions, write the value that the expression
evaluates to if you type it into `scm`. If the expression contains a
function (or multiple), write "FUNCTION" in place of that function. If
the expression causes an error, write "ERROR".

<prompt>
    scm> (cons 1 (cons 2 (cons 3 (cons 4 nil))))
    (1 2 3 4)
    scm> (cons (cons (cons 3 2) 1) (cons 4 nil))
    (((3 . 2) . 1) 4)
    scm> (cdr (cons (cdr (list 1 2)) (cons 3 (cons 4 nil))))
    (3 4)
    scm> (define lst (cons (lambda (x) (cons x x)) nil))
    scm> ((car lst) lst)
    ((FUNCTION) FUNCTION)
    scm> (define (x) (lambda (x) (list x x)))
    scm> (((car ((x) x))) 4)
    (4 4)
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `count-stairways`, which takes a number `n` as an
argument. Assuming you can only take 2 or 3 steps at a time, return the
number of ways you can reach the top of a staircase with `n` stairs.

This is different than the usual `count-stairways` -- notice that this
time, we can only take 2 or 3 steps, rather than 1 or 2.

    (define (count-stairways n)
        ; YOUR CODE HERE
        )

    ; Tests
    scm> (count-stairways 1)
    0
    scm> (count-stairways 4)
    1
    scm> (count-stairways 5)
    2
    scm> (count-stairways 8)
    4

<solution>

    (define (count-stairways n)
        (cond ((= n 1) 0)
              ((or (= n 2) (= n 3)) 1)
              (else (+ (count-stairways (- n 2))
                       (count-stairways (- n 3))))))

</solution>

<question>

Implement a function `count-serpinski`, which takes a numbero `depth`
as an argument. The function calculates how many triangles are
contained in a Serpinski's triangle with the given depth. See the tests
for examples.

![Serpinski's triangle](/public/img/review/serpinski.svg)

How can you use recursive calls on *n-1* to build your answer for *n*?

    (define (count-serpinski depth)
        ; YOUR CODE HERE
        )

    ; Tests
    scm> (count-serpinski 1)
    1
    scm> (count-serpinski 2)
    5
    scm> (count-stairways 3)
    17
    scm> (count-stairways 4)
    53

<solution>

    (define (count-serpinski n)
        (if (= n 1)
            1
            (+ 2 (* 3 (count-serpinski (- n 1))))))

The recursive call can be derived as follows:

1. There are three smaller *n-1* serpinski triangles at each of the
   corners
2. There are two additional triangles drawn -- the triangle in the
   center, and the overall triangle.

</solution>

Fill-in the blank questions
---------------------------

Fill in the blanks for the `construct` function. It takes a value and a
list of lists as arguments. It returns a new list of lists, where each
element is a list from the old list, but with the value added to the
front.

    (define (construct value lists)
        (if ______
            ______
            (cons _____________
                  _____________)))
        )

    ; Tests
    scm> (define lists '((10) () (4 3) (2 5 3)))
    lists
    scm> (construct 6 lists)
    ((6 1) (6) (6 4 3) (6 2 5 3))
    scm> (construct 6 '())
    ()

<solution>

    (define (construct value lists)
        (if (null? lists)
            nil
            (cons (cons value (car lists))
                  (construct value (cdr lists)))))

</solution>

</block contents>
