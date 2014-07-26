~ title: Source Files

Filetypes
---------

### Markdown

A basic Templar source file can simply contain regular Markdown.
See the [Templar Markdown rules](markdown.html) for a full
specification of Templar's version of Markdown.

Templar's Markdown parser supports *metadata* definitions:

    ~ variable name: variable value

That is, a tilde (`~`) followed by at least one space, a variable name,
a colon, and a variable value. Metadata declarations have the following
rules:

* `variable name` can contain any character that is not a newline and
  not a colon (`:`). This means variables can include spaces, hyphens,
  and underscores.
* `variable value` can contain any character that is not a newline.
  This means values can include spaces, hyphens, underscores, and
  colons (the first colon in the line is used as the separator)
* `variable value` will be taken *as is* (meaning it will not be parsed
  for Markdown)
* The variable declaration must be on one line

You can tell Templar to parse a content file as Markdown with use of
the `-m` flag:

    templar compile template.html -s example.md -m
    templar link example.md -m

### Other filetypes

Templar can also use non-Markdown files as content sources. For
example, we have a template called `homework.py` with the following:

<pre>
<code>
"""Python homework"""

{&#123; :all }}

if __name__ == '__main__':
    main()
</code></pre>

and a source file called `hw1.py` with the following:

    def question1(args):
        pass

    def question2(args):
        pass

Then the following command would publish a file called `pub/hw1.py`

    python3 templar compile homework.py -s hw1.py -d pub/hw1.py

Notice we omit the use of `-m`, since we are not publishing Markdown.
The contents of `pub/hw1.py` will look like the following:

    """Python homework"""

    def question1(args):
        pass

    def question2(args):
        pass

    if __name__ == '__main__':
        main()

Special tags
------------

There are also two special tags that can be used: the `<block>` tag and
the `<include>` tag. These tags can be used in any kind of source file
(Markdown or not).

### `block` tag

The `<block>` tag allows you to name a certain section of Markdown:

    Some Markdown out here

    <block example>
    Example
    -------
    This Markdown is within the block.
    </block example>

The opening `block` tag consists of triangular braces, `< >`, the word
`block`, followed by a space, and then the name of the block. In the
example above, the name of the block is `example`.

The closing `block` tag uses a forward slash and also needs to contain
the name of the block that it closes. This allows you to nest blocks
inside of each other:

    <block outer>

    <block inner>
    This stuff here would be included in both the inner block and the
    outer block
    </block inner>

    But this stuff would only be included in the outer block.
    </block outer>

Block names must be unique within a single file.

The `<block>` tag can also be surronded by extra characters on the same
line:

    # <block python>
    def hello(world):
        return hi
    # </block python>

This allows blocks to be defined in source code (e.g. Python scripts)
as comments, so that the source code can be executed.

### `include` tag

The `<include>` tag allows you to link different sources
together. The idea is that sometimes, it is useful to write modular
Markdown sources to make it easier to manage directories. This also
makes it faster to refer to the same Markdown file without duplicating
its contents. Here is an example:

<pre>
<code>
Topics
------
&lt;include path/to/topics.md&gt;

Examples
--------
&lt;include path/to/example.py&gt;

References
----------
&lt;include path/to/references:blockA&gt;
</code>
</pre>

In the example above, the first and second `include` tags simply use a
filepath. As in the example, any filetype can be included, irrespective
of the original source filetype (e.g. a Python file can be included in
a Markdown file), as long as the files are plain text.

The filepaths can be written in the following ways
* *relative to the directory in which you will run Templar*: this is
  always assumed by Templar first
* *relative to the current source file*: this is useful if the source
  file is close to other files that it is linking. Templar will assume
  the filepath is relative to the source file only if it cannot find
  the filepath relative to the working directory.

The first two `include` tags will simply copy all of the contents
listed inside of `path/to/topics.md` and `path/to/example.py` into the
locations of the `include` tags.

The third `include` tag also references a `blockA` inside of the file
`path/to/references.md`. This is useful if you only want to include a
subsection of another Markdown file. The syntax is the following:

<pre>
<code>
&lt;include path/to/file:block-name&gt;
</code>
</pre>

#### Regular expressions

The block name in an `include` tag can also be a regular expression:

<pre>
<code>
&lt;include path/to/file:block\d+&gt;
</code>
</pre>

Here, the regular expression will be `block\d+`. All blocks in
`path/to/file` whose names match the regular expression will be
included in place of the `include` tag. The blocks will be included in
the order they are defined in `path/to/file` (using their opening
`block` tag to define order).

Suppose the regular expression matches `block42`, `block2`, `block3`,
in that order. The `include` tag will be expanded into the following:

<pre>
<code>&lt;include path/to/file:block42&gt;
&lt;include path/to/file:block2&gt;
&lt;include path/to/file:block3&gt;</code>
</pre>

