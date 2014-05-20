~ title: Logic
~ level: basic

<block references>
* [Lecture: Declarative Programming](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/31-Logic_1pps.pdf)
* [Lecture: Unification](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/32-Unification_1pps.pdf)
* [Lab 11](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab11/lab11.php)
* [Discussion 12](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion12.pdf)
</block references>

<block notes>
We will be using the Logic interpreter, which you can get
[here](http://composingprograms.com/examples/logic/logic.py). You will
also need your Scheme project in the same directory. You can run the
Logic
interpreter from your terminal with:

    python3 logic.py

You can load a `.logic` file with

    python3 logic.py -load file.logic

Alternatively, you can use the [online Logic
interpreter](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/logic/logic.html)
</block notes>


<block contents>

Conceptual Questions
--------------------

<question>

Explain the difference between declarative programming and imperative
programming.

<solution>

Imperative programming is a programming paradigm where a sequence of
instructions tells the computer what to do (Python is one such
imperative programming language. Declarative programming is a
programming paradigm where a set of constraints (e.g. facts) are given
to the computer, and the computer decides what to do in order to solve
a given problem (Logic is one such declarative programming language.

</solution>

<question>

Describe the difference between a *fact* and a *query* in the Logic
language.

<solution>

A *fact* declares a certain relation to be true (i.e. once the fact is
declared, the specified relation is, *by definition*, true). A *query*
is a question that asks if a specified relation is true.  Here is a
simple example of facts and queries:

    logic> (fact (> 3 2))
    logic> (query (> 3 2))
    Success!
    logic> (fact (> 2 3))  ; false in real life, but here it's declared true!
    logic> (query (> 2 3))
    Success!

</solution>

<question>

Describe the difference between a *simple fact* and a *compound fact*
in the Logic language.

<solution>

A *simple fact* has only one clause. The syntax looks like this:

    (fact (________))


A *compound fact* is still a fact (it declares a relation to be true),
but it is composed of a *conclusion* and *hypotheses*. The conlusion
comes first, followed by the hypotheses. Think of it as a fact whose
truth depends on the truth of smaller facts. The syntax looks like
this:

    (fact (___conclusion___)
          (___hypothesis1__)
          (___hypothesis2__)
          ...)

</solution>

What would Logic print?
-----------------------

<question>

Assume the following facts have been loaded into the Logic interpreter:

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
          (sibling ?u ?p))

<prompt>
    logic> (query (parent lucille michael))
    Success!
    logic> (query (parent george-sr buster))
    Failed.
    logic> (query (parent ?who gob))
    Success!
    who: lucille
    who: george-sr
    logic> (query (parent lucille ?who))
    Success!
    who: gob
    who: michael
    who: buster
    who: lindsay
    who: annyong
    logic> (query (uncle-or-aunt buster ?who))
    Success!
    who: george-michael
    who: maeby
    who: steve
    (query (?rel lindsay tobias))
    Success!
    rel: married
</prompt>

Code-Writing question
---------------------

<question>

Write a fact or set of facts for the `first` relation, which checks
if a given item is the first element in a given list.

    (fact (first ; YOUR CODE HERE

    ; Tests
    logic> (query (first 3 (3 2 1)))
    Success!
    logic> (query (first 2 (3 2 1)))
    Failed.
    logic> (query (first ?what (1 2 3)))
    Success!
    what: 1

**Hint**: Conceptually, how would you check if a list begins with an
item? Is the process recursive?

<solution>

    (fact (first ?f (?f . ?r)))

</solution>

<question>

Write a fact or set of facts for the `rest-with` relation, which checks
if a given item is the rest (in the Rlist sense) of a list.

    (fact (rest ; YOUR CODE HERE

    ; Tests
    logic> (query (rest (2 3) (1 2 3)))
    Success!
    logic> (query (rest (3 2) (3 2 1)))
    Failed.
    logic> (query (rest ?what (1 3 2)))
    Success!
    what: (3 2)

<solution>

    (fact (rest ?r (?f . ?r)))

</solution>

<question>

Write a fact or set of facts for the `cons` relation, which checks if a
given first and rest can `cons` together (in the Scheme sense) to form
a given list.

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

<solution>

    (fact (cons ?f ?r (?f . ?r)))

</solution>

<question>

Write a fact or set of facts for the `contains` relation, which checks
if a given list contains a given item.

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

**Hint**: Conceptually, how would you check if a list contains an item?
Is this process recursive?

<solution>

(fact (contains (?item . ?r) ?item))
(fact (contains (?not-item . ?r) ?item)
      (contains ?r ?item))

</solution>

</block contents>
