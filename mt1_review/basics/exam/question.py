
#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

references = [
    ('Reference 1',),
    ('Reference 2',),
]

contents = [
    ('Conceptual', 'conceptual',
        lambda: make_concept_question,
        lambda: concept_questions),
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
# Utility functions #
#-------------------#

def make_list(maker, lst):
    return '\n'.join(map(lambda args: maker(*args), lst))

def references_li(name):
    return '<li>' + name + '</li>'

def contents_li(name, hash_id, maker=None, lst=None):
    return '<li><a href="#' + hash_id + '">' + name + '</a></li>'

def make_section(sec):
    maker, lst = sec[2](), sec[3]()
    assert callable(maker), 'Not a valid maker'
    assert type(lst) == list, 'Not a valid question lsit'
    section = '<h2 class="subtopic" id="' + sec[1] + '">' + sec[0] \
        + '</h2>\n'
    for i, question in enumerate(lst):
        section += maker(i+1, **question) + '\n'
    return section

#--------------------#
# QUESTION COMPILERS #
#--------------------#

def make_concept_question(num, description='', code=None, hint=None):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<p>' + description + '</p>\n'
    if code:
        question += '<pre class="codeblock">' + code + '</pre>\n'
    if hint:
        question += '<p class="hint"><b>Hint</b>: ' + hint + '</p>\n'
    return question

def make_print_question(num, prompts=[]):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<pre class="codeblock">\n'
    for line in prompts:
        question += '&gt;&gt;&gt; ' + line + '\n______\n'
    return question + '</pre>\n'

def make_env_question(num, code=''):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<pre class="codeblock">' + code + '</pre>\n'
    return question

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
