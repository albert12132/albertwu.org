~ title: Environment Diagrams
~ level: basic

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
    def square1(x):
        return x * x

    def square2(x):
        print(x * x)

    a = square1(3)
    b = square2(3)

    # How does return behave differently than print?
</env>

<question>

<env>
    def square(x):
        return x * x

    def sum_of_squares(x, y):
        return square(x) + square(y)

    result = sum_of_squares(3, 4)

    # How many times do we call mul?
    # How many frames do we draw for mul?
</env>

<question>

<env>
    from operator import add
    first = add(3, 4)

    def add(a, b):
        return a + b

    second = add(3, 4)

    # What changes between the first time we call add and the
    # second time? How does this affect our diagram?
</env>

<question>

<env>
    score, opp_score = 0, 0

    def assign(arg0, arg1):
        score = arg0
        opp_score = arg1
        return True

    success = assign(3, 9001)

    # But did we really succeed?
    # Did the global values of score and opp_score change?
</env>

<question>

<env>
    goal = 100

    def foo(x):
        y = x + goal
        return b

    result = foo(4)

    # What's the lookup procedure for goal?
    # Does result ever show up in the diagram?
</env>

<question>

<env>
    from operator import add, sub
    def a_plus_abs_b(a, b):
        if b < 0:
            op = sub
        else:
            op = add
        return op(a, b)

    result = a_plus_abs_b(4, -4)
</env>

</block contents>
