~ title: Lists
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1skXespdgvJRzwUmW1oSxHP54_bKkJPGkF1-N9poNRt4/edit#slide=id.p)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

<question>

<prompt>
    >>> L = [1, 2, 3, 4]
    >>> L[0]
    1
    >>> L[100]
    IndexError
    >>> L[-1]
    4
    >>> L[2] = 100
    >>> L
    [1, 2, 100, 4]
</prompt>

<question>

<prompt>
    >>> L = [1, 2, 3, 4]
    >>> L[1:3]
    [2, 3]
    >>> L[:2]
    [1, 2]
    >>> L[1:]
    [2, 3, 4]
    >>> L[:]
    [1, 2, 3, 4]
    >>> L[0:3:2]
    [1, 3]
    >>> L[::-1]
    [4, 3, 2, 1]
</prompt>

<question>

<prompt>
    >>> L = [1, 2, 3, 4]
    >>> [1, 2] + [3, 4]
    [1, 2, 3, 4]
    >>> [1, 2] * 2
    [1, 2, 1, 2]
    >>> L.append(5)
    >>> L
    [1, 2, 3, 4, 5]
    >>> L.extend([6, 7])
    >>> L
    [1, 2, 3, 4, 5, 6, 7]
    >>> L.index(5)
    4
    >>> L.remove(3)
    >>> L
    [1, 2, 4, 5, 6, 7]
    >>> L.pop()
    7
    >>> L
    [1, 2, 4, 5, 6]
</prompt>

Code-Writing questions
----------------------

<question>

Implement a function `reverse` that takes a list as an argument and
reverses the list. You should mutate the original list, without
creating any new lists. Do NOT return anything.

    def reverse(L):
        """Reverses L in place (i.e. doesn't create new lists).

        >>> L = [1, 2, 3, 4]
        >>> reverse(L)
        >>> L
        [4, 3, 2, 1]
        """
        "*** YOUR CODE HERE ***"

<solution>

    def reverse(L):
        for i in range(len(L)//2):
            L[i], L[-i-1] = L[-i-1], L[i]

</solution>

<question>

Implement a function `map_mut` that takes a list as an argument and
maps a function `f` onto each element of the list. You should mutate
the original lists, without creating any new lists. Do NOT return
anything.

    def map_mut(f, L):
        """Mutatively maps f onto each element in L.

        >>> L = [1, 2, 3, 4]
        >>> map_mut(lambda x: x**2, L)
        >>> L
        [1, 4, 9, 16]
        """
        "*** YOUR CODE HERE ***"

<solution>

    def map_mut(f, L):
        for i in range(len(L)):
            L[i] = f(L[i])

</solution>

</block contents>

