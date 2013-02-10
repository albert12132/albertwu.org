from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, make_eval_output_solution

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'exam'

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
    ('Eval/Output', 'eval',
        lambda: make_eval_output_solution,
        lambda: eval_output_solutions),
#    ('What would Python print?', 'print',
#        lambda: make_print_solution,
#        lambda: print_solutions),
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+f(x)%3A%0A++++return+lambda+y%3A++x(y)%0A%0Adef+g(x)%3A%0A++++return+lambda+%3A+f(x)+%2B+f(y)%0A%0Ay+%3D+2%0Aresult+%3D+f(g(f))&mode=display&cumulative=true&py=3&curInstr=8",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+always_roll(n)%3A%0A++++return+lambda+s0,+s1%3A+n%0A%0Adef+make_bad_strategy(p)%3A%0A++++def+strategy(s0,+s1)%3A%0A++++++++%23+next+line+is+bad+style!%0A++++++++return+always_roll(1+-+p)(s0,+s1)%0A++++return+strategy%0A%0Anum_rolls+%3D+make_bad_strategy(1)(50,+50)&mode=display&cumulative=true&py=3&curInstr=12",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+dream1(f)%3A%0A++++kick+%3D+lambda+x%3A+mind()%0A++++def+dream2(secret)%3A%0A++++++++mind+%3D+f(secret)%0A++++++++kick(2)%0A++++return+dream2%0A%0Ainception+%3D+lambda+secret%3A+lambda%3A+secret%0Areal+%3D+dream1(inception)(42)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+albert(albert)%3A%0A++++albert+%3D+albert()%0A++++def+albert()%3A%0A++++++++albert+%3D+lambda+albert%3A+albert%0A++++++++return+albert(albert)%0A++++return+albert%0A%0Aalbert(lambda%3A+albert)()&mode=display&cumulative=true&py=3&curInstr=13",
     'message': 'Link to Online Python Tutor'},
]

eval_output_solutions = [
    {'prompts': [
        'foo(2013)',
        'foo(new)',
        'foo(new(4))(16)',
        'foo(11)(11)',
        'foo(2)(4)(2)',
    ], 'answers': [
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': '4',
         'output': '4'},
    ]},
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
