from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Interpreter'
level = 'basic'

references = [
    ('Lecture: Calculator',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/25-Calculator_1pps.pdf'),
    ('Lecture: Interpreters',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/26-Interpreters_1pps.pdf'),
    ('Lab 8',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab08/lab08.php'),
    ('Discussion 10',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion10.pdf'),
]

notes = ''

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
]

concept_questions = [
    {
        'description': """Describe what a "REPL" is.""",
        'solution': """REPL stands for Read-Eval-Print-Loop. The first
        step, Read, inolves the tokenizer and the parser -- they take
        user input (a string) and convert it into data structures that
        are understood by the evaluator. The Evaluator converts those
        data structures into values, which are then Printed out to the
        screen. The loop then restarts the whole process."""
    },
    {
        'description': """Describe what a tokenizer does.""",
        'solution': """The tokenizer takes user input (a string) and
        breaks it up into tokens. This is an intermediate step in the
        Parser"""
    },
    {
        'description': """Explain the difference between a parser and
        an evaluator.""",
        'solution': """The parser converts a string of user input into
        an expression. The parser is not responsible for evaluating the
        expression -- as such, the parser checks if expressions are
        well-formed, but not if they actually evaluate to intelligible
        values (e.g. in SCheme, <tt>(3 + 2)</tt> is well-formed, but
        doesn't evaluate to a proper value).</p>
        <p>The evaluator takes expression objects given by the Parser
        and evaluates it."""
    },
    {
        'description': """The following is a list of functions and data
        structures from your Scheme project. For each one, label it
        Parser or Evaluator to describe which part of the interpreter
        it belongs to.""" + ol(contents=list(map(tt, (
                'do_lambda_form',
                'tokenize',
                'Buffer',
                'Frame',
                'read_tail',
                'make_call_frame',
                'scheme_eval',
                'scheme_read',
                'LambdaProcedure',
        )))),
        'solution': ol(contents=(
            'Evaluator',
            'Parser',
            'Parser',
            'Evaluator',
            'Parser',
            'Evaluator',
            'Evaluator',
            'Parser',
            'Evaluator',
        ))
    },
    {
        'description': """Explain how <tt>scheme_eval</tt> and
        <tt>scheme_apply</tt> from the Scheme project are mutually
        recursive.""",
        'solution': """<tt>scheme_eval</tt> will call
        <tt>scheme_apply</tt> when it is evaluating function calls.
        <tt>scheme_apply</tt> will then create a new environment, and
        call <tt>scheme_eval</tt> on the body of the function. Notice
        that this procedure is different than the one for the
        Calculator language, because Calculator was simple enough not
        to requier mutual recursion."""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

