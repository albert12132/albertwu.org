~ title: Iterators and Generators
~ level: exam

<block references>
* [Lecture: Iterators](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/29-Iterators_1pps.pdf)
* [Lab 10](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab10/lab10.php)
</block references>

<block notes>
</block notes>

<block contents>

Iterators: Cross out the errors
-------------------------------

<question>

Cross out any incorrect or unnecessary lines. You should not need to
write any new lines to make the code work. Do not cross out any
doctests.

    class Naturals:
        """Doctests.

        >>> n = Naturals()
        >>> i = iter(n)
        >>> next(i)
        0
        >>> next(i)
        1
        >>> next(i)
        2
        """
        def __init__(self):
            self.cur = 0

        def __iter__(self):
        def __iter__(self, start):
            self.cur = start
            while True:
                self.cur += 1
                return self.cur
            return NatIter(self.cur)

        def __next__(self):
            tmp = self.cur
            self.cur += 1
            return tmp

    class NatIter(Iterator)
    class NatIter:
        def __init__(self):
        def __init__(self, start):
            self.cur = start

        def __iter__(Self):
            return self

        def __next__(self):
            tmp = self.cur
            self.cur += 1
            return tmp

<solution>

    class Naturals:
        """Doctests.

        >>> n = Naturals()
        >>> i = iter(n)
        >>> next(i)
        0
        >>> next(i)
        1
        >>> next(i)
        2
        """
        def __init__(self):
            self.cur = 0

        def __iter__(self):
            return NatIter(self.cur)

    class NatIter:
        def __init__(self, start):
            self.cur = start

        def __iter__(Self):
            return self

        def __next__(self):
            tmp = self.cur
            self.cur += 1
            return tmp

</solution>

Iterators: Fill in the blanks
-----------------------------

<question>

Fill in the implementation of the iterator for the Rlist class.

    class Rlist:
        """Doctests

        >>> r = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
        >>> for item in r:
        ...     print(item)
        1
        2
        3
        4
        """
        class EmptyList:
            pass

        empty = EmptyList()

        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest
            self.cur = self

        def __iter__(self):
            return ______

        def __next__(self):
            if self.cur == ______:
                raise ______
            else:
                result = ______
                ______ = self.cur.rest
                return result

<solution>

    class Rlist:
        class EmptyList:
            pass

        empty = EmptyList()

        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest
            self.cur = self

        def __iter__(self):
            return self

        def __next__(self):
            if self.cur == Rlist.empty:
                raise StopIteration
            else:
                result = self.curr.first
                self.cur = self.cur.rest
                return result

Since we are writing a `__next__` method for the `Rlist` class,
the `Rlist` class is technically an iterator. As such, its
`__iter__` method can just return `self`. In the
`__next__` method, if the current Rlist is empty, we must raise a
`StopIteration` exception. Otherwise, we will return the *element*
(`self.curr.first`) at the current node, and change our point
(`self.curr`) to the next node in the Rlist (`self.cur.rest`)."""

</solution>

Generators: Code-writing questions
----------------------------------

<question>

Write a generator function `zip` that takes two iterators and yields
elements of thsoe iterators in pairs (see the doctests for
clarification).  `zip` will stop once one of the input iterators stops.

    def zip(iter1, iter2):
        """Doctests

        >>> i1 = iter([1, 2, 3, 4])
        >>> i2 = iter([5, 6, 7])
        >>> gen = zip(i1, i2)
        >>> for elem in gen:
        ...     print(elem)
        (1, 5)
        (2, 6)
        (3, 7)
        """
        "*** YOUR CODE HERE ***"

<solution>

    def zip(iter1, iter2):
        while True:
            try:
                yield (next(iter1), next(iter2))
            except StopIteration:
                break

</solution>

Generators: Fill in the blank
-----------------------------

<question>

Fill in the implementation of `pascals`, a generator function that
yields successive lines of Pascal's triangle every time `next` is
called.  Each line should be represented as a Python list.

**Hint**: a description of Pascal's triangle can be found
[here](http://en.wikipedia.org/wiki/Pascal's_triangle)

    def pascals():
        """Doctests

        >>> p = pascals()
        >>> next(p)
        [1]
        >>> next(p)
        [1, 1]
        >>> next(p)
        [1, 2, 1]
        >>> next(p)
        [1, 3, 3, 1]
        >>> next(p)
        [1, 4, 6, 4, 1]
        """
        curr = ______
        while True:
            yield curr
            i, new = 1, [1]
            while ______:
                new.append(______ + ______)
                i += 1
            new.append(1)
            curr = new

<solution>

    def pascals():
        curr = [1]
        while True:
            yield curr
            i, new = 1, [1]
            while i < len(curr):
                new.append(curr[i-1] + curr[i])
                i += 1
            new.append(1)
            curr = new

</solution>

</block contents>
