~ title: OOP Below-the-line
~ level: basic

<block references>
</block references>

<block notes>
The code for the below-the-line OOP is [here](/public/source/review/oop.py) for reference.
</block notes>

<block contents>

Concept Questions
-----------------
Answer the following questions about `make_class(attributes, base_class=None)`:

1. What type of built-in Python object does `make_class` return? What
   are its entries?
2. What is `attributes`? What kind of entries does this object contain?
3. What is `base_class` used for? What does it mean if `base_class` is
   `none`?

<solution>

1. `make_class` returns a dictionary. This dispatch dictionary contains
   3 entries:

        {'get' : <function get_value ...>,  # gets an attribute
         'set' : <function set_value ...>,  # sets an attribute
         'new' : <function new ...>       } # creates an instance

2. `attributes` is a dictionary of methods and class attributes. For
   example:

        {'__init__'   : <function __init__ ...>,
         'population' : 1,
         'greet'      : <function gret ...>     }

3. `base_class` is the class from which this class inherits. If
   `base_class` is `None`, it means this class does not inherit.

</solution>

<question>

Answer the following questions about `make_instance(cls)`:

1. What type of built-in Python object does `make_instance` return?
   What are its entries?
2. What is `cls`? Which function can generate such an object?
3. Where is `make_instance` called?

<solution>

1. `make_instance` returns a dictionary. This dispatch dictionary
   contains 2 entries:

        {'get' : <function get_value ...>,  # gets an attribute
         'set' : <function set_value ...>}  # sets an attribute

2. `cls` is a dispatch dictionary returned by `make_class`
3. `make_instance` is called inside the `init_instance` function.

</solution>

<question>

Answer the following questions about `init_instance(cls, *args)`:

1. How is `init_instance` different from `make_instance`?
2. Where is `init_instance` called? What does it do (conceptually)?

<solution>

1. `make_instance` just creates an empty 'shell' (an instance dispatch
   dictionary with no instance attributes). The `init_instance`
   function calls `make_instance` to create an instance, then fills up
   the instance with attributes by calling the class's `__init__`
   method.
2. `init_instance` is called in the `new` function of `make_class`.
   `init_instance`, conceptually, acts the same way as a constructor.

</solution>

<question>

Answer the following questions about `bind_method(value, instance)`:

1. Is `value` guaranteed to be a function?
2. What is `instance`?
3. What is `method` (defined inside of `bind_method`?

<solution>

1. `value` is NOT guaranteed to be a function. In fact, the
   `bind_method` function has an `if/else` to check for this. If
   `value` is NOT a function, `bind_method` just returns it.
2. `instance` is a dispatch dictionary returned by `init_instance`. It
   acts the same way as `self`.
3. `method` is a function that does the exact same thing as `value` (if
   it is a function), except that it is *bound* to `instance`. In
   other words, it does the same thing `value` would do if `instance`
   was always `value`'s first argument.

</solution>

Code-writing Questions
----------------------

<question>

Translate the following code, which uses Python's built-in class
system, into code that uses our below-the-line OOP implementation.

    class Computer:
        def __init__(self, op_sys):
            self.op_sys = op_sys
            self.software = []

        def boot(self):
            print('Booting ' + self.op_sys)

        def install(self, software):
            self.software.append(software)
            print(software + ' installed!')

<solution>

    def make_computer_class():
        def __init__(self, op_sys):
            self['set']('op_sys', op_sys)
            self['set']('software', [])

        def boot(self):
            print('Booting ' + self.op_sys)

        def install(self, software):
            self['get']('software').append(software)
            print(software + ' installed!')

        Computer = make_class({'__init__': __init__,
                             'boot'     : boot,
                             'install'  : install  })
        return Computer

</solution>

</block contents>
