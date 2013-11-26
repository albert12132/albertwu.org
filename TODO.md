Extracurricular
===============

* Unix
    * general utilities and flags
        * ls [dir]
        * rm FIRST [SECOND ...]
        * mkdir FIRST [SECOND ...]
        * mv FIRST [SECOND ...] DST
    * reading and pagers (cat, less, more)
    * filters (wc, diff, sort, head, tail, cut)
    * grep, sed
    * ssh keys
* Ubuntu/other linux for Windows

Topics
======

* Tuples, Lists, and Rlists (why use one over the other)
* Data Abstraction
* Recursion
* OOP

Course Design
=============

* Course Goals
    1. Teach problem solving skills for computer science
        * Construction of algorithms: how do we arrive at the
          solution?
        * Analysis of algorithms
    2. Teach language-agnostic computer science concepts
        * Data structures (Rlists, Trees, lists, dictionaries)
        * Abstraction, OOP
        * Don't focus too much on language features: introduce
          language-specific features with motivation of solving a
          specific dilemma
        * introduction to special topics
    3. Teach coding
        * Debugging skills
        * Coding style
        * Secondary goal: learn language-specific features
* homeworks:
    * Teaching effectiveness:
        * code writing is good!
        * maybe not as much fill in the blank; students should
          build more (e.g. the scheme derivative hw, brackulator
          hw)
            * fill in the blank questions are good if there is a
              *specific* concept that it tests
    * Measuring student progress
        * Effort-based vs correctness?
        * Autograding correctness not an issue
* projects:
    * Teaching effectiveness:
        * not as much fill in the blank
        * giving students the autograder: good or bad?
            * Pros:
                * more convenient for students
                * not as much load on server-side grader (not a big
                  problem)
                    * grading software able to parallelize grading
                    * Imposing stricter timeout thresholds will reduce
                      this problem
            * Cons:
                * students blindly run tests without understanding
                  code
                * not as much experience conducting own tests
    * Measuring student progress
        * Effort-based vs correctness?
            * If measured for correctness, students might focus more on
              finishing than taking time to understand
            * We do want to emphasize some degree of correctness
              (models real world application)
        * Impact of autograder:
            * students have ability to (almost guarantee) perfect score
            * Defeats use as a measurement?
* discussions/labs:
    * Material preparation
        * When to determine lab/discussion material
            * Proposed policy:
                * determine material for each discussion/lab no more
                  than 1.5 week before it
            * Pros:
                * Offers tighter synchronization with lecture material
                  (very important)
            * Cons:
                * Less time to prepare material (not as much of an
                  issue as database of past material increases)
                * Less time to peer review before release
        * Must have peer review before release (perhaps get readers
          to do this?)
        * distribute topics evenly -- don't have some weeks with no
          material, and other weeks crammed
    * Teaching Effectiveness
        * Consider using iPython?
            * Pros:
                * more convenient for what would Python print and other
                  tasks that involve copy/paste
            * Cons:
                * less experience using command line
        * Requiring submission of labs:
            * Proposed policy:
                * Graded on effort
                * Enforced by submission through glookup
                * Grade can only help students -- if they score below
                  certain scores on midterms, lab submissions can
                  buffer grades
            * Pros:
                * Students required to go through exercises -> more
                  likely to learn concepts
                * If enforced through submission, takes load off of
                  TAs/lab assistants for check off
            * Cons:
                * More bookkeeping for grading
                * Grade inflation? (but allows for less sugar-coating
                  on exams)
* lectures:
    * Physical space:
        * video tape lectures before hand?
    * Teaching effectiveness:
        * use more diagrams/pictures, especially for data
          structures
        * how to make more engaging? Is it worth the effort?
* Midterms:
    * Measuring student progress
        * Need a way filter out noise
            * release a mock exam before first midterm to get students
              accustomed to exam style
        * Environment diagrams
            * Pros:
                * Offers a concrete way to observe student
                  understanding of program flow
                * Offers moer partial credit opportunities than what
                  would Python print questions
            * Cons:
                * Not all students understand programs in that way (not
                  a good metric)
                * Often prompts staff to concoct contrived questions
                  with no real life relevance
        * Code writing:
            * Pros:
                * Relevant metric for real life application
            * Cons:
                * Very time-consuming to grade (does not scale well in
                  general)
                * Sometimes hard to convey meaning of question to
                  students (inaccurate metric)
                * If penalizing for language details, can be inaccurate
                  metric (doesn't test understanding)
        * Debugging questions?
            * Pros:
                * Relevant metric for real life application
            * Cons:
                * Not in line with primary goals of class (teaching
                  concepts, not software engineering)
                * No current method of writing such questions
                  (investigate further)
        * Topic synthesis (i.e. a question testing more than one topic)
            * Proposed policy:
                * topics tested in synthesis question must also be
                  individually tested
            * Pros:
                * Able to reward for understanding of individual topics
                * Able to test synthesis skills (important)
            * Cons:
                * If synthesis done in a contrived way, then not very
                  accurate measure of understanding
                * Requires more questions to be written (more work for
                  staff)
        * Grading rubrics
            * improve format of env diagram grading?
* Student distribution
    * lagging students:
        * how to deal with students who are falling behind?
    * overqualified students:
        * how to keep them interested?

* Lab 2:
    1. Debugging questions
    2. Style questions

