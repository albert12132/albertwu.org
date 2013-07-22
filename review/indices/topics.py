from utils import utils

mt1 = [
    ('Environment Diagrams', 'environments'),
    ('Control Structures', 'control'),
    ('Higher-Order Functions', 'hof'),
    ('Lambda Expressions', 'lambdas'),
    ("Newton's Method", 'newtons'),
    ("Tuples", 'tuples'),
    ("Rlists", 'rlists'),
    ("Lists", 'lists'),
]

mt2 = [
    ('Dictionaries', 'dictionaries'),
    ('Map, filter, and friends', 'functions'),
    ('Identity vs. Equality', 'identity'),
    ('Nonlocal', 'nonlocal'),
    ('OOP', 'oop'),
    ('Special Methods', 'special'),
    ('Rlists as Classes', 'mut_rlists'),
    ('Trees', 'trees'),
    ('Orders of Growth', 'oog'),
]

final = [
    ('Scheme', 'scheme'),
    ('Interpreters', 'interpreter'),
    ('Iterators and Generators', 'iterators'),
    ('Streams', 'streams'),
]

topics = mt1 + mt2 + final

def publish(contents):
    return utils.table(
        ids = 'topics',
        classes='highlight',
        headers=('Topic', 'Basic', 'Exam'),
        contents=list(map(
            lambda x: (
                x[0],
                utils.a(x[1] + '/basic/index.html', 'Questions',
                    internal=False),
                utils.a(x[1] + '/exam/index.html', 'Questions',
                    internal=False)
            ), contents))
    )
