~ title: Style Guide ~
~ style: style\_guide.css ~

In 61A, each project has a composition score, worth 3 points, that is
graded on the *style* of your code. This document provides some
guidelines.

After your code works, you should strive to do two things:

1. Make your code **easier to read**
2. Make your code **concise**
3. Make your code **efficient** (optional for this class)

Sometimes these goals conflict with each other, and sometimes there
are exceptions to the rules. Whatever you do, you should always try to
make your code easy to read.

Some of these guidelines will have one or more of the following marks:

* <N>: a "non-essential" guideline; these
  guidelines are not necessary for this class, but are generally good
  practice
* <P>: a Python-specific guideline; these
  are "Pythonic" style conventions that don't necessarily apply to
  other languages

Naming variables
----------------

1. **Meaningful names**: variable and function names should be
   *self-descriptive*:

        # bad -- don't do this!
        a, b, m = 100, 0, 0
        thing = 'hello world'
        stuff = lambda x: x % 2

        # good
        goal, score, opp_score = 100, 0, 0
        greeting = 'hello world'
        is_even = lambda x: x % 2

2. **Indices and mathematical symbols**: using one-letter names and
   abbreviations is okay for indices, mathematical symbols, or if it
   is obvious what the variables are referring to.

        i = 0         # a counter for a loop
        x, y = 0, 0   # x and y coordinates
        p, q = 5, 17  # mathematical names in the context of the question

    In general, `i`, `j`, and `k` are the most common indices used.

3. **Avoid letters 'o' and 'l'**: do not use them by themselves as
   names:

        # bad!
        o = O + 4     # letter 'O' or number 0?
        l = l + 5     # letter 'l' or number 1?

4. **Avoid profanity**: don't leave it in your code. Even if you're
   really frustrated.

        # bad!
        eff_this_class = 666

5. <N><P>: Use `lower_case_and_underscores` for variables and
   functions:

        # bad!
        TotalScore = 0
        finalScore = 1

        def Mean_Strategy(score, opp):
            ...

        # good!
        total_score = 0
        final_score = 1

        def mean_strategy(score, opp):
            ...

6. <N><P>: Use `CamelCase` for classes:

        # bad!
        class example_class:
            ...

        # good!
        class ExampleClass:
            ...

Spacing and Indentation
-----------------------

Whitespace style might seem superfluous, but using whitespace in
certain places will often make it easier to read code. In addition,
since Python code depends on whitespace, it requires extra attention.

1. **Use spaces, not tabs for indentation**: our starter code always
   uses 4 spaces instead of tabs. If you use both spaces and tabs,
   Python will raise an `IndentationError`.

2. <P>: **Use 4 spaces per indentation level**: technically, Python
   allows you to use any number of spaces as long as you are
   consistent across an indentation level. The conventional style is
   to use 4 spaces.

3. **Keep lines under 80 characters long**: other conventions use 70
   or 72 characters, but 80 is usually the upper limit.

4. **Don't double-space code**: that is, do *not* insert a blank line
   in between lines of code. Personally, I find that harder to read.

5. <N>: **Use spaces between primitive operators**: always use spaces
   between `+` and `-`. Depending on how illegible expressions get,
   you can use your own judgement for `*`, `/`, and `**` (as long as
   it's easy to read at a glance, it's fine).

        # bad!
        x=a+b*c*(a**2)/c-4

        # good!
        x = a + b*c*(a**2) / c - 4

6. <N>: **Spacing lists**: When using tuples, lists, or function
   operands, leave one space after each comma `,`:

        # bad!
        tup = (x,x/2,x/3,x/4)

        # good!
        tup = (x, x/2, x/3, x/4)

7. <N><P>: If a line gets two long, you have two options. If you are
   using parentheses or braces with multiple elements, you can
   continue them onto the next line:

        def func(a, b, c, d, e, f,
                 g, h, i):
            # body

        tup = (1, 2, 3, 4, 5,
               6, 7, 8)
        names = ('alice',
                 'bob',
                 'eve')

  Notice that the subsequent lines line up with the *start* of the
  sequence. If the above rule does not apply, you can use Python's `\`
  operator:

        total = this_is(a, very, lengthy) + line + of_code \
                    + so_it - should(be, separated) \
                    + onto(multiple, lines)

  *Where* you put the `\` in relation to binary operators (e.g.
  `hi \ + bye`  versus `hi + \ bye`) will vary from person to person
  -- for our class, it doesn't matter.

8. <N><P>: Leave a blank line between the end of a function or class and the
   next line:

        def example():
            return 'stuff'

        x = example() # notice the space above

9. <N>: Don't leave whitespace at the end of a line.

Repetition
----------

In general, **don't repeat yourself** (DRY). It wastes space and can
be computationally inefficient.

1. **DON'T** repeat complex expressions:

        if a + b - 3 * h / 2 % 47 == 4:
            total += a + b - 3 * h / 2 % 47
            return total

  **Instead**, store the expression in a variable:

        turn_score = a + b - 3 * h / 2 % 47
        if turn_score == 4:
            total += turn_score
            return total

  This will also make your code more readable.

2. **Don't repeat computationally-heavy function calls**:

        if takes_one_minute_to_run(x) != ():
            first = takes_one_minute_to_run(x)[0]
            second = takes_one_minute_to_run(x)[1]
            third = takes_one_minute_to_run(x)[2]

  **Instead**, store the expression in a variable:

        result = takes_one_minute_to_run(x)
        if result != ():
            first = result[0]
            second = result[0]
            third = result[0]

3. **DON'T** have the same code in both the `if` and the `else` clause
   of a conditional:

        if pred:            # bad!
            print('stuff')
            x += 1
            return x
        else:
            x += 1
            return x

  **Instead**, pull the line(s) out of the conditional:

        if pred:            # good!
            print('stuff')
        x += 1
        return x

Comments
--------

Recall that Python comments begin with the `#` sign. Keep in mind that
the triple-quotes are technically strings, not comments. Comments can
be helpful for explaining ambiguous code, but there are some
guidelines for when to use them.

1. <P>: **Put docstrings only at the top of functions**: docstrings are
   denoted by triple-quotes at the beginning of a function or class:

        def average(fn, samples):
            """Calls a 0-argument function SAMPLES times, and takes
            the average of the outcome."""

   You should **not** put docstrings in the middle of the function --
   only put them at the beginning.

2. **Remove commented-out code from final version**: you can comment
   lines out when you are debugging. When you are turning in your
   project, take all commented lines out (including `TODO`s) -- this
   makes it easier for readers to read your code.

3. **Don't write unnecessary comments**: for example, the
   following is bad:

        def example(y):
            x += 1            # increments x by 1
            return square(x)  # returns the square of x

   Your actual code should be *self-documenting* -- try to make it as
   obvious as possible what you are doing without resorting to
   comments. Only use comments if something is not obvious or needs to
   be explicitly emphasized


Control Structures
------------------

1. **DON'T** compare a boolean variable to `True` or `False`:

        if pred == True:   # bad!
            ...
        if pred == False:  # bad!
            ...

  **Instead**, do this:

        if pred:           # good!
            ...
        if not pred:       # good!
            ...

2. **DON'T** do this:

        if pred:            # bad!
            return True
        else:
            return False

  **Instead**, do this:

        return pred         # good!

3. (related to the previous:) **DON'T** do this:

        if num != 49:
            total += example(4, 5, True)
        else:
            total += example(4, 5, False)

  In the example above, the only thing that changes between the
  conditionals is the boolean at the end. **Instead**, do this:

        total += example(4, 5, num != 49)

5. **DON'T** use a `while` loop when you should use an `if`:

        while pred:
            x += 1
            return x

  **Instead**, use an `if`

        if pred:
            x += 1
            return x

6. <P>: **DON'T** use parentheses with conditional statements:

        if (x == 4):
            ...
        elif (x == 5):
            ...
        while (x < 10):
            ...

  Parentheses are not necessary in Python conditionals (they are in
  other languages though).

