~ title: Lambda Expressions
~ level: exam

<block references>
* [Lecture: Functions and Expressions](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/02_1pp.pdf)
* [Lecture: Environments](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/05_1pp.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Code-Writing questions
----------------------

<question>

Fill in the blanks for the following expression so that `result` is the
number 42.

    x = lambda x, y: lambda: x - y
    result = (lambda ____, question: one(__________)(x, 4)

<solution>

    result = (lambda one, question: one(46, question)())(x, 4)

</solution>

<question>

Fill in the blanks for the following expression so that `result` is the
boolean True.

    x = lambda x: lambda y: x(y)
    result = (lambda ______: x(fair)(dice))(lambda fair: fair == 3, 3)

<solution>

    result = (lambda fair, dice: x(fair)(dice))(lambda fair: fair == 3, 3)

</solution>

<quesiton>

Fill in the blanks for the following expression so that each call to
`mapper` prints the output displayed below:

    >>> def mapper(fn, num):
    ...     i = 0
    ...     while i < num:
    ...         print(fn(i))
    ...         i = i + 1
    >>> mapper(lambda x: ______, 4)
    1
    3
    5
    7
    >>> mapper(lambda x: ______, 5)
    -2
    -1
    0
    1
    2
    >>> mapper(lambda x: ______, 5)
    0
    -1
    1
    -2
    2

<solution>

    mapper(lambda x: 2 * x + 1, 4)
    mapper(lambda x: x - 2, 5)
    mapper(lambda x: (x + 1) * (-1) ** x // 2, 5)

</solution>

Environment Diagrams
--------------------

<question>

<env>
    f = lambda x: lambda y: lambda z: g(x + y + z)

    g = f(3)
    f(4)(5)(6)
</env>

<question>

<env>
    fn = lambda f, a: f(f(2*a))

    result = fn(lambda x: x*x, 2)
</env>

<question>

<env>
    fn = lambda: lambda: print('hi')

    def example(x):
        print('example')
        return x

    result = example(fn())()
</env>

</block contents>
