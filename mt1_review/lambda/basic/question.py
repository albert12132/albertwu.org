from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_question, make_print_question, make_env_question

#---------#
# CONTENT #
#---------#

title = 'Lambda Expressions'
level = 'basic'

references = [
    ('Lecture: Environments and Lambda',),
    ('Lab 3',),
    ('Discussion 3',),
]

contents = [
    ('Conceptual', 'conceptual',
        lambda: make_concept_question,
        lambda: concept_questions),
    ('What would Python print?', 'print',
        lambda: make_print_question,
        lambda: print_questions),
    ('Environment Diagrams', 'env',
        lambda: make_env_question,
        lambda: env_questions),
    ('Code Writing', 'code',
        lambda: make_concept_question,
        lambda: code_questions),
]

concept_questions = [
    {'description': """What are some differences between <tt>def</tt>
statements and <tt>lambda</tt> expressions?""",
     'code': None,
     'hint': None,
    },
]

print_questions = [
    {'prompts': [
        """lambda x: x * x""",
        """g = lambda x: x**2
g(4)""",
        """(lambda x, y: x * y)(4, 5)""",
        ]},
]

code_questions = [
    {'description': """Translate the following def statements into
lambda expressions.""",
     'code': """
# 0
def square(x):
    return x * x

# this one is done for you
# square = lambda x: x * x

# 1
def double(f):
    def inner(x):
        return f(f(x))
    return double

# 2
def 

""",
     'hint': None,
    }
]

env_questions = [
    {'code': """
def code(test):
    return test
"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

contents_str = make_list(contents_li, contents)
references_str = make_list(references_li, references)
questions_str = '\n'.join(map(make_section, contents))

tag_names = {
    'title': title,               # title here
    'level': level,
    'references': references_str, # references
    'contents': contents_str,     # table of contents
    'questions': questions_str,
}
