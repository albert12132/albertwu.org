Exam Reviews
============

This directory holds the `review` app. Content is written here,
and automatically generated into static HTML files.

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

Makefile
-----------------
* Configuration: these variables can be changed in the `Makefile`
    * `MT1_TOPICS`, `MT2_TOPICS`, and `FINAL_TOPICS`: a list of topics
    * `BASE_PATH`: filepath of the destination base directory
    * `REVIEW_PATH`: filepath of the destination review directory
* Command line options
    * `make all-(exam)`: compiles all existing content for that exam
    * `make index-(exam)`: compiles main html file for that exam
    * `make pub-(topic)`: compiles the specified topic
    * `make (topic)`: initializes an app directory for the specified
      topic. The variable `TOPICS` must contain the topic.
    * `make destroy`: removes all published materials for the review
      app

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

If a topic uses assets (e.g. `png` files), you can create an `assets`
directory in its directory. For example, if Recursion: basics uses a
picture called `example.png`, you would create a directory calld
`recursion/basic/assets` with `example.png` inside.

Several utility functions have been provided for HTML tags. You can
import these with the following

    from utils import utils             # top level utilities
    from review.utils.utils import *    # review app utitilies


Customizing Templates
---------------------

See the README for the main page.
