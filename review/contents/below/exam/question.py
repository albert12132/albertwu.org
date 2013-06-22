from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'OOP Below-the-line'
level = 'exam'

references = [
    'Reference 1',
    'Reference 2',
]

notes = 'The code for the below-the-line OOP is <a href="oop.py">here</a> for reference.'

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker': make_code_question,
         'questions': lambda: code_questions},
]

concept_questions = [
    {'description': """Consider what would happen if we took out the <tt>new</tt> function in the <tt>make_class</tt> function. Would we still be able to create instances of classes? If so, how would we do it?""",

    'solution': """Yes, we can still create instances of classes. You would have to explicitly call <tt>init_instance</tt>:""" + pre("""
init_instance(ExampleClass, arg1, arg2)""",
classes='prettyprint'),
    },

    {'description': """What would happen if we changed the <tt>get_value</tt> function in <tt>make_instance</tt> to the following (changes are bolded)? How would this change the way we call "methods"?""",
     'code': """
def get_value(name):
    if name in attributes:
        return attributes[name]
    else:
        value = cls['get'](name)
        <b>return value</b>""",

    'solution': """Methods would never get bound to instances. We would still be able to call methods, but we would have to pass in the instance explicitly whenever we called them:""" + pre("""
# original
inst['get']('method1')(arg1, arg2)

# after change
inst['get']('method1')(inst, arg1, arg2)""",
classes='prettyprint')
    },

    {'description': """What would happen if the <tt>attributes</tt> dictionary passed to the <tt>make_class</tt> function did not contain an <tt>__init__</tt> method? Consider two cases: 1) <tt>base_class</tt> is <tt>None</tt>; 2) <tt>base_class</tt> is something other than <tt>None</tt>.""",
    'solution': """There are two cases:""" + utils.ol((
        """<tt>base_class</tt> is <tt>None</tt>: this class doesn't inherit from anything, so there would be no <tt>__init__</tt> method available to it. As such, it will have no instance attributes upon creation.""",
        """<tt>base_class</tt> is not <tt>None</tt>: this class can use its superclass's <tt>__init__</tt> method. Notice in <tt>make_class</tt>'s <tt>get_value</tt> function, there is an <tt>elif</tt> clause that will look in the superclass if <tt>name</tt> is not found.""",
        ))
    },

    {'description': """What would happen if we changed the <tt>get_value</tt> function in <tt>make_instance</tt> to the following (changes are bolded):""",
     'code': """
def get_value(name):
    if name in attributes:
        return attributes[name]
    else:
        <b>return None</b>""",

    'solution': """Instances would have no way of looking in the class for unfound attributes. This means we would not be able to retrieve class variables or methods.""",
    },
]

code_questions = [
    {'description': """Translate the following code, which uses Python's built-in class system, into code that uses our below-the-line OOP implementation.""",
     'code': """
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
            print("Sorry!")""",
    'solution': """
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
                            base_class)""",
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

