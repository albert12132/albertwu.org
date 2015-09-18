~ title: Linked Lists
~ level: basic

<block references>
* [Lecture: Sequences](http://cs61a.org/assets/slides/13-Sequences_1pps.pdf)
</block references>

<block notes>
We will be using the following implementation of immutable linked
lists. Keep in mind that your code should not depend on the assumption
that links are implemented as lists -- preserve data abstraction!

    empty = None

    def link(first, rest=empty):
        return [first, rest]

    def first(s):
        return s[0]

    def rest(s):
        return s[1]
</block notes>

<block contents>

Concept Questions
-----------------

<question>

What type of object can `first` be (e.g.  int, string, function, etc.)?
What type of object can `rest` be?

<solution>

`first` can be any type of object, even a linked list. `rest` can only be a
linked list.

</solution>

<question>

Which of the following are valid linked list constructors?

1. `link(1, 3)`
2. `link(1, None)`
3. `link(1, link(4, empty))`
4. `link(1, empty)`
5. `link()`

<solution>

The correct answers are in bold:

1. `link(1, 3)`
2. `link(1, None)`
3. **`link(1, link(4, empty))`**
4. **`link(1, empty)`**
5. `link()`

</solution>

<question>

Construct a linked list that contains the following elements:

    1, 3, lambda x: x, 'hi'

<solution>

    link(1, link(3, link(lambda x: x, link('hi', empty))))

</solution>

<question>

What is the third element of the following link?

    link('this', link(link('is', link('a', empty)), link('question', empty)))

<solution>

`'question'`

</solution>

<question>

What is the length of the linked list in the previous question (i.e.
how many elements are in the linked list, not including the elements of
nested linked lists?

<solution>

3

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> r = link(1, link(2, link(3, empty)))
    >>> first(r)
    1
    >>> rest(r)
    (2, (3, None))
    >>> rest(rest(r))
    (3, None)
    >>> first(rest(r))
    2
    >>> first(rest(rest(r)))
    3
</prompt>

Code-Writing Questions
----------------------

<question>

Implement a function `link_to_list` that takes a linked as an argument,
and returns a list that contains the same elements as the linked list.

    def link_to_list(lst):
        """Returns a list that contains the same elements as the
        linked list.

        >>> r = link(1, link(2, link(3, empty)))
        >>> link_to_tup(r)
        (1, 2, 3)
        """
        "*** YOUR CODE HERE ***"

<solution>

A recursive version:

    def link_to_list(lst):
        if lst == empty:
            return []
        return [first(lst)] + link_to_list(rest(lst))

An iterative version:

    def link_to_list(lst):
        new = []
        while lst != empty:
            new += [first(lst)]
            lst = rest(lst)
        return new

</solution>

<question>

Implement a function `map_link` that maps a function `f` onto each element of
a linked list.

    def map_link(lst, f):
        """Maps f onto each element in the linked list.

        >>> r = link(1, link(2, link(3, empty)))
        >>> link_to_list(map_link(r, lambda x: x**2))
        [1, 4, 9]
        """
        "*** YOUR CODE HERE ***"

<solution>

A recursive version:

    def map_link(lst, f):
        if lst == empty:
            return empty
        return link(f(first(lst)), map_link(rest(lst), f))

An iterative version:

    def map_link(lst, f):
        new = empty
        while lst != empty:
            new = link(f(first(lst)), new)
            lst = rest(lst)
        while new != empty:
            lst = link(first(new), lst)
            new = rest(new)
        return lst

</solution>
</block contents>
