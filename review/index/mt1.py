from utils import utils

exam = 'Midterm 1'

contents = [
    ('Environment Diagrams', 'environments'),
    ('Control Structures', 'control'),
    ('Higher-Order Functions', 'hof'),
    ('Lambda Expressions', 'lambdas'),
    ("Newton's Method", 'newtons'),
    ("Tuples", 'tuples'),
    ("Rlists", 'rlists'),
    ("Lists", 'lists'),
    ("Dictionaries", 'dictionaries'),
]

notes = "Don't forget about <b>data abstraction</b> and <b>recursion</b>! The extra problems in Discussion 2a are very good for recursion practice."

contents = utils.table(
    ids = 'topics',
    classes='highlight',
    headers=('Topic', 'Basic', 'Exam'),
    contents=list(map(
        lambda x: (
            x[0],
            utils.a(x[1] + '/basic/question.html', 'Questions',
                internal=False),
            utils.a(x[1] + '/exam/question.html', 'Questions',
                internal=False)
        ), contents))
)


attrs = globals()
