from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Nonlocal'
level = 'basic'

references = [
    ('Lecture: Mutable Data',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/14-Mutation_1pps.pdf'),
    ('Lab 5',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab05/lab05.php'),
]

notes = ''

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
    {'name': 'Environment Diagrams',
     'id': 'env',
     'maker': make_env_question,
     'questions': lambda: env_questions},
]

concept_questions = [
    {
        'description': """Would this code work? If not, how would you
        fix it?""",
        'code': """
def make_counter():
    count = 0
    def counter():
        count += 1
        return count
    return counter""",
        'solution': """No, this code would not work. Here's how we
        can find out:""" + ol((
            """The line <tt>count += 1</tt> is equivalent to
            <tt>count = count + 1</tt>, so we rewrite it as such.""",
            """Python notices that <tt>count</tt> appears on the left
            side of an assignment statement, so Python remembers to
            treat <tt>count</tt> as a local variable.""",
            """Python then begins executing the line. To compute
            <tt>count + 1</tt> Python must look up <tt>count</tt>.""",
            """But Python had previously marked <tt>count</tt> as a
            local variable, and it doesn't have a value yet! So Python
            raises an error.""",
        )) + """To fix it, add a nonlocal statement:""" + prettify("""
def make_counter():
    count = 0
    def counter():
        <b>nonlocal count</b>
        count += 1
        return count
    return counter""")
    },
    {
        'description': """For the following code, answer these
        questions:""" + ol((
            """In which function's frame does Python start looking for
            <tt>alice</tt>?""",
            """In which function's frame does Python stop looking for
            <tt>alice</tt>?""",
            """In which function's frame does Python start looking for
            <tt>bob</tt>?""",
            """In which function's frame does Python stop looking for
            <tt>bob</tt>?""",
        )),
        'code': """
def fn1(bob):
    def fn2(alice):
        def fn3(alice):
            def fn4():
                nonlocal bob, alice
                return bob + alice
            return fn4
        return fn3
    return fn2""",
        'solution': ol(list(map(tt, (
            'fn3',
            'fn3',
            'fn3',
            'fn1',
        )))),
    },
    {
        'description': """Identify all the errors regarding nonlocal
        in the following code:""",
        'code': """
bob = 2
def fn1(bob):
    eve = 3
    def fn2(alice):
        nonlocal bob, alice
        eve = 4
        return eve + alice
    return fn2""",
        'solution': """Errors are bolded:""" + prettify("""
bob = 2
def fn1(bob):
    eve = 3
    def fn2(alice):
        nonlocal bob<b>, alice</b>
        <b>eve = 4</b>
        return bob + alice
    return fn2""") + ul((
            """<b><tt>nonlocal alice</tt></b> is incorrect, since
            <tt>alice</tt> is already defined in the same frame (as a
            parameter to <tt>fn2</tt>).""",
            """<b><tt>eve = 4</tt></b> will NOT cause any errors,
            since <tt>eve</tt> is not being referenced before
            assignment.  However, because <tt>eve</tt> is not declared
            as nonlocal, the <tt>eve</tt> in <tt>fn1</tt> will retain
            the value of 3.""",
        ))
    },
]

env_questions = [
    {
        'code': """
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
counter()
counter()""",
    },
    {
        'code': """
def foo():
    lst = []
    def bar(m):
        nonlocal lst
        lst = lst + [m]
        return lst
    return bar

bar = foo()
bar(3)
bar(4)""",
    },

    {
        'code': """
def foo():
    lst = []
    def bar(m):
        lst.append(m)
        return lst
    return bar

bar = foo()
bar(3)
bar(4)""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

