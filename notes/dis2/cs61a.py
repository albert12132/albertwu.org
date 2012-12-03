# 1
def foo(n):
    def bar():
        return n
    return bar
f = foo(23)
g = foo(23)
foo == bar
_____

# 2
def swap(a, b):
    temp = a
    a = b
    b = temp
x, y = 3, 4
swap(x, y)
x
___
y
___

# 3
from operator import mul
def fooply(x):
    x = 3
    def garple(x):
        print("first")
        return mul(x, 3)
    print("second")
    return garple
fooply(5)(7)
_____
_____
_____

# 4
def outer(x, y):
    def inner():
        return x*y
    return inner()
a = outer(3, 4)
a
____
def outer(x, y):
    def inner():
        return x*y
    return inner
a = outer(3, 4)
a
____

# 5
nest = lambda f, x: lambda y: f(x, y)
nest(nest, print)("hello")("world")
_____

# 6
def albert(albert):
    albert = albert(albert)
    def albert():
        return albert
    return (lambda albert: albert)(albert())
albert(lambda albert: albert)

