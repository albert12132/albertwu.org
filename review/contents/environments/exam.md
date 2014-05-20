~ title: Environment Diagrams
~ level: exam

<block references>
* [Lecture: Names and Environments](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/03_1pp.pdf)
* [Lecture: Environments](http://inst.eecs.berkeley.edu/~cs61a/sp14/slides/05_1pp.pdf)
* [Discussion 1](http://inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion01.pdf)
* [Discussion 2](http://inst.eecs.berkeley.edu/~cs61a/sp14/disc/discussion02.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Environment Diagrams
--------------------

<question>

<env>
    def funny(joke):
        hoax = joke + 1
        return funny(hoax)

    def sad(joke):
        hoax = joke - 1
        return hoax + hoax

    funny, sad = sad, funny
    result = funny(sad(1))

    # pay special attention to the names of
    # the frames!
</env>

<question>

<env>
    def double(x):
        return double(x + x)

    first = double

    def double(y):
        return y + y

    result = first(10)
</env>

<question>

<env>
    def fun(fun):
        def time(time):
            return fun(x)
        x = 4
        return time

    def boo(x):
        return x**2
        x = 5

    result = fun(boo)(10)
</env>

<question>

<env>
    from operator import sub
    def trick(me, you):
        sub = treat
        return sub

    def treat(me, you):
        return sub(me, 1)

    treat = trick
    trick(3, 4)
</env>

<question>

<env>
    def easy(x):
        def peasy(y):
            def ironic(name):
                return name(x, y)
            return y
        return peasy

    result = easy(4)(easy)(2)
</env>

</block contents>
