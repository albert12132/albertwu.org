import re
import argparse

temp_tag = '(?<=\{\{\s).+?(?=\s\}\})'
tag_pattern = lambda tag: '\{\{ ' + tag + ' \}\}'

def compile(template, tag_names, dest):
    tags = set(re.findall(temp_tag, template))
    for tag in tags:
        if tag not in tag_names:
            print('Cannot find tag ' + tag)
            exit(1)
        template = re.sub(tag_pattern(tag), tag_names[tag], template)
    with open(dest, 'w') as f:
        f.write(template)
        print('Finished compiliing ')
        print('Result can be found at ' +  dest)

def parse_template(template):
    with open(template, 'r') as f:
        template = f.read()
    return template

def parse_content(content):
    if content.endswith('.py'):
        content = content[:-3]
    content = content.replace('/', '.')
    a = {}
    exec('from ' + content + ' import tag_names', a)
    return a['tag_names']

def parse_dest(dest, content):
    content = content[:-3] if content.endswith('.py') else content
    return dest + '/' + content + '.html'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('template', help='The filepath of the template')
    parser.add_argument('content', help='The filepath of the content. Content should be a python file.')
    parser.add_argument('dest', help='The destination directory.')
    args = parser.parse_args()
    template = parse_template(args.template)
    tag_names = parse_content(args.content)
    dest = parse_dest(args.dest, args.content)
    compile(template, tag_names, dest)
