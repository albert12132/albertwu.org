from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Logic'
level = 'exam'

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
    # {'name': 'What would Logic print?',
    #  'id': 'print',
    #  'maker': make_print_question,
    #  'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
]

print_questions = [
    {
        'description': """Assume the following facts have been loaded
        into the Logic interpreter:""" + pre("""
"""),
        'symbol': 'logic> ',
        'prompts': [
            ('x + 2', '4'),
            ('x + 4',),
        ]
    },
]

code_questions = [
    {
        'description': """Write a fact or set of facts for the
        <tt>interleave</tt> relation, which checks if two given
        lists will interleave into a third given list. You cannot
        assume that the lists are of equal length.""",
        'code': """
(fact (interleave ; YOUR CODE HERE

; Tests
logic> (query (interleave (1 2) (3 4) (1 3 2 4)))
Success!
logic> (query (interleave (1 2) (3 4) (1 2 3 4)))
Failed.
logic> (query (interleave (1 2) (3 4 5) ?what))
Success!
what: (1 3 2 4 5)
""",
        'solution': """
(fact (interleave ?lst () ?lst))
(fact (interleave () ?lst ?lst))
(fact (interleave (?a . ?x) (?b . ?y) (?a ?b . ?z))
      (interleave ?x ?y ?z))"""
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>zip</tt> relation, which checks if two given
        lists will zip into a third given list (see the tests to
        get an idea of what "zip" means). You can
        assume that the lists are of equal length.""",
        'code': """
(fact (zip ; YOUR CODE HERE

; Tests
logic> (query (zip (1 2) (3 4) ((1 3) (2 4))))
Success!
logic> (query (zip (1 2) (3 4) (1 3 2 4)))
Failed.
""",
        'solution': """
(fact (zip () () ()))
(fact (zip (?a . ?x) (?b . ?y) ((?a ?b) . ?z))
      (zip ?x ?y ?z))"""
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>reverse</tt> relation, which takes two lists and checks
        if the second list is the reverse of the first. You can
        assume the <tt>append</tt> relation is already defined.""",
        'code': """
(fact (reverse ; YOUR CODE HERE

; Tests
logic> (query (reverse (1 2 3 4) (4 3 2 1)))
Success!
logic> (query (reverse (1 2 3) (2 1 3)))
Failed.
logic> (query (reverse (4 2 5) ?what))
Success!
what: (5 2 4)
""",
        'solution': """
(fact (reverse () ()))
(fact (reverse (?f . ?rest) ?lst)
      (reverse ?rest ?reverse-rest)
      (append ?reverse-rest (?f) ?lst))""",
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>remove</tt> relation, which takes a list and an item, and
        checks that a second list contains the same items as the
        first, but with all instances of the item removed.""",
        'code': """
(fact (remove ; YOUR CODE HERE

; Tests
logic> (query (remove (1 2 3 4) 1 (2 3 4)))
Success!
logic> (query (remove (1 2 1) 1 (2)))
Failed.
logic> (query (remove (2 2) 2 ?what))
Success!
what: ()
""",
        'solution': """
(fact (remove () ?item ()))
(fact (remove (?item . ?r) ?item ?lst)
      (remove ?r ?item ?lst))
(fact (remove (?f . ?r) ?item (?f . ?s))
      (remove ?r ?item ?s))""",
    },
    {
        'description': """Write a fact or set of facts for the
        <tt>subsequence</tt> relation, which takes two lists, and
        checks if the first list is a non-contiguous subsequence of
        the second list. <i>Non-contiguous</i> means the elements
        of the first list do not have to appear consecutively in the
        second list, but they do have to appear in order.""",
        'code': """
(fact (subsequence ; YOUR CODE HERE

; Tests
logic> (query (subsequence (1 2 3) (0 1 2 0 0 3)))
Success!
logic> (query (subsequence (1 2 3) (1 3 2 3)))
Success!
logic> (query (subsequence (1 2 3) (1 3 2)))
Failed.
logic> (query (subsequence () (1 3 2)))
Success!
""",
        'solution': """
(fact (subsequence () ?lst))
(fact (subsequence (?f . ?r) (?f . ?s))
      (subsequence ?r ?s))
(fact (subsequence (?a . ?r) (?b . ?s))
      (subsequence (?a . ?r) ?s))""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

