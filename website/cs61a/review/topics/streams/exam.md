~ title: Streams
~ level: exam

<block notes>
</block notes>

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/111ucG9UwZ8ESAWGY5zWq65Nd6er_lICOfXnsEZMtSik/edit#slide=id.g63e95c8f9_111_1134)
</block references>

<block contents>

Conceptual Questions
--------------------

<question>

Given the following function, list the first 5 elements of the Stream
that is returned by `stream1()`.

    (define (stream1)
        (cons-stream 0
            (cons-stream 1
                (add-streams (stream1) (stream-cdr (stream1))))))

<solution>

0, 1, 1, 2, 3 (the Fibonacci numbers)

</solution>

<question>

Given the following function, list the first 5 elements of the Stream
that is returned by `stream2()`.

    (define (stream2)
        (cons-stream 1
            (add-streams (stream2) (stream2))))

<solution>

1, 2, 4, 8, 16 (the powers of 2)

</solution>

Code-Writing questions
----------------------

<question>

Create a function `make-fact-stream`, which returns a Stream whose
*n*th element is *n*!  (factorial of *n*).

    (define (make-fact-stream)
        'YOUR-CODE-HERE
    )


    scm> (stream-to-list (make-fact-stream) 4)
    (1 1 2 6)

**Hint**: Try writing an iterative factorial function first, then
convert it into the Stream function.  You should also use a helper
function.

<solution>

    (define (make-fact-stream)
        (helper 0 1))

    (define (helper n total)
        (cons-stream total
            (helper (+ n 1)
                    (* total (+ n 1)))))

    # here's the iterative factorial we use to convert
    def infinite_fact():
        n, total = 0, 1
        while True:
            print(total)
            n, total = n + 1, total * (n + 1)

</solution>

More practice problems
----------------------

> *Note*: The following link contains Stream questions, but the questions use the
> Python version of streams. The thought process behind each problem is the same,
> but if you feel that you would not benefit from reading Python stream code (as
> opposed to Scheme stream code), then it's better if you find stream questions
> elsewhere (Summer 2014 final is a good idea).

This
[link](http://www-inst.eecs.berkeley.edu/~cs61a/su12/lab/lab13/lab13.php)
contains Stream problems (as well as iterator and generator problems)
from the summer 2012 version of 61A. They are pretty tough (probably
tougher than final material), so don't get discouraged if you get
stuck!

Solutions are also included in the lab (in the form of toggle buttons).
Don't worry about the Py section -- we didn't cover that this
semester.

</block contents>
