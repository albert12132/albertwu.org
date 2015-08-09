~ title: Final review from section 12/5

<block notes>

These questions were written for my section on 12/5/2014.

</block notes>

<block contents>

Scheme
------

<question>

Implement a function `flatten` which takes a nested Scheme list and
flattens it. For example,

    STk> (flatten '(1 (2 (3) 4) 5 6))
    (1 2 3 4 5 6)

Here is the skeleton code:

    (define (flatten lst)
      ; Your code here
      )

<solution>

    (define (flatten lst)
      (cond ((null? lst) nil)
            ((list? (car lst)) (append (flatten (car lst))
                                       (flatten (cdr lst))))
            (else (cons (car lst) (flatten (cdr lst))))
      )
    )

This question tests various list manipulation techniques. The solution
is written recursively, with the following cases:

* If the list is empty, then flattening it does nothing. Just return an
  empty list.
* If the first element of the list is a nested list (`(list? (car
  lst))`), then append it to the flattened version of the rest of the
  list. For example, for the list

        ((2 (3) 4) 5 6)

  The first element is `(2 (3) 4)`, so to get the flattened list, we do
  the following:
    1. Flatten the first element: `(flatten '(2 (3) 4)) --> (2 3 4)`
    2. Flatten the rest: `(flatten '(5 6)) --> (5 6)`
    3. Join the results by using `append`, e.g.
* Otherwise, the first element of the list is not a list. Simply leave
  it as is and flatten the rest of list.

</solution>

Interpreters
------------

<question>

Find the `Pair` representation of the following Scheme expression:

    (1 2 . (3 . 4))

<solution>

First, notice that this is the same thing as

    (1 2 3 . 4)

Then the `Pair` representation is

    Pair(1,
         Pair(2,
              Pair(3, 4)))

Notice that this is different than the `Pair` representation for `(1 2
3 4)`, which would be

    Pair(1,
         Pair(2,
              Pair(3,
                   Pair(4, nil))))

</solution>

<question>

*From Fall 2013*: Convert the following Scheme expression into its Pair
representation (i.e. what `scheme_read` would return):

    (+ 3 '(4 8) 'hi)

<solution>

Let `P` denote `Pair`. The solution is

    P('+',
      P(3,
        P( P('quote', P(P(4, P(8, nil)), nil)),
          P( P('quote', P('hi', nil)),
            nil)))):

First ignore the nested lists and quotes:

    (+ 3 ___  ___)

This would generate the following Pair representation

    P('+', P(3, P(___, P(___, nil))))

Now we just have to fill in the two blanks. The first blank corresponds
to `'(4 8)`. This has a Pair representation like this

    P('quote', P( P(4, P(8, nil)) , nil))

(Review Q1 of Proj4 if you are unsure why the quote was converted in this way). The
second blank correpsonds to `'hi` and it gets converted into

    P('quote', P('hi', nil))

Put these together to get the final solution.

</solution>

<question>

Count how many times `scheme_eval` and `scheme_apply` are called for
the following expression:

    (+ 1 (- 2 3))

<solution>

* `scheme_apply` is called 2 times. Observe that there are only two
  function calls in this expression: `+` and `-`.
* `scheme_eval` is called 7 times:
    1. Once for the entire expression `(+ 1 (- 2 3))`
    2. Once for `+`
    3. Once for `1`
    4. Once for `(- 2 3)`. Since this is also a function call, we need
       to evaluate all of its operators and operands:
    5. Once for `-`
    6. Once for `2`
    7. Once for `3`.

</solution>

<question>

Given the following function

    (define (square x) (* x x))

How many times are `scheme_eval` and `scheme_apply` called for the
following expression?

    (+ 2 (square 4))

<solution>

* `scheme_eval`: 10 times
* `scheme_apply`: 3 times

For apply, a good rule of thumb is to count the number of functions
(primitive and user-defined) that are called. In this case, we call
`+`, `square`, and `*` (when we evaluate the body of `square`).  Thus,
apply is called 3 times.

For eval, each of the following bullets represents one
call to `scheme_eval`::

* `(+ 2 (square 4))`
    * `+`
    * `2`
    * `(square 4)`
        * `square`
        * `4`
        * `(* x x)`
            * `*`
            * `x`
            * `x`

Thus, we have a total of 10 calls to `scheme_eval`.

</solution>

Iterators and Generators
------------------------

Implement an iterable class `IndexOf`, which takes a string and a
substring in its constructor.  When you iterate over an instance of
`IndexOf`, it will produce the indices at which the substring occurs in
the string. Consider the following example:

    >>> indices = IndexOf('aba', 'ababaaba')
    >>> for i in indices:
    ...     print(i)
    0
    2
    5

The substring `'aba'` occurs at indices 0, 2, and 5 in the string
`'ababaaba'`.

*Hint*: Strings have a method called `startswith`, which can be used to
check if a string startswith another string. For example:

    >>> 'ababaaba'.startswith('aba')
    True

You may modify the following class definition in any way you like.

    class IndexOf:
        def __init__(self, substr, string):
            self.string = string
            self.substr = substr
        "*** YOUR CODE HERE ***"

<solution>

There are many ways to solve this question. We will present two ways:
1) by using an `__iter__` and `__next__` method; and 2) by implementing
`__iter__` as a generator function.

Here is a solution for using `__iter__` and `__next__`:

    class IndexOf:
        def __init__(self, substr, string):
            self.string = string
            self.substr = substr
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            while self.index < len(self.string) \
                  and not self.string[self.index:].startswith(self.substr):
                self.index += 1
            if self.index >= len(self.string):
                raise StopIteration
            elif self.string[self.index:].startswith(self.substr):
                answer = self.index
                self.index += 1
                return answer

Again, there are many variants to this, but the solutions should all
have the following components:

* Have a way to keep track of the current index (`self.index`)
* Raise a `StopIteration` error if the index exceeds the length of the
  string. This is how Python will know that the iterator stops.
* Move down `self.string`, one character at a time.
    * If the suffix of `self.string` starting at the current index does
      not start with `self.substr`, move down `self.string` until this
      is the case. For example, if we are at index 1 in our string,
      then the suffix starting at index 1 is `self.string[1:] =
      'babaaba'`.
    * If the suffix of `self.string` starting at the current index
      starts with `self.substr`, then return that index.

The second way to solve this is to make `__iter__` a generator
function:

    class IndexOf:
        def __init__(self, substr, string):
            self.string = string
            self.substr = substr

        def __iter__(self):
            index = 0
            while index < len(self.string):
                if self.string[index:].startswith(self.substr):
                    yield index
                index += 1

Recall that if a function uses a `yield` statement, it is considered by
Python to be a generator function. When a generator function is called,
it will **return a generator object**. That means when `__iter__` is
called, it will return a generator object.

The generator itself works as follows:
1. Move down `self.string`, one character at a time, while keeping
   track of each index.
2. If the suffix starting at the current index starts with
   `self.substr`, yield that index.

Once the while loop terminates, the generator will implicitly raise a
`StopIteration`, so there is no reason to write `raise StopIteration`.

</solution>

Streams
-------

<question>


Given the following function that returns a stream, what are the first
5 elements of the stream?

    (define (my-stream)
        (cons-stream 2
            (add-stream (my-stream) (scale-stream 2 (my-stream)))))

<solution>

    2, 6, 18, 54, 162

First, we write down our stream, with variables filling in the values
we don't know:

    s = 2 a b c d

Notice that, to compute the rest, we add together two streams: the
original stream, plus the original stream scaled by 2. This looks like
this:

    s = 2 | a b  c  d
    ------------------
          | 2 a  b  c
        + | 4 2a 2b 2c
    ------------------

We go ahead and add up the first column to get 2 + 4 = 6. Now we know
that `a = 6`. We can use this new information to calculate `b = a + 2a
= 6 + 2(6) = 18`. We continue this process to get the remaining
elements:

    s = 2 | a b  c  d
    ------------------
          | 2 a  b  c
        + | 4 2a 2b 2c
    ------------------
          | 6 18 54 162

</solution>

<question>

Implement a function `num-stream` that returns a Stream whose elements
have the following pattern:

    1, 1, 2, 1, 2, 3, 1, 2, 3, 4, ...
    _  ____  _______  __________

A skeleton has been provided:

    (define (num-stream)
        (define (helper i j)
            (cons-stream ______
                _______________
                _______________
                _______________
        (helper ______ ______)
    )

<solution>

First, notice the pattern of the sequence:

    1, 1, 2, 1, 2, 3, 1, 2, 3, 4, ...
    _  ____  _______  __________
    1  2     3        4

We can use `i`  to keep track of which block we're in and use `j` to
keep track of where we are in that block:

    s: 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, ...
       _  ____  _______  __________
    i: 1  2  2  3  3  3  4  4  4  4
    j: 1  1  2  1  2  3  1  2  3  4

It follows that `j` should never be greater than `i`. With this, we can
complete our solution:

    (define (num-stream)
        (define (helper i j)
            (cons-stream j
                (if (>= j i) (helper (+ i 1) 1)
                             (helper (i (+ j 1))))))
        (helper 1 1)
    )

In the rest of the stream, when `j >= i`, then `i` should move onto the next
block (`(+ i 1)`), and `j` should restart to 1 (since it's the start of
the new block).

</solution>

</block contents>
