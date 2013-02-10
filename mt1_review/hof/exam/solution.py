from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'exam'

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
#    ('What would Python print?', 'print',
#        lambda: make_print_solution,
#        lambda: print_solutions),
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+f(x)%3A%0A++++return+lambda+y%3A++x(y)%0A%0Adef+g(x)%3A%0A++++return+lambda+%3A+f(x)+%2B+f(y)%0A%0Ay+%3D+2%0Aresult+%3D+f(g(f))&mode=display&cumulative=true&py=3&curInstr=8",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+dream1(f)%3A%0A++++kick+%3D+lambda+x%3A+mind()%0A++++def+dream2(secret)%3A%0A++++++++mind+%3D+f(secret)%0A++++++++kick(2)%0A++++return+dream2%0A%0Ainception+%3D+lambda+secret%3A+lambda%3A+secret%0Areal+%3D+dream1(inception)(42)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python Tutor'},
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
