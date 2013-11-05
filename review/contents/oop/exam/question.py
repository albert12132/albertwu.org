from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'OOP'
level = 'exam'

references = [
    ('Lecture: Objects',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/15-Objects_1pps.pdf'),
    ('Lecture: Inheritance',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/16-Inheritance_1pps.pdf'),
    ('Discussion 6',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion06.pdf'),
    ('Lab 6',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab06/lab06.php'),
]

notes = ''

contents = [
    {'name': 'What would Python print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

print_questions = [
    {
        'description': """For the following questions, use the following
        class definition:""" + pre("""
class Account:
    \"\"\"A class computer account. Each account has a two-letter ID
    and the name of the student who is registered to the account.
    \"\"\"
    num_of_accounts = 0
    def __init__(self, id):
        self.id = id
        Account.num_of_accounts += 1

    def register(self, student):
        self.student = student
        print('Registered ' + student)

    @property
    def type(self):
        return type(self)""", classes='prettyprint'),

        'prompts': [
            ('acc_aa = Account("aa")',),
            ('acc_aa.register("Peter Perfect")', 'Registered Peter Perfect'),
            ('Account.register(self, "Jom Magrotker")', "NameError: 'self' is not defined"),
            ('Account.register(acc_aa, "Jom Magrotker")', "Registered Jom Magrotker"),
            ('Account.register("Jom Magrotker")', "TypeError: requires 2 arguments, since it's not a bound method"),
        ]
    },
    {
        'description': """Use the <tt>acc_aa</tt> from the previous
        question""",
        'prompts': [
            ('f1 = Account.register',),
            ('f1(acc_aa, "Peter Perfect")', 'Registered Peter Perfect'),
            ('f2 = acc_aa.register',),
            ('f2(acc_aa, "Peter Perfect")', 'TypeError: should only take one argument, since it is a bound method!'),
            ('f2("Peter Perfect")', 'Registered Peter Perfect'),
        ]
    },
    {
        'description': """Use the <tt>acc_aa</tt> from the previous
        question""",
        'prompts': [
            ('Account.register = lambda self: "WAT"',),
            ('Account.register(acc_aa, "Hello")', 'TypeError: should only take one argument, self (but it is not a bound method!)'),
            ('Account.register("Hello")', "'WAT' # self is 'Hello'"),
            ('acc_aa.register("goodbye")', "TypeError: should only take one argument, given 2 (acc_aa, 'goodbye')"),
            ('acc_aa.register()', "'WAT'"),
        ]
    },
    {
        'description': """Assume you have started a new Python
        interactive session with the original definition of the
        <tt>Account</tt> class.""",
        'prompts': [
            ('acc_aa = Account("aa")',),
            ('acc_aa.register("Peter Perfect")', 'Registered Peter Perfect'),
            ('acc_zz = Account("zz")',),
            ('acc_aa.register = acc_zz.register',),
            ('acc_aa.register("Bozo")', 'Registered Bozo'),
            ('acc_aa.student', "'Peter Perfect'"),
            ('acc_zz.student', "'Bozo'"),
        ]
    },
]

code_questions = [
    {
        'description': """Write a <tt>Chef</tt> class with the
        following qualities:""" + ul(contents=(
            """Each <tt>Chef</tt> is initialized with a list of
            required ingredients. Each item in the list is added to
            a storage that is shared by all the <tt>Chef</tt>s with an
            initial stock of 2. If the item is already in the storage,
            do NOT add it in again.""",
            """Each <tt>Chef</tt> can <tt>fetch_ingredients</tt> from
            a storage that is shared by all the <tt>Chef</tt>s. Each
            <tt>Chef</tt> only needs 1 of each ingredient.""",
            """Each <tt>Chef</tt> can <tt>serve</tt>, where they put
            their finished food in a shared list of <tt>finished</tt>
            foods.""",
        )) + """For finer details of implementation, see the
        doctest.""",
        'code': """
class Chef:
    \"\"\"Doctests:

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
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,

        'solution': """
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
        self.cooked = False"""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

