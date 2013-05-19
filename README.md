61A TA
======

This is the repo for my TA materials for CS 61A, an introductory
CS course offered at UC Berkeley.

Main Directory Makefile Commands
================================

* `make pub-assets`: publishes public assets (like CSS and JS)
* `make pub-index`: publishes index.html
* `make app-%`: creates a directory structure for a new app
* `make destroy`: removes all published materials

Contents
========

* `index.py`: contents for index.html (used by compiler)
* `local_config.py`: local configurations for compiler. Not included
  in git.
* `Makefile`: user interface for compiler
* `public`: Directory for public assets (CSS, JS)
* `templates`: Directory for templates (usually HTML, but can be any
  plain text language) for compiler
* `utils`: utilities for compiler
* `.example_app`: a directory housing skeletons for new apps

Apps
====

* `review`: exam practice problems
* `notes`: miscellaneous notes

Compiler
========

I wrote the compiler (`compile.py`) specifically for this repo. The
compiler acts as a static templating engine that publishes plain text
files (usually HTML). Its templating language is inspired by
[Django](https://www.djangoproject.com/).

Dependencies
------------

* [Python3.2](http://www.python.org/download/releases/3.2.4/)
* [argparse module](http://docs.python.org/3.2/library/argparse.html)

Basic Usage
-----------

Usually you won't be running `compile.py` directly -- the `Makefile`s
are designed to provide a simpler interface. In the event that you
need to run `compile.py` (or want to write new `Makefile`s), you can
use the `-h` flag:

    $ python3 compile.py -h
    usage: compile.py [-h] template content dest

    positional arguments:
      template    The template's filename
      content     The content's filename. Content should be a Python
                  file
      dest        The destination directory

    optional arguments:
      -h, --help  show this help message and exit

* `template`: the name of the template, without a filepath (e.g. just
  `index.html`, not `templates/index.html`). Templates can be defined
  locally for apps, and should be housed in a local `templates`
  directory.
* `content`: a Python file containing content. Content is expressed as
  strings that are assigned to variables -- these variables will be
  directly substituted into the template to generate the result
* `dest`: filepath of the destination. Relative paths are okay, but
  to avoid unexpectated behavior it is recommended to use absolute
  paths.

Local Configuration
-------------------

`local_config.py` should be located in the home directory of the repo.
It specifies some settings for the compiler. It must contain the
following variables:

* `BASE_PATH`: the filepath of the repo directory
* `TEMPLATE_DIRS`: a list of directories containing `templates`
  directories (do not include `templates` in the actual filepath)
* `CONFIGS`: a dictionary of variables used by templates (usually for
  resource path configuration).

Here is an example:

    import os

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_DIRS = [
        BASE_PATH,
        os.path.join(BASE_PATH, 'review'),
        os.path.join(BASE_PATH,'notes'),
    ]
    CONFIGS = {
        'MASTER_DIR': '/',
        'REVIEW_DIR': '/review',
    }

`CONFIGS` is usually used for path configuration -- any apps you
create should be added to `CONFIGS` with their published paths (where
they will be published) as string.

For development, the '/' should be replaced with the absolute path to
the published materials. For production, '/' should remain, since the
server will handle URL routing relative to '/'.

Content
-------

Content files must be Python files, designed for
[Python3.2](http://www.python.org/download/releases/3.2.4/). Anything
can go in these files (subroutines, variables, etc.), but there
**must** be a variable called `attrs` that contains all the variables
you want to use when compiling. Standard procedure is to include this
line at the end:

    attrs = globals()

There are utilities provided in a directory called `utils`, so you can
import them with this line at the top

    from utils import utils

Templates
---------

Templates can be any type of plain-text file (usually but not limited
to HTML). They must be housed in a directory called `templates`. The
syntax for templates is based partially off of [Embedded
JS](http://embeddedjs.com/) and Django.

### Inheritance ###

The following line must be the **very first line** in the template:

    <% extends template_name %>

where `template_name` is any template from which you wish to inherit.
**Note the spaces**: there must be exactly one space in each of the
specified positions above, or else the parser will not work.

**Note**: there is no "multiple inhertiance" -- each template can only
inherit from one parent (the parent itself can inherit).

### Sub tags ###

To specify a block that a sub-template can inherit:

    {% tag_name %}

where `tag_name` is the name of the tag. Sub-templates will reference
the tag by that name. **Note the spaces**.


### Super tags ###

To poplate an inherited tag, you will need both an opening tag and a
closing tag:

    <% tag_name %>
    contents...
    </% tag_name %>

where `tag_name` is the name of the inherited tag, and `contents` is
anything. Note the spaces, as before. Also, **the open and close tags
must be on their own lines**. The following is invalid:

    <% tag_name %>contents</% tag_name %>

The parser will treat that literally, without marking it for
inheritance.

### Expression tags ###

You can execute Python expressions by using this tag:

    {{ expression }}

As always, note the spaces. `expression` can be any Python expression,
but it cannot be a Python statement. The tag will be replaced with the
`str` of the final expression.

How it works
------------

The compiler itself is implemented entirely in `compile.py`. It
follows a three step process

1. resolve template inheritance
2. evaluate expressions
3. write into destination
