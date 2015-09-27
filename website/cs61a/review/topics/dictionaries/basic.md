~ title: Dictionaries
~ level: basic

<block references>
* [Albert and Robert's
  slides](https://docs.google.com/presentation/d/1skXespdgvJRzwUmW1oSxHP54_bKkJPGkF1-N9poNRt4/edit#slide=id.ga2e4b373c_0_5)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What type of objects can be used as keys for dictionaries? What type of
objects can be used as values?

<solution>

Any **immutable** object can be used as a key -- this includes numbers,
strings, and tuples. Mutable objects, such as lists and dictionaries,
are not allowed to be used as keys.  Anything can be used as a value,
however.

</solution>

<question>

How many objects can a single key map to?

<solution>

A single key can only map on to one value. That value can, however, be
a sequence like a tuple or a list, so you can effectively map to
multiple things (but it still only counts as one value).

</solution>

<question>

Are dictionaries ordered?

<solution>

Python dictionaries are not ordered. If you were to iterate through the
dictionary, the order in which you iterate through them is not
necessarily the order in which you added them.

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> logins = {'albert': 'cs61a-tg'}"
    >>> logins['albert']
    'cs61a-tg'
    >>> logins['cs61a-tg']
    KeyError
    >>> logins['allen'] = None
    >>> len(logins)
    2
    >>> for elem in logins:
    ...     print(elem)
    allen
    albert  # not necessarily in that order
    >>> for key, value in logins.items():
    ...     print(key, value)
    allen None
    albert cs61a-tg # not necessarily in that order
</prompt>

</block contents>
