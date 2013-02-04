Midterm 1 Review
================

This directory holds the midterm 1 review app. Content is written here,
and automatically generated into static html files.

Topics
------
* Environment Diagrams (environments)
* Control Structures (control)
* Higher-Order Functions (hof)
* Lambda Expressions (lambda)
* Newton's Method (newton)

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
        * `solution.py`
        * `utils.py`
        * `question.html`
        * `solution.html`
        * `style.css`

Overview
--------
The compiler consists of parts:
* `compile.py`: script that compiles content with html templates.
    * Usage:
        python3 compile.py [template_path] [content_path] [destination_path]
    * In general, you will not be explicitly running `compile.py`.
    The `Makefile` handles that isntead.
* `Makefile`: main interface for users of the app.
    * *Configuration*: these variables can be changed in the `Makefile`
        * `TOPICS`: a list of topics
        * `BASE_PATH`: filepath of the destination directory
        * `TEMPLATE_DIR`: filepath of the template directory
    * *Command line options*
        * `make all`: compiles all existing content
        * `make main`: compiles `index.html` and `style.css`
        * `make $(TOPICS)`: initializes an app directory for the
        specified topic. The variable `TOPICS` must contain the topic.
        * `make reload-%`: Wipes the specified topic directory and
        re-initializes
        * `make compile-%`: Compiles the specified topic for the first
        time
        * `make recompile-%`: Recompiles the specified topic
        * `make clean-%`: Removes the compiled version of the topic
        * `make clean-all`: Removes the entire compiled app.

Content
-------
Initializing a topic will yield the given directory structure:
* Topic
    * `__init__.py`
    * basic
        * `__init__.py`
        * `question.py`
        * `solution.py`
    * exam
        * `__init__.py`
        * `question.py`
        * `solution.py`
The `__init__.py` files are necessary for Python's package system.
Questions will be written in `question.py` and Solutions will be
written in `solution.py`.

Customizing Templates
---------------------
More on this later.
