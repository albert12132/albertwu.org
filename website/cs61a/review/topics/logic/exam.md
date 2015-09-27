~ title: Logic
~ level: exam

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1UQeqb496rhwwNmGY-82wJ63ag8FTbIOtKDYnEbGOfXc/edit)
</block references>

<block notes>
We will be using the Logic interpreter, which you can get
[here](http://cs61a.org/lab/lab15/logic).  You can run the Logic interpreter
from your terminal with:

    python3 logic

You can load a `.logic` file with

    python3 logic -load file.logic

Alternatively, you can use the [online Logic
interpreter](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/logic/logic.html)
</block notes>


<block contents>

Code-Writing questions
----------------------

<question>

Write a fact or set of facts for the `interleave` relation, which
checks if two given lists will interleave into a third given list. You
cannot assume that the lists are of equal length.

    (fact (interleave ; YOUR CODE HERE

    ; Tests
    logic> (query (interleave (1 2) (3 4) (1 3 2 4)))
    Success!
    logic> (query (interleave (1 2) (3 4) (1 2 3 4)))
    Failed.
    logic> (query (interleave (1 2) (3 4 5) ?what))
    Success!
    what: (1 3 2 4 5)

<solution>

    (fact (interleave ?lst () ?lst))
    (fact (interleave () ?lst ?lst))
    (fact (interleave (?a . ?x) (?b . ?y) (?a ?b . ?z))
          (interleave ?x ?y ?z))

</solution>

<question>

Write a fact or set of facts for the `zip` relation, which checks if
two given lists will zip into a third given list (see the tests to get
an idea of what "zip" means). You can assume that the lists are of
equal length.

    (fact (zip ; YOUR CODE HERE

    ; Tests
    logic> (query (zip (1 2) (3 4) ((1 3) (2 4))))
    Success!
    logic> (query (zip (1 2) (3 4) (1 3 2 4)))
    Failed.

<solution>

    (fact (zip () () ()))
    (fact (zip (?a . ?x) (?b . ?y) ((?a ?b) . ?z))
          (zip ?x ?y ?z))

</solution>

<question>

Write a fact or set of facts for the `reverse` relation, which takes
two lists and checks if the second list is the reverse of the first.
You can assume the `append` relation is already defined.

    (fact (reverse ; YOUR CODE HERE

    ; Tests
    logic> (query (reverse (1 2 3 4) (4 3 2 1)))
    Success!
    logic> (query (reverse (1 2 3) (2 1 3)))
    Failed.
    logic> (query (reverse (4 2 5) ?what))
    Success!
    what: (5 2 4)

<solution>

    (fact (reverse () ()))
    (fact (reverse (?f . ?rest) ?lst)
          (reverse ?rest ?reverse-rest)
          (append ?reverse-rest (?f) ?lst))

</solution>

<!---
<question>

Write a fact or set of facts for the `subsequence` relation, which
takes two lists, and checks if the first list is a non-contiguous
subsequence of the second list. *Non-contiguous* means the elements of
the first list do not have to appear consecutively in the second list,
but they do have to appear in order.

    (fact (subsequence ; YOUR CODE HERE

    ; Tests
    logic> (query (subsequence (1 2 3) (0 1 2 0 0 3)))
    Success!
    logic> (query (subsequence (1 2 3) (1 3 2 3)))
    Success!
    logic> (query (subsequence (1 2 3) (1 3 2)))
    Failed.
    logic> (query (subsequence () (1 3 2)))
    Success!

<solution>

    (fact (subsequence () ?lst))
    (fact (subsequence (?f . ?r) (?f . ?s))
          (subsequence ?r ?s))
    (fact (subsequence (?a . ?r) (?b . ?s))
          (subsequence (?a . ?r) ?s))

</solution>

-->

Logical Trees (courtesy of Sarah Kim)
-------------------------------------

*The following questions were written by [Sarah Kim](http://www.sarahjikim.com/)
for Summer 2013.*

Let's create a series of facts on a tree diagram. The facts are of the
following form:

    (fact (tree number entry left right))

Some examples:

    (fact (tree tree-1 6 tree-2 tree-3))
    (fact (tree tree-2 4 tree-4 tree-5))
    (fact (tree tree-3 8 tree-6 tree-7))
    (fact (tree tree-4 3 tree-8 none))
    (fact (tree tree-5 5 none none))
    (fact (tree tree-6 7 none none))

    (fact (tree tree-7 11 tree-9 tree-10))
    (fact (tree tree-8 2 tree-11 none))
    (fact (tree tree-9 9 none tree-12))
    (fact (tree tree-10 12 none none))
    (fact (tree tree-11 1 none none))
    (fact (tree tree-12 10 none none))

<question>

Write a `find-entry` fact that associates tree number to tree entry.

    logic> (query (find-entry tree-12 10))
    Success!
    logic> (query (find-entry tree-2 ?x))
    Success!
    x: 4
    logic> (query (find-entry ?tree 11))
    Sucess!
    tree: tree-7

<solution>

    (fact (find-entry ?number ?entry)
          (tree ?number ?entry ?left ?right))

</solution>

<question>

Write a `check-leaf` fact that checks if a tree is a leaf (no trees in
left or right).

    logic> (query (check-leaf tree-12))
    Sucess!
    logic> (query (check-leaf tree-4))
    Failed.

<solution>

    (fact (check-leaf ?number)
          (tree ?number ?leaf none none))

</solution>

<question>

What would Logic print?

<prompt>
    logic> (query (check-leaf ?x))
    Success!
    x: tree-5
    x: tree-6
    x: tree-10
    x: tree-11
    x: tree-12
</prompt>


<question>
Write a `smallest-entry` fact that finds the smallest entry of a tree.

    logic> (query (smallest-entry tree-2 ?leaf))
    Success!
    leaf: 1
    logic> (query (smallest-entry tree-12 ?leaf))
    Success!
    leaf: 10
    logic> (query (smallest-entry tree-7 ?leaf))
    leaf: 9

<solution>

    (fact (smallest-entry ?number ?entry)
          (tree ?number ?entry none ?right))
    (fact (smallest-entry ?number ?entry)
          (tree ?number ?other-entry ? left ?right)
          (smallest-entry ?left ?entry))

</solution>

<question>

Write a `find-parent` fact, which finds the parent of a number.

    logic> (query (find-parent tree-11 ?parent))
    Success!
    parent: tree-8

<solution>

    (fact (find-parent ?number ?parent)
          (tree ?parent ?entry ?number ?right))
    (fact (find-parent ?number ?parent)
          (tree ?parent ?entry ?left ?number))

</solution>

<question>

Write a `generation` fact, which lists all the members of a tree's
family tree.

    logic> (query (generation tree-11 ?members))
    Success!
    members: tree-1
    members: tree-2
    members: tree-4
    members: tree-8
    members: tree-11

<solution>

    (fact (generation ?number ?grandfather)
          (find-parent ?number ?father)
          (generation ?father ?grandfather))
    (fact (generation ?number ?number))

</solution>

<question>

What would happen if for the `generation` fact, we put the second fact
before the first fact?

    logic> (query (generation tree-11 ?members))

<solution>

    Success!
    members: tree-11
    members: tree-8
    members: tree-4
    members: tree-2
    members: tree-1

</solution>

</block contents>
