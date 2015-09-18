~ title: Streams
~ level: basic

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

What are the advantages to using a stream as opposed to a regular
list?

<solution>

A stream can be used to "store" infinite amounts of data. Because the
data is not computed until you need it, you can use memory more
efficiently.

</solution>

<question>

The signature of the Stream constructor is `Stream(item, compute_rest)`
-- `compute_rest` will be a function that computes the rest of the
Stream. How many arguments can `compute_rest` take? What type of object
must it return?

<solution>

`compute_rest` must take zero arguments, or else the `Stream.rest`
property method will not work. `compute_rest` must return another
Stream object.

</solution>

<question>

Given the following function, list the first 5 numbers in the Stream
that `my_stream()` returns.

    def my_stream():
        def compute_rest():
            return add_streams(integer_stream(),
                               map_stream(lambda x: 3*x,
                                          integer_stream()))
        return Stream(0, compute_rest)

<solution>

0, 4, 8, 12, 16

</solution>

Code-Writing questions
----------------------

<question>

Write a function `odd_stream()` that returns a stream of odd-numbered
integers, start from 1.

    def odd_stream():
        """Returns a Stream of odd numbers starting at 1.

        >>> s = odd_stream()
        >>> first_k_as_list(s, 5)
        [1, 3, 5, 7, 9]
        """
        "*** YOUR CODE HERE ***"


<solution>

    def odd_stream():
        def compute_rest():
            return map_stream(lambda x: x + 2, odd_stream())
        return Stream(1, compute_rest)

Let `s` be the result of calling `odd_Stream()`:

    s = 1,    3,        5,      7,    ...
      = 1, (1 + 2), (3 + 2), (5 + 2), ...

The rest of `s` is just the elements of `s`, but with 2 added to each
element.

</solution>

<question>

Write a function `reduce_first_k()` that reduces the first *k*
elements in a given Stream, using a given combiner. If the stream has
fewer than *k* elements, reduce all the elements in the stream.

    def reduce_first_k(s, k, combiner):
        """Reduces the first k elements in s with combiner.

        >>> s = integer_stream()
        >>> reduce_first_k(s, 4, lambda x, y: x + y)
        10
        >>> s1 = Stream(1, lambda: Stream(2))
        >>> reduce_first_k(s1, 4, lambda x, y: x + y)
        3
        "*** YOUR CODE HERE ***"

<solution>

    def reduce_first_k(s, k, combiner):
        total, s = s.first, s.rest
        while k > 1 and s != Stream.empty:
            total = combiner(total, s.first)
            s = s.rest
            k -= 1
        return total

We start the total with the first element of `s`. We keep iterating
until `k` is equal to 1, because we've already visited the first
element of `s` (so we only need to iterate `k - 1` times.

</solution>

</block contents>
