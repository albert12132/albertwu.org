~ title: Autograder

In 61A, we provide students with an autograder for projects. This
autograder periodically (usually every 30 minutes) emails students
about the correctness of their submissions.

It is important to understand a few aspects of the autograder,
described below.

Grading
-------

Passing the autograder does NOT ensure a perfect score. The sanity
autograder we release before the deadline does not run every test that
we have. When we actually grade your final submission, we will have
extra tests for edge cases.

Admittedly, this might stress some students out, but the point is to
get you in the habit of testing your own code. When working on any
project, it is prudent to make sure your code works, even for edge
cases.

On the other hand, if you DON'T pass the sanity autograder, you will
most likely not get a perfect score, so make sure you at least pass
the sanity autograder.

One more note: some other classes at Berkeley do not even have
autograders for their projects. Some might even argue this is a better
educational practice. In any case, keep in mind that the autograder is
designed to remind you of bugs or implementations you might have
forgotten.

Debugging
---------

The autograder is NOT a debugger. The only thing the autograder does
is run your code against a suite of inputs. If your code does not
produce the desired output, the autograder notifies you.

While the autograder is great for detecting the existence of bugs, it
does not tell you where the bugs are, nor does it tell you how to fix
them. Debugging is up to you to do.

For this reason, please don't keep submitting to the autograder every
time you make a minute change in your code. You should do everything
possible to debug, test, and fix your code before you submit to the
autograder.

Design philosophy
-----------------

As noted above, the autograder tests your code against a suite of
inputs and checks against a suite of outputs. While some students
might find this format "stifles student creativity," keep in mind
that most programs you write are intended for some target audience. If
your program doesn't behave in an expected fashion, you will receive
lots of complaints from that audience. In other words, having an "exact-answer" requirement is not
unreasonable.
