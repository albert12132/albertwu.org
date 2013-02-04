from template.utils import make_list, references_li, contents_li, \
        make_section, make_env_solution

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'basic'

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_solution,
        lambda: env_solutions),
]

env_solutions = [
        {'link': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+square1(x)%3A%0A++++return+x+*+x%0A%0Adef+square2(x)%3A%0A++++print(x+*+x)%0A%0Aa+%3D+square1(3)%0Ab+%3D+square2(3)%0A%0A%23+How+does+return+behave+differently+than+print%3F&mode=display&cumulative=true&py=3&curInstr=0',
     'message': 'Link to Online Python tutor'},
        {'link': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=def+mul(a,+b)%3A%0A++++return+a+*+b%0A%0Adef+sum_of_squares(x,+y)%3A%0A++++return+mul(x,+x)+%2B+mul(y,+y)%0A%0Aresult+%3D+sum_of_squares(3,+4)%0A%0A%23+How+many+times+do+we+call+mul%3F%0A%23+How+many+frames+do+we+draw+for+mul%3F&mode=display&cumulative=true&py=3&curInstr=0',
     'message': 'Link to Online Python tutor'},
        {'link': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+add%0Afirst+%3D+add(3,+4)%0A%0Adef+add(a,+b)%3A%0A++++return+a+%2B+b%0A%0Asecond+%3D+add(3,+4)%0A%0A%23+What+changes+between+the+first+time+we+call+add+and+the%0A%23+second+time%3F+How+does+this+affect+our+diagram%3F&mode=display&cumulative=true&py=3&curInstr=0',
     'message': 'Link to Online Python tutor'},
        {'link': 'http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=score,+opp_score+%3D+0,+0%0A%0Adef+assign(arg0,+arg1)%3A%0A++++score+%3D+arg0%0A++++opp_score+%3D+arg1%0A++++return+True%0A%0Asuccess+%3D+assign(3,+9001)%0A%0A%23+But+did+we+really+succeed%3F%0A%23+Did+the+global+values+of+score+and+opp_score+change%3F&mode=display&cumulative=true&py=3&curInstr=0',
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=goal+%3D+100%0A%0Adef+foo(x)%3A%0A++++y+%3D+x+%2B+goal%0A++++return+b%0A%0Aresult+%3D+foo(4)%0A%0A%23+What's+the+lookup+procedure+for+goal%3F%0A%23+Does+result+every+show+up+in+the+diagram%3F&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=from+operator+import+add,+sub%0Adef+a_plus_abs_b(a,+b)%3A%0A++++if+b+%3C+0%3A%0A++++++++op+%3D+sub%0A++++else%3A%0A++++++++op+%3D+add%0A++++return+op(a,+b)%0A%0Aresult+%3D+a_plus_abs_b(4,+-4)&mode=display&cumulative=true&py=3&curInstr=0",
     'message': 'Link to Online Python tutor'},
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
