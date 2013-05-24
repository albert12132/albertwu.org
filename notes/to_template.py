from utils.utils import table_to_html, insert_into_table, li, a
import sys
import re

title_tag = re.compile('~ (.*) ~')
header_tag = re.compile('<h(\d) id="(.*)">(.*)</h\d>')

title = []
table = []


def read():
    """Reads from file handle F an HTML document. The document is
    expected to be the result of converting from markdown, and so needs
    to be processed to fit the notes.html template."""
    lines = []
    for line in sys.stdin:
        check_title = title_tag.search(line)
        if check_title:
            title.append(check_title.group(1))
            continue
        check_header = header_tag.match(line)
        if check_header:
            level, html_id, name = check_header.group(1, 2, 3)
            level = int(level)
            insert_into_table(table, level, name, html_id)


        if '<li><p>' in line:
            line = line.replace('<li><p>', '<li>')
        if '</p></li>' in line:
            line = line.replace('</p></li>', '</li>')
        if '<pre><code>' in line:
            line = line.replace('<pre><code>', '<pre class="prettyprint">')
        if '</code></pre>' in line:
            line = line.replace('</code></pre>', '</pre>')
        lines.append(line)
    return lines

if __name__ == '__main__':
    print('<% extends base.html %>')

    lines = read()
    if title:
        print("""
<% title %>
{}
<%/ title %>""".format(title[0]))
    print('<% body %>')
    if title:
        print("""
<div id='header'>
  <div id ='logo'>
    <h1>{}</h1>
  </div>
</div>""".format(title[0]))
    print(table_to_html(table))
    print(''.join(lines))
    print('<%/ body %>')

