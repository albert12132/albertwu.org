~ title: Nonlocal
~ level: basic

<block references>
* [Albert's and Robert's
  lectures](https://docs.google.com/presentation/d/1PC5Yw-AxxOyTaPhZ-kJ0JvVMwaVCyVmBmWdiNqGZeVo/edit#slide=id.g5b71800b6_1_94)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Would this code work? If not, how would you fix it?

    def make_counter():
        count = 0
        def counter():
            count += 1
            return count
        return counter

<solution>

No, this code would not work. Here's how we can find out:

* The line `count += 1` is equivalent to `count = count + 1`, so we
  rewrite it as such.
* Python notices that `count` appears on the left side of an assignment
  statement, so Python remembers to treat `count` as a local variable.
* Python then begins executing the line. To compute `count + 1` Python
  must look up `count`.
* But Python had previously marked `count` as a local variable, and it
  doesn't have a value yet! So Python raises an error.

To fix it, add a nonlocal statement:

    def make_counter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

</solution>

<question>

Consider the following code:

    def fn1(bob):
        def fn2(alice):
            def fn3(alice):
                def fn4():
                    nonlocal bob, alice
                    return bob + alice
                return fn4
            return fn3
        return fn2

Answer the following questions:

1. In which function's frame does Python start looking for `alice`?
2. In which function's frame does Python stop looking for `alice`?
3. In which function's frame does Python start looking for `bob`?
4. In which function's frame does Python stop looking for `bob`?

<solution>

1. `fn3`
1. `fn3`
1. `fn3`
1. `fn1`

</solution>

<question>

Identify all the errors regarding nonlocal in the following code:

    bob = 2
    def fn1(bob):
        eve = 3
        def fn2(alice):
            nonlocal bob, alice
            eve = 4
            return eve + alice
        return fn2

<solution>

**`nonlocal alice`** is incorrect, since
`alice` is already defined in the same frame (as a
parameter to `fn2`).

**`eve = 4`** will NOT cause any errors,
since `eve` is not being referenced before
assignment.  However, because `eve` is not declared
as nonlocal, the `eve` in `fn1` will retain
the value of 3.

</solution>

Environment Diagrams
--------------------

<question>

<env>
    def make_counter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

    counter = make_counter()
    counter()
    counter()
</env>

<question>

<env>
    def foo():
        lst = []
        def bar(m):
            nonlocal lst
            lst = lst + [m]
            return lst
        return bar

    bar = foo()
    bar(3)
    bar(4)
</env>

<question>

<env>
    def foo():
        lst = []
        def bar(m):
            lst.append(m)
            return lst
        return bar

    bar = foo()
    bar(3)
    bar(4)
</env>

</block contents>
