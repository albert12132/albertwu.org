from utils import utils

exam = 'Final'

contents = [
    ('Orders of Growth', 'oog'),
    ('Scheme', 'scheme'),
    ('Interpreters', 'interpreter'),
    ('Iterators and Generators', 'iterators'),
    ('Streams', 'streams'),
]

contents = utils.table(
    ids = 'topics',
    classes='highlight',
    headers=('Topic', 'Basic', 'Exam'),
    contents=list(map(
        lambda x: (
            x[0],
            utils.a(x[1] + '/basic/question.html', 'Questions',
                internal=False) + \
            '<br/>' + \
            utils.a(x[1] + '/basic/solution.html', 'Solutions',
                internal=False),
            utils.a(x[1] + '/exam/question.html', 'Questions',
                internal=False) + \
            '<br/>' + \
            utils.a(x[1] + '/exam/solution.html', 'Solutions',
                internal=False)
        ), contents))
)


attrs = globals()
