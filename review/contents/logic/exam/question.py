from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Logic'
level = 'exam'

references = [
    ('Lecture: Declarative Programming', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/31-Logic_1pps.pdf'),
    ('Lecture: Unification', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/32-Unification_1pps.pdf'),
    ('Lab 11', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab11/lab11.php'),
    ('Discussion 12', 'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion12.pdf'),
]

notes = """We will be using the Logic interpreter, which you can get
""" + a('http://composingprograms.com/examples/logic/logic.py', 'here', internal=False) + """. You will also need your
Scheme project in the same directory. You can run the Logic
interpreter from your terminal with:""" + pre("""
python3 logic.py""", classes='prettyprint') + """You can load a
<tt>.logic</tt> file with""" + pre("""
python3 logic.py -load file.logic""", classes='prettyprint') + """Alternatively,
you can use the """ + a('http://www-inst.eecs.berkeley.edu/~cs61a/fa13/logic/logic.html',
'online Logic interpreter', internal=False) + '.'

contents = [
    # {'name': 'What would Logic print?',
    #  'id': 'print',
    #  'maker': make_print_question,
    #  'questions': lambda: print_questions},
    {'name': 'Code Writing',
     'id': 'code',
     'maker': make_code_question,
     'questions': lambda: code_questions},
    {'name': 'Logical Trees (courtesy of Sarah Kim)',
     'id': 'sarah',
     'maker': make_code_question,
     'questions': lambda: sarah_questions,
     'notes': lambda: sarah_notes},
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
#     {
#         'description': """Write a fact or set of facts for the
#         <tt>remove</tt> relation, which takes a list and an item, and
#         checks that a second list contains the same items as the
#         first, but with all instances of the item removed.""",
#         'code': """
# (fact (remove ; YOUR CODE HERE
# 
# ; Tests
# logic> (query (remove (1 2 3 4) 1 (2 3 4)))
# Success!
# logic> (query (remove (1 2 1) 1 (2)))
# Success!
# logic> (query (remove (2 2) 2 ?what))
# Success!
# what: ()
# """,
#         'solution': """
# (fact (remove () ?item ()))
# (fact (remove (?item . ?r) ?item ?lst)
#       (remove ?r ?item ?lst))
# (fact (remove (?f . ?r) ?item (?f . ?s))
#       (remove ?r ?item ?s))""",
#     },
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

sarah_notes = """<i>The following questions were written by Sarah Kim
for Summer 2013.</i></p>
<p>Let's create a series of facts on a tree
        diagram. The facts are of the following form:""" + pre("""
(fact (tree number entry left right))""", classes='prettyprint') + """
        Some examples:""" + pre("""
(fact (tree tree-1 6 tree-2 tree-3))
(fact (tree tree-2 4 tree-4 tree-5))
(fact (tree tree-3 8 tree-6 tree-7))
(fact (tree tree-4 3 tree-8 none))
(fact (tree tree-5 5 none none))
(fact (tree tree-6 7 none none))

(fact (tree tree-7 11 tree-9 tree-10))
(fact (tree tree-8 2 tree-11 none))
(fact (tree tree-9 9 none tree-12))
(fact (tree tree-10 12 none none))
(fact (tree tree-11 1 none none))
(fact (tree tree-12 10 none none))""", classes='prettyprint')

sarah_questions = [
    {
        'description': """Write a <tt>find-entry</tt> fact that
        associates tree number to tree entry.""",
        'code': """
logic> (query (find-entry tree-12 10))
Success!
logic> (query (find-entry tree-2 ?x))
Success!
x: 4
logic> (query (find-entry ?tree 11))
Sucess!
tree: tree-7
""",
        'solution': """
(fact (find-entry ?number ?entry) (tree ?number ?entry ?left ?right))""",
    },
    {
        'description': """Write a <tt>check-leaf</tt> fact that checks
        if a tree is a leaf (no trees in left or right).""",
        'code': """
logic> (query (check-leaf tree-12))
Sucess!
logic> (query (check-leaf tree-4))
Failed.
""",
        'solution': """
(fact (check-leaf ?number) (tree ?number ?leaf none none))""",
    },
    {
        'description': """What would Logic print?""",
        'code': """
logic> (query (check-leaf ?x))
""",
        'solution': """
Success!
x: tree-5
x: tree-6
x: tree-10
x: tree-11
x: tree-12""",
    },
    {
        'description': """Write a <tt>smallest-entry</tt> fact that
        finds the smallest entry of a tree.""",
        'code': """
logic> (query (smallest-entry tree-2 ?leaf))
Success!
leaf: 1
logic> (query (smallest-entry tree-12 ?leaf))
Success!
leaf: 10
logic> (query (smallest-entry tree-7 ?leaf))
leaf: 9
""",
        'solution': """
(fact (smallest-entry ?number ?entry)
      (tree ?number ?entry none ?right))
(fact (smallest-entry ?number ?entry)
      (tree ?number ?other-entry ? left ?right)
      (smallest-entry ?left ?entry))""",
    },
    {
        'description': """Write a <tt>find-parent</tt> fact, which
        finds the parent of a number.""",
        'code': """
logic> (query (find-parent tree-11 ?parent))
Success!
parent: tree-8
""",
        'solution': """
(fact (find-parent ?number ?parent)
      (tree ?parent ?entry ?number ?right))
(fact (find-parent ?number ?parent)
      (tree ?parent ?entry ?left ?number))""",
    },
    {
        'description': """Write a <tt>generation</tt> fact, which
        lists all the members of a tree's family tree.""",
        'code': """
logic> (query (generation tree-11 ?members))
Success!
members: tree-1
members: tree-2
members: tree-4
members: tree-8
members: tree-11
""",
        'solution': """
(fact (generation ?number ?grandfather)
      (find-parent ?number ?father)
      (generation ?father ?grandfather))
(fact (generation ?number ?number))""",
    },
    {
        'description': """What would happen if for the
        <tt>generation</tt> fact, we put the second fact before the
        first fact?""",
        'code': """
logic> (query (generation tree-11 ?members))
""",
        'solution': """
Success!
members: tree-11
members: tree-8
members: tree-4
members: tree-2
members: tree-1""",
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

