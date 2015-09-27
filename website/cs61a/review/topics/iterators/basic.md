~ title: Iterators and Generators
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1zqKEmNFG90YUoBtFvEX5nsMURhrR5fXQz36tXKVECb0/edit)
</block references>

<block notes>
</block notes>

<block contents>

Iterators: Conceptual questions
-------------------------------

<quesiton>

Given any object `obj`, what special method will `iter(obj)` call? What
type of object will it return?

<solution>

The built-in Python function `iter` will implicitly call
`obj.__iter__`, a method. This method will return an **Iterator
object**, which is any object that has a `__next__` method.

</solution>

<question>

What is wrong with the following code?

    >>> obj = SomeObj()
    >>> i = iter(obj)
    >>> next(obj)

<solution>

`obj` is not necessarily an iterator, so you should not call `next` on it.
`next` should be called on `i` instead.

**NOTE:** even if the `__iter__` method of `SomeObj` returns `self`,
you still should not call `next` on `obj`. This is to protect
abstraction barriers.

</solution>

Iterators: Code-Writing Questions
---------------------------------

<question>

Write an iterator for a Fibonacci class. The iterator should return the
next Fibonacci number every time `next` is called on it.

    class Fibonacci:
        """Doctests

        >>> f = Fibonacci()
        >>> i = iter(f)
        >>> next(i)
        0
        >>> next(i)
        1
        >>> next(i)
        1
        >>> next(i)
        2
        """
        "*** YOUR CODE HERE ***"

<solution>

    class Fibonacci:
        def __init__(self):
            self.cur, self.next = 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            tmp = self.cur
            self.cur, self.next = self.next, self.next + self.cur
            return tmp

</solution>

Generators: Conceptual questions
--------------------------------

<question>

Given the following generator function, what will the call to `gen()`
return?

    def gen():
        start = 0
        while start != 10:
            yield start
            start += 1

<solution>

`gen()` will return a generator object, NOT the number 0. None of the
code inside the generator function will be executed.

</solution>

<question>

When does a generator raise a `StopIteration` exception?

<solution>

When the end of the generator function is reached.

</solution>

Generators: Code-Writing questions
----------------------------------

<question>

Write a generator function `map_gen` that takes a one-argument function
and an iterator as arguments. The return result should be a generator
whose elements are the elements of the iterator, but with the function
mapped onto them.

    def map_gen(fn, iter1):
        """Doctests

        >>> i = iter([1, 2, 3, 4])
        >>> fn = lambda x: x**2
        >>> m = map_gen(fn, i)
        >>> next(m)
        1
        >>> next(m)
        4
        >>> next(m)
        9
        >>> next(m)
        16
        >>> next(m)
        Traceback (most recent call last):
          ...
        StopIteration
        """
        "*** YOUR CODE HERE ***"

<solution>

    def map_gen(fn, iter1):
        for elem in iter1:
            yield fn(elem)

Since `iter1` is an iterator, we can iterate over it in a for loop.

</solution>

<question>

Write another iterator for a Fibonacci class. Like before, the iterator
should return the nxt Fibonacci number every time `next` is called on
it. This time, write the iterator using a generator function.

    class Fibonacci:
        """Doctests

        >>> f = Fibonacci()
        >>> i = iter(f)
        >>> next(i)
        0
        >>> next(i)
        1
        >>> next(i)
        1
        >>> next(i)
        2
        """
        "*** YOUR CODE HERE ***"

<solution>

    class Fibonacci:
        def __iter__(self):
            cur, next = 0, 1
            while True:
                yield cur
                cur, next = next, cur + next

The generator in the `__iter__` method can keep track of state, so we
don't need to initialize anything. We also don't need to write a
`__next__` method, since the `__iter__` method is not returning `self`.

</solution>

</block contents>
