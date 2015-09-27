~ title: Map, filter, and friends
~ level: exam

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1skXespdgvJRzwUmW1oSxHP54_bKkJPGkF1-N9poNRt4/edit#slide=id.ga2e4b373c_0_10)
</block references>

<block notes>
**NOTE**: The questions in this seciton are **NOT** reflective of the
level of midterm -- they are much more difficult.  You should treat
these questions as extra for experts -- don't focus too much on these
questions!
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<prompt>
    >>> tup = (1, 2, 3)
    >>> pairs = ((1, 2), (3, 4))
    >>> tuple(map(lambda x: tuple(map(lambda y: x*y, tup)), tup))
    ((1, 2, 3), (2, 4, 6), (3, 6, 9))
    >>> tuple(map(lambda x: x*2, pairs))
    ((1, 2, 1, 2), (3, 4, 3, 4))
    >>> tuple(map(lambda x, y: (y, x), pairs))
    TypeError
    >>> tuple(map(lambda x, y: (y, x), tup, tup))
    ((1, 1), (2, 2), (3, 3))
    >>> tuple(map(lambda x, y: x + y, (1, 2, 3), (1, 2)))
    (2, 4)
    >>> tuple(filter(None, tup))
    (1, 2, 3)
</prompt>

<question>

<prompt>
    >>> from functools import reduce
    >>> reduce(lambda x, y: x + y, tup, 100)
    106
    >>> reduce(lambda x, y: (x, y), tup)
    ((1, 2), 3)
    >>> reduce(lambda x, y: y + x, "hello world!")
    '!dlrow olleh'
    >>> reduce(lambda x, y: x + y, map(lambda x: x**2, tup))
    14
    >>> tuple(map(reduce, (lambda x, y: x + y,)*4, pairs))
    (3, 7)
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `capitalize` that takes a string and capitalizes
words if they are at the start of a sequence. **Hint:** the
`capitalize` string method, which capitalizes the first character of a
string, may help you here.

    def capitalize(s):
        """Capitalizes words in the string if they are at the start of
        a sentence.

        >>> s = 'this is spot. see spot run.'
        >>> capitalize(s)
        'This is spot. See spot run.'
        """
        "*** YOUR CODE HERE ***"

<solution>

    def capitalize(s):
        return reduce(lambda x, y: x + ' ' + y,
                  map(lambda x, y: x.capitalize() if y.endswith('.') \\
                                                      else x,
                          s.split(),
                          ['.'] + s.split()))

</solution>

<question>

Implement `shuffle` that takes a sequence, splits it in two halves, and
interleaves the elements of both halves. The return value should be the
result of that interleave, and should be a list. **Note**: you may
assume the list is of even length.

    def shuffle(seq):
        """Splits seq in half and interleaves elements of both halves.

        >>> seq = [1, 2, 3, 4, 5, 6]
        >>> shuffle(seq)
        [1, 4, 2, 5, 3, 6]
        """
        "*** YOUR CODE HERE ***"

<solution>

    def shuffle(seq):
        return list(reduce(lambda x, y: x + y,
                           map(lambda x, y: [x, y],
                               seq[:len(seq)//2],
                               seq[len(seq)//2:])))

</solution>

</block contents>
