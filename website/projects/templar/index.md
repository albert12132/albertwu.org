~ title: Templar

Introduction
------------

Templar is a static templating engine primarily designed for Python
programmers with a focus on writing articles -- blog posts, classroom
materials, news articles, and more.

Templar strives to achieve two core principles:

* **Simplicity**: setting up a publishing framework should be quick and
  easy. Templar is designed to be lightweight -- all it takes to get
  started is a config file, a template, and a bit of Markdown.
* **Customizability**: the minimal amount of setup code also allows
  Templar to be flexible in terms of configuration. Content files can
  be located anywhere the user wants; any sort of text file can be
  published using templates; and configuration files take advantage of
  the power of Python so that users can define complex custom patterns.

[Get started with Templar](getting-started.html).

Some key features of Templar include:

* Templating
    * Template inheritance
    * Embedded Python
* Linking
    * Modularizing content
* Custom patterns
    * User-defined expansions of source files
    * Customizable table of contents
* Markdown
    * Standard Markdown syntax
    * Extended Markdown features

Templar is an open-source project that can be found on
[Github](https://github.com/albert12132/templar).

Found a bug? [File an
issue](https://github.com/albert12132/templar/issues?state=open) on
Github.

Acknowledgements
----------------

Templar is an extension of the program that used to generate my
personal website. The idea for linking (the `include` and `block` tags)
conceived while developing the publisher for UC Berkeley's CS 61A labs.

The Markdown parser is a re-implementation of
[markdown2](https://github.com/trentm/python-markdown2), a Python
implementation of the original Perl Markdown parser. The variant of
Markdown that Templar supports is a subset of [Daring Fireball's
Markdown
specification](http://daringfireball.net/projects/markdown/syntax).

Syntax for template inheritance and expression substitution are
inspired by [Django](https://www.djangoproject.com/)'s templating
syntax, as well as [ejs](http://embeddedjs.com/)'s templating syntax.
