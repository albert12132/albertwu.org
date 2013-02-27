import re
import argparse

temp_tag = '(?<=\{\{\s).+?(?=\s\}\})'
tag_pattern = lambda tag: '\{\{ ' + tag + ' \}\}'

def compile(template, attrs, dest):
    for tag in re.findall(temp_tag, template):
        val = eval(tag, attrs)
        template = re.sub('\{\{\s.+?\s\}\}', str(val), template, count=1)
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
    content = content.split('/')
    content = '.'.join(content)
    thing= __import__(content, fromlist=['attrs'])
    print(thing)
    return thing.attrs

def parse_dest(dest, content, template):
    content = '/'.join(content.split('/')[:-1]) +'/'+ template.split('/')[-1]
    return dest + '/' + content

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('template', help='The filepath of the template')
    parser.add_argument('content', help='The filepath of the content. Content should be a python file.')
    parser.add_argument('dest', help='The destination directory.')
    args = parser.parse_args()
    template = parse_template(args.template)
    tag_names = parse_content(args.content)
    dest = parse_dest(args.dest, args.content, args.template)
    compile(template, tag_names, dest)
