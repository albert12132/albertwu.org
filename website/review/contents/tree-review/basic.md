~ title: OOP Trees final review

<block contents>

OOP Trees
---------

<question>

Implement a function `same_shape`, which takes two `Tree`s and returns
True if the trees have the same structure, but not necessarily the same
entries.

    def same_shape(t1, t2):
        "*** YOUR CODE HERE ***"

<solution>

    def same_shape(t1, t2):
        if not t1.branches or not t2.branches:
            return not t1.branches and not t2.branches
        elif len(t1.branches) != len(t2.branches):
            return False
        for i in range(len(t1.branches)):
            if not same_shape(t1.branches[i], t2.branches[i]):
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
        if not t.branches:
            t.branches = [Tree(v) for v in vals]
        else:
            for branch in t.branches:
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
        if not t.branches:
            if t.entry not in vals:
                return t
            else:
                return None
        new_branches = [prune_leaves(branch, vals) for branch in t.branches]
        t.branches = [b for b in new_branches if b is not None]
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
        return max_tree(b.right)

</solution>

    def min_bst(b):
        "*** YOUR CODE HERE ***"

<solution>

    def min_bst(b):
        if b.left.is_empty:
            return b.entry
        return min_tree(b.left)

</solution>

<question>

Implement a function `valid_bst`, which takes a `BinaryTree` and
returns `True` if it is a valid binary search tree. You may find
`min_bst` and `max_bst` helpful.

    def valid_bst(b):
        "*** YOUR CODE HERE ***"

<solution>

    def valid_bst(b):
        if b.is_empty:
            return True
        elif not valid_bst(b.left) or not valid_bst(b.right):
            return False
        elif b.left and max_bst(b.left) > t.entry:
            return False
        elif b.right and min_bst(b.right) < t.entry:
            return False
        else:
            return True

</solution>

<quesiton>

Implement a function `bst_in_order`, which takes a binary search tree
and returns a list of all the elements of the tree in ascending order.

    def bst_in_order(b):
        "*** YOUR CODE HERE ***"

<solution>

    def bst_in_order(b):
        if b.is_empty:
            return []
        else:
            return bst_in_order(b.left) + [b.entry] + bst_in_order(b.right)

</solution>

</block contents>
