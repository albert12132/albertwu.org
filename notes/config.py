import re
from utils.html import HeaderParser

style_guide_re = re.compile(r"<([NP])>")
def style_guide_sub(match):
    style = match.group(1)
    if style == 'N':
        return '<span class="non-ess">N</span>'
    elif style == 'P':
        return '<span class="python">P</span>'

style_guide_code_re = re.compile(r"""
<(good|bad)>\s*     # \1 is good/bad
<pre><code>
(.*?)                # \2 is codeblock content
</code></pre>\s*
</\1>
""", re.S | re.X)
def style_guide_code_sub(match):
    return '<pre><code class="style-{}">{}</code></pre>'.format(
            match.group(1), match.group(2))

SUBSTITUTIONS = [
    (style_guide_re, style_guide_sub),
    (style_guide_code_re, style_guide_code_sub),
]

VARIABLES = {
}

TOC_BUILDER = HeaderParser
