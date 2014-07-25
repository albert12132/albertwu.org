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

<render>
    <p>This is paragraph 1. It contains content
    that pertains to the first paragraph.</p>
    
    <p>This is paragraph 2. Notice the blank line
    above the start of this paragraph.</p>
</render>

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

### Blockquotes

Blockquotes are preceded with `> `. Blockquotes may contain lists, headers, paragraphs, code blocks, and nested blockquotes:

<markdown>
    > ### Beginning of a blockquote
    > This is an example of a block quote
    > 
    >     Here is a codeblock
</markdown>

<render>
    <blockquote><h3 id="beginning-of-a-blockquote">Beginning of a blockquote</h3>
    
    <p>This is an example of a block quote</p>
    
    <pre><code>Here is a codeblock</code></pre></blockquote>
</render>

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

#### Nested paragraphs inside lists

If a list item contains multiple paragraphs, each paragraph after the first one must be indented at least **two** spaces.
This differs from original Markdown syntax, which requires 4 spaces.

<markdown>
    * This is a list item.
      The list item will have two
      paragraphs.
      
      This is the second paragraph
      in the list item.
    * This is the second list item.
</markdown>

<render>
    <ol>
      <li><p>This is a list item.
      The list item will have two
      paragraphs.</p>
      
      <p>This is the second paragraph
      in the list item.</p></li>
      <li>This is the second list item.</li>
    </ol>
</render>

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

#### Nested code blocks in lists

To include a code block inside of a list, the code block requires **four leading spaces for every list level**.
For example:

<markdown>
    * List item
    
            Code block with 8 trailing spaces:
            4 spaces for 1 list level
            + 4 spaces for code block
            
      End list item
        * Nested list item
                
                Code block with 12 trailing spaces:
                8 spaces for 2 list levels
                + 4 spaces for code block
</markdown>

<render>
    <ol>
      <li><p>List item</p>
      
      <pre><code>Code block with 8 trailing spaces:
      4 spaces for 1 list level
      + 4 spaces for code block</code></pre>
      
      <p>End list item</p>
      
      <ul>
        <li><p>Nested list item</p>
        
        <pre><code>Code block with 12 trailing spaces:
        8 spaces for 2 list levels
        + 4 spaces for code block</code></pre></li>
      </ul></li>
    </ol>
</render>

#### Nested blockquotes in lists

As with code blocks, blockquotes nested in lists also require **four leading spaces per list level**:

<markdown>
    * List item
    
        > Block quote
        > with 4 leading spaces
        
      End list item
        * Nested list item
        
            > Block quote
            > with 8 leading spaces
</markdown>

<render>
    <ol>
      <li><p>List item</p>
      
      <blockquote>Block quote
      with 4 leading spaces</blockquote>
      
      <p>End list item</p>
      
      <ul>
        <li><p>Nested list item</p>
        
        <blockquote>Block quote
        with 8 leading spaces</blockquote></li>
      </ul>
    </ol>
</render>

### Tables

Extended Markdown provides syntax for tables -- this has been implemented by Templar:

<markdown>
    Header 1 | Header 2 | Header 3
    :-------:|---------:|:--------
    center   | right    | left
</markdown>

<render>
    <table>
      <tr>
        <th>Header 1</th>
        <th>Header 2</th>
        <th>Header 3</th>
      </tr>
      <tr>
        <td align="center">center</td>
        <td align="right">right</td>
        <td align="left">left</td>
      </tr>
    </table>
</render>

The colons control which alignment to use for each column:

* Two colons, one on each side, converts to center alignment
* One colon on the right converts to right alignment
* One colon on the left converts to left alignment

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

