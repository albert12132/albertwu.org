from utils.utils import *

#-------------------#
# Utility functions #
#-------------------#

PROMPT='>>> '

def has_keys(keys, d):
    if type(keys) != list:
        keys = [keys]
    for key in keys:
        assert key in d, 'No key {}'.format(key)
    

def contents_li(contents):
    has_keys(['name', 'id'], contents)
    name, hash_id = contents['name'], contents['id']
    return a(hash_id, name)

def make_section(sec, maker):
    maker, questions = sec[maker], sec['questions']()
    assert callable(maker), 'Not a valid maker'
    assert type(questions) == list, 'Not a valid question list'
    section = h(2, sec['name'], ids=sec['id'], classes='subtopic')
    for i, question in enumerate(questions):
        section += maker(i+1, question) + '\n'
    return section

def make_question_section(sec):
    return make_section(sec, 'maker')

#--------------------#
# QUESTION COMPILERS #
#--------------------#


def toggle_button(tag):
    return "<button id='{}' class='toggleButton'>Toggle Solution</button>".format(tag)

def make_counter():
    i = 0
    def counter():
        nonlocal i
        result = i
        i += 1
        return result
    return counter

counter = make_counter()

def make_concept_question(num, question):
    has_keys(['description', 'solution'], question)
    text = h(3, 'Q' + str(num), classes='question')
    text += p(question['description'])
    if 'code' in question:
        text += pre(question['code'], classes='prettyprint')
    if 'hint' in question:
        text += p(b('Hint') + ': ' + question['hint'], classes='hint')

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    text += div(p(b('Answer: ') + question['solution']),
              classes=['solution', tag])
    return text

def make_code_question(num, question):
    has_keys(['description', 'solution'], question)
    text = h(3, 'Q' + str(num), classes='question')
    text += p(question['description'])
    if 'code' in question:
        text += pre(question['code'], classes='prettyprint')
    if 'hint' in question:
        text += p(b('Hint') + ': ' + question['hint'], classes='hint')

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    solution = pre(question['solution'], classes='prettyprint')
    if 'explanation' in question:
        solution += p(b('Explanation: ') + question['explanation'])
    text += div(solution, classes=['solution', tag])
    return text

def make_print_question(num, question):
    has_keys('prompts', question)
    prompts = question['prompts']
    text = h(3, 'Q' + str(num), classes='question')
    if 'description' in question:
        text += p(question['description'])
    symbol = question['symbol'] if 'symbol' in question else PROMPT

    tag = '{}'.format(counter())
    prints = []
    for line in prompts:
        prints.append(symbol + line[0])
        if len(line) == 2:
            prints.append(span('______', classes='blank'+tag) + \
                          span(line[1], classes=['solution', tag]))
    text += pre('\n'.join(prints), classes='prettyprint')
    text += toggle_button(tag)
    return text

def make_env_question(num, question):
    has_keys('code', question)
    text = h(3, 'Q' + str(num), classes='question')
    text += pre(question['code'], classes='prettyprint')

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    text += div(a(question['solution'], 'Link to Online Python Tutor', internal=False),
            classes=['solution', tag])
    return text

