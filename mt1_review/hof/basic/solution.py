from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
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
]

concept_solutions = [
        {'explanation': """A function is a higher-order function if it satisfies at least one of the following:
<li>It takes at least one function as an argument</li>
<li>It returns a function</li>
"""},
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+my_strat(score)%3A%0A++++return+score+%2B+2%0A%0Adef+play(strat)%3A%0A++++i,+roll+%3D+0,+strat(0)%0A++++while+i+%3C+roll%3A%0A++++++++result+%3D+my_strat(i)%0A++++++++i+%2B%3D+1%0A++++return+i%0A%0Aresult+%3D+play(my_strat)%0A%0A%23+How+many+times+do+we+call+my_strat%3F%0A%23+Remember+to+label+the+frames+with+the+intrinsic%0A%23+name+of+the+functions&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+fun(x)%3A%0A++++return+x**2%0A%0Adef+time(y)%3A%0A++++y,+x+%3D+4,+5%0A++++def+fun(y)%3A%0A++++++++return+y+%2B+x%0A++++return+fun%0A%0Aa+%3D+time(10)%0Ab+%3D+a(2)%0A%0A%23+Which+fun+is+called%3F%0A%23+Which+y+is+used%3F%0A%23+What+type+of+object+is+a%3F&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=x+%3D+4%0A%0Adef+outer(f)%3A%0A++++def+inner(g)%3A%0A++++++++return+f(g(x))%0A++++return+inner%0A%0Adef+square(x)%3A%0A++++return+x**2%0A%0Ac+%3D+outer(square)(square)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+one(f)%3A%0A++++a+%3D+1%0A++++def+two(g)%3A%0A++++++++b+%3D+2%0A++++++++def+three(h)%3A%0A++++++++++++c+%3D+3%0A++++++++++++return+f(a)+%2B+g(b)+%2B+h(c)%0A++++++++return+three%0A++++return+one%0A%0Adef+identity(x)%3A%0A++++return+x%0A%0Adef+square(x)%3A%0A++++return+x**2%0A%0Adef+cube(x)%3A%0A++++return+x**3%0A%0Amiddle+%3D+one(identity)(square)%0Aresult+%3D+middle(cube)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
]

code_solutions = [
    {'code': """
def make_mod(n):
    def mod_n(x):
        return x % n
    return mod_n
""",
     'explanation': "",
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
