from utils import utils

mt1 = [
    ('Environment Diagrams', 'environments'),
    ('Control Structures', 'control'),
    ('Higher-Order Functions', 'hof'),
    ('Lambda Expressions', 'lambdas'),
    ("Newton's Method", 'newtons'),
    ("Recursion", 'recursion'),
]

mt2 = [
    ("Tuples", 'tuples'),
    ("Rlists", 'rlists'),
    ("Lists", 'lists'),
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
    ('Tail Recursion', 'tail'),
    ('Interpreters', 'interpreter'),
    ('Iterators and Generators', 'iterators'),
    ('Streams', 'streams'),
    ('Logic', 'logic'),
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
                utils.a(x[1] + '/basic/', 'Questions',
                    internal=False),
                utils.a(x[1] + '/exam/', 'Questions',
                    internal=False)
            ), contents))
    )
