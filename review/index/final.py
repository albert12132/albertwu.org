from utils import utils

exam = 'Final'

contents = [
    ('Trees', 'trees'),
    ('Orders of Growth', 'oog'),
    ('Scheme', 'scheme'),
    ('Interpreters', 'interpreter'),
    ('Iterators and Generators', 'iterators'),
    ('Streams', 'streams'),
]

notes = """
Don't forget about <b>Logic</b> and <b>Dynamic Scope</b>!
"""

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
