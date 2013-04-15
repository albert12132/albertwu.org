Exam Reviews
================

This directory holds the review app. Content is written here,
and automatically generated into static html files.

Templates
---------
* main.html      (used for each exam)
* question.html
* solution.html

Public
------
* style.css

Utilities
---------
* `utils.py` (review problem specific utilites)

Makefile
--------
* Configuration: these variables can be changed in the `Makefile`
    * `MT1_TOPICS`, `MT2_TOPICS`, and `FINAL_TOPICS`: a list of topics
    * `BASE_PATH`: filepath of the destination base directory
    * `REVIEW_PATH`: filepath of the destination review directory
* Command line options
    * `make (exam)`: compiles all existing content for that exam
    * `make index-(exam)`: compiles all existing content for that exam
    * `make publish-(topic)`: compiles the specified topic
    * `make (topic)`: initializes an app directory for the
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

The template engine also supports template inheritance, by use of a
tags:

    <% extends base.html %>

To override an inherited block, do

    <% block_name %>
    content
    <%/ block_name %>
