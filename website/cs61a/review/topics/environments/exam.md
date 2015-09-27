~ title: Environment Diagrams
~ level: exam

<block references>
* [Albert's and Robert's slides part
  1](https://docs.google.com/presentation/d/1p6rgyp4_lPLT6mtOdyKQ1VsuZOuiqaUIVYSm2c7CCu8/edit#slide=id.ga1f0264d1_0_49)
* [Albert's and Robert's slides part
  2](https://docs.google.com/presentation/d/1RijXoFtQxe2zdl6dYzwn0KMTW8gXiP7MMQgKd-MHXBo/edit#slide=id.g5a5e1377d_0_448)
* [Albert's and Robert's slides part
  3](https://docs.google.com/presentation/d/1K4a54Qp716fWcGaTLDAyAYv-CCBy4p6P66M97eTAFgI/edit#slide=id.ga22ca5c9c_0_294)
* [Albert's and Robert's slides part
  4](https://docs.google.com/presentation/d/11-75T8zaVP1V2rwADDDtyt77hX-LKIeUu1hPMmfGXME/edit#slide=id.ga271ab36d_0_45)
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
