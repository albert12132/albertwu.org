~ title: Object Oriented Programming

Introduction
------------

**Object Oriented Programming** is a programming paradigm (i.e. a way
of organizing code) that is supported in many different programming
languages, such as Python.

Understanding OOP is not just about learning the syntax (although that
is a big part of it). Having an intuition about design philosphy is
also essential for OOP.

If you have programmed in another object-oriented programming
language, see the section about [comparisons between Java and
Python](#java-a-comparison).

Terminology
-----------

In this section, we will use the following Python class as an example:

    class Computer(object):
        population = 0

        def __init__(self, owner, operating_system):
            self.owner = owner
            self.operating_system = operating_system
            Computer.population += 1

        def boot(self):
            print('Starting up', self.operating_system)
            time = 10
            while time > 0:
                print(time)
                time -= 1

Here's a list of terminology we will be covering:

* [class](#term-class)
* [object / instance](#term-object)
* [constructor](#term-constructor)
* [method](#term-method)
* [local variable](#term-local-variable)
* [instance variable](#term-instance-variable)
* [class variable](#term-class-variable)

### Basics ###

A <span id='term-class'>**class**</span> is like a blueprint that
is used to create an object. In this case, we have a class that is
used to create a `Computer`.

An <span id='term-object'>**object**</span> is an **instance** of a
class. For example, the code above tells Python *how* to build a
`Computer`, but it won't actually create a new `Computer`. To create
objects, you use the following syntax:

    my_computer = Computer('Albert', 'Linux')

The left side is just a variable assignment -- nothing new. On the
right side, it looks like we are calling `Computer` as if it was a
function. This is known as the <span
id='term-constructor'>**constructor**</span> of an object. In general,
the syntax for creating objects is

    ClassName(args)

### Methods ###

One question you might have is, where is the constructor defined?
Take a look at `__init__` definition in the `Computer` class:

    def __init__(self, owner, operating_system):
        ...

It looks like we're defining a function. When we use a `def`
statement inside of a `class`, we create a method. A <span
id='term-method'>**method**</span> is very much like a function -- we
can call it with arguments, and it performs some computations. The
only difference is that a method is tied to the class. To see what
this means, consider the following code:

    my_computer = Computer('Albert', 'Linux')
    my_computer.boot()

The second line is how we call the `boot` method. This will print out
"`Starting up Linux`", followed by a countdown. Notice the syntax we
use: we put the instance (`my_computer`), followed by a dot (`.`),
then the method name (`boot`). Just like with functions, we call
methods with parentheses.

You might be wondering why we passed in zero arguments to `boot`, when
it looks like it should take in one:

    def boot(self):
        ...

The `self` argument refers to the object that is calling `boot` -- in
this case, `self` is `my_computer`. The dot notation *implicitly*
passes in `my_computer` as `self`, so we don't have to put it as an
argument when we call `boot`. We'll talk more about this later.

In Python, the **`__init__`** method is a special method that is
used as the constructor for an object. For example, when we create a
`Computer` object like this

    my_computer = Computer('Albert', 'Linux')

we are really calling the `__init__` method. `'Albert'` gets bound to
the `owner` parameter, and `'Linux'` gets bound to the
`operating_system` parameter.

### Variables ###

There are three types of variables:

* Local variables
* Instance variables
* Class variables

Which type a variable belongs to depends on the syntax with which it
is created.

#### Local Variables ####

A <span id='term-local-variable'>**local variable**</span> exists only
in the local frame of a method. For example, the variable `time` in
the `boot` method is a local variable. Notice that it looks just like
a normal variable. When `boot` is called, the local variable `time` is
initialized to `10`, and decremented until it reaches `0`. Once we
finish calling `boot`, `time` gets discarded along with the local
frame for `boot`.

Here's a list of instance variables in the `Computer` class:

* Inside `__init__`:
    * `self`
    * `owner` (not to be confused with `self.owner`)
    * `operating_system` (not to be confused with
      `self.operating_system`)
* Inside `boot`:
    * `self`
    * `time`

#### Instance Variables ####

An <span id='term-instance-variable'>**instance variable**</span> has
a couple of properties:

* **persists across method calls**: unlike a local variable, an
  instance variable retains its most recent value even after a method
  call finishes.
* **each instance has its own instance variables**: an instance
  variable for one instance might have a different value for another
  instance. Each instance keeps track of its own instance variables.

Notice in the `__init__` method that we create two instance variables:
`self.owner` and `self.operating_system`. Instance variables are
always preceded by `self.`. This means the variable `self.owner` is a
different variable than `owner` -- they just happen to have similar
names.

The first property (persistence) is demonstrated with the
`self.operating_system` instance variable. When we call `__init__`,
`self.operating_system` is assigned to `'Linux'` (in the case of
`my_computer`). When we call `boot`, the value of
`self.operating_system` is still `'Linux'`.

The second property is demonstrated with the following:

    computer1 = Computer('Albert', 'Linux')
    computer2 = Computer('Robert', 'Mac')

For `computer1`, the `self.owner` instance variable is assigned to
`'Albert'`. The `self.owner` variable for `computer2` is different, as
it is assigned to `'Robert'`.

Here's a list of instance variables in the `Computer` class:

* `self.owner`
* `self.operating_system`

#### Class Variables ####

The final type of variable is called a <span
id='term-class-variable'>**class variable**</span>, also known as a
**static variable**. A class variable has the following properties:

* **persists across method calls**: just like an instance variable
* **same for all instances**: every instance shares the same class
  variable.

Like instance variables, class variables have persistent state. The
difference between the two is that class variables are shared by all
instances of the class. In the `Compter` class, the `population`
variable is a class variable, and has an initial value of `0`. To
illustrate this, consider the following:

    computer1 = Computer('Albert', 'Linux')   # population is now 1
    computer2 = Computer('Robert', 'Mac')     # population is now 2

Notice that, every time we create a new `Computer`, the `population`
class variable is incremented by `1`.

Syntax
------

### Defining classes ###

Now that we know the terminology associated with OOP, we have to know
how to use it.

To define a **class**, we do the following:

    class ClassName(object):
        ...

By convention, class names are written in
[CamelCase](http://en.wikipedia.org/wiki/CamelCase) (e.g. `ClassName`
as opposed to `class_name`). Don't worry about the `object` part yet
-- we'll explain that when we talk about [inheritance](#inheritance).

To create **methods**, use a `def` statement inside the class:

    class ClassName(object):

        def method_name(self, args):
            ...

The first argument of every method must be a reference to the
instance (we don't talk about static methods in this class). This
parameter is, by convention, called `self`. You can technically call
it anything you want, but you shouldn't. Other than that, writing a
method is just like writing a normal function.

The **`__init__`** method, as mentioned above, is used to construct
objects of that class:

    class ClassName(object):

        def __init__(self, args):
            ...

You *must* put two underscores (`_`) before and after `init`,
otherwise Python will not be able to find `__init__`.

To call a method inside of another method, use dot notation:

    class ClassName(object):

        def method1(self, arg):
            self.method2(arg, 10)

        def method2(self, arg1, arg2):
            return arg1 + arg2

We call `method2` from within `method1`. Notice the `self.` notation.

To create a **class variable**, we usually put the variable
declaration at the top of the class:

    class ClassName(object):
        class_variable = 9001

        def __init__(self, args):
            ClassName.class_variable -= 10

Notice that, when declaring the `class_variable` outside of a method,
we just put the variable name without dot notation (i.e.
`class_variable` as opposed to `ClassName.class_variable`). If we
access the class variable from *inside* a method, we need to use dot
notation (i.e. `ClassName.class_variable`, as opposed to
`class_variable`). Notice we put the name of the class before the dot.

**Instance variables** must be accessed inside of methods. This is
because we need a `self` variable, and `self` is a local variable
defined inside of methods. Here is some sample syntax using instance
variables:

    class ClassName(object):

        def method(self, arg):
            self.instance_variable = arg
            local_variable = self.instance_variable + 4
            return self.instance_variable / local_variable

### Using a class ###

To create an instance of a class, we use this syntax:

    ClassName(args)

Keep in mind that the **constructor** calls the `__init__` method. The
`object` in

    class ClassName(object):
        ...

has nothing to do with the arguments passed into the constructor.

To call an instance's **method**, use dot notation:

    instance = ClassName(arg1, arg2)
    instance.method1(foo)

You can also access **instance variables** with similar syntax:

    x = instance.instance_variable
    instance.instance_variable = 5

The first line just gets the value associated with
`instance_variable`. The second line reassigns the `instance_variable`
to 5 (remember that every isntance keeps its own copy of instance
variables).

To access **class variables**, use the following syntax:

    ClassName.class_variable = 4
    x = ClassName.class_variable

Inheritance
-----------

A powerful feature of OOP is **inheritance**. The idea is that a class
can "inherit" methods and variables from another class. We can use
this to create a *hierarchy* of classes. For example:

* Animal
    * Mammal
        * Dog
        * Cat
    * Fish
        * Shark

Notice that each sublist is a more specific version of its
predecessor (e.g. Dogs are a more specific type of Mammal).

We can implement this inheritance in code like this:

    class Animal(object):
        ...

    class Mammal(Animal):
        ...

    class Dog(Mammal):
        ...

    class Cat(Mammal):
        ...

Notice that we put class names inside the parentheses. For example,
`class Mammal(Animal)` reflects the fact that `Mammal`s are a more
specific type of `Animal`. We call `Mammal` the **subclass** (the
inheriting class) and `Animal` the **superclass** (the inherited
class).

When a subclass inherits from a superclass, the subclass has access to
all the methods of the superclass. Consider the following example:

    class A(object):
        def method1(self, arg):
            print('hi')

    class B(A):
        ...

When we create a `B` object, we will be able to do the following:

    b = B()
    b.method1(4)

The second line will print out `hi`. Notice that, even though we don't
define `method1` explicitly in `B`, we can still call it. When looking
for `b.method1`, Python will first look in the `B` class for a method
call `method1`. If it can't find one (as in this case), it looks in
the superclass (`A`) for `method1`.

This is useful for writing concise code -- we don't need to repeat
something we've already written.

### Overriding methods ###

If we want a subclass to have a method that shares the same name as a
superclass method, we can **override** that method:

    class A(object):
        def method1(self, arg):
            print(arg)

    class B(A):
        def method1(self):
            print('hello')

Both `A` and `B` have a method called `method1`. Consider the
following example:

    b = B()
    b.method1()

When Python looks for `b.method1`, it looks in the current class first
(i.e. `B`). Because it's able to find `method1` in `B`, it immediately
uses that version of `method1`. That's why the second line takes 0
arguments and always prints `hello`.

You can also call a superclass method, even if you override it:

    class A(object):
        def method1(self, arg):
            print(arg)

    class B(A):
        def method1(self):
            A.method1(self, 'hello')

The last line introduces syntax for calling a superclass method. We
use dot notation, where the superclass name (`A`) precedes the dot.
Also notice that, when we call `A.method1`, we have to *explicitly*
pass in `self` as the first argument.

**Note 1**: this implementation of `B` will also print out `hello`,
just like in the previous implementation. The only difference is that
this implementation calls the superclass method.

**Note 2**: we don't cover `super()` in this class. If you're
interested, see
[this](http://docs.python.org/3.1/library/functions.html#super).

### `object` ###

You'll undoubtedly have noticed the `object` in most of our class
definitions:

    class ClassName(object):
        ...

What is `object`? Notice the syntax is the same as if we were using
inheritance. In fact, that's exactly what is happening: when we put
`object` there, we inherit from the `object` class.

`object` is the superclass of all classes in Python -- all classes
inherit from `object`. The `object` class has some general methods
defined, such as `__init__`.

Design Principles
-----------------

In addition to understanding the terminology and syntax of OOP, we
also need to understand some design principles for OOP. The power of
OOP comes from several qualities:

* **data abstraction**: classes can be used to represent literally any
  object the programmer wants. In addition, selectors and constructors
  are logically grouped inside of classes
* **inheritance**: class hierarchies and method overriding can make
  code more concise, and in some cases make class behavior more
  intuitive
* **Polymorphism and interfaces**: method overriding allows methods of
  the same name to do different things. This means other programmers
  need only use one method to achieve different behavior for different
  types of objects (it's easier just to remember one method name and
  makes code cleaner)

With that being said, here are some fundamental design principles.
These principles apply to any object-oriented language, not just
Python.

### Use inheritance whenever possible ###

If you find that two or more classes share a lot of the same code, you
can make one class the superclass. This way, the other classes can
just inherit methods, making your code concise.

In addition to aesthetiscm, there is a practical use to inheritance.
If you need to update a method (to make it more efficient, do
something different, etc.) that is shared by many classes, inheritance
allows you to change it in just one class. If you don't use
inheritance, you'll have to go through each class that shares that
method -- this makes it easier to make mistakes! For this reason,
inheritance makes code maintenance a lot easier.

Consider the following example:

    class Animal(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Mammal(Animal):
        def __init__(self, name, age):
            self.name = name
            self.age = age

Notice that the `__init__` method of both classes takes exactly the
same arguments, and also creates the exact same instance variables.
Using inheritance, we could omit the `__init__` definition in the
`Mammal` class completely!

### Call superclass methods when possible ###

This is similar to the first principle. Instead of duplicating code
inside of a method, just call the superclass method instead:

    class Animal(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Pet(Animal):
        def __init__(self, name, age, owner):
            self.name = name
            self.age = age
            self.owner = owner

In this example, defining an `__init__` in `Pet` is necessary, since
it takes in one more argument than `Animal`, and also creates another
instance variable. However, we can call the superclass method to make
this more concise:

    class Animal(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Pet(Animal):
        def __init__(self, name, age, owner):
            Animal.__init__(self, name, age)
            self.owner = owner

Don't forget to pass in `self` when calling a superclass method.

### Instance vs. Class variables ###

Deciding whether a variable should be an instance variable or a class
variable is an important consideration. Part of it depends on the
programmer and the application, but there are some general guidelines:

* If a variable is different for every instance of a class, it should
  be an instance variable
* If a variable is always the same for every instance, it should be a
  class variable

### Methods vs. Variables ###

In general, methods can be thought of as "actions", while variables
can be thought of as "data." For example, consider the following
class:

    class Dog(object):
        def __init__(self, age):
            self.age = age

        def bark(self):
            return 'woof!'

Notice that `bark` is a method, even though it always returns the same
thing (`'woof!'`), because `bark`ing is an action. Conversely, `age`
is an instance variable because it is piece of information about the
`Dog`.

Other Features
--------------

Python includes a variety of features for OOP, some of which are
shared by other languages, some of which are not.

### Variable lookup ###

When we ask Python to lookup a variable like this:

    my_instance.variable

where `my_instance` is an instance of a class, Python will first look
for an instance variable called `variable`. If it finds one, it just
uses that.

If Python can't find an instance variable by that name, it will look
for a class variable called `variable`. If it can't find one, Python
looks in the superclass for a class variable called `variable`. Python
continues this process until it hits `object`, at which point it
raises an `AttributeError` to signal that it couldn't find that
variable.

### Property methods ###

Python supports a feature called **property methods**. Consider the
following code:

    class A(object):

        @property
        def age(self):
            ...

The `@property` decorator labels the `age` method as a property
method. Now when we want to use `age`, we access it *as if it were a
variable*, not a method:

    a = A()
    x = a.age
    y = a.age()   # Error!

Notice that you cannot call a property method.

Property methods are useful for a number of reasons:

* **Data protection**: you cannot reassign a property method. This
  prevents other users from tampering with your classes (e.g. you
  can't do `a.age = 5` in the code above)
* **Polymorphism**: say an external program is interacting with many
  different classes, some of which have `age` as an instance variable,
  some of which have `age` as a property method. The fact that `age`
  is a property method for some classes makes no difference for the
  external program, since it access `age` the same way it does an
  instance variable.

### Static methods ###

We don't talk about static methods in 61A, but they do exist in
Python. In Python, there is a distinction between **static methods**
and **class methods**. Each one is created with a decorator:

    class A(object):

        def normal_method(self, arg):
            ...

        @staticmethod
        def static_method(arg):
            ...

        @classmethod
        def class_method(cls, arg):
            ...

Compare each type of method with the normal method. The static method
does not take in a `self`, and thus has no way to reference the
instance. You can call static methods by using dot notation, with the
class name preceding the dot:

    A.static_method(4)
    a = A()
    a.static_method(4)  # Error!

Class methods also do not take in a `self`, so they don't have access
to the instance. However, they do take in a `cls`, which is a
reference to the class. To call a class method, you can use dot
notation with either an instance or the class:

    A.class_method(4)
    a = A()
    a.class_method(4)

### Multiple Inheritance ###

We don't talk about multiple inheritance in 61A, but Python does
support it. When defining a class, you can make it inherit from
multiple superclasses:

    class Sub(Sup1, Sup2, Sup3):
        ...

Python allows an arbitrary number of superclasses.

Multiple inheritance gets complicated when two or more superclasses
have methods of the same name. Python (version 3 and beyond) resolves
name conflicts by always looking at superclasses from left to right.
For example, if `Sup1` and `Sup3` both have a method called `method`,
Python will use `Sup1`'s version of `method`.

Java: a comparison
------------------

If you have programmed in Java, you will be familiar with many of the
OOP concepts present in Python. There are some differences however:

* **There is no `this` in Python.** `self` is a close equivalent, but
  `self` is *always* required, whereas `this` in Java is optional.
* **`self` is always required in non-static methods in Python.**
  Furthermore, `self` is actually bound to an object.
* **Variables and methods can be dynamically created in Python.** If
  an attribute was not created in the `__init__`, it can still be
  created inside of other methods, or even by external programs.
* **There are no protection modifiers in Python.** There isn't a
  formal way to declare a variable `private`; in other words, all
  variables are public. There is a partial remedy: if a variable name
  begins with two underscores and ends with at most one underscore,
  Python *name-mangles* the variable so that it has a different name.
  If an external program can guess the new name (which is easy to do),
  it will still have access to the variable.
* **When a variable is declared in Python, it must be immediately
  initialized with a value**. This is true of Python variables in
  general.
* **There are no final variables in Python.**
* **There is no method overloading.** A name can be bound to only one
  method at a time. There's a partial remedy to this in the form of
  default arguments.
* **Methods and variables share the same namespace.** That means a
  method and an instance/class variable cannot share the same name.
* **super behaves differently in Python**. There is a `super`
  function, but its syntax is different than `super` in Java.
* **There are no abstract classes in Python.**
* **Only class names are CamelCase in Python**. Methods and variables,
  by convention, should use `lower_case_and_underscores`.
* **Python supports multiple inheritance.**
