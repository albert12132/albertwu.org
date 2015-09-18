~ title: Orders of Growth
~ level: exam

<block references>
* [Lecture: Orders of Growth](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/18-Growth_1pps.pdf)
* [Discussion 7](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion07.pdf)
</block references>

<block notes>
This [link](http://www-inst.eecs.berkeley.edu/~cs61a/su12/lab/lab04/lab04.php)
(from the Summer 2012 version of 61A) has some practice problems
for orders of growth. Take a look!
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

Find the time complexity of `main` in big-Theta (&theta;) notation.

    def helper(x):
        for i in range(x):
            print(i)
        return x

    def main(n):
        if n == 2:
            return 0
        else:
            return helper(n - 1) + helper(n - 2)

<solution>

&theta;(n)

</solution>

<question>

Find the time complexity of `bar` in big-Theta (&theta;) notation.

    def foo(x):
        for i in range(x):
            for j in range(x):
                print(x)

    def bar(n):
        while n > 0:
            foo(100000)
            n -= 1

<solution>

&theta;(n)

</solution>

<question>

Find the time complexity of `funny` in big-Theta (&theta;) notation.

    def joke(n):
        for i in range(n**2):
            print(i)

    def funny(n):
        for i in range(n**2):
            print(joke(100))
        return 'haha'

<solution>

&theta;(n<sup>2</sup>)

</solution>

</block contents>
