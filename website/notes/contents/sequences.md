~ title: Tuples, Lists, and Rlists

Introduction
------------

Sequences are data structure (objects that organize data) that have
two properties:

1. Finite Length
2. Item selection (through zero-based indexing)

Recall Python's two built-in sequence types: tuples and lists. Both
these data types support these properties:

    >>> tup = (1, 2, 3)
    >>> len(tup)
    3
    >>> tup[0]
    1
    >>> lst = [1, 2, 3]
    >>> len(lst)
    3
    >>> lst[0]

Lists have the additional benefit of being *mutable*, meaning their
contents can be modified after creation. Contrast this with tuples,
which are *immutable* (contents cannot be modified after creation).

### List and Tuple Methods

Here are some tuple and list methods:

* tuples:
    * `count(item)`: returns the number of times `item` appears in the
      tuple.
    * `index(item)`: returns the first index at which `item` appears
* lists:
    * `append(item)`: adds `item` to the end of the original list.
      Returns `None`
    * `extend(iterable)`: adds elements in `iterable` to the end of
      the original list
    * `pop()`: with no argument, removes the last item in the list and
      returns it. With an index, it deletes the item at the given
      `index` and returns it.
    * `count(item)`: same as the tuple version
    * `index(item)`: same as tuple version
    * `insert(index, item)`: inserts `item` before the `index`.
      Mutates the original list.
    * `remove(item)`: removes the first occurrence of `item`.
    * `reverse()`: reverses the list in place (does not return a new
      list)
    * `sort()`: sorts the list in place (does not return a new list)

As you can see, lists support many more methods, mostly due to the
fact that they are mutable.

### Why use tuples?

At this point, you might be wondering why we bother using tuples at
all. 
