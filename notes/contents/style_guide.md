~ title: Style Guide
~ style: style-guide.css

Introduction
------------

In 61A, each project has a composition score, worth 3 points, that is
graded on the *style* of your code. This document provides some
guidelines.

After your code works, you should strive to do the following things:

1. Make your code **easier to read**
2. Make your code **concise**
3. Make your code **efficient** (optional for this class)

Sometimes these goals conflict with each other, and **sometimes there
are exceptions to the rules**. Whatever you do, you should always try
to make your code easy to read -- use your judgement.

Some of these guidelines have one or more of the following marks:

* <N>: a "non-essential" guideline; these guidelines are not necessary
  for this class, but are generally good practice
* <P>: a Python-specific guideline; these are "Pythonic" style
  conventions that don't necessarily apply to other languages

Finally, here is a link to to
[PEP-8](http://www.python.org/dev/peps/pep-0008/), the official Python
style guide.

Names and variables
-------------------

### Meaningful names

Variable and function names should be *self-descriptive*:

<bad>
    a, b, m = 100, 0, 0
    thing = 'hello world'
    stuff = lambda x: x % 2
</bad>

<good>
    goal, score, opp_score = 100, 0, 0
    greeting = 'hello world'
    is_even = lambda x: x % 2
</good>

### Indices and mathematical symbols

Using one-letter names and abbreviations is okay for indices,
mathematical symbols, or if it is obvious what the variables are
referring to.

<good>
    i = 0         # a counter for a loop
    x, y = 0, 0   # x and y coordinates
    p, q = 5, 17  # mathematical names in the context of the question
</good>

In general, `i`, `j`, and `k` are the most common indices used.

### 'o' and 'l'

Do not use the letters 'o' and 'l' by themselves as names:

<bad>
    o = O + 4     # letter 'O' or number 0?
    l = l + 5     # letter 'l' or number 1?
</bad>

### Unnecessary variables

Don't create unnecessary variables. For example,

<bad>
    result = answer(argument)
    return result
</bad>

<good>
    return answer(argument)
</good>

However, if it is unclear what your code is referring to, or if the
expression is too long, you *should* create a variable:

<bad>
    do_something(lambda x: x % 49 == 0, (total + 1) // 7)
</bad>

<good>
    divisible_49 = lambda x: x % 49 == 0
    score = (total + 1) // 7
    do_somethig(divisible_49, score)
</good>

### Profanity

Don't leave profanity in your code. Even if you're really frustrated.

<bad>
    eff_this_class = 666
</bad>

### Naming convention:

<N><P>: Use `lower_case_and_underscores` for variables and functions:

<bad>
    TotalScore = 0
    finalScore = 1

    def Mean_Strategy(score, opp):
        ...
</bad>

<good>
    total_score = 0
    final_score = 1

    def mean_strategy(score, opp):
        ...
</good>

On the other hand, use `CamelCase` for classes:

<bad>
    class example_class:
        ...
</bad>

<good>
    class ExampleClass:
        ...
</good>

Spacing and Indentation
-----------------------

Whitespace style might seem superfluous, but using whitespace in
certain places (and omitting it in others) will often make it easier
to read code. In addition, since Python code depends on whitespace
(e.g. indentation), it requires some extra attention.

### Spaces vs. tabs

Use spaces, not tabs for indentation. Our starter code always uses 4
spaces instead of tabs. If you use both spaces and tabs, Python will
raise an `IndentationError`.

### Indent size

<P>: Use 4 spaces to denote an indent. Technically, Python allows you
to use any number of spaces as long as you are consistent across an
indentation level. The conventional style is to use 4 spaces.

### Line Length

Keep lines under 80 characters long. Other conventions use 70 or 72
characters, but 80 is usually the upper limit.

### Double-spacing

Don't double-space code. That is, do *not* insert a blank line in
between lines of code. Personally, I find that harder to read.

### Spaces with operators

<N>: Use spaces between `+` and `-`. Depending on how illegible
expressions get, you can use your own judgement for `*`, `/`, and `**`
(as long as it's easy to read at a glance, it's fine).

<bad>
    x=a+b*c*(a**2)/c-4
</bad>

<good>
    x = a + b*c*(a**2) / c - 4
</good>

### Spacing lists

<N>: When using tuples, lists, or function operands, leave one space
after each comma `,`:

<bad>
    tup = (x,x/2,x/3,x/4)
</bad>

<good>
    tup = (x, x/2, x/3, x/4)
</good>

### Line wrapping

<N><P>: If a line gets too long, you have two options. If you are
using parentheses or braces with multiple elements, you can continue
them onto the next line:

<good>
    def func(a, b, c, d, e, f,
             g, h, i):
        # body

    tup = (1, 2, 3, 4, 5,
           6, 7, 8)
    names = ('alice',
             'bob',
             'eve')
</good>

Notice that the subsequent lines line up with the *start* of the
sequence. If the above rule does not apply, you can use Python's `\`
operator:

<good>
    total = this_is(a, very, lengthy) + line + of_code \
                + so_it - should(be, separated) \
                + onto(multiple, lines)
</good>

*Where* you put the `\` in relation to binary operators (e.g.
`hi \ + bye`  versus `hi + \ bye`) will vary from person to person
-- for our class, it doesn't matter.

### Blank lines

<N><P>: Leave a blank line between the end of a function or class and
the next line:

<good>
    def example():
        return 'stuff'

    x = example() # notice the space above
</good>

### Trailing whitespace

<N>: Don't leave whitespace at the end of a line.

Repetition
----------

In general, **don't repeat yourself** (DRY). It wastes space and can
be computationally inefficient.

### Complex expressions

Do not repeat complex expressions:

<bad>
    if a + b - 3 * h / 2 % 47 == 4:
        total += a + b - 3 * h / 2 % 47
        return total
</bad>

Instead, store the expression in a variable:

<good>
    turn_score = a + b - 3 * h / 2 % 47
    if turn_score == 4:
        total += turn_score
        return total
</good>

This will also make your code more readable.

### Computation-heavy function calls

Don't repeat computationally-heavy function calls:

<bad>
    if takes_one_minute_to_run(x) != ():
        first = takes_one_minute_to_run(x)[0]
        second = takes_one_minute_to_run(x)[1]
        third = takes_one_minute_to_run(x)[2]
</bad>

Instead, store the expression in a variable:

<good>
    result = takes_one_minute_to_run(x)
    if result != ():
        first = result[0]
        second = result[1]
        third = result[2]
</good>

### if/else conditions

DON'T have the same code in both the `if` and the `else` clause of a
conditional:

<bad>
    if pred:            # bad!
        print('stuff')
        x += 1
        return x
    else:
        x += 1
        return x
</bad>

Instead, pull the line(s) out of the conditional:

<good>
    if pred:            # good!
        print('stuff')
    x += 1
    return x
</good>

Comments
--------

Recall that Python comments begin with the `#` sign. Keep in mind that
the triple-quotes are technically strings, not comments. Comments can
be helpful for explaining ambiguous code, but there are some
guidelines for when to use them.

### Docstrings

<P>: Put docstrings only at the top of functions. Docstrings are
denoted by triple-quotes at the beginning of a function or class:

<good>
    def average(fn, samples):
        """Calls a 0-argument function SAMPLES times, and takes
        the average of the outcome.
        """
</good>

You should not put docstrings in the middle of the function -- only
put them at the beginning.

### Remove commented-out code

Remove commented-out code from final version. You can comment lines
out when you are debugging. When you are turning in your project, take
all commented lines out (including `TODO`s) -- this makes it easier
for readers to read your code.

### Unnecessary comments

Don't write unnecessary comments. For example, the following is bad:

<bad>
    def example(y):
        x += 1            # increments x by 1
        return square(x)  # returns the square of x
</bad>

Your actual code should be *self-documenting* -- try to make it as
obvious as possible what you are doing without resorting to
comments. Only use comments if something is not obvious or needs to
be explicitly emphasized


Control Structures
------------------

### Boolean comparisons

Don't compare a boolean variable to `True` or `False`:

<bad>
    if pred == True:   # bad!
        ...
    if pred == False:  # bad!
        ...
</bad>

Instead, do this:

<good>
    if pred:           # good!
        ...
    if not pred:       # good!
        ...
</good>

### Redundant if/else

Don't do this:

<bad>
    if pred:            # bad!
        return True
    else:
        return False
</bad>

Instead, do this:

<good>
    return pred         # good!
</good>

### Similar if/else suites

(related to the previous:) Don't do this:

<bad>
    if num != 49:
        total += example(4, 5, True)
    else:
        total += example(4, 5, False)
</bad>

In the example above, the only thing that changes between the
conditionals is the boolean at the end. Instead, do this:

<good>
    total += example(4, 5, num != 49)
</good>

### while vs. if

Don't use a `while` loop when you should use an `if`:

<bad>
    while pred:
        x += 1
        return x
</bad>

Instead, use an `if`

<good>
    if pred:
        x += 1
        return x
</good>

### Parentheses

<P>: Don't use parentheses with conditional statements:

<bad>
    if (x == 4):
        ...
    elif (x == 5):
        ...
    while (x < 10):
        ...
</bad>

Parentheses are not necessary in Python conditionals (they are in
other languages though).

Miscellaneous
-------------

### Semicolons

<P>: Do not use semicolons. This is not C/C++/Java/etc.

### Checking `None`

<P>: Use `is` and `is not` for `None`, not `==` and `!=`.

### Implicit `False`

<P>: Use the "implicit" `False` value when possible. Examples include
empty containers like `[]`, `()`, `{}`, `set()`.

<good>
    if lst:       # if lst is not empty
        ...
    if not tup:   # if tup is empty
        ...
</good>

### Generator expressions

<P>: Generator expressions are okay for simple expressions. This
includes list comprehensions, dictionary comprehensions, set
comprehensions, etc.  Generator expressions are neat ways to concisely
create lists. Simple ones are fine:

<good>
    ex = [x*x for x in range(10)]
    L = [pair[0] + pair[1]
         for pair in pairs
         if len(pair) == 2]
</good>

However, complex generator expressions are very hard to read, even
illegible. As such, do not use generator expressions for complex
expressions.

<bad>
    L = [x + y + z for x in nums if x > 10 for y in nums2 for z in nums3 if y > z]
</bad>

Use your best judgement.
