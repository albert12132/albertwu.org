from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_question, make_print_question, make_env_question

#---------#
# CONTENT #
#---------#

title = 'Control Structures'
level = 'basic'

references = [
        ('Lecture: Control and Higher-Order Functions',),
        ('Lab 1',),
]

contents = [
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

print_questions = [
    {'prompts': [
            """x = 4
&gt;&gt;&gt; x > 2 and x < 6""",
            """True and not True    # a.k.a. a contradiction""",
            """True and True        # a.k.a. a tautology""",
            """False and True or True""",
            """False and (True or True)""",
            """False or True or 1 / 0""",
            """False and 1 / 0""",
            """3 and 4""",
            """3 or 4""",
        ]},
    {'prompts': [
        """if True:
...     print('True!')
... else:
...     print('False!')""",

        """if 4:
...     print('True!')
... else:
...     print('False!')""",

        """if 0:
...     print('True!')
... else:
...     print('False!')""",

        """x = 42
&gt;&gt;&gt; if x < 0:
...     print('negative')
... elif x == 42:
...     print('The answer to everthing')
... else:
...     print('Boring number')""",
        ]},
    {'prompts': [
        """x = 0
&gt;&gt;&gt; while x < 5:
...     print(x)
...     x += 1""",

        """while False:
...     print('hi!')""",

        """while True:
...     print('hi!')
...     # press Control C to get out of this""",
        ]},
]

env_questions = [
    {'code': """
def branch(x):
    if x &gt; 10:
        x -= 5
    elif x &gt; 7:
        x -= 2
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

a = branch(12)
b = branch(8)
"""
    },
    {'code': """
def uhoh(x):
    if x:
        y = 5
    return y

a = uhoh(True)
b = uhoh(False)
"""
    },
    {'code': """
def is_even(x):
    return x % 2 == 0

i = 0
while i < 2:
    if is_even(i):
        print(i)
    i += 1
"""
    },
]

code_questions = [
    {'description': """For each of the following functions, try to make the code more concise.""",
     'code': """
def one(x):
    if x == True:
        return 'input is true'
    else:
        return 'input is false'

def two(x):
    if x == 100:
        return True
    else:
        return False

def three(x):
    if x % 6 == 0:
        x += x // 6
        return x
    else:
        return x

def four(ones_win):
    if ones_win == True:
        result = 6
    elif ones_win == False:
        result = 4
""",
     'hint': None,
    },
    {'description': """Write a function <tt>summation</tt> that
adds the first <tt>n</tt> elements in a sequence. The <tt>k</tt>th
element in the sequence can be computed by evaluating <tt>term(k)</tt>.
""",
     'code': """
def summation(n, term):
    \"\"\"Computes the summation of the first n numbers in the sequence
    defined by the function term.

    &gt;&gt;&gt; square = lambda x: x * x
    &gt;&gt;&gt; summation(5, square)
    55
    \"\"\"
    \"*** YOUR CODE HERE ***\"
""",
     'hint': None,
    },
    {'description': """Write a function <tt>is_fib</tt> that returns <tt>True</tt> if its input is a fibonacci number, and False otherwise.""",
     'code': """
def is_fib(n):
    \"\"\"Returns True if n is a fibonacci number,
    else False

    &gt;&gt;&gt; is_fib(8)
    True
    &gt;&gt;&gt; is_fib(9)
    False
    \"\"\"
    \"*** YOUR CODE HERE ***\"
""",
     'hint': None,
    }
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
