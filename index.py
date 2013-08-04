from utils import utils

name = 'Albert Wu'

email = 'cs61a-te@imail.eecs.berkeley.edu'

office_hours = 'MW 10:00 - 11:00 AM, 651 Soda'

################
# SECTION INFO #
################

sections = [
    {
        'number': 104,
         'time': '5:00 - 6:30',
         'lab':  ('271 Soda', 'MW'),
         'discussion':  ('320 Soda', 'TuTh'),
     },
]

def compile_section(s):
    form = '{0}<br/>{1}'
    return [
        form.format(s['number'], s['time']),
        form.format(*s['lab']),
        form.format(*s['discussion']),
    ]

sections = utils.table(
    list(map(compile_section, sections)),
    headers=('Section #<br/>Time', 'Lab', 'Discussion'),
)

#####################
# PRACTICE PROBLEMS #
#####################

practice = [
    ('Midterm 1 Review', 'review/mt1.html', False),
    ('Midterm 2 Review', 'review/mt2.html', False),
    ('Final Review', 'review/final.html', False),
]

practice = utils.table_to_html(practice)


notes = [
    ('Coursework',),
    [
        ('Submitting assignments', 'notes/submission.html', False),
        ('Debugging', 'notes/debugging.html', False),
        ('Style Guide', 'notes/style_guide.html', False),
        ('Autograder', 'notes/autograder.html', False),
    ],
    ('Concepts',),
    [
        ('Environment Diagrams', 'notes/environments.html', False),
        ('Indexing and Slicing', 'notes/indexing.html', False),
    ],
    ('Programs',),
    [
        ('Vim', 'notes/vim.html', False),
        [
            ('Vimrc: configuring Vim', 'notes/vimrc.html', False),
        ],
        ('Git', 'notes/git.html', False),
    ],
]

notes = utils.table_to_html(notes)

attrs = globals()
