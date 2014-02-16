from utils.utils import insert_into_table
import utils.utils as utils
import re
import os
from markdown2 import markdown
import argparse
import importlib

header_tag = re.compile('<h(\d) id="(.*)">(.*)</h\d>')
attr_tag = re.compile('~ (.*):(.*) ~')

def scan(html):
    table = []
    contents = { 'table': table }

    attrs = re.finditer(attr_tag, html)
    for attr in attrs:
        key, value = attr.group(1, 2)
        contents[key.strip().lower()] = value.strip()
    headers = re.finditer(header_tag, html)
    for header in headers:
        level, html_id, name = header.group(1, 2, 3)
        level = int(level)
        insert_into_table(table, level, name, html_id)
        if level == 2:
            insert_into_table(table, level+1, 'Intro', html_id)
    return contents

def format(html):
    html = re.sub(attr_tag, '', html)
    html = html.replace('<li><p>', '<li>')
    html = html.replace('</p></li>', '</li>')
    html = html.replace('<p></p>', '')
    html = html.replace('"""', '\\"\\"\\"')
    html = re.sub(r'<h(\d)',
                  lambda s: '<h{} class="anchor"'.format(s.group(1)),
                  html)
    return html

def compile_table(table):
    html = ''
    for header in table:
        if type(header) == list:
            html += '<div>' + compile_list(header) + '</div>'
        else:
            html += '<h3>{}</h3>'.format(header[0])
    return html

def compile_list(table):
    html = '<ul>'
    for item in table:
        if type(item) is list:
            html += compile_list(item)
        else:
            html += utils.li(utils.a(item[1], item[0]))
    return html + '</ul>'

compiled = """
title = '{title}'
table = \"\"\"{table}\"\"\"
html = \"\"\"{html}\"\"\"
style = '{style}'
attrs = globals()
"""

def preproc(src):
    filename = os.path.basename(src).replace('.md', '')
    if os.path.exists(os.path.join('preproc', filename + '.py')):
        preproc = importlib.import_module('preproc.' + filename).run
    else:
        preproc = lambda x: x
    with open(src, 'r') as f:
        return markdown(preproc(f.read()), extras=['header-ids'])

def compile(src, dst):
    html = preproc(src)
    attributes = scan(html)
    html = format(html)

    with open(dst, 'w') as f:
        title = attributes.get('title')
        table = ''
        if attributes['table']:
            table = compile_table(attributes['table'])
        style = ''
        if 'style' in attributes:
            style = attributes['style']
        result = compiled.format(title=title, table=table, html=html,
                                 style=style)
        f.write(result)

def main():
    parser = argparse.ArgumentParser(description='Compiler for notes')
    parser.add_argument('src',
        help='Filepath of Markdown file'
    )
    parser.add_argument('dst',
        help='Filepath of destination (HTML)'
    )
    args = parser.parse_args()
    compile(args.src, args.dst)

if __name__ == '__main__':
    main()
    exit(0)

