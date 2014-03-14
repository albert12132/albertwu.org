from utils import utils

name = 'Albert Wu'

email = 'cs61a-te@imail.eecs.berkeley.edu'

office_hours = 'Tu 5-6, 651 Soda <i>and</i> Thu 6-7, 411 Soda'

################
# SECTION INFO #
################

sections = [
    {
        'number': '124',
        'time': '11 - 12:30',
        'lab':  ('Wed', '271 Soda'),
        'discussion':  ('Fri', '310 Soda'),
    },
    {
        'number': '25',
        'time': '12:30 - 2',
         'lab':  ('', ''),
         'discussion':  ('Fri', '310 Soda'),
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
    ('Midterm 1 Review', 'review/mt1', False),
    ('Midterm 2 Review', 'review/mt2', False),
    ('Final Review', 'review/final', False),
]

practice = utils.table_to_html(practice)


notes = [
    ('Coursework',),
    [
        ('Submitting assignments', 'notes/submission', False),
        ('Debugging', 'notes/debugging', False),
        ('Style Guide', 'notes/style_guide', False),
        ('Autograder', 'notes/autograder', False),
    ],
    ('Concepts',),
    [
        ('Environment Diagrams', 'notes/environments', False),
        ('Indexing and Slicing', 'notes/indexing', False),
        # ('Object-Oriented Programming', 'notes/oop.html', False),
    ],
    ('Programs',),
    [
        ('Vim', 'notes/vim', False),
        ('Vimrc: configuring Vim', 'notes/vimrc', False),
        ('Git', 'notes/git', False),
    ],
]

notes = utils.table_to_html(notes)

attrs = globals()
