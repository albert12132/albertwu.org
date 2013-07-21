import sys
import os
sys.path.append(os.getcwd())

from utils import utils
from indices.topics import topics as contents

exam = 'All topics'


contents.sort()

notes = 'The following topics are sorted by alphabetical order.'

contents = utils.table(
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


attrs = globals()
