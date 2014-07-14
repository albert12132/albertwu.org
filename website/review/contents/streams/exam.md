~ title: Streams
~ level: exam

<block references>
* [Lecture: Streams](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30-Streams_1pps.pdf)
* [Lab 10](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab10/lab10.php)
</block references>

<block notes>
You can find the source code that contains the Stream class
[here](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/30.py).
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Given the following function, list the first 5 elements of the Stream
that is returned by `stream1()`.

    def stream1():
        def compute_rest():
            return add_streams(stream1(), stream1().rest)
        return Stream(0, lambda: Stream(1, compute_rest))

<solution>

0, 1, 1, 2, 3 (the Fibonacci numbers)

</solution>

<question>

Given the following function, list the first 5 elements of the Stream
that is returned by `stream2()`.

    def stream2():
        def compute_rest():
            return add_streams(stream2(), stream2())
        return Stream(1, compute_rest)

<solution>

1, 2, 4, 8, 16 (the powers of 2)

</solution>

Code-Writing questions
----------------------

<question>

Create a function `make_fact_stream`, which returns a Stream whose
*n*th element is *n*!  (factorial of *n*).

    def make_fact_stream():
        """Returns a Stream of factorials.

        >>> s = make_fact_stream()
        >>> s.first      # 0!
        1
        >>> s.rest.first # 1!
        1
        >>> s.rest.rest.first   # 2!
        2
        >>> s.rest.rest.rest.first  # 3!
        6
        """
        "*** YOUR CODE HERE ***"

**Hint**: This is similar to the `make_fib_stream()` function from
discussion. Try writing an iterative factorial function first, then
convert it into the Stream function.  You should also use a helper
function.

<solution>

    def make_fact_stream():
        return fact_help(0, 1)

    def fact_help(n, total)
        def rest():
            return fact_help(n + 1, total * (n + 1))
        return Stream(total, rest)

    # here's the iterative factorial we use to convert
    def infinite_fact():
        n, total = 0, 1
        while True:
            print(total)
            n, total = n + 1, total * n

</solution>

More practice problems
----------------------

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
