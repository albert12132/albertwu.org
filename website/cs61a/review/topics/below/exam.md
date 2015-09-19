~ title: OOP Below-the-line
~ level: exam

<block references>
</block references>

<block notes>
The code for the below-the-line OOP is [here](/public/source/review/oop.py) for reference.
</block notes>


<block contents>

Concept Questions
-----------------

<question>

Consider what would happen if we took out the `new` function in the
`make_class` function. Would we still be able to create instances of
classes? If so, how would we do it?

<solution>

Yes, we can still create instances of classes. You would have to explicitly call `init_instance`:

    init_instance(ExampleClass, arg1, arg2)

</solution>

<question>

What would happen if we changed the `get_value` function in
`make_instance` to the following? How would this change the way we call
"methods"?

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return value   # this line changed

<solution>

Methods would never get bound to instances. We would still be able to
call methods, but we would have to pass in the instance explicitly
whenever we called them:

    # original
    inst['get']('method1')(arg1, arg2)

    # after change
    inst['get']('method1')(inst, arg1, arg2)

</solution>

<question>

What would happen if the `attributes` dictionary passed to the
`make_class` function did not contain an `__init__` method? Consider
two cases: 1) `base_class` is `None`; 2) `base_class` is something
other than `None`.

<solution>

There are two cases:

1. `base_class` is `None`: this class doesn't inherit from anything, so
   there would be no `__init__` method available to it. As such, it
   will have no instance attributes upon creation.
2. `base_class` is not `None`: this class can use its superclass's
   `__init__` method. Notice in `make_class`'s `get_value` function,
   there is an `elif` clause that will look in the superclass if `name`
   is not found.

</solution>

<question>

What would happen if we changed the `get_value` function in
`make_instance` to the following:

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            return None    # this line changed

<solution>

Instances would have no way of looking in the class for unfound
attributes. This means we would not be able to retrieve class variables
or methods.

</solution>

Code-Writing Questions
----------------------

<question>

Translate the following code, which uses Python's built-in class
system, into code that uses our below-the-line OOP implementation.

    class Shop:
        def __init__(self, inventory):
            self.inventory = inventory

        def sell(self, item):
            if item in self.inventory and self.inventory[item] > 0:
                self.inventory[item] -= 1
                return item
            else:
                print("No " + item + " in inventory!")

    class AppleStore(Shop):
        def sell(self, item):
            product = Shop.sell(self, item)
            if product is None:
                print("Would you like to preorder?")

        def fix_product(self, item):
            if item in self.inventory:
                print("We can fix that!")
            else:
                print("Sorry!")

<solution>

    def make_shop_class():
        def __init__(self, inventory):
            self['set']('inventory', inventory)

        def sell(self, item):
            if item in self['get']('inventory') and \
                       self['get']('inventory')[item] > 0:
                self['get']('inventory')[item] -= 1
                return item
            else:
                print("No " + item + " in inventory!")

        Shop = make_class({'__init__' : __init__, 'sell': sell})
        return Shop

    def make_applestore_class(base_class=make_shop_class()):
        def sell(self, item):
            product = base_class['get']('sell')(self, item)
            if product is None:
                print("Would you like to preorder?")

        def fix_product(self, item):
            if item in self['get']('inventory'):
                print("We can fix that!")
            else:
                print("Sorry!")

        AppleStore = make_class({'sell': sell,
                                 'fix_product' : fix_product},
                                base_class)

</solution>

</block contents>
