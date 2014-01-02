from utils import utils

name = 'Albert Wu'

email = 'cs61a-te@imail.eecs.berkeley.edu'

office_hours = 'TuTh 6:00 - 7:00 PM, 411 Soda'

################
# SECTION INFO #
################

sections = [
    {
        'number': 35,
         'time': '5:00 - 6:30',
         'lab':  ('275 Soda', 'M'),
         'discussion':  ('3113 Etcheverry', 'W'),
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
        [
            ('Vimrc: configuring Vim', 'notes/vimrc', False),
        ],
        ('Git', 'notes/git', False),
    ],
]

notes = utils.table_to_html(notes)

attrs = globals()
