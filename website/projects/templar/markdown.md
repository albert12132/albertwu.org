~ title: Markdown

Templar uses a specially-built parser to process Markdown. In addition to the [original Markdown specification](http://daringfireball.net/projects/markdown/syntax), Templar also includes a subset of [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/) features. This article documents all of hte Markdown rules used by Templar.

Whitespace
----------

### Tabs

All tabs are converted into at most 4 spaces. Templar tries to do this in a "smart" way (using a technique borrowed from [markdown2](https://github.com/trentm/python-markdown2)). Each tab is converted into enough spaces so that the number of characters on the line up to the last space is a multiple of 4. This is done to better preserve formatting.

### Trailing whitespace

All trailing whitespace (`\s+$`) is removed.

Comments
--------

Templar's Markdown processor supports Pandoc-style comments:

    <!--- Use three leading hyphens to create a
    Pandoc comment. These comments are removed
    from the final document -->
    

    
### Header slugs

Templar's Markdown parser adds slugs to headers (`<h[1-6]>`). These
slugs are added as `id` attributes of the headers.

