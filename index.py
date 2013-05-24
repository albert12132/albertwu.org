from utils import utils

name = 'Albert Wu'

email = 'cs61a-tg@imail.eecs.berkeley.edu'

office_hours = 'MW 5:00 - 6:00, 651 Soda'

################
# SECTION INFO #
################

sections = [
    {'number': 25,
     'time': '2:00 - 3:30',
     'lab':  ('271 Soda', 'Wed'),
     'discussion':  ('310 Soda', 'Fri'),
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
    ('review/mt1.html', 'Midterm 1 Review'),
    ('review/mt2.html', 'Midterm 2 Review'),
    ('review/final.html', 'Final Review'),
]

practice = utils.ul(
    contents=map(lambda x: utils.a(*x, internal=False), practice)
)


notes = [
    ('notes/debugging.html', 'Debugging'),
    ('notes/style_guide.html', 'Style Guide'),
    ('notes/env2.pdf', 'Environment Diagrams'),
    ('notes/indexing.html', 'Indexing and Slicing'),
    ('notes/vim.html', 'Vim'),
    ('notes/vimrc.html', 'Vimrc: configuring Vim'),
]

notes = utils.ul(
    contents=map(lambda x: utils.a(*x, internal=False), notes)
)

attrs = globals()
