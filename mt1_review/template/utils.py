#-------------------#
# Utility functions #
#-------------------#

def code(text):
    return '<tt>' + text + '</tt>'

def make_list(maker, lst):
    return '\n'.join(map(lambda args: maker(*args), lst))

def references_li(name):
    return '<li>' + name + '</li>'

def contents_li(name, hash_id, maker=None, lst=None):
    return '<li><a href="#' + hash_id + '">' + name + '</a></li>'

def make_section(sec):
    maker, lst = sec[2](), sec[3]()
    assert callable(maker), 'Not a valid maker'
    assert type(lst) == list, 'Not a valid question lsit'
    section = '<h2 class="subtopic" id="' + sec[1] + '">' + sec[0] \
        + '</h2>\n'
    for i, question in enumerate(lst):
        section += maker(i+1, **question) + '\n'
    return section

#--------------------#
# QUESTION COMPILERS #
#--------------------#

def make_concept_question(num, description='', code=None, hint=None):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<p>' + description + '</p>\n'
    if code:
        question += '<pre class="prettyprint">' + code + '</pre>\n'
    if hint:
        question += '<p class="hint"><b>Hint</b>: ' + hint + '</p>\n'
    return question

def make_print_question(num, prompts=[]):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<pre class="prettyprint">\n'
    for line in prompts:
        question += '&gt;&gt;&gt; ' + line + '\n______\n'
    return question + '</pre>\n'

def make_env_question(num, code=''):
    question = '<h3 class="question">Q' + str(num) + '</h3>\n'
    question += '<pre class="prettyprint">' + code + '</pre>\n'
    return question

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

def make_concept_solution(num, explanation=''):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<p class="solution">' + explanation + '</p>\n'
    return solution

def make_env_solution(num, link='', message=None):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<a href="' + link + '">'
    solution += link if not message else message
    solution += '</a>\n'
    return solution

def make_code_solution(num, code='', explanation=None):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<pre class="prettyprint">' + code + '</pre>\n'
    if explanation:
        solution += '<p class="solution">' + explanation + '</p>\n'
    return solution

def make_print_solution(num, answers=[]):
    solution = '<h3 class="question">Q' + str(num) + '</h3>\n'
    solution += '<pre class="codeblock">\n'
    for i, answer in enumerate(answers):
        solution += str(i+1) + ') ' + answer + '\n'
    return solution + '</pre>\n'

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
