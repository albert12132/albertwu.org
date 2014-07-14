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
* Homeworks:
    * Teaching effectiveness:
        * code writing is good!
        * maybe not as much fill in the blank; students should
          build more (e.g. the scheme derivative hw, brackulator
          hw)
            * fill in the blank questions are good if there is a
              *specific* concept that it tests
    * Difficulty:
        * Consider making homeworks with fewer questions, but more
          code writing for each question
            * Pros:
                * (Arguably) same amount of work
                * Easier to detect plagiarism
                * Students would get experience writing functions from
                  scratch, as opposed to filling in blanks
            * Cons:
                * Might be too difficult for students
                * Covers fewer questions -> learn fewer concepts
    * Measuring student progress:
        * Effort-based vs correctness?
        * Consider 1 pt for effort, 1 pt for correctness
            * Pros:
                * Forces students to work harder on homeworks
                * Students are still (somewhat) rewarded for effort
            * Cons:
                * Might induce more cheating
                * Especially for summer courses, fast pace makes it
                  harder for students to write fully correct homeworks
        * Autograding correctness not an issue
    * Monitoring plagiarism:
        * Should start running Moss on homeworks
            * Requires homeworks to be more free-form for better
              detection
        * Penalty:
            * -2 for each copied homework?
            * -10 for each copied homework?
* Projects:
    * Teaching effectiveness:
        * Should not have as much fill in the blank
        * giving students the autograder: good or bad?
            * Pros:
                * more convenient for students
                * not as much load on server-side grader (not a big
                  problem)
                    * grading software able to parallelize grading
                    * Imposing stricter timeout thresholds will reduce
                      this problem
                * Unlocking mechanism (theoretically) forces students
                  to understand more of the program
            * Cons:
                * students blindly run tests without understanding
                  code (possibly mitigated by unlocking)
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
    * Monitoriing plagiarism:
        * Moss can detect blatant cheating, but has a harder time
          detecting cheating for code that is common across all
          students
            * Mostly because project solutions are usually 3 to 6 lines
              each function
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
* Labs:
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
        * Length: recently, students have had trouble finishing labs --
          too much material
            * This can be mitigated by distributing lecture material
              more evenly
    * Teaching debugging:
        * Labs are supposed to be opportunities for students to play
          around with actual code-writing -- debugging is a very
          important part of that
        * Debugging should be taught in the lab(s) leading up to the
          due date of the first project
        * When covering topics that have new tracebacks (e.g. OOP with
          `AttributErrors`), should have a short section on debugging
          that new error
* Discussions:
    * Teaching effectiveness:
        * Designed to focus more on problem solving techniques -- how
          to approach different types of questions
* Lectures:
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
* Grade distribution
    * Should design midterms with a target score/distribution in mind
        * Can then measure deviation in expected distribution and
          actual distribution
    * Adjusting distributions at the end:
        * Might be (psychologically) better for students to start with
          lower distribution and then bump up to target distribution,
          rather than starting with target distribution
            * Pros:
                * same final outcome, but students will be more
                  appreciative at the end
                * It is easier to adjust grades up rather than adjust
                  down
            * Cons:
                * Might dishearten students at the beginning
                    * But this could also be a good way of filtering
                      out students who are less enthusiastic about
                      learning computer science
    * lagging students:
        * how to deal with students who are falling behind?
    * overqualified students:
        * how to keep them interested?
* Readers:
    * Readers should be chosen after TAs. TAs should be allowed to pick
      one reader. This immediately makes readers more involved with the
      rest of the course staff, and so they are likely to be more
      productive
    * With recent course development, readers have become less tied to
      a single TA. While TAs should still be involved in choosing
      readers, students should be assigned uniformly at random to
      readers (proportional to their work-hours)
    * In addition to assigning composition scores, readers should hold
      "office hours" after each project to meet with the students
      they graded. They should discuss the reasoning behind scores, and
      give suggestions on how to improve it
    * Possibility, but hard to scale: have readers provide feedback
      on homework composition too? (students get more feedback)
        * Students can peer review, and receive points on a system
          similar to labs (only receive points if they need it in the
          class
* Piazza:
    * Having a Piazza curator (or rotational amongst TAs) would be nice
        * Someone who renames posts to have more informative names and
          marks duplicates
        * Wait 30 minutes before answer a question -- allow students
          the chance to answer each other's questions
            * Also don't make students dependent on Piazza -- they
              should learn to debug their own assignments
* Miscellaneous:
    * **Github workshop** after the 2nd project (3rd project is first
      project to split up work between partners)
    * **Website**: would like to make it easier to find material by
      topic
        * Have a way to sort by various fields (date, topic, resource
          type, etc.)

Schedule
========
* Lab 2:
    1. Debugging questions
    2. Style questions

