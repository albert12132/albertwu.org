from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

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
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

print_questions = [
    {'prompts': [
            ('tup = (1, 2, 3)',),
            ('pairs = ((1, 2), (3, 4))',),
            ('tuple(map(lambda x: tuple(map(lambda y: x*y, tup)), tup))', '((1, 2, 3), (2, 4, 6), (3, 6, 9))'),
            ('tuple(map(lambda x: x*2, pairs))', '((1, 2, 1, 2), (3, 4, 3, 4))'),
            ('tuple(map(lambda x, y: (y, x), pairs))', 'TypeError'),
            ('tuple(map(lambda x, y: (y, x), tup, tup))', '((1, 1), (2, 2), (3, 3))'),
            ('tuple(map(lambda x, y: x + y, (1, 2, 3), (1, 2)))', '(2, 4)'),
            ('tuple(filter(None, tup))', '(1, 2, 3)'),
        ]},
    {'prompts': [
            ('from functools import reduce'),
            ('reduce(lambda x, y: x + y, tup, 100)', '106'),
            ('reduce(lambda x, y: (x, y), tup)', '((1, 2), 3)'),
            ('reduce(lambda x, y: y + x, "hello world!")', "'!dlrow olleh'"),
            ('reduce(lambda x, y: x + y, map(lambda x: x**2, tup))', '14'),
            ('tuple(map(reduce, (lambda x, y: x + y)*4, pairs))', '(3, 7)'),
        ]},
]

code_questions = [
    {'description': """Implement a function <tt>capitalize</tt> that
    takes a string and capitalizes words if they are at the start of
    a sequence. <b>Hint:</b> the <tt>capitalize</tt> string method,
    which capitalizes the first character of a string, may help you
    here.""",
     'code': """
def capitalize(s):
    \"\"\"Capitalizes words in the string if they are at the start of
    a sentence.

    &gt;&gt;&gt; s = 'this is spot. see spot run.'
    &gt;&gt;&gt; capitalize(s)
    'This is spot. See spot run.'
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def capitalize(s):
    return reduce(lambda x, y: x + ' ' + y,
                  map(lambda x, y: x.capitalize() if y.endswith('.') \
                                                  else x,
                      s.split(),
                      ['.'] + s.split()))""",
    },
    {'description': """Implement <tt>shuffle</tt> that takes a
    sequence, splits it in two halves, and interleaves the elements of
    both halves. The return value should be the result of that
    interleave, and should be a list. <b>Note</b>: you may assume the
    list is of even length.""",
     'code': """
def shuffle(seq):
    \"\"\"Splits seq in half and interleaves elements of both halves.

    &gt;&gt;&gt; seq = [1, 2, 3, 4, 5, 6]
    &gt;&gt;&gt; shuffle(seq)
    [1, 4, 2, 5, 3, 6]
    \"\"\"
    \"*** YOUR CODE HERE ***\" """,
    'solution': """
def shuffle(seq):
    return list(reduce(lambda x, y: x + y,
                       map(lambda x, y: [x, y],
                           seq[:len(seq)//2],
                           seq[len(seq)//2:])))""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

