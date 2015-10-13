~ title: Streams
~ level: basic

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

What are the advantages to using a stream as opposed to a regular
list?

<solution>

A stream can be used to "store" infinite amounts of data. Because the
data is not computed until you need it, you can use memory more
efficiently.

</solution>

<question>

What is a promise? How is this related to the `force` and `delay` functions?

<solution>

A promise is an object that encapsulates an expression. You can create promises
by using the `delay` function:

    scm> (delay (/ 1 0))
    #[promise (not forced)]

The expression `(/ 1 0)`, when evaluated, will cause a `ZeroDivisionError`.
However, since we are *delaying* its evaluation, we don't actually compute `(/ 1
0)` just yet.

We can *force* evaluation of a promise's expression by using the `force`
function:

    scm> (define p (delay (/ 1 0)))
    p
    scm> p
    #[promise (not forced)]
    scm> (force p)
    ZeroDivisionError

It is only after we try to `force` the promise `p` that we evaluate `(/ 1 0)`
and cause the `ZeroDivisionError`.

</solution>

<question>

Consider the following stream:

    (define my-stream
            (cons-stream 1 (cons-stream 2 (cons-stream 3 nil))))

What type of object is `(cdr my-stream)`

<solution>

`(cdr my-stream)` -- in other words, the rest of `my-stream`, is a **promise**
object.

> Remember that `(cons-stream first rest)` is equivalent to `(cons first (delay
> rest))`

</solution>

What type of object is `(stream-cdr my-stream)`?

<solution>

`(stream-cdr my-stream)`  is a **stream**, specifically the stream `(cons-stream
2 (constream 3 nil))`.

> Remember that `(stream-cdr my-stream)` is equivalent to `(force (cdr
> my-stream))`

</solution>


Code-Writing questions
----------------------

<question>

Define a function called `odd-stream` that returns a stream of odd-numbered
integers, starting from a given odd number `n` (you can always assume `n` is
odd).

    (define (odd-stream n)
      ; YOUR-CODE-HERE
    )

In other words, `odd-stream` should have the following behavior:

    scm> (stream-to-list (odd-stream 1) 5)
    1 3 5 7 9

<solution>

    (define (odd-stream n)
        (cons-stream n (odd-stream (+ n 2))))

</solution>

<question>

Write a function `add-streams` that takes two (possibly infinite) streams called
`s1` and `s2` and returns a stream whose elements are elements of `s1` and `s2`
added pairwise. For example calling `add-streams` on

    s1 = 1 2 3 4 ...
    s2 = 5 6 7 8 ...

would return the following stream:

    6 8 10 12 ...

If either of streams is finite, the returned stream contain as many elements as
the shorter input stream.

    (define (add-streams s1 s2)
      ; YOUR-CODE-HERE
    )


<solution>

    (define (add-streams s1 s2)
      (if (or (null? s1) (null? s2))
          nil
          (cons-stream (+ (car s1) (car s2))
                       (add-streams (stream-cdr s1)
                                    (stream-cdr s2))))
    )

</solution>

<question>

Write a function `reduce-first-k()` that reduces the first *k*
elements in a given stream, using a given combiner. If the stream has
fewer than *k* elements, reduce all the elements in the stream.

    (define (reduce-first-k s k combiner)
      ; YOUR-CODE-HERE
    )

> You may assume the input stream `s` contains at least 2 elements, and that `k`
> always starts out as greater than or equal to 2. Do not use
> `stream-to-list`.

    ; Tests
    scm> (define s (ints 1))
    s
    scm> (reduce-first-k s 4 +)  ; 1 + 2 + 3 + 4
    10
    scm> (define s1 (cons-stream 1 (cons-stream 2 nil))
    s1
    scm> (reduce-first-k s1 4 +) ; 1 + 2
    3

<solution>

    (define (reduce-first-k s k combiner)
      (if (or (= k 2) (null? (cdr (cdr s))))
          (combiner (car s)
                    (car (cdr s)))
          (combiner (car s)
                    (reduce-first-k (stream-cdr s)
                                    (- k 1)
                                    combiner))))

</solution>

<question>

Given the following function, list the first 5 numbers in the Stream
that `my-stream` returns.

    (define (my-stream)
      (cons-stream 0
        (add-streams (ints 1)
                     (map-stream (lambda (x) (* 3 x))
                                 (ints 1)))))

<solution>

    0, 4, 8, 12, 16

Here's how I like to solve these types of questions. We know that the first
element of `my-stream` is 0, but we don't know what the rest of the elements
are. Assign variables to those unknown elements:

    my-stream = 0 a b c d

Our goal is to figure out what `a`, `b`, and `c` are. How do we compute the rest
of `my-stream`? With the second argument of `cons-stream`:

    (add-streams (ints 1)
                 (map-stream (lambda (x) (* 3 x))
                             (ints 1)))))

Here, we are adding two streams together:

1. `(ints 1)`: this is just the stream `1, 2, 3, 4, ...`
3. `(map-stream (lambda (x) (* 3 x)) (ints 1)))))`: this is the stream `1, 2, 3,
   4, ...`, but with each element multiplied by 3. In other words, this stream
   contains the elements `3, 6, 9, 12, ...`

In other words, the rest of `my-stream` (remember we called this `a, b, c, d` is
going to be the result of adding `1, 2, 3, 4, ...` and `3, 6, 9, 12, ...`.
Diagramatically:

    my-stream = 0 | a  b  c  d
    --------------|------------
                  | 1  2  3  4
                + | 3  6  9  12
                --|------------
                  | 4  8  12 16

Thus, the first 5 elements of `my-stream` are 0, 4, 8, 12, and 16.

</solution>

</block contents>
