#-------------------#
# Utility functions #
#-------------------#

def make_id_class(kargs):
    """Makes the id and class attributes of a tag, if they are present
    in KARGS.

    KARGS -- a dictionary. It may or may not contain keys 'id' and/or
             'class'

    >>> make_id_class({'id': ['hi', 'bom'], 'class': 'boink'})
    ' id="hi bom" class="boink"'
    >>> make_id_class({})
    ''
    """
    if 'ids' not in kargs:
        ids = ''
    elif type(kargs['ids']) == str:
        ids = ' id="' + kargs['ids'].strip() + '"'
    else:
        ids = ' id="' + ' '.join(kargs['ids']) + '"'

    if 'classes' not in kargs:
        classes = ''
    elif type(kargs['classes']) == str:
        classes = ' class="' + kargs['classes'].strip() + '"'
    else:
        classes = ' class="' + ' '.join(kargs['classes']) + '"'
    return ids + classes

def li(item, **kargs):
    ids = make_id_class(kargs)
    return '<li{}>{}</li>'.format(ids, item)

def pre(code, **kargs):
    """Makes a <pre> tag"""
    ids = make_id_class(kargs)
    return '<pre{}>{}</pre>\n'.format(ids, code)

def a(href, contents, internal=True, **kargs):
    """Makes an <a> tag"""
    ids = make_id_class(kargs)
    if internal:
        href = '#' + href
    return '<a{} href="{}">{}</a>'.format(ids, href, contents)

def b(contents, **kargs):
    ids = make_id_class(kargs)
    return '<b{}>{}</b>'.format(ids, contents)

def tt(contents, **kargs):
    ids = make_id_class(kargs)
    return '<tt{}>{}</tt>'.format(ids, contents)

def code(contents, **kargs):
    ids = make_id_class(kargs)
    return '<code{}>{}</code>'.format(ids, contents)

def p(contents, **kargs):
    """Makes a <p> tag"""
    ids = make_id_class(kargs)
    return '<p{}>{}</p>\n'.format(ids, contents)

def h(num, title, **kargs):
    """Makes a header tag"""
    ids = make_id_class(kargs)
    return '<h{0}{1}>{2}</h{0}>\n'.format(num, ids, title)

def ul(contents, **kargs):
    ids = make_id_class(kargs)
    result = '<ul{}>\n'.format(ids)
    for li in contents:
        result += '  <li>{}</li>\n'.format(li)
    return result + '</ul>'

def ol(contents, **kargs):
    ids = make_id_class(kargs)
    result = '<ol{}>\n'.format(ids)
    for li in contents:
        result += '  <li>{}</li>\n'.format(li)
    return result + '</ol>'

def table(contents, headers=None, **kargs):
    ids = make_id_class(kargs)
    width = max(map(len, contents))
    result = '<table{}>\n'.format(ids)
    if headers:
        result += '  <tr>\n'
        for cell in headers:
            result += '    <th>{}</th>\n'.format(cell)
        result += '  </tr>\n'
    for content in contents:
        result += '  <tr>\n'
        for cell in content:
            result += '    <td>{}</td>\n'.format(cell)
        result += '  </tr>\n'
    return result + '</table>'

#####


def make_eval_output_question(num, code='', prompts=[]):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += """<p>After opening an interpreter, the folowing code
    is entered. In the table below, fill in what each line
    <i>evaluates to</i>, and what the interpreter will display.</p>
    """
    question += '<pre class="prettyprint">' + code  + '</pre>\n'
    question += """<table class='no-center'>
  <tr>
    <th></th>
    <th>Evaluates to</th>
    <th>Outputs</th>
  </tr>
"""
    for line in prompts:
        question += '<tr><td>' + line + '</td><td></td><td></td></tr>'
    return question + '</table>\n'


#--------------------#
# SOLUTION COMPILERS #
#--------------------#

def make_eval_output_solution(num, prompts=[], answers=[]):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += """<table class='no-center'>
  <tr>
    <th></th>
    <th>Evaluates to</th>
    <th>Outputs</th>
  </tr>
"""
    for i, line in enumerate(prompts):
        question += '<tr><td>' + line + '</td>\n'
        question += '<td>' + answers[i]['eval'] + '</td>\n'
        question += '<td>' + answers[i]['output'] + '</td></tr>'
    return question + '</table>\n'
