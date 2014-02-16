from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'OOP Below-the-line'
level = 'basic'

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
    {'description': """Answer the following questions about <tt>make_class(attributes, base_class=None)</tt>:""" + utils.ol((
        'What type of built-in Python object does <tt>make_class</tt> return? What are its entries?',
        'What is <tt>attributes</tt>? What kind of entries does this object contain?',
        'What is <tt>base_class</tt> used for? What does it mean if <tt>base_class</tt> is <tt>none</tt>?'
        )),
    'solution': utils.ol((
        '<tt>make_class</tt> returns a dictionary. This dispatch dictionary contains 3 entries:' + prettify("""
{'get' : <function get_value ...>,  # gets an attribute
 'set' : <function set_value ...>,  # sets an attribute
 'new' : <function new ...>       } # creates an instance"""),

        '<tt>attributes</tt> is a dictionary of methods and class attributes. For example:' + prettify("""
{'__init__'   : <function __init__ ...>,
 'population' : 1,
 'greet'      : <function gret ...>     }"""),

        '<tt>base_class</tt> is the class from which this class inherits. If <tt>base_class</tt> is <tt>None</tt>, it means this class does not inherit.'
        )),
    },

    {'description': """Answer the following questions about <tt>make_instance(cls)</tt>:""" + utils.ol((
        'What type of built-in Python object does <tt>make_instance</tt> return? What are its entries?',
        'What is <tt>cls</tt>? Which function can generate such an object?',
        'Where is <tt>make_instance</tt> called?',
        )),
    'solution': utils.ol((
        '<tt>make_instance</tt> returns a dictionary. This dispatch dictionary contains 2 entries:' + prettify("""
{'get' : <function get_value ...>,  # gets an attribute
 'set' : <function set_value ...>}  # sets an attribute"""),

        '<tt>cls</tt> is a dispatch dictionary returned by <tt>make_class</tt>',

        '<tt>make_instance</tt> is called inside the <tt>init_instance</tt> function.',
        )),
    },

    {'description': """Answer the following questions about <tt>init_instance(cls, *args)</tt>:""" + utils.ol((
        'How is <tt>init_instance</tt> different from <tt>make_instance</tt>?',
        'Where is <tt>init_instance</tt> called? What does it do (conceptually)?',
        )),
    'solution': utils.ol((
        "<tt>make_instance</tt> just creates an empty 'shell' (an instance dispatch dictionary with no instance attributes). The <tt>init_instance</tt> function calls <tt>make_instance</tt> to create an instance, then fills up the instance with attributes by calling the class's <tt>__init__</tt> method."

        '<tt>init_instance</tt> is called in the <tt>new</tt> function of <tt>make_class</tt>. <tt>init_instance</tt>, conceptually, acts the same way as a constructor.',
        )),
    },

    {'description': """Answer the following questions about <tt>bind_method(value, instance)</tt>:""" + utils.ol((
        'Is <tt>value</tt> guaranteed to be a function?',
        'What is <tt>instance</tt>?',
        'What is <tt>method</tt> (defined inside of <tt>bind_method</tt>?',
        )),
    'solution': utils.ol((
        "<tt>value</tt> is NOT guaranteed to be a function. In fact, the <tt>bind_method</tt> function has an <tt>if/else</tt> to check for this. If <tt>value</tt> is NOT a function, <tt>bind_method</tt> just returns it.",

        '<tt>instance</tt> is a dispatch dictionary returned by <tt>init_instance</tt>. It acts the same way as <tt>self</tt>.',

        "<tt>method</tt> is a function that does the exact same thing as <tt>value</tt> (if it is a function), except that it is <i>bound</i> to <tt>instance</tt>. In other words, it does the same thing <tt>value</tt> would do if <tt>instance</tt> was always <tt>value</tt>'s first argument."
        )),
    },
]

code_questions = [
    {'description': """Translate the following code, which uses Python's built-in class system, into code that uses our below-the-line OOP implementation.""",
     'code': """
class Computer:
    def __init__(self, op_sys):
        self.op_sys = op_sys
        self.software = []

    def boot(self):
        print('Booting ' + self.op_sys)

    def install(self, software):
        self.software.append(software)
        print(software + ' installed!')""",
    'solution': """
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
    return Computer"""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

