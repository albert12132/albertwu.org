~ title: Mutable Trees
~ level: exam

<block references>
* [Albert's and Robert's slides](https://docs.google.com/presentation/d/1_Z2YtfB-tjhD-9FO2KJSOs-wAeIjOfsKUzTz9beCOhw/edit)
</block references>

<block notes>
We will be using the OOP implementation of `Tree`s from lecture,
found
[here](http://www-inst.eecs.berkeley.edu/~cs61a/sp13/slides/25.py)
</block notes>

<block contents>

Trees
-----

<question>

Implement a function `equal` which takes two trees and returns `True`
if they satisfy all the following conditions:

* The data of both Trees are equal
* The Trees have the same number of children
* All corresponding pairs of sub-Trees are also `equal`

    def equal(t1, t2):
        """Returns Tree if t1 and t2 are equal trees.

        >>> t1 = Tree(1,
        ...           [Tree(2, [Tree(4)]),
        ...            Tree(3)])
        >>> t2 = Tree(1,
        ...           [Tree(2, [Tree(4)]),
        ...            Tree(3)])
        >>> equal(t1, t2)
        True
        >>> t3 = Tree(1,
        ...           [Tree(2),
        ...            Tree(3, [Tree(4)])])
        >>> equal(t1, t3)
        False
        """
        "*** YOUR CODE HERE ***"

<solution>

    def equal(t1, t2):
        if t1.entry != t2.entry:
            return False
        elif len(t1.subtrees) != len(t2.subtrees):
            return False
        else:
            return all(equal(child1, child2) for child1, child2
                       in zip(t1.subtrees, t2.subtrees))

</solution>

<question>

Implement a function `size` that returns the number of elements in a
given Tree.

    def size(t):
        """Returns the number of elements in a tree.

        >>> t1 = Tree(1,
        ...           [Tree(2, [Tree(4)]),
        ...            Tree(3)])
        >>> size(t1)
        4
        """
        "*** YOUR CODE HERE ***"

<solution>

    def size(t):
        return 1 + sum([size(child) for child in t.subtrees])

</solution>

<question>

Implement a function `height`, which returns the height of a Tree. The
*height* of a tree is defined as the number of branches from the
*root* to the bottom-most *leaf* of the Tree.

By definition, a leaf has a height of 0, since there are 0 branches
from the root to the root.

    def height(t):
        """Returns the height of the tree.

        >>> leaf = Tree(1)
        >>> height(leaf)
        0
        >>> t1 = Tree(1,
        ...           [Tree(2, [Tree(4)]),
        ...            Tree(3)])
        >>> height(t1)
        2
        """
        "*** YOUR CODE HERE ***"

<solution>

    def height(t):
        if len(t.subtrees) == 0:
            return 0
        return 1 + max([height(child) for child in t.subtrees])

</solution>

<question>

Implement a function `same_shape`, which takes two `Tree`s and returns
True if the trees have the same structure, but not necessarily the same
entries.

    def same_shape(t1, t2):
        "*** YOUR CODE HERE ***"

<solution>

    def same_shape(t1, t2):
        if not t1.subtrees or not t2.subtrees:
            return not t1.subtrees and not t2.subtrees
        elif len(t1.subtrees) != len(t2.subtrees):
            return False
        for i in range(len(t1.subtrees)):
            if not same_shape(t1.subtrees[i], t2.subtrees[i]):
                return False
        return True

</solution>

<question>

Implement a function `sprout_leaves`, which takes a `Tree` and a list
of values. For every leaf of the `Tree`, mutate it so that it has a
list of branches where the items are the elements in the list of
values.

    def sprout_leaves(t, vals):
        "*** YOUR CODE HERE ***"

<solution>

    def sprout_leaves(t, vals):
        if not t.subtrees:
            t.subtrees = [Tree(v) for v in vals]
        else:
            for branch in t.subtrees:
                sprout_leaves(branch, vals)

</solution>

<question>

Implement a function `prune_leaves`, which takes a `Tree` and a list
of values. For every leaf of the `Tree`, remove it if its entry is in
the list of values.

    def prune_leaves(t, vals):
        "*** YOUR CODE HERE ***"

<solution>

    def prune_leaves(t, vals):
        if not t.subtrees:
            if t.entry not in vals:
                return t
            else:
                return None
        new_branches = [prune_leaves(branch, vals) for branch in t.subtrees]
        t.subtrees = [b for b in new_branches if b is not None]
        return t

</solution>

Binary Search Trees
-------------------

<question>

Implement two functions, `max_bst` and `min_bst`, which take a binary
search tree and returns the maximum and minimum values, respectively.

    def max_bst(b):
        "*** YOUR CODE HERE ***"

<solution>

    def max_bst(b):
        if b.right.is_empty:
            return b.entry
        return max_bst(b.right)

</solution>

    def min_bst(b):
        "*** YOUR CODE HERE ***"

<solution>

    def min_bst(b):
        if b.left.is_empty:
            return b.entry
        return min_bst(b.left)

</solution>

<!---

<question>

Implement a function `valid_bst`, which takes a Tree object and
determines if it is a valid **binary search tree**. If the Tree is a
valid BST, then return True; if it is invalid, return False.

**Hint**: Recall that a binary search tree is a binary Tree, with these
added constraints:

* Every item in the left branch must be less than the entry
* Every item in the right branch must be greater than the entry

You may assume two functions, `max_tree` and `min_tree` are already
defined.

    def valid_bst(b):
        """If B is a valid BST, return True; else return False.

        >>> b1 = Tree(2,
        ...           Tree(1),
        ...           Tree(4, Tree(3)))
        >>> valid_bst(b1)
        True
        >>> invalid = Tree(2,
        ...                Tree(3),
        ...                Tree(4))
        >>> valid_bst(invalid)
        False
        """
        "*** YOUR CODE HERE ***"

<solution>

    def valid_bst(b):
        """The solution could be a lot more concise, but is written out
        to be clearer."""
        if b is None:
            return True
        elif not valid_bst(b.left) or not valid_bst(b.right):
            return False
        elif b.left and max_tree(b.left) >= t.entry:
            return False
        elif b.right and min_tree(b.right) <= t.entry:
            return False
        else:
            return True

</solution>

-->

<question>

Implement the function `contains`, which takes a binary search tree and
an item, and returns True if the binary search tree contains the item,
and False if it doesn't.

    def contains(b, item):
        """Returns True if B contains ITEM.

        >>> b1 = Tree(2,
        ...           Tree(1),
        ...           Tree(4, Tree(3)))
        >>> contains(b1, 4)
        True
        >>> contains(b1, 8)
        False
        """
        "*** YOUR CODE HERE ***"

<solution>

    def contains(b, item):
        if b is None:
            return False
        elif b.entry == item:
            return True
        elif b.entry > item:
            return contains(b.left, item)
        elif b.entry < item:
            return contains(b.right, item)

</solution>

<question>

Implement the function `in_order`, which takes a binary search tree,
and returns a list containing its items from smallest to largest. In
computer science, this is known as an **in-order traversal**.

    def in_order(b):
        """Returns the items in B, a binary search tree, in sorted
        order.

        >>> b1 = Tree(2,
        ...           Tree(1),
        ...           Tree(4, Tree(3)))
        >>> in_order(b1)
        [1, 2, 3, 4]
        >>> singleton = Tree(4)
        >>> in_order(singleton)
        [4]
        """
        "*** YOUR CODE HERE ***"

<solution>

    def in_order(b):
        if b is None:
            return []
        else:
            left = in_order(b.left)
            right = in_order(b.right)
            return left + [b.entry] + right

</solution>

<question>

Implement a function `nth_largest`, which takes a **binary search
tree** and a number `n` (greater than or equal to 1), and returns the
`nth` largest item in the tree. For example, `nth_largest(b, 1)` should
return the largest item in `b`. If `n` is greater than the number of
items in the tree, return None.

**Hint**: You can assume there is a `size` function that returns the
number of elements in a given tree.

    def nth_largest(b, n):
        """Returns the Nth largest item in T.

        >>> b1 = Tree(2,
        ...           Tree(1),
        ...           Tree(4, Tree(3)))
        >>> nth_largest(b1, 1)
        4
        >>> nth_largest(b1, 3)
        2
        >>> nth_largest(b1, 4)
        1
        """
        "*** YOUR CODE HERE ***"

<solution>

    def nth_largest(b, n):
        if b is None:
            return None
        right = size(b.right)
        if right == n - 1:
            return b.entry
        elif right > n - 1:
            return nth_largest(b.right, n)
        elif right < n - 1:
            return nth_largest(b.left, n - 1 - right)

</solution>

</block contents>
