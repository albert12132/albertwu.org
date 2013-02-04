from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution

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
