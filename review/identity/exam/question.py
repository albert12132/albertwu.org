from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Identity vs. Equality'
level = 'exam'

references = [
    'Reference 1',
    'Reference 2',
]

notes = ''

contents = [
        {'name': 'What would Python print?',
         'id': 'print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
]

print_questions = [
    {'prompts': [
            ("""def outer():
...     def inner():
...         return 42
...     return inner""",),
            ('outer is outer', 'True   # referring to the function outer'),
            ('outer() is outer()', 'False  # referring to the return value of outer; draw an environment diagram to see why it is False'),
            ('outer() == outer()', 'False  # == for functions behaves like is'),
            ('[1, 2, (3, 4)] == [1, 2, (3, 4)]', 'True'),
            ('[1, 2, outer()] == [1, 2, outer()]', 'False  # == for list checks if each pair of elements satisfies =='),
        ]},

    {'prompts': [
            ('a = [1, 2, 3, 4]',),
            ('a[0] = a',),
            ('a is a[0]', 'True'),
            ("a = {'hi': 3}",),
            ("b = {'hi': 3}",),
            ("a is b", 'False'),
            ('a == b', 'True'),
            ("a['hi'] = 10",),
            ("a == b", 'False  # keys AND values must be equivalent'),
        ]},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

