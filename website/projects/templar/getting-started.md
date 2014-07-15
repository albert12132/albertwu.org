~ title: Getting Started

Installing Templar
------------------

The latest version of Templar can be installed through `pip`:

    pip install templar

**Note**: Templar is currently supported only for Python3.3 and above.

You should now have access to two command-line utilities:

* `templar`: the primary command for Templar. We'll go over the various
  options throughout this document.
* `markdown`: a convenience command that is equivalent to `templar
  markdown`.

config.py
---------

Choose a directory in which you will be publishing work using Templar
(this can be any directory in your project structure). For example,
suppose we want to publish in a directory called `<project>/blog/`.

Create a `config.py` file with the following command:

    cd <project>/blog
    templar config

> Alternatively, you can create `config.py` without changing
> directories with
> 
>     templar config <project>/blog

This will create a file called `config.py` in `<project>/blog/`
with the following (paraphrased) contents:

    FILEPATH = ...  # filepath of config.py

    configurations = {
        'TEMPLATE_DIRS': [
            FILEPATH,
            # list of directories that contain a templates directory
        ]

        'VARIABLES': {
            # variables used by templates
        }

        'SUBSTITUTIONS': [
            # (regex, sub) pairs
        ]
    }

This basic setup is enough to start using Templar, but you can
customize each of the variables found in `config.py`. `TEMPLATE_DIRS`
is explained next; other customizations are described later.

### `TEMPLATE_DIRS`

Suppose we change `TEMPLATE_DIRS` to the following:

    'TEMPLATE_DIRS': [
        FILEPATH,
        os.path.join(FILEPATH, 'food'),
    ]

Continuing from our previous example, `FILEPATH` is
`<project>/blog` (since that is where `config.py` is located).
Templar will now look in two directories to find templates:

1. `<project>/blog/templates/`
2. `<project>/blog/food/templates/`

Templates will be searched in that order.

Notice that each filepath in `TEMPLATE_DIRS` is assumed to have a
`templates` directory -- this is where template files should be placed.

**Note**: The `FILEPATH` variable is not required, though it is
helpful as a reference point for other directories that contain
templates.

Basic Templating
----------------

Continuing from our example above, suppose we are publishing content
from the filepath `<project>/blog/`.

First, create a content file anywhere -- for example, we'll create a
Markdown file called `pumpkin-pie.md`:

    ~ title: Pumpkin Pie

    This is a recipe for making **pumpkin pie**.

This file contains standard Markdown, except for the first line `~
title: ...`. This is a *variable* declaration, which has the
following syntax:

    ~ variable name: variable value

Variables can be referenced from within templates (explained later) and
are useful for storing metadata about the content. Some things to note:

* `variable name` can contain any character that is not a newline and
  not a colon (`:`). This means variables can include spaces, hyphens,
  and underscores.
* `variable value` can contain any character that is not a newline.
  This means values can include spaces, hyphens, underscores, and
  colons (the first colon in the line is used as the separator)
* `variable value` will be taken *as is* (meaning it will not be parsed
  for Markdown)
* The variable declaration must be on exactly one line

Once we are done with the content file, let's create a directory called
`templates`:

    mkdir templates

Add a sample template file called `recipe.html` to the `templates`
directory:

    <html>
      <head>
        <title>\{\{ title }}</title>
      </head>
      <body>
        <h1>\{\{ title }}</title>
        <p>Published: <i>\{\{ datetime.now() }}</i></p>

        \{\{ :all }}
      </body>
    </html>

This template demonstrates three fundamental features:

* **Variables** (`\{\{ title }}`): variables can be defined in either
  the content file (as seen above in `example.md`) or in `config.py`
  (explained later). Variables can be reused (e.g. multiple references
  to `title`).
* **Python expressions** (`\{\{ datetime.now() }}`): any valid Python
  *expression* can be used -- the `str` of the final value will be used
  in place of the `\{\{ ... }}`. For example, `datetime.now()` will
  evaluate to the current time (`datetime` is imported automatically by
  Templar)

* **Blocks** (`\{\{ :all }}`): a **block** is a section of the content
  file (see the section on Blocks below). All block expressions in
  templates start with a colon (`:`).

  Templar reserves the special block name `:all` to mean the entire
  content file. In this case, we are replacing `\{\{ :all }}` with all
  of the contents of our file.

To publish the content, use the following command:

    templar compile recipe.html -s pumpkin-pie.md -m -d result.html

* `compile` tells Templar to compile a template
* `template.html` is the template that we are using
* `-s pumpkin-pie.md` specifies the source content. This flag is
  optional (Templar allows templating without use of a source file;
  this is useful if you still want to take advantage of Templar's
  template inheritance)
* `-m` tells Templar to convert the contents of `pumpkin-pie.md` from
  Markdown into HTML before templating occurs
* `-d result.html` tells Templar to write the result to a file called
  `result.html`. This option is optional -- if omitted, Templar will
  print the result of templating to standard out.

That's it! There should now be a file in `<project>/blog/` called
`result.html` that contains the following:

    <html>
      <head>
        <title>Pumpkin Pie</title>
      </head>
      <body>
        <h1>Pumpkin Pie</title>
        <p>Published: <i>2014-06-08</i></p>

        <p>This is a recipe for making <strong>pumpkin pie</strong>.</p>
      </body>
    </html>

Notice that all `\{\{ ... }}` expressions have been replaced
accordingly (the `\{\{ datetime.now() }}` expression will be different
depending on when you publish.

Our final directory structure looks like this:

    <project>/
        blog/
            templates/
                recipe.html
            config.py
            pumpkin-pie.md
            result.html
