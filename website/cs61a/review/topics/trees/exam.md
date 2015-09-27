~ title: Tree ADT
~ level: exam

<block references>
* [Albert's and Robert's slides](https://docs.google.com/presentation/d/1BXO9nB7I-iyzDuoBbvWqo4vUbJqBBhhVlxzOVv9aFAA/edit)
</block references>

<block notes>
</block notes>


<block contents>

Tree ADT
--------

Recall that we learned two different tree representations in this
class:

* Abstract data type (defined in terms of functions). This is what this
  worksheet covers.
* Object-oriented programming (defined in termes of classes and
  methods). This will be covered in another review session.

The tree abstract data type is defined in terms of these four
functions:

    def tree(root, subtrees=[]):
        return [root] + list(subtrees)

    def root(t):
        return t[0]

    def subtrees(t):
        return t[1:]

    def is_leaf(t):
        return not subtrees(t)

Since this is an ADT, we don't care so much about the implementation of
the constructors and selectors: as long as we know what they do, we can
use them.

Remember, trees are **recursively defined** (trees are constructed
using smaller trees). For most questions involving the tree ADT, you
can break down the thought process into three steps:

1. **Base case**: Usually, this is if the tree is a leaf (use the
   `is_leaf` function)
2. **Recursive call**: Consider what a recursive call on a single
   branch will do. What information does it give you?
3. **Recursive case**: Make recursive calls on each branch (using a
   `for` loop or a list comprehension) and combine that in some way
   with the root for your final answer.

<question>

Implement a function `contains`, which takes a tree `t` and an element
`e`. `contains` will return True if `t` contains the element `e`, and
False otherwise.

    def contains(t, e):
        "*** YOUR CODE HERE ***"

<solution>

    def contains(t, e):
        if e == root(t):
            return True
        elif is_leaf(t):
            return False
        else:
            for b in subtrees(t):
                if contains(b, e):
                    return True
            return False

It is possible to use a list comprehension to solve this problem,
thanks to the built-in `any` function. The `any` function takes a list
of booleans and returns True if any of those booleans is True:

    def contains(t, e):
        if e == root(t):
            return True
        elif is_leaf(t):
            return False
        else:
            return any([contains(b, e) for b in subtrees(t)])

While this version is more concise, it is also more inefficient (why?).

</solution>

<question>

Implement a function `all_paths`, which takes a tree `t`. `all_paths`
will return a list of paths from the root to each leaf. For example,
consider the following tree:

      5
     / \
     3  6
    / \
    2  1

Calling `all_paths` on this tree would return

    [[5, 3, 2],
     [5, 3, 1],
     [5, 6]    ]

The list contains three paths (each path is itself a list).

    def all_paths(t):
        "*** YOUR CODE HERE ***"

<solution>

    def all_paths(t):
        if is_leaf(t):
            return [[root(t)]]
        else:
            total = []
            for b in subtrees(t):
                for path in all_paths(b):
                    total.append([root(tree)] + path)
            return total

It is possible to solve this using a list comprehension, but the list
comprehension gets a little complicated:

    def all_paths(t):
        if is_leaf(t):
            return [[root(t)]]
        else:
            return [[root(tree)] + path for b in subtrees(t)
                                        for path in all_paths(b)]

Notice that the `for` statements in the list comprehension are exactly
the same as the two `for` loops in the original solution.

</solution>

<question>

Implement a function `max_tree`, which takes a tree `t`. It returns a
new tree with the exact same structure as `t`; at each node in the new
tree, the entry is the largest number that is contained in that node's
subtrees or the corresponding node in `t`. For example, consider this
tree:

      5
     / \
     3  6
    / \
    2  4

Calling `max_tree` will return the following tree:

      6
     / \
     4  6
    / \
    2  4

For example, the largest number that occurs at the root or below it is
6 (i.e. `max(5, 3, 2, 4, 6) = 6`), so the root of the new tree is 6.

    def max_tree(t):
        "*** YOUR CODE HERE ***"

<solution>

    def max_tree(t):
        if is_leaf(t):
            return tree(root(t))
        else:
            new_subtrees = [max_tree(b) for b in subtrees(t)]
            new_root = max([root(t)] + [root(s) for s in new_subtrees])
            return tree(new_root, new_subtrees)

</solution>

</block contents>
