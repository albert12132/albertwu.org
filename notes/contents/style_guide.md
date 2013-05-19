~ Style Guide ~

In 61A, each project has a composition score, out of 3 points, that is
graded on the *style* of your code. This document provides some
guidelines.

After your code works, you should strive to do two things: (1) make
your code **easier to read**, and (2) make your code **concise**.
Sometimes these two goals conflict with each other -- if that is the
case, you should choose to make your code easy to read.

One last note: many of these guidelines are **Python-specific**. If
you find yourself working on code in other languages, make sure to
check out their style guides.

Essentials
----------

### Variables and Names

1. **DON'T** give your variables meaningless names:

        c = 'hello world!'
        t = lambda x: x % 2
        kablooey = (1, 2, 3)
        l = 6 + l    # very bad! is that a 1 or an l?
        o = 4 * o    # very bad! is that a 0 or an o?

   **Instead**, give variables self-descriptive names:

        msg = 'hello world'
        is_even = lambda x: x % 2
        numbers = (1, 2, 3)

2. Using one-letter names is okay for indices, mathematical symbols,
   or if it is obvious what the variables are referring to:

        i = 0         # a counter for a loop
        x, y = 0, 0   # x and y coordinates
        p, q = 5, 17  # mathematical names in the context of the question

    In general, `i`, `j`, and `k` are the most common indices used.

3. **DON'T** define functions or create variables that are
   unnecessary:

        total = 100   # bad!
        return total

  For the example above, just do this:

        return 100

4. **DON'T** repeat complex expressions:

        if a + b - 3 * h / 2 % 47 == 4:
            total += a + b - 3 * h / 2 % 47
            return total

  **Instead**, store the expression in a variable:

        turn_score = a + b - 3 * h / 2 % 47
        if turn_score == 4:
            total += turn_score
            return total

  This will also make your code more readable.

5. **DON'T** use profanity in your code:

        hell = lambda y: y**2
        i_hate_this_class = 42
        # I've seen much worse than this -- don't do it!

### Control Structures

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

4. **DON'T** have the same code in both the `if` and the `else` clause
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

  In general, if you find yourself repeating code, find a way to
  fix it.

5. **DON'T** use a `while` loop when you should use an `if`:

        while pred:
            x += 1
            return x

  **Instead**, use an `if`

        if pred:
            x += 1
            return x

### Miscellaneous

1. **DON'T** use tabs for indentation. Our starter files use spaces,
   which will be incompatible with tabs. Most editors have an option
   to convert tabs to spaces.

2. **DON'T** write `return None`. You can always just write `return`,
   which implicitly returns `None`:

        def example(x):
            print('not two')
            return None

  In other languages, you might have to explicitly say `return None`,
  but in Python, functions without it will implicitly return `None`:

        def example(x):
            print('not two')
            return

  We can even simplify this further by removing the very last
  `return`, but keeping it isn't necessarily bad style.

3. **DON'T** leave unused code in your file (even if it is commented
   out!). It makes it harder for others to read:

        def example(y):
            # print('--- debugging ---')
            # print('y is', y)
            # y += 4
            # return y - 6
            return y - 2

4. **DON'T** make unnecessary comments:

        def example(y):
            x += 1            # increments x by 1
            return square(x)  # returns the square of x

  If you give your variables and functions self-descriptive names,
  you often will not need to have any comments.


Non-Essentials
--------------

These style guidlines are not high priority, but it does make your
code nicer to read.

### Spacing and Formatting

1. Use 4 spaces per indentation level.

2. Lines should not be longer than 80 characters.

3. If a line gets two long, you have two options. If you are using
   parentheses or braces with multiple elements, you can continue them
   onto the next line:

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

  *Where* you put the `\` in relation to binary operators (e.g. `hi \
  + bye`  versus `hi + \ bye`) will vary from person to person -- for
  our class, it doesn't matter

4. Leave a blank line between the end of a function or class and the
   next line:

        def example():
            return 'stuff'

        x = example() # notice the space above

5. **DON'T** clump expressions together without whitespace:

        total=a+b-2*helper(4,3)

  Doing so makes it harder to read. **Instead** use spaces in between
  operators:

        total = a + b - 2 * helper(4, 3)

6. **DON'T** leave whitespace (tabs or spaces) at the end of lines.

### Operators and Symbols

1. **DON'T** use parentheses with conditional statements:

        if (x == 4):
            ...
        elif (x == 5):
            ...
        while (x &lt; 10):
            ...

  Parentheses are not necessary in Python conditionals (they are in
  other languages though).

2. Use `+=` and its variants when possible:

        total = total + 5   # ok
        total += 5          # good!

        total = total - 5 + foo   # ok
        total -= 5 + foo          # good!

3. Use single quotes for strings -- only use double quotes when the
   string contains single quotes. (This is different for other
   languages.)

        'this is a string'
        'he typed "hello" into vim'
        "This is 'a double quote' moment"

### Naming conventions

These naming conventions are specific to Python. Other languages have
different conventions.

1. Variables, functions, and methods should be
   `lowercase_with_underscores`:

        def is_even(x):
            return x % 2 == 0

        num_dice = 5

2. Class names should be `CamelCase`:

        class Example:
            ...

        class SecondExample:
            ...
