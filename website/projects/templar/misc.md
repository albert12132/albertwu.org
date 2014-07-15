~ title: Other Features

### Linking

Templar's primary publishing method is to use templates via the
`compile` subcommand. However, if you do not need to use a template,
and simply want to link a source content file (through use of `include`
tags), you can use the `link` subcommand:

    python3 templar link example.md -m -d result.html

* `example.md` is the source file to link. This is a required argument
* `-m` tells Templar to parse the content as Markdown. You can omit
  this flag to skip Markdown parsing
* `-d result.html` tells Templar to write the result to a file called
  `result.html`. If this argument is omitted, Templar will print the
  result to standard out.

### Table of Contents

Templar has the capability to scrape headers to create a table of
contents. You can specify exactly *what* is defined to be a header in
`config.py`:

    header_regex = r"..."

    def header_translate(match):
        return ...

    def table_of_contents(lst):
        ...

* `header_regex` can either be a string or a `RegexObject`, and tell
Templar how to recognize a "header".
* `header_translate` takes a regular expression match and extracts
  information (e.g. the `id` attribute and title of an HTML `<h1>` tag)
* `table_of_contents` takes a list of expressions returned by
  `header_translate` and compiles the final table of contents.

The table of contents that is returned by `table_of_contents` is
available to templates with the expression

    `{{ table-of-contents }}`
