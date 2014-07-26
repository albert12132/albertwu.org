~ title: Interfaces
~ level: basic

<block references>
[Lecture: Multiple representations](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/20-Interfaces_1pps.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Special methods provide a common interface across many different types
of objects. List some special methods and the contexts in which they
are used.

<solution>

Here are some examples:

* `__init__`: used to create instances of a class.
* `__len__`: called by the built-in `len` to calculate the "length" of
  an object.
* `__getitem__`: used with square brackets (`[ ]`) to retrieve an
  element at a certain index.
* `__repr__`: returns a string representation of an object that is
  "Python readable" (could be typed into Python to replicate the same
  object).
* `__str__`: returns a string representation of an object that is human
  readable".
* `__eq__`: called when the `==` operator is used. Determines how to
  check if two objects are equal.
* `__add__`: called when the `+` operator is used.

</solution>

<question>

What do the underscores (e.g.  `__init__`) in special method names do?

<solution>

Functionally, the underscores don't do anything -- they are just part
of the method name. However, when Python looks for a certain special
method, it expects the name to have those underscores, so you can't
leave them out!

</solution>

What would Python print?
------------------------

For the following questions, assume the following class has been
defined in the interpreter:

    class Box(object):
        def __init__(self, item):
            self.item = item
            print('Created a box!')

        def __getitem__(self, index):
            item, self.item = self.item, None
            return item

        def __setitem__(self, index, item):
            self.item = item

        def __repr__(self):
            return 'Box(' + repr(self.item) + ')'

        def __str__(self):
            rep = self.item if self.item is not None else ''
            return '|_{}_|'.format(rep)

<question>

<prompt>
    >>> d = Box(4)
    Created a box!
    >>> repr(d)
    'Box(4)'
    >>> str(d)
    '|_4_|'
    >>> d
    Box(4)
    >>> d[0]
    4
    >>> str(d)
    '|__|'
    >>> d[1000] = 1
    >>> str(d)
    '|_1_|'
</prompt>

<question>

<prompt>
    >>> a = Box(Box(4))
    Created a box!
    Created a box!
    >>> str(a)
    '|_|_4_|_|'
    >>> a[0][0]
    4
    >>> str(a)
    '|__|'
    >>> a[0] = a
    >>> repr(a)
    RuntimeError: maximum recursion depth...
</prompt>

Code-Writing questions
----------------------

<question>

Implement a class called `DoubleList`, such that its doctest passes.

    class DoubleList(object):
        """See doctests for behavior.

        >>> d = DoubleList([1, 2, 3])
        >>> repr(d)
        'DoubleList([1, 2, 3])'
        >>> str(d)
        '[1, 1, 2, 2, 3, 3]'
        >>> d[2]
        2
        >>> d[3]
        2
        >>> d[4]
        3
        >>> len(d)
        6
        >>> d.append(4)
        >>> str(d)
        '[1, 1, 2, 2, 3, 3, 4, 4]'
        """

<solution>

    class DoubleList(object):
        def __init__(self, lst):
            self.lst = lst

        def append(self, item):
            self.lst.append(item)

        def __repr__(self):
            return 'DoubleList(' + repr(self.lst) + ')'

        def __str__(self):
            rep = '['
            for elem in self.lst:
                rep += '{0}, {0}, '.format(elem)
            return rep[:-2] + ']'

        def __len__(self):
            return 2 * len(self.lst)

        def __getitem__(self, index):
            return self.lst[index // 2]

</solution>

</block contents>
