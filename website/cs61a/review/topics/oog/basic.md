~ title: Orders of Growth
~ level: basic

<block references>
* [Albert's and Robert's
  slides](https://docs.google.com/presentation/d/1cmJY7GNCTm4YqeEaS3Qp4U0PAGRPdoe1Akb05JOkgP4/edit)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual Questions
--------------------

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def one(n):
        for a in range(n):
            for b in range(n/2):
                for c in range(n/4):
                    print(a + b + c)

<solution>

&theta;(n<sup>3</sup>)

</solution>

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def two(n):
        for a in range(n):
            for b in range(1000000000):
                for c in range(n):
                    print(a + b + c)

<solution>

&theta;(n<sup>2</sup>)

</solution>

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def three(n):
        while n > 1:
            result = n * n
            print(result)
            n = n / 10
        return False

<solution>

&theta;(log*n*)

</solution>

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def four(lst):
        if len(lst) < 12345:
            return lst[0]
        return four(lst[1:])

<solution>

&theta;(n), where *n* is the length of the list.

</solution>

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def five(n):
        def helper(x):
            return x + n
        return helper(n/2)

<solution>

&theta;(1)

</solution>

<question>

What is the time complexity of this function in big-Theta (&theta;)
notation?

    def reverse(lst):
        if not lst:
            return []
        result = reverse(lst[1:])
        result.append(lst[0])
        return result

<solution>

&theta;(n), where *n* is the size of the list.

</solution>

</block contents>
