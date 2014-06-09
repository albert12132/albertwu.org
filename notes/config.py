import re

style_guide_re = re.compile(r"<([NP])>")
def style_guide_sub(match):
    style = match.group(1)
    if style == 'N':
        return '<span class="non-ess">N</span>'
    elif style == 'P':
        return '<span class="python">P</span>'

header_regex = re.compile(r"""
    <\s*
    h([1-6])        # \1 is the header level
    (?:
        .*?         # attributes
        id=(['"])   # \2 is the quote
        (.*?)       # \3 is the actual id
        \2          # closing quote
        .*?         # attributes
    )?>
    (.*?)           # \4 is the header title
    <\s*/\s*
    h\1             # closing header tag
    \s*>
""", re.X)
def header_translate(match):
    return match.group(1), match.group(3), match.group(4)
def table_of_contents(lst):
    if not lst:
        return ''
    cur = 0
    text = ''
    for level, tag, title in lst:
        level = int(level)
        if level > cur:
            text += '<ul>\n'
        elif level < cur:
            text += '</ul>\n'
        text += '<li><a href="#{0}">{1}</a></li>\n'.format(tag, title)
        if level != cur:
            cur = level
    if cur != lst[0][0]:
        text += '</ul>\n'
    text += '</ul>\n'
    return text

SUBSTITUTIONS = [
    (style_guide_re, style_guide_sub),
]

VARIABLES = {
}
