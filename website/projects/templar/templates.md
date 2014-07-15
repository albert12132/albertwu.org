~ title: Templates

Introduction
------------

Templates are stored in a directory called `templates`, which can be
located anywhere as long as the parent directory is listed in the
`TEMPLATE_DIRS` variable in `config.py`. The most basic "template" is
simply a regular HTML file.

In addition, you can add *expressions* in the templates that the
compiler will resolve. For example, the following template can be used
to fill in contact information:

    <ul>
      <li>Name: {{ name }}</li>
      <li>Age: {{ age }}</li>
      <li>Occupation: {{ job }}</li>
    </ul>

Expressions are denoted by two sets of curly braces, such as `{{ name
}}` or `{{ age }}`. The expression within the curly braces can be one
of the following:

* A **variable** defined either within a Markdown source file or
  `config.py`. These "variable" names are more flexible than Python
  variable names, as they can include spaces and hyphens (the only
  restriction is they cannot contain newlines or colons).
* A **Python expression**. Any valid Python *expression* (not
  statements) can be used -- the `str` of the final value will be used
  in place of the `{{ ... }}`:

        <p>Date published: {{ datetime.now() }}</p>

  **Note**: `{{ ... }}` expressions will always be treated as variables
  first; if no such variable exists, before Templar will evaluate the
  expression as a Python expression instead.
* A block defined within a Markdown source file. For example, suppose a
  source file has the following block:

        <block example>
        Some Markdown here.
        </block example>

  The block `example` can then be used in an expression like so:

        <body>
          <p>Some HTML here</p>

          {{ :example }}

  Notice the colon that precedes the block name.

### Template Inheritance

Templar also supports template inheritance. A "child" template can
specify which "parent" template to inherit by including the following
on the *very first line of the child template*:

    <% extends parent.html %>

In the "parent" template, you can define labels that "child" templates
can fill. Suppose the following content is found in `parent.html`:

    <div id='nav-bar'>
      <h3>Title</h3>

      {% block nav-bar %}
    </div>

The `{% block nav-bar %}` tag allows child templates to "override"
parent labels. Suppose the following content is found in `child.html`:

    <% extends parent.html %>

    <% block nav-bar %>
    <h3>Some other stuff</h3>
    <h3>Some more stuff</h3>
    <% block nav-bar %>

The result of compiling `child.html` will look like this:

    <div id='nav-bar'>
      <h3>Title</h3>

      <h3>Some other stuff</h3>
      <h3>Some more stuff</h3>
    </div>

If a child template chooses not to inherit a tag, that tag will simply
be removed from the final document.
