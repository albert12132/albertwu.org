~ title: Interpreters
~ level: basic

<block references>
* [Lecture: Calculator](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/25-Calculator_1pps.pdf)
* [Lecture: Interpreters](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/26-Interpreters_1pps.pdf)
* [Lab 8](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab08/lab08.php)
* [Discussion 10](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion10.pdf)
</block references>

<block notes>
</block notes>

<block contents>

Conceptual questions
--------------------

<question>

Describe what a "REPL" is.

<solution>

REPL stands for Read-Eval-Print-Loop. The first step, Read, inolves the
tokenizer and the parser -- they take user input (a string) and convert
it into data structures that are understood by the evaluator. The
Evaluator converts those data structures into values, which are then
Printed out to the screen. The loop then restarts the whole process.

</solution>

<question>

Describe what a tokenizer does.

<solution>

The tokenizer takes user input (a string) and breaks it up into tokens.
This is an intermediate step in the Parser.

</solution>

<question>

Explain the difference between a parser and an evaluator.

<solution>

The parser converts a string of user input into an expression. The
parser is not responsible for evaluating the expression -- as such, the
parser checks if expressions are well-formed, but not if they actually
evaluate to intelligible values (e.g. in SCheme, `(3 + 2)` is
well-formed, but doesn't evaluate to a proper value).

The evaluator takes expression objects given by the Parser and
evaluates it.

</solution>

<question>

The following is a list of functions and data structures from your
Scheme project. For each one, label it Parser or Evaluator to describe
which part of the interpreter it belongs to.

1. `do_lambda_form`
2. `tokenize`
3. `Buffer`
4. `Frame`
5. `read_tail`
6. `make_call_frame`
7. `scheme_eval`
8. `scheme_read`
9. `LambdaProcedure`

<solution>

1. Evaluator
2. Parser
3. Parser
4. Evaluator
5. Parser
6. Evaluator
7. Evaluator
8. Parser
9. Evaluator

</solution>

<question>

Explain how `scheme_eval` and `scheme_apply` from the Scheme project
are mutually recursive.

<solution>

`scheme_eval` will call `scheme_apply` when it is evaluating function
calls.  `scheme_apply` will then create a new environment, and call
`scheme_eval` on the body of the function. Notice that this procedure
is different than the one for the Calculator language, because
Calculator was simple enough not to requier mutual recursion.

</solution>

</block contents>

