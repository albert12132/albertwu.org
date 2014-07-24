~ title: Markdown

Templar uses a specially-built parser to process Markdown. In addition to the [original Markdown specification](http://daringfireball.net/projects/markdown/syntax), Templar also includes a subset of [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/) features. This article documents all of hte Markdown rules used by Templar.

## Block-level elements

### Paragraphs

A paragraph is just a block of text. Multiple paragraphs are separated by at least one blank line:

<markdown>
    This is paragraph 1. It contains content
    that pertains to the first paragraph.
    
    This is paragraph 2. Notice the blank line
    above the start of this paragraph.
</markdown>

<rendered>
    <p>This is paragraph 1. It contains content
    that pertains to the first paragraph.</p>
    
    <p>This is paragraph 2. Notice the blank line
    above the start of this paragraph.</p>
</rendered>

To force line breaks (`<br/>`) instead of a new paragraph, add two spaces at the end of the last line.
**In the example below, the `~~` represents two spaces**:

<markdown>
    This paragraph will
    contain a line break~~
    
    This is still part of the
    same paragraph
</markdown>

<render>
    <p>This paragraph will
    contain a line break<br/>
    
    This is still part of the
    the same paragraph</p>
</render>

### Code blocks

Code blocks are denoted by adding at least four spaces to the front of each line in the code block:

<markdown>
    This text is just in a normal paragraph
    
        def hello(world):
            return world > 2
            
        print(hello(3))
            
    Back to normal paragraphs
</markdown>

<render>
    <p>This text is just in a normal paragraph</p>
    
    <pre><code>def hello(world):
        return world &gt; 2
        
    print(hello(3))</code></pre>
        
    <p>Back to normal paragraphs</p>
</render>

Notice that whitespace that occurs after the four leading spaces is preserved. In addition, the characters
`>`, `<`, and `&` are escaped to HTML entities; this makes it more conveninet to write code blocks.

### Lists

#### Unordered lists

Un-ordered lists look like the following:

<markdown>
    * List item 1
    * List item 2
    * List item 3
</markdown>

<render>
    <ul>
      <li>List item 1</li>
      <li>List item 2</li>
      <li>List item 3</li>
    </ul>
</render>

The "bullets" can be any of the following characters: `*`, `+`, `-`. These characters can be used interchangeably in
a single list.

#### Ordered Lists

Ordered lists look like the following:

<markdown>
    1. List item 1
    2. List item 2
    3. List item 3
</markdown>

<render>
    <ol>
      <li>List item 1</li>
      <li>List item 2</li>
      <li>List item 3</li>
    </ol>
</render>

The numbering of the lists does not matter. As long as list items are of the format `\d+\.`, they will be considered
as the next list item.

#### Nested lists inside lists

Lists can be nested inside of other lists by adding four leading spaces *for every level of nesting*. The type of list (unordered or ordered) does not have to be the same as
the outer list:

<markdown>
    1. Ordered list item 1
        * Unordered list item 1
        * Unordered list item 2
            * Inner unordered list item 1
        * Unordered list item 3
    2. Ordered list item 2
</markdown>

<render>
    <ol>
      <li><p>Ordered list item 1</p>
      
      <ul>
        <li>Unordered list item 1</li>
        <li><p>Unordered list item 2</p>
        
        <ul>
          <li>Inner unordered list item 1<li>
        </ul></li>
        <li>Unordered list item 3</li>
      </ul></li>
      <li>Ordered list item 2</li>
    </ol>
</render>

Whitespace
----------

### Tabs and Whitespace

All tabs are converted into at most 4 spaces. All trailing whitespace (`\s+$`) is removed.

Comments
--------

Templar's Markdown processor supports Pandoc-style comments:

    <!--- Use three leading hyphens to create a
    Pandoc comment. These comments are removed
    from the final document -->
    

    
### Header slugs

Templar's Markdown parser adds slugs to headers (`<h[1-6]>`). These
slugs are added as `id` attributes of the headers.

