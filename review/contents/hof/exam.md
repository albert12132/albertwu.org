~ title: Higher-Order Functions
~ level: exam

<block references>
* [Lecture: Environments](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/05_1pp.pdf)
* [Lab 2](http://www-inst.eecs.berkeley.edu/~cs61a/sp14/lab/lab02/lab02.php)
* [Discussion 2](http://www-inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion02.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Environment Diagrams
--------------------

<question>

<env>
    def f(x):
        return lambda y: x(y)

    def g(x):
        return lambda : f(x) + f(y)

    y = 2
    result = f(g(f))
</env>

<question>

<env>
    def always_roll(n):
        return lambda s0, s1: n

    def make_bad_strategy(p):
        def strategy(s0, s1):
            # next line is bad style!
            return always_roll(1 - p)(s0, s1)
        return strategy

    num_rolls = make_bad_strategy(1)(50, 50)
</env>

<question>

<env>
    def test(fn):
        def new_fn(x):
            if x > 10:
                return new_fn(x % 10)
            else:
                return fn(x)
        return new_fn
    x = 10
    new = test(lambda score: score - x)
    new(42)
</env>

<question>

<env>
    x = 4
    def foo(foo):
        def bar(y):
            y += foo
            return lambda : y + x
        foo += 3
        return bar
    x = 5
    foo(5)(4)()
</env>

<question>

<env>
    def dream1(f):
        kick = lambda x: mind()
        def dream2(secret):
            mind = f(secret)
            kick(2)
        return dream2

    inception = lambda secret: lambda: secret
    real = dream1(inception)(42)
</env>

<question>

<env>
    def albert(albert):
        albert = albert()
        def albert():
            albert = lambda albert: albert
            return albert(albert)
        return albert

    albert(lambda: albert)()
</env>

</block contents>
