from utils.utils import *
#-------------------#
# Utility functions #
#-------------------#

def make_id_class(kargs):

def make_list(iterable, **kargs):

def pre(code, **kargs):

def a(href, contents, internal=True, **kargs):

def p(contents, **kargs):

def h(num, title, **kargs):

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
