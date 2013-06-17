~ title: Environment Diagrams ~

Environment Diagrams are a visual tool to keep track of bindings and
state of a computer program. In this class, we use Python as our
primary language, but the diagrams we teach can be applied to similar
languages.

Preface: a defense
------------------

Every semester, lots of students ask why we teach environment
diagrams. The simple answer is we think environment diagrams help
students learn the evaluation process of a computer program.

However, this usually isn't a satisfactory explanation, so here is an
attempt to address the more nuanced concerns of former (and current)
students.

**Disclaimer**: the answers provided are my own (Albert), and do not
necessarily reflect the views of the rest of the teaching staff.

* **Environment diagrams are too conceptual/not practical.**

  61A (and Computer Science in general) is not just about writing code
  -- it's about understanding *why* things work the way they do.
  Environment diagrams are very conceptual, but that fits into the
  goal of this course.

  As for practicallity, I admit that environment diagrams are more of
  a learning tool. They don't scale well to large programs.

* **This is a CS class. Why are we drawing things?**

  Environment diagrams provide a way to visualize the state of a
  program. I've found that having a physical diagram to look at helps
  students learn faster than having them stare at lines of code.

* **Environment diagrams are non-intuitive.**

  There might be two reasons why you find them difficult:

  1. You can't remember all the rules. If that's the case, just keep
     practicing and practicing. Also, keep in mind that these rules
     aren't arbitrary -- they reflect what a computer actually does.
     Each rule exists for a reason.
  2. You expect the program to behave differently than the diagram. In
     that case, you should take the time to really understand why each
     step occurs.

* **I can understand programs just fine. Why do I have to learn
  environment diagrams?**

  From a logistical perspective, the teaching staff needs a way to
  gauge how well students are learning. Having a uniform "system"
  makes it easier for us to do this.

  I understand that some students can "run the code in their head" and
  get the correct output. Unfortunately, on a test, by simply asking
  students to write the final output of a program, it is more likely
  that students will be able to guess the answer. That defeats the
  purppose of the exam, which is to see how well students understand
  the material, not how well they can guess.

* **Environment diagrams on exams are too difficult.**

  Sorry. We'll try to keep the tricks to a minimum.

  I agree that no sane programmer would write code as confusing as our
  exam questions. That being said, my opinion is if you can
  successfully evaluate something that complicated, you'll be able to
  handle anything you see in the real world.

* **I hate environment diagrams.**

  :(

Purpose
-------

Environment diagrams are designed to keep track of name bindings. In
other words, it acts as a sort of bookkeeping device: if you (or the
interpreter) wants to know what value is bound to a variable called
`foo`, an environment diagram will help you do that.

As programs grow more complex (with higher-order functions, nonlocal
state, etc.), environment diagrams are designed to provide a
systematic way to keep track of otherwise unclear effects.

Terminology
-----------

### Frames

A **frame** keeps track of variable-to-value bindings. Every function
call keeps track of its own set of bindings (e.g. it has its own
**scope**), so every *function call* has a corresponding frame.

The **global frame**, or "Global" for short, is the starting frame.
Global doesn't correspond to a specific function

Every frame except for Global has a **parent frame**. When function is
called, its corresponding frame immediately has a parent -- that
parent is the *frame in which that function was defined*. When doing
variable lookup, if you can't find a variable in the current frame,
you look in its parent.

Frames might also have **frame numbers**. These numbers are used to
label frames that are parents. If a frame is never a parent, it
doesn't have to have a number.

### Variables versus Values

A **variable** (or a **name**) is distinct from the **value** to which
it is assigned. For example, consider the following simple assignment:

    x = 3

The variable is `x`, and the value is `3`. Think of a variable as a
box with a label, and the value is the thing you put inside the box.

This distinction becomes especially important when it comes to
functions. Consider the following:

    def square(x):
        return x*x

In this case, the variable is `square`, and the value is *a function
object*. Remember, in Python, functions are objects just like
everything else, so they are distinct from the variable to which they
are bound.

### Arrows/Pointers

In some bindings, we draw **arrows** (or **pointers**) from the
variable to the value. This isn't just an arbitrary aesthetic design.
A pointer represents a *reference* to a value. We'll talk more about
this later.

Drawing diagrams
----------------

We'll be using the following code example throughout this document:

    ~~ linenums
    x = 3
    y = 1 + 2 + 3

    def square(x):
        return x*x

    def double(x):
        ans = x + x
        return ans

    square(y)
    result = square(double(x))

### Global Frame

Always start by drawing the Global frame. This occurs before any of
the code is executed (e.g. before `x = 3` is executed).

### Bindings

We draw **bindings** when one of the following occurs:

* variable assignment
* `def` statement
* `import` statement

There's a simple three-step process for drawing bindings:

1. **Evaluate the value** of the binding
2. In the current frame, **draw a small box with the value**
3. **Write the variable** to the left of the box

There is one small detail for the second step: if the value is a
**primitive**, we put it *in* the box; otherwise, we draw an arrow to
the object. Here are some examples of primitives and non-primitives:

* **Primitives** (draw *in* box):
    * numbers (`42`, `3.14`)
    * booleans (`True`, `False`)
    * Strings (`"hello world!"`)
* **Non-primitives** (draw arrow):
    * functions (`def square(x): ...`, `lambda x: x*x`)
    * tuples and lists (`(1, 2, 3)`, `[1, 2, 3]`)

Let's walk through the example. The first line is a variable
assignment:

    x = 3

where `x` is the variable and `3` is the value.

![x = 3]({{ NOTES_DIR }}/public/environments/x-equals-3.png)

The second line is a little more involved. There is a complex
expression on the right-hand side of the `=`, so we must *evaluate* it
first. Notice in the following diagram that `y` is bound to `6`, not
`1 + 2 + 3`:

![y = 1 + 2 + 3]({{ NOTES_DIR }}/public/environments/y-equals-6.png)

The next line is a `def` statement:

    def square(x):
        return x*x

Here, we are just *defining* a function -- we are **not** *calling*
the function. That makes sense; when you type in a `def` statement to
an interpreter, you don't execute the body of the function right away
(e.g. when you define `square`, you don't immediately calculate
`x*x`). Instead, we just make a **binding**.

![def square(x):]({{ NOTES_DIR }}/public/environments/def-square.png)

The variable is `square`, and the value is an arrow pointing to a
function object. Notice the *function object* also says `square` --
this is called its **intrinsic name**, and is a separate entity from
the *variable* -- even though, right now, they both say `square`, they
are distinct.

The second `def` statement behaves in the same way.

    def double(x):
        ans = x + x
        return ans

We create a binding, and we don't execute any part of the function
body (as expected):

![def double(x):]({{ NOTES_DIR }}/public/environments/def-double.png)

### Function calls

So far, we've only dealt with bindings, such as variable assignments
and `def` statements. Now, we will draw **function calls**. An example
of a function call is `square(y)`. There are five simple steps:

1. **Evaluate the operands**. If an operand is itself a function call,
   apply this procedure to it
2. **Draw a new frame**. Label it with the following:
    1. the function's **intrinsic name** at the top of the frame
    2. the frame's **parent** (the frame in which the function was
       defined), in the top-right corner. If the parent is Global, you
       don't have to write anything
    3. a **frame number** in the top-left corner -- this is only
       needed if there are nested functions.
3. **Bind formal parameters**. In step 1, you already evaluated and
   simplified the operands. Now you you just have to bind variables to
   those values.
4. **Execute the body of the function**. Depending on what you see,
   you'll be drawing more bindings or drawing new frames.
5. **Write the return value in the frame**. If the function doesn't
   return anything, write its return value as `None`.

Let's try the first function call in the example:

    square(y)

1. **Evaluate the operands**: the only operand is `y`. Since our
   current frame is still Global, we start looking in Global for the
   value of `y`, which is `6`.
2. **Draw a new frame**.
    1. The **intrinsic name** of the function is `square` (we know
       this from the *function object* on the right-hand side)
    2. Since the parent is Global, we don't need to label the parent
    3. Since `square` won't have any nested functions, we don't need
       to label the frame with a number
3. **Bind formal parameters**: looking at the `square` function
   object, we see it has one formal parameter, called `x`. In step 1,
   we evaluated the corresponding operand to have a value of `6`. Now
   we draw the binding:

   ![square(y)]({{ NOTES_DIR }}/public/environments/square-y.png)
4. **Execute the body of the function**. The body of `square` just
   says `return x*x`. There are no bindings and no function calls, so
   just compute `x*x`.

   Notice that this `x` is different than the one in Global. The `x`
   in `square` is called a **local variable**.

5. **Write the return value** (which is `6*6 = 36`):

   ![`return x*x`]({{ NOTES_DIR }}/public/environments/return-x-times-x.png)

And that's it! Once we're done with the function call, we exit the
frame, and our current frame becomes Global once more.

### Additional rules

* Don't draw frames for built-in functions like `add`, `mul`, `print`,
  etc.
* Variables should never have other variables as values

### A more complicated example

The last line gets more challenging.

    result = square(double(x))

Try drawing it on your own first by following the steps illustrated
above!

First, we're starting in the Global frame again (since we finished
calling `square`, we left its frame).

1. **Evaluate the value**. The value is `square(double(x))`, which is
   a function call:
    1. **Evaluate the operands**. The operand of `square` is
       `double(x)`, which is itself a function call:
        1. **Evaluate the operands**. The operand of `double` is `x`.
           Since we're in Global, the value of `x` is `3`.
        2. **Draw a new frame** for `double`.

        3. **Bind formal parameters**. `double`'s only parameter is
           `x`, and its operand is `3`, so bind `x` to `3` in the new
           frame. Your diagram should look like this now:

           ![`double(x)`]({{ NOTES_DIR }}/public/environments/double-x.png)
        4. **Execute the body of the function**.

           The first line binds `ans = x + x`
           1. **Evaluate the value**: `x + x` is `3 + 3`, so the
              value is `6`
           2. **Draw a box with the value**
           3. **Write the variable**, which is `ans`

           ![`ans = x + x`]({{ NOTES_DIR }}/public/environments/ans-equals-x-plus-x.png)
        5. **Write the return value**. The return value is `ans`,
           which is `6`.

           ![`return ans`]({{ NOTES_DIR }}/public/environments/return-ans.png)
    2. **Draw a new frame** for `square`
    3. **Bind formal parameters**. We saw in step 1 that `double(x)`
       is `6`. `square` has a single parameter called `x`, so we bind
       `x` to `6` in the new frame for `square`

       ![`square(double(x))`]({{ NOTES_DIR }}/public/environments/square-double-x.png)
    4. **Execute the body of the function**. `square` just says
       `return x*x`. Since `x` is `6`, `x*x = 36`
    5. **Write the return value**, which is `36`

       ![`return x*x`]({{ NOTES_DIR }}/public/environments/return-x-times-x2.png)
2. **Draw a box with the value**, which is `36`
3. **Write the variable**, which is `result`

   ![`result = square(double(x))`]({{ NOTES_DIR }}/public/environments/result-equals-square.png)
