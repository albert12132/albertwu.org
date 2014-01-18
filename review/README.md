Exam Reviews
============

This directory holds the `review` app. Content is written here,
and automatically generated into static HTML files.

Makefile commands
-----------------
* `all`: publishes all index files, review files, and public assets
* `all-%`: publishes all files related to `%`, which is either `mt1`,
  `mt2`, or `final`
* `pub-assets`: publishes all public assets
* `index-%`: publishes the index file for `%`, which is either `mt1`,
  `mt2`, `final`, or `index` (which publishes the a "All topics" index)
* `pub-%`: publishes the specified topic
* `%`: creates a directory structure for the specified topic. The topic
  must have already been added to the `TOPICS` variable

Subdirectories
--------------
* `templates`: templates for compiler
* `public`: directory for public assets (don't need to be compiled)
* `utils`: Python utilities for content and compiler
* `indices`: Python files housing content for index.html's
* `contents`: Python files housing content for topics

Templates
---------
* review.html    (super-template)
* main.html      (used for each exam)
* question.html

Public Assets
-------------
* style.css
* toggle.js (for solution toggle buttons)

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

Customizing Templates
---------------------

See the README for the main page.
