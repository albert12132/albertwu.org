from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Nonlocal'
level = 'exam'

references = [
    'Lecture: Objects, Lists, Dictionaries, Mutable Data',
    'Lecture: Mutable Data, Mutable data types',
    'Lab 3b'
]

notes = ''

contents = [
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

code_questions = [
        {'description': """Implement a function <tt>make_sassy_function</tt> which takes a function <tt>f</tt> and returns a modified version of <tt>f</tt>: the new function should only work every other function call. The other half of the time, it should return a rude message.""",
     'code': """
def make_sassy_function(f, msg):
    \"\"\"Returns a version of f that only works every other function
    call.

    >>> f = lambda x: x**2
    >>> sassy_f = make_sassy_function(f, 'Um, excuse me?')
    >>> sassy_f(4)
    16
    >>> sassy_f(5)
    'Um, excuse me?'
    >>> sassy_f(6)
    36
    >>> g = lambda x, y: x*y
    >>> sassy_g = make_sassy_function(g, "Don't tell me what to do!")
    >>> sassy_g(1, 2)
    2
    >>> sassy_g(5, 4)
    "Don't tell me what to do!"
    \"\"\" """,
    'solution': """
def make_sassy_function(f, msg):
    sassy = True
    def sassy_f(*args):
        nonlocal sassy
        sassy = not sassy
        if sassy:
            return msg
        return f(*args)
    return sassy_f"""
    },
        {'description': """Implement a function <tt>sentence_buffer</tt> which returns another one-argument function. This function will take in a word at a time, and it saves all the words that it has seen so far. If takes in a word that ends in a period ("."), that denotes the end of a sentence, and the function returns all the words in the sentence. It will also clear its memory, so that it no longer remembers any words.""",
     'code': """
def sentence_buffer():
    \"\"\"Returns a function that will return entire sentences when it
    receives a string that ends in a period.

    >>> buffer = sentence_buffer()
    >>> buffer("This")
    >>> buffer("is")
    >>> buffer("Spot.")
    'This is Spot.'
    >>> buffer("See")
    >>> buffer("Spot")
    >>> buffer("run.")
    'See Spot run.'
    \"\"\" """,
    'solution': """
def sentence_buffer():
    sentence = ''
    def buffer(word):
        nonlocal sentence
        sentence += word + ' '
        if word[-1] == '.':
            result, sentence = sentence, ''
            return result.strip()
    return buffer"""
    }
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

