from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'exam'

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+funny(joke)%3A%0A++++hoax+%3D+joke+%2B+1%0A++++return+funny(hoax)%0A%0Adef+sad(joke)%3A%0A++++hoax+%3D+joke+-+1%0A++++return+hoax+%2B+hoax%0A%0Afunny,+sad+%3D+sad,+funny%0Aresult+%3D+funny(sad(1))&mode=display&cumulative=true&py=3&curInstr=13",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+fun(fun)%3A%0A++++def+time(time)%3A%0A++++++++return+fun(x)%0A++++x+%3D+4%0A++++return+time%0A%0Adef+boo(x)%3A%0A++++return+x**2%0A++++x+%3D+5%0A%0Aresult+%3D+fun(boo)(10)&mode=display&cumulative=true&py=3&curInstr=11",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+sub%0Adef+trick(me,+you)%3A%0A++++sub+%3D+treat%0A++++return+sub%0A%0Adef+treat(me,+you)%3A%0A++++return+sub(me,+1)%0A%0Atreat+%3D+trick%0Atrick(3,+4)&mode=display&cumulative=true&py=3&curInstr=8",
     'message': 'Link to Online Python Tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+easy(x)%3A%0A++++def+peasy(y)%3A%0A++++++++def+ironic(name)%3A%0A++++++++++++return+name(x,+y)%0A++++++++return+y%0A++++return+peasy%0A%0Aresult+%3D+easy(4)(easy)(2)&mode=display&cumulative=true&py=3&curInstr=11",
     'message': 'Link to Online Python Tutor'},
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
