~ title: Trees
~ level: exam

<block references>
* [Lecture: Recursive Data](http://cs61a.org/assets/slides/20-Composition_1pps.pdf)
* [Lab 6](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab06/lab06.php)
* [Discussion 7](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion07.pdf)
</block references>

<block notes>
We will be using the OOP implementation of `Tree`s from lecture,
found
[here](http://www-inst.eecs.berkeley.edu/~cs61a/sp13/slides/25.py)
</block notes>

<block contents>

Code-Writing questions
----------------------

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
        elif len(t1.branches) != len(t2.branches):
            return False
        else:
            return all(equal(child1, child2) for child1, child2
                       in zip(t1.branches, t2.branches))

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
        return 1 + sum([size(child) for child in t.branches])

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
        if len(t.branches) == 0:
            return 0
        return 1 + max([height(child) for child in t.branches])

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

<!---

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

-->

<!---

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

-->

<!---

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

-->

</block contents>
