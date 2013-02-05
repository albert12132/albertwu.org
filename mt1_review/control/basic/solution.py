from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_print_solution, make_env_solution, make_code_solution

#---------#
# CONTENT #
#---------#

title = 'Control Structures'
level = 'basic'

contents = [
    ('What would Python print?', 'print',
        lambda: make_print_solution,
        lambda: print_solutions),
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
    ('Code Writing', 'code',
        lambda: make_code_solution,
        lambda: code_solutions),
]

print_solutions = [
    {'answers': [
        """True""",
        """False""",
        """True""",
        """True""",
        """False""",
        """True""",
        """False""",
        """4""",
        """3""",
    ]},
    {'answers': [
        """True!""",
        """True!""",
        """False!""",
        """The answer to everything""",
    ]},
    {'answers': [
        """
0
1
2
3
4
""",
        """# nothing happens
""",
        """
hi!
hi!
hi!
# forever
""",
    ]},
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+branch(x)%3A%0A++++if+x+%3E+10%3A%0A++++++++x+-%3D+5%0A++++elif+x+%3E+7%3A%0A++++++++x+-%3D+2%0A++++if+x+%25+2+%3D%3D+0%3A%0A++++++++return+'even'%0A++++else%3A%0A++++++++return+'odd'%0A%0Aa+%3D+branch(12)%0Ab+%3D+branch(8)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+uhoh(x)%3A%0A++++if+x%3A%0A++++++++y+%3D+5%0A++++return+y%0A%0Aa+%3D+uhoh(True)%0Ab+%3D+uhoh(False)&mode=undefined&cumulative=true&py=3",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+is_even(x)%3A%0A++++return+x+%25+2+%3D%3D+0%0A%0Ai+%3D+0%0Awhile+i+%3C+2%3A%0A++++if+is_even(i)%3A%0A++++++++print(i)%0A++++i+%2B%3D+1&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
]

code_solutions = [
    {'code': """
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
""",
     'explanation': '',
    },
    {'code': """
def summation(n, term):
    k, total = 1, 0
    while k <= n:
        total += term(k)
        k += 1
    return total
""",
     'explanation': '',
    },
    {'code': """
def is_fib(n):
    cur, next = 0, 1
    while cur < n:
        cur, next = next, cur + next
    return cur == n
""",
     'explanation': '',
    },
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
