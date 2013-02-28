from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Lists'
level = 'basic'

references = [
    'Lecture: Objects, Lists, and Dictionaries',
    'Discussion 6',
]

notes = ''

contents = [
        {'name': 'What would Python print?',
         'id': 'print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]


print_questions = [
    {'prompts': [
            ('L = [1, 2, 3, 4]',),
            ('L[0]', '1'),
            ('L[100]', 'IndexError'),
            ('L[-1]', '4'),
            ('L[2] = 100',),
            ('L', '[1, 2, 100, 4]'),
        ]},
    {'prompts': [
            ('L = [1, 2, 3, 4]',),
            ('L[1:3]', '[2, 3]'),
            ('L[:2]', '[1, 2]'),
            ('L[1:]', '[2, 3, 4]'),
            ('L[:]', '[1, 2, 3, 4]'),
            ('L[0:3:2]', '[1, 3]'),
            ('L[::-1]', '[4, 3, 2, 1]'),
        ]},
    {'prompts': [
            ('L = [1, 2, 3, 4]',),
            ('[1, 2] + [3, 4]', '[1, 2, 3, 4]'),
            ('[1, 2] * 2', '[1, 2, 1, 2]'),
            ('L.append(5)',),
            ('L', '[1, 2, 3, 4, 5]'),
            ('L.extend([6, 7])',),
            ('L', '[1, 2, 3, 4, 5, 6, 7]'),
            ('L.index(5)', '4'),
            ('L.remove(3)',),
            ('L', '[1, 2, 4, 5, 6, 7]'),
            ('L.pop()', '7'),
            ('L', '[1, 2, 4, 5, 6]'),
        ]},
]

code_questions = [
    {'description': """Implement a function <tt>reverse</tt> that takes
        a list as an argument and reverses the list. You should mutate
        the original list, without creating any new lists. Do NOT
        return anything.""",
     'code': """
def reverse(L):
    \"\"\"Reverses L in place (i.e. doesn't create new lists).

    &gt;&gt;&gt; L = [1, 2, 3, 4]
    &gt;&gt;&gt; reverse(L)
    &gt;&gt;&gt; L
    [4, 3, 2, 1]
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def reverse(L):
    for i in range(len(L)//2):
        L[i], L[-i-1] = L[-i-1], L[i]"""
    },
    {'description': """Implement a function <tt>map_mut</tt> that takes
        a list as an argument and maps a function <tt>f</tt> onto each
        element of the list. You should mutate the original lits,
        without creating any new lists. Do NOT return anything.""",
     'code': """
def map_mut(f, L):
    \"\"\"Mutatively maps f onto each element in L.

    &gt;&gt;&gt; L = [1, 2, 3, 4]
    &gt;&gt;&gt; map_mut(lambda x: x**2, L)
    &gt;&gt;&gt; L
    [1, 4, 9, 16]
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def map_mut(f, L):
    for i in range(len(L)):
        L[i] = f(L[i])"""
    },
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

