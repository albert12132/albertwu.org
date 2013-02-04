
#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

contents = [
    ('Conceptual', 'conceptual',
        lambda: make_concept_solution,
        lambda: concept_solutions),
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
    ('Code Writing', 'code',
        lambda: make_code_solution,
        lambda: code_solutions),
    ('What would Python print?', 'print',
        lambda: make_print_solution,
        lambda: print_solutions),
]

concept_solutions = [
    {'explanation': """Solution explanation."""},
]

env_solutions = [
    {'link': 'link to online python tutor',
     'message': None,}
]

code_solutions = [
    {'code': """
Code solution.
""",
     'explanation': """Solution explanation.""",
    },
]

print_solutions = [
    {'answers': [
        """solution""",
        """solution""",
    ]},
]

#-------------------#
# Utility functions #
#-------------------#

def make_list(maker, lst):
    return '\n'.join(map(lambda args: maker(*args), lst))

def contents_li(name, hash_id, maker=None, lst=None):
    return '<li><a href="#' + hash_id + '">' + name + '</a></li>'

def make_section(sec):
    maker, lst = sec[2](), sec[3]()
    assert callable(maker), 'Not a valid maker'
    assert type(lst) == list, 'Not a valid question lsit'
    section = '<h2 class="subtopic" id="' + sec[1] + '">' + sec[0] \
        + '</h2>\n'
    for i, solution in enumerate(lst):
        section += maker(i+1, **solution) + '\n'
    return section

#--------------------#
# QUESTION COMPILERS #
#--------------------#

def make_concept_solution(num, explanation=''):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<p class="solution">' + explanation + '</p>\n'
    return solution

def make_env_solution(num, link='', message=None):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<a href="' + link + '">'
    solution += link if not message else message
    solution += '</a>\n'
    return solution

def make_code_solution(num, code='', explanation=None):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<pre class="codeblock">' + code + '</pre>\n'
    if explanation:
        solution += '<p class="solution">' + explanation + '</p>\n'
    return solution

def make_print_solution(num, answers=[]):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<pre class="codeblock">\n'
    for i, answer in enumerate(answers):
        solution += str(i+1) + ') ' + answer + '\n'
    return solution + '</pre>\n'

#-------------------#
# COMPILING STRINGS #
#-------------------#

contents_str = make_list(contents_li, contents)
solutions_str = '\n'.join(map(make_section, contents))

tag_names = {
    'title': title,               # title here
    'level': level,
    'contents': contents_str,     # table of contents
    'solutions': solutions_str,
}
