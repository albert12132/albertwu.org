import re

style_guide_re = re.compile(r"<([NP])>")
def style_guide_sub(match):
    style = match.group(1)
    if style == 'N':
        return '<span class="non-ess">N</span>'
    elif style == 'P':
        return '<span class="python">P</span>'

def toc(lst):
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

regexes = [
    (style_guide_re, style_guide_sub),
]

configs = {
}
