~ title: Substitutions

Custom Patterns
--------------------

You can define custom patterns (also known as **substitutions**) in
your source files, like the following:

    Question 1
    ----------

    A question here.

    <solution>

    This is the solution to the question: `f = lambda x: f(x)`.

    </solution>

You can specify how to convert the `<solution>...</solution>` pattern
by defining a regular expression in `config.py`. For example,

    solution_re = re.compile(r"<solution>(.*?)</solution>", re.S)
    def solution_sub(match):
        return "<b>Solution</b>: " + match.group(1)

    configurations = {
        'SUBSTITUTIONS': [
            (solution_re, solution_sub),
        ]
    }

would replace the `solution` tag with a boldface "Solution: " followed
by the contents within the solution tag. All regular expressions should
be listed inside of the `SUBSTITUTIONS` list (in `config.py`), along
with the corresponding substitution function.

**Important note**: the custom patterns are evaluated **after** all
linking (`include` tags) and all Markdown parsing has occurred. Thus,
in the example above, `solution_re` should expect the contents of the
solution tag to look like this:

    <p>this is the solution to the question: <code>f = lambda x:
    f(x)</code>.</p>
