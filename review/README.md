Midterm 1 Review
================

This directory holds the review app. Content is written here,
and automatically generated into static html files.

Topics
------
* Midterm 1
    * Environment Diagrams (environments)
    * Control Structures (control)
    * Higher-Order Functions (hof)
    * Lambda Expressions (lambda)
* Midterm 2
    * Tuples (tuples)
    * Lists (lists)
    * Recursive Lists (rlists)
    * Map, Filter, and friends (functions)
    * Dictionaries (dictionaries)
    * Identity (identity)
    * Nonlocal (nonlocal)
    * OOP (oop)

_Note_: each topic is listed with its official name (displayed on the
site) and its internal name (used by the compiler).

Directory Structure
-------------------
* Base Path
    * `compile.py`
    * `index.html`
    * `Makefile`
    * `template`
        * `__init__.py`
        * `question.py`
        * `utils.py`
        * `question.html`
        * `solution.html`
        * `style.css`
    * `utils`
        * `__init__.py`
        * `utils.py`

Overview
--------
The compiler consists of parts:

* `compile.py`: script that compiles content with html templates.
    * Usage:
        python3 compile.py [template_path] [content_path] [destination_path]
    * In general, you will not be explicitly running `compile.py`. The `Makefile` handles that instead.

* `Makefile`: main interface for users of the app.
    * Configuration: these variables can be changed in the `Makefile`
        * `MT1_TOPICS`, `MT2_TOPICS`, and `FINAL_TOPICS`: a list of topics
        * `BASE_PATH`: filepath of the destination directory
        * `TEMPLATE_DIR`: filepath of the template directory
    * Command line options
        * `make (exam)`: compiles all existing content for that exam
        * `make (exam)-%`: compiles the specified topic for that exam
        * `make $(TOPICS)`: initializes an app directory for the
        specified topic. The variable `TOPICS` must contain the topic.
        * `make clean-(exam)`: Removes the compiled version of the
        exam directory

Content
-------
Initializing a topic will yield the given directory structure

* Topic
    * `__init__.py`
    * basic
        * `__init__.py`
        * `question.py`
    * exam
        * `__init__.py`
        * `question.py`

The `__init__.py` files are necessary for Python's package system.
Questions and solutions will be written in `question.py`.

Several utility functions have been provided for HTML tags. These can
be found in `utils/utils` and `template/utils`.

Customizing Templates
---------------------
HTML templates are written just like normal HTML. For customizable
content, you can add a set of double curly braces like so:

    {{ # python expression here }}

You can put any Python3 expression in between the curly braces, but it
must be an expression; statements like `def`, `for`, etc. will not
work. Furthermore, you can use the utilities in `utils/utils` and
`template/utils`.
