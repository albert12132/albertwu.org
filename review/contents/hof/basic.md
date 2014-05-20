~ title: Higher-Order Functions
~ level: basic

<block references>
* [Lecture: Environments](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/05_1pp.pdf)
* [Lab 2](http://www-inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab02/lab02.php)
* [Discussion 2](http://www-inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion02.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What is the definition of a higher-order function?

<solution>

A function is a higher-order function if it satisfies at least one of
the following:

* It takes at least one function as an argument
* It returns a function

</solution>

<question>

In the following code, what type of object (number, boolean, string,
function) does `foo` return?  What type of object should `x`
be for this function to work?

    def foo(x):
        def inner(y):
            return x(y)
        return inner

<solution>

`foo` should return a **function** object (in particular, the function
`inner`).  `x` should also be a **function**, or else calling `inner`
will result in an error (because it will try `x(y)`).

</solution>


What would Python print?
------------------------

<question>

<prompt>
    >>> def silly():
    ...     def rabbit(y):
    ...         return 'Tricks are for kids!'
    ...     print('Lucky Charms?')
    ...     return False
    >>> a = silly()
    Lucky Charms?
    >>> a
    False
    >>> a(5)
    TypeError
</prompt>

<question>

<prompt>
    >>> def func1(fn):
    ...     def inner():
    ...         return fn(2)
    ...     return inner
    >>> def func2(fn):
    ...     def inner():
    ...         return fn(2)
    ...     return inner()
    >>> func1(lambda x: x * x)
    <function inner at ...>
    >>> func2(lambda x: x * x)
    4
</prompt>

<question>

<prompt>
    >>> def dream1(totem):
    ...     def dream2(totem_guess):
    ...         print('I think my totem is a', totem_guess)
    ...         return totem_guess == totem
    ...     return dream2
    >>> inception = dream1('top')
    >>> inception
    <function dream2 at ...>
    >>> inception('spinning top')
    I think my totem is a spinning top
    False
</prompt>

Environment Diagrams
--------------------

<question>

<env>
    def my_strat(score):
        return score + 2

    def play(strat):
        i, roll = 0, strat(0)
        while i < roll:
            result = my_strat(i)
            i += 1
        return i

    result = play(my_strat)

    # How many times do we call my_strat?
    # Remember to label the frames with the intrinsic
    # name of the functions
</env>

<question>

<env>
    def fun(x):
        return x**2

    def time(y):
        y, x = 4, 5
        def fun(y):
            return y + x
        return fun

    a = time(10)
    b = a(2)

    # Which fun is called?
    # Which y is used?
    # What type of object is a?
</env>

<question>

<env>
    def square(x):
        return x * x

    def boom(fn):
        def bam(x):
            print(x)
            return fn(x)
        return bam

    boom(square)
    a = boom(square)
    a(4)
</env>

<question>

<env>
    x = 4

    def outer(f):
        def inner(g):
            return f(g(x))
        return inner

    def square(x):
        return x**2

    c = outer(square)(square)
</env>

<question>

<env>
    def one(f):
        a = 1
        def two(g):
            b = 2
            def three(h):
                c = 3
                return f(a) + g(b) + h(c)
            return three
        return two

    def identity(x):
        return x

    def square(x):
        return x**2

    def cube(x):
        return x**3

    middle = one(identity)(square)
    result = middle(cube)

    # what function is middle?
    # What are the parents of each frame?
</env>

Code-Writing questions
----------------------

<question>

Write a function `make_mod` that takes a number, `n`, as an argument,
and returns a new function. The new function should take a single
argument, `x`, and return the result of `x` modulo `n`.

    def make_mod(n):
        """Returns a function that takes an argument x.
        That function will return x modulo n.

        >>> mod_7 = make_mod(7)
        >>> mod_7(3)
        3
        >>> mod_7(41)
        6
        """
        "*** YOUR CODE HERE ***"

<solution>

    def make_mod(n):
        def mod_n(x):
            return x % n
        return mod_n

</solution>

</block contents>
