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
        return x + x

    result = square(y)
    square(double(x))

### Global Frame

Always start by drawing the Global frame. This occurs before any of
the code is executed (e.g. before `x = 3` is executed).

### Bindings

We draw **bindings** when one of the following occurs:

* variable assignment
* `def` statement
* `import` statement

There's a simple three-step process for drawing bindings:

1. In the current frame, **draw a small box**
2. **Evaluate the value** of the binding and **draw the result in the
   box**
3. **Write the variable** to the left of the box

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
