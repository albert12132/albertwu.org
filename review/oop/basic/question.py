from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'OOP'
level = 'basic'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'Variables: Conceptual',
         'id': 'var-conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: var_concept_questions},
        {'name': 'Variables: What would Python print?',
         'id': 'var-print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: var_print_questions},
        {'name': 'Methods: Conceptual',
         'id': 'method-conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: meth_concept_questions},
        {'name': 'Methods: What would Python print?',
         'id': 'meth-print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: meth_print_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

var_concept_questions = [
    {'description': """Define each of the following terms: 1) Local variable, 2) Instance variable, 3) Class variable""",
        'solution': """<b>Local variable</b>: a variable that is only visible within the scope of a method. Once the method finishes executing, the local variable is erased.</p>

<p><b>Instance variable</b>: a variable that persists -- even after methods are done executing, these variables will still exist and retain their value.</p>

<ul>
    <li><b>Tip</b>: you can tell a variable is an instance variable if it has <tt>self.</tt> in front of it (e.g. <tt>self.name</tt>). Instance variable</li>
    <li>Instance variables can only be used within methods.</li>
    <li>Instance variables are unique to each instance of the class. They are not shared by instances.</li>
</ul>

<p><b>Class variable</b>: like instance variables, class variables also persist. However, class variables ARE shared by all instances of the class.</p>
<ul>
    <li>When initialized outside of methods (which is usually the case), the class variable has no "dot" modifier (e.g. just <tt>num_of_accounts</tt></li>
    <li>When referenced in methods, the class variable must be referenced with the following syntax: <tt>class_name.variable</tt> (e.g. <tt>Account.num_of_accounts)</tt></li>
</ul>"""
    },
    {'description': """For the following code, determine whether each of these variables are local, instance, or class variables:</p>
<ul>
    <li><tt>name</tt></li>
    <li><tt>self.name</tt></li>
    <li><tt>balance</tt></li>
    <li><tt>self.balance</tt></li>
    <li><tt>interest</tt></li>
    <li><tt>amt</tt></li>
    <li><tt>total</tt></li>
</ul>""",
        'code': """
class Account:
    interest = 0.02
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        total = self.balance + amt
        self.balance = total""",
        'solution': """
<ul>
    <li><tt>name</tt>: local</li>
    <li><tt>self.name</tt>: instance</li>
    <li><tt>balance</tt>: local</li>
    <li><tt>self.balance</tt>: instance</li>
    <li><tt>interest</tt>:class</li>
    <li><tt>amt</tt>: local</li>
    <li><tt>total</tt>: local</li>
</ul>""",
    },
    {'description': """For the code following code, let's say we want to have a variable that keeps track of all the Person objects ever created.
<ul>
    <li>What type of variable should this be? (local, instance, or class)</li>
    <li>Modify the code to initialize <tt>population</tt> to 0, and to increment it by 1 every time you create a new Person object.</li>
</ul>""",
        'code': """
class Person:
    def __init__(self, name):
        self.name = name""",
        'solution': """
<ul>
    <li>Class Variable</li>
    <li>New code:<pre class='prettyprint'>
class Person:
    <b>population = 0</b>
    def __init__(self, name):
        self.name = name
        <b>Person.population += 1</b></pre></li>
</ul>""",
    },
]

var_print_questions = [
    {'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
        ]},
]

meth_concept_questions = [
    {'description': """Define each of the following terms: 1) Local variable, 2) Instance variable, 3) Class variable""",
        'solution': """<b>Local variable</b>: a variable that is only visible within the scope of a method. Once the method finishes executing, the local variable is erased.</p>

<p><b>Instance variable</b>: a variable that persists -- even after methods are done executing, these variables will still exist and retain their value.</p>

<ul>
    <li><b>Tip</b>: you can tell a variable is an instance variable if it has <tt>self.</tt> in front of it (e.g. <tt>self.name</tt>). Instance variable</li>
    <li>Instance variables can only be used within methods.</li>
    <li>Instance variables are unique to each instance of the class. They are not shared by instances.</li>
</ul>

<p><b>Class variable</b>: like instance variables, class variables also persist. However, class variables ARE shared by all instances of the class.</p>
<ul>
    <li>When initialized outside of methods (which is usually the case), the class variable has no "dot" modifier (e.g. just <tt>num_of_accounts</tt></li>
    <li>When referenced in methods, the class variable must be referenced with the following syntax: <tt>class_name.variable</tt> (e.g. <tt>Account.num_of_accounts)</tt></li>
</ul>"""
    },
]

meth_print_questions = [
    {'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
        ]},
]

code_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    }
]

env_questions = [
    {'code': """
def code(test):
    return test
""",
'solution': 'hi',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

