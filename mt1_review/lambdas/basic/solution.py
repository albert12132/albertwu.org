from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution

#---------#
# CONTENT #
#---------#

title = 'Test'
level = 'basic'

contents = [
    ('Conceptual', 'conceptual',
        lambda: make_concept_solution,
        lambda: concept_solutions),
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

concept_solutions = [
    {'explanation': """Some differences between lambdas and def statements include:
<ul>
    <li>lambdas are expressions (they are a value), while defs are
    statements.</li>
    <li>lambdas can only be one liners</li>
</ul>"""},
]

env_solutions = [
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=square+%3D+lambda+x%3A+x+*+x%0Ahigher+%3D+lambda+f%3A+lambda+y%3A+f(f(y))%0A%0Ahigher(square)(5)&mode=display&cumulative=true&py=3&curInstr=11",
     'message': 'Link to Online Python tutor.'},
        {'link': "http://inst.eecs.berkeley.edu/~cs61a-py/OnlinePythonTutor/v3/tutor.html#code=a+%3D+(lambda+f,+a%3A+f(a))(lambda+b%3A+b+*+b,+2)&mode=display&cumulative=true&py=3&curInstr=5",
     'message': 'Link to Online Python tutor.'},
]

code_solutions = [
    {'code': """
# 1
square = lambda x: x * x

# 2
compose = lambda f, g: lambda x: f(g(x))
""",
     'explanation': "",
    },
    {'code': """
# 1
def pow(x, y):
    return x**y

# 2
def foo(x):
    def f(y):
        def g(z):
            return x + y * z
        return g
    return f
""",
     'explanation': "",
    },
]

print_solutions = [
    {'answers': [
        """&lt;function &lt;lambda&gt; at ...&gt;""",
        """16""",
        """20""",
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
