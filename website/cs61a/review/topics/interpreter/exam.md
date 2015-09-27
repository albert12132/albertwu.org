~ title: Interpreters
~ level: exam

<block references>
* [Albert's and Robert's slides part
  1](https://docs.google.com/presentation/d/1KWpVvk9Zo3vrEGr2u_rxzNFOQY_8qvszaT3MgdkyA18/edit)
* [Albert's and Robert's slides part
  2](https://docs.google.com/presentation/d/1fhm6j1i7pq17tKp8DkM-79dSgLfuP_yd8-2c_3dFWuw/edit)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Given the following Scheme expressions, what would `scheme_read` from
Project 4 return? If the parser would raise an error, write ERROR.

<prompt>
    > (+ 2 3)
    Pair('+', Pair(2, Pair(3, nil)))
    > '(1 2 3)
    Pair('quote', Pair(Pair(1, Pair(2, Pair(3, nil))), nil))
    > (1 . 2)
    Pair(1, 2)
    > 3
    3
    > (1 . (3 2))
    Pair(1, Pair(3, Pair(2, nil)))
    > ('hi . 3 4)
    ERROR
</prompt>

<question>

Given each of the following Pair objects, determine how many times
`scheme_eval` and `scheme_apply` are called (not `calc_eval` and
`calc_apply`!). Be sure to include the first `scheme_eval`. The first
one has been done for you.

**Note**: assume that the following `double` function has been defined:

    (define (double x) (+ x x))

Don't include the calls to `scheme_eval` and `scheme_apply` for the
code above in your answers.

    (+ 2 3)
    ; eval  4   (1 for whole expression, 1 for each element in list)
    ; apply 1   ('+' is primitive)

    3
    ; eval  ________
    ; apply ________

    (+ 3 (+ 5 2))
    ; eval  ________
    ; apply ________

    (double 4)
    ; eval  ________
    ; apply ________

    (double (double 4))
    ; eval  ________
    ; apply ________

<solution>

    3
    ; eval  1
    ; apply 0

    (+ 3 (+ 5 2))
    ; eval  7
    ; apply 2

    (double 4)
    ; eval  7
    ; apply 2

    (double (double 4))
    ; eval  13
    ; apply 4

</solution>

Code-Writing question
---------------------

<question>

Write a function `is_pyramid` that takes in a list of tokens, and
checks if the list of tokens forms a pyramid. A *pyramid* is a list
that is symmetric in *shape* (not necessarily the contents), and each
list can only have one nested list at its level. The following are
examples of valid pyramids:

    (3 4 (5 (1) 3) 2 3)
    (1 2 3 4)           # no nested lists is okay
    (1 (2 () 3) 4)      # empty lists are okay
    (1 (2) 3) )()       # junk, )(), after a valid pyramid is okay
    (1 () 2) s d fs     # junk after a valid pyramid is okay

The following are examples of invalid pyramids:

    (2 (3) 4 5)     # too many elements on the right side
    ((3) (4))       # too many nested lists on the first level
    (3 4            # missing closing parenthesis

Given the examples above, implement the `is_pyramid` function:

    def is_pyramid(tokens):
        """Returns true if the list of tokens begins with a valid
        pyramid. Junk at the end is okay.

        >>> t1 = ['(', 3, '(', 4, ')', 5, ')']  # (3 (4) 5)
        >>> is_pyramid(t1)
        True
        >>> t2 = ['(', '(', '(', ')', ')', ')'] # ((()))
        >>> is_pyramid(t2)
        True
        >>> t3 = ['(', 3, '(', 2, 3, ')', 4, ')', 3, 4] # (3 (2 3) 4) 3 4
        >>> is_pyramid(t3)
        True
        >>> f1 = ['(', 2, '(', 3, ')', 4, 5, ')'] # (2 (3) 4 5)
        >>> is_pyramid(f1)
        False
        >>> f2 = ['(', '(', 3, ')', '(', 4, ')', ')'] # ((3) (4))
        >>> is_pyramid(f2)
        False
        >>> f3 = ['(', 3, 4] # (3 4
        >>> is_pyramid(f3)
        False
        """
        if not tokens or tokens[0] != '(':
            return False
        tokens.pop(0)
        "*** YOUR CODE HERE ***"

<solution>

    def is_pyramid(tokens):
        if not tokens or tokens[0] != '(':
            return False
        tokens.pop(0)
        count, direction = 0, 1
        while tokens and tokens[0] != ')':
            if direction == -1 and count == 0:
                return False
            elif tokens[0] == '(':
                if direction == -1 or not is_pyramid(tokens):
                    return False
                else:
                    direction = -1
            else:
                tokens.pop(0)
                count += direction
        if not tokens:
            return False
        else:
            tokens.pop(0)
            return direction == 1 or count == 0

**Explanation**: The base case that is provided checks that the tokens
begin with an '('. If it doesn't, then we immediately know that it is
not a pyramid. We then remove the '('.

First, let's write code that simply goes through each element and
removes it from the list of tokens. The word *each* indicates that we
need some looping structure, so we'll use a while look. Our while loop
should stop if we reach the end of the list of tokens, or if we see a
')':

    def is_pyramid(tokens):
        if not tokens or tokens[0] != '(':
            return False
        tokens.pop(0)
        while tokens and tokens[0] != ')':
            if tokens[0] == '(':
                # handle case for nested lists
            else:
                # handle case for numbers

How do we handle a nested list? Simply make a recursive call; if the
nested list is not a valid pyramid, the recursive call will return
False. The recursive call has the additional benefit of removing the
nested list, including its closing parenthesis:

    ...
    if tokens[0] == '(':
        if not is_pyramid(tokens):
            return False
    ...

How do we handle a number? Simply remove it from the list of tokens:

    ...
    else:
        tokens.pop(0)
    ...

What happens if we break out of our while loop? There are two
scenarios: 1) if we run out of tokens, and 2) if the first token is a
')'. If we run out of tokens, we should return False, because that
means we never saw the corresponding ')'. If the first token is a ')',
then we successfully closed the list and we can just pop it off and
return True:

    ...
    while tokens and tokens[0] != ')':
        ...
    if not tokens:
        return False
    else:
        tokens.pop(0)
        return True

At this point, our code looks like this:

    def is_pyramid(tokens):
        if not tokens or tokens[0] != '(':
            return False
        tokens.pop(0)
        while tokens and tokens != ')':
            if tokens[0] == '(':
                if not is_pyramid(tokens):
                    return False
            else:
                tokens.pop(0)
        if not tokens:
            return False
        else:
            return True

This looks promising, but it doesn't account for the symmetry of the
list.  Here's the idea. We'll keep track of two variables: 1) a
`count`, which counts the number of elements before the nested list,
and then checks that the number of elements after the nested list
matches; 2) a `direction`, that tells us whether we're before the
nested list or after it:

    ...
    tokens.pop(0)
    count, direction = 0, 1
    while tokens and tokens[0] != ')':
        ...

We'll use the convention that, when direction is 1, we are incrementing
our count, and when direction is -1, we are decrementing our count.

Now, let's go in the while loop. If `tokens[0] == '('` (meaning we
see a nested list), this tells us that we've reached our midpoint, and
we should begin decrementing count after this:

    if tokens[0] == '(':
        if not is_pyramid(tokens):
            return False
        else:
            direction = -1

In addition, if our direction is already -1 (meaning we've already seen
a nested list), and we see another nested list, this breaks our
definition of a pyramid, so we should return False (e.g. the case `((3)
(4))`):

    if tokens[0] == '(':
        if direction == -1 or not is_pyramid(tokens):
            return False
        else:
            direction = -1

What about the case of regular numbers? In addition to removing the
token, we also need to update our `count`. If direction is 1, we should
increment; if it is -1 (i.e. we've seen a nested list already), we
should decrement:

    else:
        tokens.pop(0)
        count += direction

We need one other case inside the while loop; what happens if we see
`(3 (4) 5 6)`? There are too many elements on the right side! Walk
through the code we have right now, and you'll notice that when we
reach the 6, `count` will be 0, and `direction` will be -1. This is the
red flag we look for to tell us to return False:

    while tokens and tokens[0] != ')':
        if direction == -1 and count == 0:
            return False
        if tokens[0] == '(':
            ...

Almost done! At the end, we need to update the case where `tokens` is
not empty.  Consider this example: `(3 4 () 3)`. The right side
contains too few elements. How can we tell? `count` will be nonzero!
Instead of just returning True, we add the additional check on
count:

    if not tokens:
        return False
    else:
        return direction == 1 or count == 0

Overall, our code looks like this:

    def is_pyramid(tokens):
        if not tokens or tokens[0] != '(':
            return False
        tokens.pop(0)
        count, direction = 0, 1
        while tokens and tokens[0] != ')':
            if direction == -1 and count == 0:
                return False
            elif tokens[0] == '(':
                if direction == -1 or not is_pyramid(tokens):
                    return False
                else:
                    direction = -1
            else:
                tokens.pop(0)
                count += direction
        if not tokens:
            return False
        else:
            tokens.pop(0)
            return direction == 1 or count == 0

</solution>

</block contents>
