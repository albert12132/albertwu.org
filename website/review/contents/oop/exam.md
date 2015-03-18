~ title: OOP
~ level: exam

<block references>
* [Lecture: Objects](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/15-Objects_1pps.pdf)
* [Lecture: Inheritance](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/16-Inheritance_1pps.pdf)
* [Discussion 6](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion06.pdf)
* [Lab 6](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab06/lab06.php)
</block references>

<block notes>
</block notes>

<block contents>

What would Python print?
------------------------

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
            print('Registered ' + student)

        @property
        def type(self):
            return type(self)

<question>

<prompt>
    >>> acc_aa = Account("aa")
    >>> acc_aa.register("Peter Perfect")
    Registered Peter Perfect
    >>> Account.register(self, "Jom Magrotker")
    NameError: 'self' is not defined
    >>> Account.register(acc_aa, "Jom Magrotker")
    Registered Jom Magrotker
    >>> Account.register("Jom Magrotker")
    TypeError: requires 2 arguments, since it's not a bound method
</prompt>

<question>

Use the `acc_aa` from the previous question.

<prompt>
    >>> f1 = Account.register
    >>> f1(acc_aa, "Peter Perfect")
    Registered Peter Perfect
    >>> f2 = acc_aa.register
    >>> f2(acc_aa, "Peter Perfect")
    TypeError: should only take one argument, since it is a bound method!
    >>> f2("Peter Perfect")
    Registered Peter Perfect
</prompt>

<question>

Use the `acc_aa` from the previous question.

<prompt>
    >>> Account.register = lambda self: "WAT"
    >>> Account.register(acc_aa, "Hello")
    TypeError: should only take one argument, self (but it is not a bound method!)
    >>> Account.register("Hello")
    'WAT' # self is 'Hello'
    >>> acc_aa.register("goodbye")
    TypeError: should only take one argument, given 2 (acc_aa, 'goodbye')
    >>> acc_aa.register()
    'WAT'
</prompt>

<question>

Assume you have started a new Python interactive session with the
original definition of the `Account` class.

<prompt>
    >>> acc_aa = Account("aa")
    >>> acc_aa.register("Peter Perfect")
    Registered Peter Perfect
    >>> acc_zz = Account("zz")
    >>> acc_aa.register = acc_zz.register
    >>> acc_aa.register("Bozo")
    Registered Bozo
    >>> acc_aa.student
    'Peter Perfect'
    >>> acc_zz.student
    'Bozo'
</prompt>

Code-Writing questions
----------------------

<question>

In computer science, a [circular buffer](http://en.wikipedia.org/wiki/Circular_buffer)
a type of data structure that is used to store temporary, sequential
data in a constant amount of space (this is commonly used to buffer
data streams) in a first-in-first-out manner (the first element to be
added is the first element to be removed). A circular buffer has the
following properties:

* Each buffer has a fixed size of `n` elements (e.g. strings). This
  size is determined upon creation of the buffer. Note that the total
  number of elements that can be inserted into the buffer can exceed
  `n`, but the number of elements in buffer at *any given time* must
  be less than or equal to `n`.
* Each buffer has a `start` that keeps track of the earliest element
  that is currently in the buffer.  Similarly, each buffer has a `end`
  that keeps track of the most recent element that is currently in the
  buffer.
* The buffer has a `append` method, which adds a given element into the
  buffer. If the buffer is full, (i.e. the buffer already has `n`
  elements), do not add the element, and instead print "Buffer exceeded
  capacity".
* The buffer has a `remove` method, which removes the earliest element
  that is still in the buffer. If there are no elements in the buffer,
  print "Buffer is empty".

In order to implement the `append` and `remove` methods, you should
have list of length `n` that stores the elements currently in the
buffer. When you append the *i*th element, you should insert it into
index (*i* mod *n*) of the list. Similarly, when you are removing the
*j*th element, you should extract the element at index (*j* mod *n*) of
the list. For more descriptions of the behavior, see the doctest.

    class CircularBuffer:
        """Doctests:

        >>> buffer = CircularBuffer(3)
        >>> buffer.remove()
        Buffer is empty
        >>> buffer.append('a')
        >>> buffer.remove()
        'a'
        >>> buffer.remove()
        Buffer is empty
        >>> buffer.append('b')
        >>> buffer.append('c')
        >>> buffer.append('d')
        >>> buffer.append('e')
        Buffer capacity exceeded
        >>> buffer.remove()
        'b'
        >>> buffer.remove()
        'c'
        >>> buffer.remove()
        'd'
        >>> buffer.remove()
        Buffer is empty
        """
        def __init__(self, n):
            self.array = [None]*n   # list of length n
            self.n = n
            self.start = 0
            self.end = 0

        def append(self, elem):
            "*** YOUR CODE HERE ***"

        def remove(self):
            "*** YOUR CODE HERE ***"

<solution>

    class CircularBuffer:
        def __init__(self, n):
            self.array = [None]*n   # list of length n
            self.n = n
            self.start = 0
            self.end = 0

        def append(self, elem):
            if self.end - self.start == self.n:
                print('Buffer capacity exceeded')
            else:
                self.array[self.end % self.n] = elem
                self.end += 1

        def remove(self):
            if self.end == self.start:
                print('Buffer is empty')
            else:
                elem = self.array[self.start % self.n]
                self.start += 1
                return elem

</solution>

<question>

Write a `Chef` class with the following qualities:

* Each `Chef` is initialized with a list of required ingredients. Each
  item in the list is added to a storage that is shared by all the
  `Chef`s with an initial stock of 2. If the item is already in the
  storage, do NOT add it in again.
* Each `Chef` can `fetch_ingredients` from a storage that is shared by
  all the `Chef`s. Each `Chef` only needs 1 of each ingredient.
* Each `Chef` can `serve`, where they put their finished food in a
  shared list of `finished` foods.

For finer details of implementation, see the doctest.

    class Chef:
        """Doctests:

        >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
        >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
        >>> ramsay.cook()
        'Not enogh ingredients!'
        >>> ramsay.serve()
        'No food to serve!'
        >>> ramsay.fetch_ingredients()     # 1 salt remaining
        "Fetched: ['meat', 'bbq sauce', 'salt']"
        >>> ramsay.cook()
        'Cooked steak!'
        >>> ramsay.serve()
        >>> Chef.finished
        ['steak']
        >>> albert.fetch_ingredients()     # 0 salt remaining
        "Fetched: ['egg', 'cheese', 'cream', 'salt']"
        >>> albert.cook()
        'Cooked quiche!'
        >>> albert.serve()
        >>> Chef.finished
        ['steak', 'quiche']
        >>> ramsay.fetch_ingredients()
        'No more salt!'
        """
        "*** YOUR CODE HERE ***"

<solution>

    class Chef:
        storage = {}
        finished = []

        def __init__(self, food, ingredients):
            self.food, self.ingredients = food, ingredients
            self.fetched, self.cooked = False, False
            for elem in self.ingredients:
                Chef.storage[elem] = 2

        def fetch_ingredients(self):
            for elem in self.ingredients:
                if Chef.storage[elem] == 0:
                    return 'No more ' + elem + '!'
                Chef.storage[elem] -= 1
            self.fetched = True
            return 'Fetched: ' + str(self.ingredients)

        def cook(self):
            if self.fetched:
                self.cooked, self.fetched = True, False
                return 'Cooked ' + self.food + '!'
            return 'Not enough ingredients!'

        def serve(self):
            if not self.cooked:
                return 'No food to serve!'
            Chef.finished.append(self.food)
            self.cooked = False

</solution>

</block contents>
