from utils.utils import table_to_html, insert_into_table
import sys
import re

header_tag = re.compile('<h(\d) id="(.*)">(.*)</h\d>')
attr_tag = re.compile('~ (.*):(.*) ~')


def read(f=sys.stdin):
    """Reads from file handle F (default STDIN). The input is expected
    to be the result of converting from markdown, and so needs to be
    processed to fit the notes.html template."""
    lines, table = [], []
    contents = { 'lines': lines, 'table': table }

    for line in f:
        check_attr = attr_tag.search(line)
        if check_attr:
            key, value = check_attr.group(1, 2)
            contents[key.strip().lower()] = value.strip()
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
            line = line.replace('<pre><code>',
                                '<pre class="prettyprint">')
        if '</code></pre>' in line:
            line = line.replace('</code></pre>', '</pre>')
        lines.append(line)
    return contents

def get_template(contents):
    extends_tag = '<% extends {} %>'
    base = contents.get('template', 'base.html')
    return extends_tag.format(base)

def render_title(title=None):
    contents = """
<% title %>
{0}
<%/ title %>

<% body %>

<div id='header'>
  <div id ='logo'>
    <h1>{0}</h1>
  </div>
</div>"""
    if title:
        return contents.format(title)
    else:
        return '<% body %>'

if __name__ == '__main__':

    try:
        if len(sys.argv) >= 2:
            f = open(sys.argv[1], 'r')
        else:
            f = sys.stdin
        contents = read(f)
        f.close()
    except IOError as e:
        print('I/O error while reading {}'.format(sys.argv[1]),
              file=sys.stderr)
        print(e, file=sys.stderr)
        f.close()
        exit(1)

    print(get_template(contents))

    if 'style' in contents:
        print("""
<% styles %>
<link rel='stylesheet' type='text/css' href='{{ NOTES_DIR }}/public/""" + contents['style'] + """'>
<%/ styles %>""")

    title = contents.get('title')
    print(render_title(title))

    if contents['table']:
        print(table_to_html(contents['table']))

    print(''.join(contents['lines']))
    print('<%/ body %>')

