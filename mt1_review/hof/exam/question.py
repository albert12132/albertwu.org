from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_question, make_print_question, make_env_question

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'exam'

references = [
    ('Lecture: Higher-Order Functions',),
    ('Discussion 2',),
    ('Discussion 3',),
    ('Discussion 3',),
]

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_question,
        lambda: env_questions),
    ('Code Writing', 'code',
        lambda: make_concept_question,
        lambda: code_questions),
    ('What would Python print?', 'print',
        lambda: make_print_question,
        lambda: print_questions),
]

concept_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
     'hint': None,
    },
]

print_questions = [
    {'prompts': [
            """x + 3""",
            """x + 2""",
        ]},
]

code_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
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
