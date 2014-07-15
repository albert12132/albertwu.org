~ title: Configuring Templar

### Multiple `config.py` files

It can be useful to have a hierarchical `config` structure if you have
multiple directories with content, each with their own publishing
configurations. For example, suppose we have the following directory
structure:

    <project>/
        lib/
            templar/
        articles/
            config.py
            blog/
                config.py
            projects/
                config.py

We have a directory for articles that contains some general
configurations (e.g. a table of contents scraper). In the `blog` and
`projects` directories, we have more specific config files (e.g.
substitutions for different types of articles).

If we run Templar from the `blog` directory

    templar compile ...

Templar will use the following method to search for configs:

* Find the lowest common ancestor of `<project>/articles/blog/` and
  `<project>/lib/templar/` (in this case, the ancestor is `<project>/`
* Starting from the ancestor (`<project>/`), Templar will traverse down
  to `<project>/articles/blog/`
* At each intermediate directory, Templar will scan for a `config.py`
  file. If one exists, it will accumulate the contents of that
  `config.py` with all the other configs it has seen before.
