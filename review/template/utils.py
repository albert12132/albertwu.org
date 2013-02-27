from utils.utils import *

#-------------------#
# Utility functions #
#-------------------#

def make_list(iterable, modifier=None):
    if modifier is None:
        modifier = lambda x: x
    return '\n'.join(map(lambda items: li(modifier(items)), iterable))

def contents_li(contents):
    assert 'name' in contents, 'No valid name'
    assert 'id' in contents, 'no valid tag'
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
    return make_section(sec, 'maker q')

def make_solution_section(sec):
    return make_section(sec, 'maker s')

#--------------------#
# QUESTION COMPILERS #
#--------------------#

def make_concept_question(num, question):
    assert 'description' in question, 'no description'
    text = h(3, 'Q' + str(num), classes='question')
    text += p(question['description'])
    if 'code' in question:
        text += pre(question['code'], classes='prettyprint')
    if 'hint' in question:
        text += p(b('Hint') + ': ' + question['hint'], classes='hint')
    return text

def make_print_question(num, question):
    assert 'prompts' in question, 'not a valid print question'
    prompts = question['prompts']
    text = h(3, 'Q' + str(num), classes='question')
    prints = []
    for line in prompts:
        prints.append(PROMPT + line[0])
        if len(line) == 2:
            prints.append('______')
    text += pre('\n'.join(prints), classes='prettyprint')
    return text

def make_env_question(num, question):
    assert 'code' in question, 'not a valid environment diagram'
    text = h(3, 'Q' + str(num), classes='question')
    text += pre(question['code'], classes='prettyprint')
    return text

#--------------------#
# SOLUTION COMPILERS #
#--------------------#

def make_concept_solution(num, question):
    assert 'solution' in question, 'No solution'
    text = h(3, 'Q' + str(num), classes='question')
    text += p(question['solution'], classes='solution')
    return text

def make_env_solution(num, question):
    assert 'solution' in question, 'Not a valid solution'
    text = h(3, 'Q' + str(num), classes='question')
    text += a(question['solution'], 'Link to Online Python Tutor', internal=False)
    return text

def make_code_solution(num, question):
    assert 'solution' in question, 'Not a valid solution'
    text = h(3, 'Q' + str(num), classes='question')
    text += pre(question['solution'], classes='prettyprint')
    return text

def make_print_solution(num, question):
    assert 'prompts' in question, 'no prompts'
    text = h(3, 'Q' + str(num), classes='question')
    prompts = filter(lambda x: len(x) == 2, question['prompts'])
    prompts = make_list(prompts, lambda prompt: pre(prompt[1], classes='prettyprint'))
    text += ol(prompts)
    return text

