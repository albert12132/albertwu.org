from utils.utils import *
from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Nonlocal'
level = 'basic'

references = [
        'Lecture: Mutable Data',
        'Lab 6',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker q': make_env_question,
         'maker s': make_env_solution,
         'questions': lambda: env_questions},
]

concept_questions = [
        {'description': """Would this code work? If not, how would you
            fix it?""",
     'code': """
def make_counter():
    count = 0
    def counter():
        count += 1
        return count
    return counter""",
    'solution': """No, this code would not work. Here's how we can find
    out:""" + ol(make_list([
        """The line <tt>count += 1</tt> is equivalent to <tt>count =
        count + 1</tt>, so we rewrite it as such.""",
        """Python notices that <tt>count</tt> appears on the left side
        of an assignment statement, so Python remembers to treat
        <tt>count</tt> as a local variable.""",
        """Python then begins executing the line. To compute
        <tt>count + 1</tt> Python must look up <tt>count</tt>.""",
        """But Python had previously marked <tt>count</tt> as a local
        variable, and it doesn't have a value yet! So Python raises
        an error.""",
        ])) + """To fix it, add a nonlocal statement:""" + pre("""
def make_counter():
    count = 0
    def counter():
        <b>nonlocal count</b>
        count += 1
        return count
    return counter""", classes='prettyprint')
    },

]

print_questions = [
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

