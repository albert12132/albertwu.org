import re

style_guide_re = re.compile(r"<([NP])>")
def style_guide_sub(match):
    style = match.group(1)
    if style == 'N':
        return '<span class="non-ess">N</span>'
    elif style == 'P':
        return '<span class="python">P</span>'

regexes = [
    (style_guide_re, style_guide_sub),
]

configs = {
}
