from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Control Structures'
level = 'basic'

references = [
    'Lecture: Control and Higher-Order Functions',
    'Lab 1',
]

notes = ''

contents = [
        {'name': 'What would Python print?',
         'id': 'print',
         'maker q': make_print_question,
         'maker s': make_print_solution,
         'questions': lambda: print_questions},
        {'name': 'Environment Diagrams',
         'id': 'env',
         'maker q': make_env_question,
         'maker s': make_env_solution,
         'questions': lambda: env_questions},
        {'name': 'Code Writing',
         'id': 'code',
         'maker q': make_concept_question,
         'maker s': make_code_solution,
         'questions': lambda: code_questions},
]

print_questions = [
    {'prompts': [
            ('x = 4',),
            ('x &gt; 2 and x &lt; 6', 'True'),
            ('True and not True    # a.k.a. a contradiciton', 'False'),
            ('True and True        # a.k.a. a tautology', 'True'),
            ('False and True or True', 'True'),
            ('False and (True or True)', 'False'),
            ('False or True or 1 / 0', 'True'),
            ('False and 1 / 0', 'False'),
            ('3 and 4', '4'),
            ('3 or 4', '3'),
        ]},
    {'prompts': [
        ("""if True:
...     print('True!')
... else:
...     print('False!')""", 'True!'),

        ("""if 4:
...     print('True!')
... else:
...     print('False!')""", 'True!'),

        ("""if 0:
...     print('True!')
... else:
...     print('False!')""", 'False!'),

        ("""x = 42
&gt;&gt;&gt; if x < 0:
...     print('negative')
... elif x == 42:
...     print('The answer to everthing')
... else:
...     print('Boring number')""", 'The answer to everything'),
        ]},

    {'prompts': [
        ("""x = 0
&gt;&gt;&gt; while x < 5:
...     print(x)
...     x += 1""", """0
1
2
3
4"""),

        ("""while False:
...     print('hi!')""", '# nothing happens'),

        ("""while True:
...     print('hi!')
...     # press Control C to get out of this""", """hi!
hi!
hi!
# forever"""),
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
b = branch(8)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+branch(x)%3A%0A++++if+x+%3E+10%3A%0A++++++++x+-%3D+5%0A++++elif+x+%3E+7%3A%0A++++++++x+-%3D+2%0A++++if+x+%25+2+%3D%3D+0%3A%0A++++++++return+'even'%0A++++else%3A%0A++++++++return+'odd'%0A%0Aa+%3D+branch(12)%0Ab+%3D+branch(8)&mode=display&cumulative=true&py=3&curInstr=0",
    },

    {'code': """
def uhoh(x):
    if x:
        y = 5
    return y

a = uhoh(True)
b = uhoh(False)""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+uhoh(x)%3A%0A++++if+x%3A%0A++++++++y+%3D+5%0A++++return+y%0A%0Aa+%3D+uhoh(True)%0Ab+%3D+uhoh(False)&mode=undefined&cumulative=true&py=3",
    },

    {'code': """
def is_even(x):
    return x % 2 == 0

i = 0
while i < 2:
    if is_even(i):
        print(i)
    i += 1""",
    'solution': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+is_even(x)%3A%0A++++return+x+%25+2+%3D%3D+0%0A%0Ai+%3D+0%0Awhile+i+%3C+2%3A%0A++++if+is_even(i)%3A%0A++++++++print(i)%0A++++i+%2B%3D+1&mode=display&cumulative=true&py=3&curInstr=0",
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
    'solution': """
def one(x):
    if <b>x</b>:
        return 'input is true'
    return 'input is false'

def two(x):
    <b>return x == 100</b>

def three(x):
    if x % 6 == 0:
        x += x // 6
    <b>return x</b>

def four(ones_win):
    <b>result = 6 if ones_win else 4</b>
"""
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
    'solution': """
def summation(n, term):
    k, total = 1, 0
    while k <= n:
        total += term(k)
        k += 1
    return total
"""
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
    'solution': """
def is_fib(n):
    cur, next = 0, 1
    while cur < n:
        cur, next = next, cur + next
    return cur == n
"""
    }
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()

