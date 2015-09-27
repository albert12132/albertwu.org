~ title: Lambda Expressions
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1K4a54Qp716fWcGaTLDAyAYv-CCBy4p6P66M97eTAFgI/edit#slide=id.ga22ca5c9c_0_367)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What are some differences between `def` statements and `lambda`
expressions?

<solution>

Some differences between lambdas and def statements include:

* lambdas are expressions (they are a value), while defs are
  statements.
* lambdas can only be one liners
* lambdas are anonymous -- they have no intrinsic names

</solution>

<question>

What are the intrinsic names of the following functions?

    def cube(x):
        return x * x * x

    square = lambda x: x * x

<solution>

The first function has an intrinsic name of `cube`. The second function
does not have an intrinsic name, since it is a lambda. **Note** that
the intrinsic name is the name you should write in your environment
diagram frames!

</solution>

What would Python print?
------------------------

<question>

<prompt>
    >>> lambda x: x * x
    <function <lambda > at ...>
    >>> g = lambda x: x**2'
    >>> g(4)
    16
    >>> (lambda x, y: x * y)(4, 5)
    20
</prompt>


Code-Writing questions
----------------------

<question>

Translate the following def statements into lambda expressions.

    # 1
    def square(x):
        return x * x

    # 2
    def compose(f, g):
        def h(x):
            return f(g(x))
        return h

<solution>

    # 1
    square = lambda x: x * x

    # 2
    compose = lambda f, g: lambda x: f(g(x))

</solution>

<question>

Translate the following lambda expressions into def statements.

    # 1
    pow = lambda x, y: x**y

    # 2
    foo = lambda x: lambda y: lambda z: x + y * z

<solution>

    # 1
    def pow(x, y):
        return x**y

    # 2
    def foo(x):
        def f(y):
            def g(z):
                return x + y * z
            return g
        return f

</solution>

Environment Diagrams
--------------------

<question>

<env>
    square = lambda x: x * x
    higher = lambda f: lambda y: f(f(y))

    higher(square)(5)
</env>

<question>

<env>
    a = (lambda f, a: f(a))(lambda b: b * b, 2)
</env>

</block contents>
