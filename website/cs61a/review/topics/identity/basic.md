~ title: Identity vs. Equality
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1PC5Yw-AxxOyTaPhZ-kJ0JvVMwaVCyVmBmWdiNqGZeVo/edit#slide=id.g5b71800b6_0_281)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What condition must be satisfied for the expression `a is b` to be
`True`?

<solution>

`a` and `b` must reference the same physical object in memory.

</solution>

<question>

What special method determines if `a == b` to be `True`?

<solution>

In each class, the `__eq__` determines if two objects are equivalent
(but not identical). For user-defined types (i.e.  classes), you can
implement your own `__eq__` method!  Otherwise, the default `__eq__`
for user-defined types behaves the same way as `is`.

</solution>

<question>

For built-in types, if `a is b` is `True`, is `a == b` guaranteed to be
`True`?

<solution>

Yes. in other words, a built-in object is, by definition, equivalent
with itself. However, for user-defined types, you are able to break
this property!

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> s = [1, 2, 3, 4]
    >>> s == [1, 2, 3, 4]
    True
    >>> s is [1, 2, 3, 4]
    False
    >>> [1, 2, 3, 4] is [1, 2, 3, 4]
    False  # 2 separate objects in memory!
    >>> a = s
    >>> a is s
    True
    >>> a[1:] is s[1:]
    False  # slicing always creates new objects in memory
</prompt>

<question>

<prompt>
    >>> s = (1, 2, 3, 4)
    >>> s is (1, 2, 3, 4)
    False  # Immutability has nothing to do with identity
    >>> s == [1, 2, 3, 4]
    False  # a tuple cannot be equivalent to a list
    >>> 'hello' == 'hello'
    True
    >>> 'hello' is 'hello'
    True   # strings are special -- Python only creates one copy of a string literal in memory
</prompt>

</block contents>
