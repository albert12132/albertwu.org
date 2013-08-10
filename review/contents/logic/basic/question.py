from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Logic Programming'
level = 'basic'

references = [
    'Lecture: Declarative programming, unification',
    'Lab 7b',
]

notes = """We will be using the Logic interpreter, which you can get
""" + a('http://www-inst.eecs.berkeley.edu/~cs61a/su13/lab/lab07b/logic/logic.py', 'here', internal=False) + """. You will also need your
Scheme project in the same directory. You can run the Logic
interpreter from your terminal with:""" + pre("""
python3 logic.py""", classes='prettyprint') + """You can load a
<tt>.logic</tt> file with""" + pre("""
python3 logic.py -load file.logic""", classes='prettyprint')

contents = [
    {'name': 'Conceptual',
     'id': 'conceptual',
     'maker': make_concept_question,
     'questions': lambda: concept_questions},
    {'name': 'What would Logic print?',
     'id': 'print',
     'maker': make_print_question,
     'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

concept_questions = [
    {
        'description': """Explain the difference between declarative
        programming and imperative programming.""",

        'solution': """Imperative programming is a programming
        paradigm where a sequence of instructions tells the computer
        what to do (Python is one such imperative programming
        language. Declarative programming is a programmign paradigm
        where a set of constraints (e.g. facts) are given to the
        computer, and the computer decides what to do in order to
        solve a given problem (Logic is one such declarative
        programming language."""
    },
    {
        'description': """Describe the difference between a
        <i>fact</i> and a <i>query</i> in the Logic language.""",

        'solution': """A <i>fact</i> declares a certain relation
        to be true (i.e. once the fact is declared, the specified
        relation is, <i>by definition</i>, true). A <i>query</i>
        is a question that asks if a specified relation is true.
        Here is a simple example of facts and queries:""" + pre("""
logic> (fact (> 3 2))
logic> (query (> 3 2))
Success!
logic> (fact (> 2 3))  ; false in real life, but here it's declared true!
logic> (query (> 2 3))
Success!
""", classes='prettyprint')
    },
    {
        'description': """Describe the difference between a
        <i>simple fact</i> and a <i>compound fact</i> in the Logic
        language.""",

        'solution': """A <i>simple fact</i> has only one clause.
        The syntax looks like this:""" + pre("""
(fact (________))""", classes='prettyprint') + """
        A <i>compound fact</i> is still a fact (it declares a relation
        to be true), but it is composed of a <i>conclusion</i>
        and <i>hypotheses</i>. The conlusion comes first, followed
        by the hypotheses. Think of it as a fact whose truth depends
        on the truth of smaller facts. The syntax looks like this:
        """ + pre("""
(fact (___conclusion___)
      (___hypothesis1__)
      (___hypothesis2__)
      ...)""", classes='prettyprint')
    },
]

print_questions = [
    {
        'description': """Assume the following facts have been loaded
        into the Logic interpreter:""" + pre("""
(fact (married lucille george-sr))
(fact (married lindsay tobias))

(fact (parent lucille gob))
(fact (parent george-sr gob))
(fact (parent lucille michael))
(fact (parent george-sr michael))
(fact (parent lucille buster))
(fact (parent oscar buster))
(fact (parent lucille lindsay))
(fact (parent lucille annyong))

(fact (parent michael george-michael))
(fact (parent lindsay maeby))
(fact (parent tobias maeby))
(fact (parent gob steve))

(fact (sibling ?s1 ?s2)
      (parent ?p1 ?s1)
      (parent ?p1 ?s2))

(fact (uncle-or-aunt ?u ?c)
      (parent ?p ?c)
      (sibling ?u ?p))""", classes='prettyprint'),
        'symbol': 'logic> ',
        'prompts': [
            ('(query (parent lucille michael))', 'Success!'),
            ('(query (parent george-sr buster))', 'Failed.'),
            ('(query (parent ?who gob))', """Success!
who: lucille
who: george-sr"""),
            ('(query (parent lucille ?who))', """Success!
who: gob
who: michael
who: buster
who: lindsay
who: annyong"""),
            ('(query (uncle-or-aunt buster ?who))', """Success!
who: george-michael
who: maeby
who: steve"""),
            ('(query (?rel lindsay tobias))', """Success!
rel: married"""),
        ],
    },
]

code_questions = [
    {
        'description': """Write a fact or set of facts for the
        <tt>first</tt> relation, which checks if a given
        item is the first element in a given list.""",
        'code': """
(fact (first ; YOUR CODE HERE

; Tests
logic> (query (first 3 (3 2 1)))
Success!
logic> (query (first 2 (3 2 1)))
Failed.
logic> (query (first ?what (1 2 3)))
Success!
what: 1
""",
        'hint': """Conceptually, how would you check if a list begins
        with an item? Is the process recursive?""",
        'solution': """
(fact (first ?f (?f . ?r)))"""
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>rest-with</tt> relation, which checks if a given
        item is the rest (in the Rlist sense) of a list.""",
        'code': """
(fact (rest ; YOUR CODE HERE

; Tests
logic> (query (rest (2 3) (1 2 3)))
Success!
logic> (query (rest (3 2) (3 2 1)))
Failed.
logic> (query (rest ?what (1 3 2)))
Success!
what: (3 2)
""",
        'solution': """
(fact (rest ?r (?f . ?r)))"""
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>cons</tt> relation, which checks if a given
        first and rest can <tt>cons</tt> together (in the Scheme
        sense) to form a given list.""",
        'code': """
(fact (cons ; YOUR CODE HERE

; Tests
logic> (query (cons 1 (2 3) (1 2 3)))
Success!
logic> (query (cons (3 2) 1 (3 2 1)))
Failed.
logic> (query (cons 3 ?what (3 1 2)))
Success!
what: (1 2)
logic> (query (cons ?what (1 2) (3 1 2)))
Success!
what: 3
""",
        'solution': """
(fact (cons ?f ?r (?f . ?r)))"""
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>contains</tt> relation, which checks if a given
        list contains a given item.""",
        'code': """
(fact (contains ; YOUR CODE HERE

; Tests
logic> (query (contains (2 1 3) 1))
Success!
logic> (query (contains (4 2 3) 5))
Failed.
logic> (query (contains (3 4 2) ?what))
Success!
what: 3
what: 4
what: 2
""",
        'hint': """Conceptually, how would you check if a list
        contains an item? Is this process recursive?""",
        'solution': """
(fact (contains (?item . ?r) ?item))
(fact (contains (?not-item . ?r) ?item)
      (contains ?r ?item))"""
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

