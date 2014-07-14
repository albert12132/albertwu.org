~ title: Control Structures
~ level: exam

<block references>
* [Lecture: Control](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/04_1pp.pdf)
* [Lab 2](http://inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab02/lab02.php)
* [Discussion 2](http://inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion02.pdf)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

The following code is loaded into the Python interpreter

    def is_even(x):
        if x % 2 == 0:
            print('even')
        print('odd')
        return x - 1

    def branch(x):
        if x > 5:
            print('one')
        elif x > 0:
            print('two')
        if x > 10:
            print('three')
        else:
            print('four')
        return x + 5

What would Python print for the following lines?

<prompt>
    >>> a = is_even(4)
    even
    odd
    >>> b = branch(20)
    one
    three
    >>> c = branch(3)
    two
    four
    >>> d = is_even(is_even(5))
    odd
    even
    odd
    >>> e = branch(branch(3))
    two
    four
    one
    four
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `is_ascending`, which takes in a number `n`.
`is_ascending` returns `True` if the one's digit of `n` is less than or
equal to the ten's digit, and the ten's digit is less than or equal to
the hundred's digit, and so on. In other words, the digits of the
number going from right to left must be in ascending order.

    def is_ascending(n):
        """Returns True if the digits of N are in ascending order.

        >>> is_ascending(321)
        True
        >>> is_ascending(123)
        False
        >>> is_ascending(4432221)
        True
        >>> is_ascending(5492)
        False
        >>> is_ascending(5420)
        True
        """
        "*** YOUR CODE HERE ***"

<solution>

    def is_ascending(n):
        largest = 0
        while n > 0:
            ones = n % 10
            if ones < largest:
                return False
            largest = ones
            n = n // 10
        return True

</solution>

<question>

Implement a function `count_one`, which takes in a number `n`, and
returns the number of ones in the digits of `n`.

    def count_one(n):
        """Counts the number of 1s in the digits of n

        >>> count_one(7007)
        0
        >>> count_one(123)
        1
        >>> count_one(161)
        2
        >>> count_one(1)
        1
        """
        "*** YOUR CODE HERE ***"

<solution>

    def count_one(n):
        count = 0
        while n > 0:
            if n % 10 == 1:
                count += 1
            n = n // 10
        return count

</solution>

<question>

Implement a function `total_one`, which takes in a number `n`, and
returns the number of ones in the digits of all numbers from 1 to `n`.

**Hint**: You can use the `count_one` function from above.

    def total_ones(n):
        """Returns number of 1s in the digits of all numbers from 1 to
        n.

        >>> total_ones(10) # 1, 10 -> two 1s
        2
        >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
        8
        >>> total_ones(21)
        13
        """
        "*** YOUR CODE HERE ***"

<solution>

    def total_ones(n):
        i, total = 1, 0
        while i <= n:
            total += count_one(i)
            i += 1
        return total

</solution>

</block contents>
