~ title: OOP
~ level: basic

<block references>
* [Albert's and Robert's slides (Pokemon
  examples!)](https://docs.google.com/presentation/d/1MgFiiLa1xtQ4LfGOFZ0McvifBh0F5RaLZ23B5E1cRyQ/edit)
* [Albert's and Robert's slides (inheritance)](https://docs.google.com/presentation/d/1KlUU5wxUvSig1q4ZXoe_ujSn9zSfp-ehzBvzaX19KPM/edit)
</block references>

<block notes>
</block notes>

<block contents>

Variables: Conceptual Questions
-------------------------------

<question>

Define each of the following terms:

1. Local variable
2. Instance variable
3. Class variable

<solution>

1. **Local variable**: a variable that is only visible within the scope
   of a method. Once the method finishes executing, the local variable
   is erased.
2. Instance variable: a variable that persists -- even after methods
   are done executing, these variables will still exist and retain
   their value.
    * **Tip**: you can tell a variable is an instance variable if it
    has `self.` in front of it (e.g.  `self.name`).
    * Instance variables can only be used within methods.
    * Instance variables are unique to each instance of
      the class. They are not shared by instances.
3. Class variable: like instance variables, class variables also
   persist. However, class variables ARE shared by all instances of the
   class.
    * When initialized outside of methods (which is usually the case),
      the class variable has no "dot" modifier (e.g. just
      `num_of_accounts`
    * When referenced in methods, the class variable must
      be referenced with the following syntax: `class_name.variable`
      (e.g.  `Account.num_of_accounts)`

</solution>

<question>

Consider the following code:

    class Account:
        interest = 0.02
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance

        def deposit(self, amt):
            total = self.balance + amt
            self.balance = total

Determine whether each of these variables are local, instance, or class
variables:

1. `name`
2. `self.name`
3. `balance`
4. `self.balance`
5. `interest`
6. `amt`
7. `total`

<solution>

1. `name`: local
2. `self.name`: instance
3. `balance`: local
4. `self.balance`: instance
5. `interest`: class
6. `amt`: local
7. `total`: local

</solution>

<question>

Consider the following code:

    class Person:
        def __init__(self, name):
            self.name = name

Let's say we want to have a variable that keeps track of all the Person
objects ever created.

* What type of variable should this be? (local, instance, or class)
* Modify the code to initialize `population` to 0, and to increment it
  by 1 every time you create a new Person object.

<solution>

This would be a **class variable**. The new code would look like this:

    class Person:
        population = 0
        def __init__(self, name):
            self.name = name
            Person.population += 1

</solution>

Variables: What would Python print?
-----------------------------------

For the following questions, use the following class definition:

    class Account:
        """A class computer account. Each account has a two-letter ID
        and the name of the student who is registered to the account.
        """
        num_of_accounts = 0
        def __init__(self, id):
            self.id = id
            Account.num_of_accounts += 1

        def register(self, student):
            self.student = student
            print('Registered!')

        @property
        def type(self):
            return type(self)

<question>

<prompt>
    >>> self.id
    NameError
    >>> acc_aa = Account("aa")
    >>> acc_aa.id
    'aa'
    >>> acc_aa.student
    AttributeError (self.student not defined yet)
    >>> acc_aa.register("Peter Perfect")
    Registered!
    >>> acc_aa.student
    'Peter Perfect'
    >>> num_of_accounts
    NameError
    >>> Account.num_of_accounts
    1
    >>> acc_aa.num_of_accounts
    1
    >>> acc_zz = Account("zz")
    >>> Account.num_of_accounts
    2
    >>> acc_aa.num_of_accounts
    2
    >>> acc_zz.num_of_accounts
    2
    >>> acc_aa.num_of_accounts = 100
    >>> acc_aa.num_of_accounts
    100
    >>> acc_zz.num_of_accounts
    2
    >>> Account.num_of_accounts
    2
    >>> Account.num_of_accounts = 9001
    >>> acc_aa.num_of_accounts
    100
    >>> acc_zz.num_of_accounts
    9001
</prompt>

Methods: Conceptual Questions
-----------------------------

<question>

Here is the same `Account` class from the previous section:

    class Account:
        """A class computer account. Each account has a two-letter ID
        and the name of the student who is registered to the account.
        """
        num_of_accounts = 0
        def __init__(self, id):
            self.id = id
            Account.num_of_accounts += 1

        def register(self, student):
            self.student = student
            print('Registered!')

        @property
        def type(self):
            return type(self)

Why is it that, when I call `acc_aa.register('me')` no errors will be
raised, even though I didn't pass in an argument for `self`?

<solution>

The dot notation will implicitly pass `acc_aa` into `type` as `self`.
This is known as a **bound method**. Another way to think about it is
that `acc_aa.register` acts like a curried function

    >>> acc_aa.register = curry2(Account.register)(acc_aa)
    >>> acc_aa.register('me')
    Registered!

</solution>

<question>

Can a method have the same name as a variable?

<solution>

No; in python, variables and methods share the same namespace, so
variable and method names can collide if you aren't careful.

</solution>

<question>

What does the `@property` decorator do?

<solution>

The `@property` decorator allows you to use the affected method to
be accessed like a variable. For example, the following method

    >>> class Example:
    ...     @property
    ...     def foo(self):
    ...         return 3""") + """can be accessed like
    ...         this:""" + prettify("""
    >>> a = Example()
    >>> a.foo
    3

</solution>

Methods: What would Python print?
---------------------------------

For the following questions, use the `Account` class defined below:

    class Account:
        """A class computer account. Each account has a two-letter ID
        and the name of the student who is registered to the account.
        """
        num_of_accounts = 0
        def __init__(self, id):
            self.id = id
            Account.num_of_accounts += 1

        def register(self, student):
            self.student = student
            print('Registered!')

        @property
        def type(self):
            return type(self)

<question>

<prompt>
    >>> acc_aa = Account("aa")
    >>> acc_aa.register
    <bound method Account.register ...>
    >>> Account.register
    <function register at ...> # (not a bound method!)
    >>> acc_aa.register(self, "Peter Perfect")
    NameError
    >>> acc_aa.register("Peter Perfect")
    Registered!
    >>> acc_aa.type()
    TypeError
    >>> acc_aa.type
    <class '__main__.Account'>
    >>> acc_aa.type = "Nothing"
    AttributeError
</prompt>

</block contents>

