~ title: Newton's method
~ level: basic

<block references>
* [Lecture: Newton's method](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/06_1pp.pdf)
</block references>

<block notes>
We will be using the implementation of Newton's method and
iterative improvement from lecture:

    # iterative improvement framework

    def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess

    def approx_eq(x, y, tolerance=1e-5):
        return abs(x - y) < tolerance

    # Newton's method

    def make_derivative(f, delta=1e-5):
        def derivative(x):
            df = f(x + delta) - f(x)
            return df / delta
        return derivative

    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

    def find_zero(f, df):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero)""")

</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Describe what iterative improvement is and how it works.

<solution>

Iterative improvement is a programming technique that involves updating
an initial guess until it comes close enough to the correct solution.
Iterative improvement algorithms have two major components: an
`update` function; and an `close` function (which tells you
when you can stop).

</solution>

<question>

Conceptually, what is the `update` function for Newton's method? What
is the `close` function for Newton's method?

    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

    # the following is defined inside find_zero
    def near_zero(x):
        return approx_eq(f(x), 0)

<solution>

`newton_update` is not the actual update function -- instead,
depending on what `f` is given, it will create an `update` function
that follows the mathematical equation for Newton's Method.
`near_zero` is the `close` function, and returns True when `f(x)` is
approximately equal to 0 -- this is the goal of Newton's method.

</solution>

</block contents>
