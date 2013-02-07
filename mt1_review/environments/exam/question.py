from template.utils import make_list, references_li, contents_li, \
        make_section, \
        make_concept_question, make_print_question, make_env_question

#---------#
# CONTENT #
#---------#

title = 'Environment Diagrams'
level = 'exam'

references = [
    ('Discussion 2',),
    ('Lecture: Names',),
    ('Lecture: Control and Higher-Order Functions',),
    ('Lecture: Higher-Order Functions',),
]

contents = [
    ('Environment Diagrams', 'env',
        lambda: make_env_question,
        lambda: env_questions),
]

env_questions = [
    {'code': """
def funny(joke):
    hoax = joke + 1
    return funny(hoax)

def sad(joke):
    hoax = joke - 1
    return hoax + hoax

funny, sad = sad, funny
result = funny(sad(1))

# pay special attention to the names of
# the frames!
"""
    },
    {'code': """
def fun(fun):
    def time(time):
        return fun(x)
    x = 4
    return time

def boo(x):
    return x**2
    x = 5

result = fun(boo)(10)
"""
    },
    {'code': """
from operator import sub
def trick(me, you):
    sub = treat
    return sub

def treat(me, you):
    return sub(me, 1)

treat = trick
trick(3, 4)
"""
    },
    {'code': """
def easy(x):
    def peasy(y):
        def ironic(name):
            return name(x, y)
        return y
    return peasy

result = easy(4)(easy)(2)
"""
    },
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
