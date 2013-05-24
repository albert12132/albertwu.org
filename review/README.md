Exam Reviews
============

This directory holds the `review` app. Content is written here,
and automatically generated into static HTML files.

Subdirectories
--------------
* `templates`: templates for compiler
* `public`: directory for public assets (don't need to be compiled)
* `utils`: Python utilities for content and compiler
* `index`: Python files housing content for index.html's
* `contents`: Python files housing content for topics

Templates
---------
* review.html    (super-template)
* main.html      (used for each exam)
* question.html
* solution.html

Public Assets
-------------
* style.css

Utilities
---------
* `utils/utils.py` (review problem specific utilites)

Index
-----
For each exam, create a Python file for it, e.g. `mt1.py`. Index files
use the `main.html` template.

Content
-------
Initializing a topic will yield the given directory structure

* `contents`
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

If a topic uses assets (e.g. `png` files), you can create an `assets`
directory in its directory. For example, if Recursion: basics uses a
picture called `example.png`, you would create a directory calld
`recursion/basic/assets` with `example.png` inside.

Several utility functions have been provided for HTML tags. You can
import these with the following

    from utils import utils             # top level utilities
    from review.utils.utils import *    # review app utitilies


Makefile
--------
* Configuration: these variables can be changed in the `Makefile`
    * `MT1_TOPICS`, `MT2_TOPICS`, and `FINAL_TOPICS`: a list of topics
    * `BASE_PATH`: filepath of the destination base directory
    * `REVIEW_PATH`: filepath of the destination review directory
* Command line options
    * `make all`: compiles all content for all exams
    * `make pub-assets`: publishes public assets
    * `make all-(exam)`: compiles all existing content for that exam
    * `make index-(exam)`: compiles main html file for that exam
    * `make pub-(topic)`: compiles the specified topic
    * `make (topic)`: initializes an app directory for the specified
      topic. The variable `TOPICS` must contain the topic.
    * `make destroy`: removes all published materials for the review
      app


Customizing Templates
---------------------

See the README for the main page.
