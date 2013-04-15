from local_config import *
import re
import argparse
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRS = [
    os.path.join(BASE_PATH, 'review'),
    os.path.join(BASE_PATH, 'notes'),
    BASE_PATH,
]
# the following should be configured in local_config.py
# MASTER_DIR = BASE_PATH # for development
# MASTER_DIR = '/' # for production


EXTEND_TAG = '(?<=<%\sextends\s).+?(?=\s%>)'

SUPER_TAG_OPEN = '(?<=<%\s).+?(?=\s%>)'
SUPER_TAG_CLOSE = '(?<=<%/\s).+?(?=\s%>)'

SUB_TAG = '(?<=\{%\s).+?(?=\s%\})'

EXPR_TAG = '(?<=\{\{\s).+?(?=\s\}\})'


def get_template(filename):
    """Returns the contents FILENAME.

    FILENAME is expected to be a relative path to a template file
    (usually an html template). GET_TEMPLATE will look through the
    list TEMPLATE_DIRS in order, and search in a directory called
    'templates' in each of them for FILENAME.

    NOTE: by default, the current directory '.' is searched after the
    app directories.

    If no such FILENAME is found, the program exits with status 1.
    """
    for path in TEMPLATE_DIRS:
        template = os.path.join(path, 'templates', filename)
        if os.path.exists(template):
            with open(template, 'r') as f:
                template = f.read()
            return template
    print(filename + ' could not be found in:')
    for path in TEMPLATE_DIRS:
        print(os.path.join(path, 'templates'))
    exit(1)

def get_all_templates(filename, templates):
    contents = get_template(filename)
    if contents.startswith('<% extends '):
        extends, newline, contents = contents.partition('\n')
        match = re.search(EXTEND_TAG, extends)
        if not match:
            print('Improper template inheritance:')
            print(extends)
            exit(1)
        parent = match.group(0)
        get_all_templates(parent, templates)
    templates.append(contents)
    return templates

def compile(templates, attrs, dest):
    # process template inheritance first
    templates.reverse()
    template = compile_inheritance(templates)
    attrs['MASTER_DIR'] = MASTER_DIR

    for tag in re.findall(EXPR_TAG, template):
        val = eval(tag, attrs)
        template = re.sub('\{\{\s.+?\s\}\}', str(val), template, count=1)
    with open(dest, 'w') as f:
        f.write(template)
        print('Finished compiliing ')
        print('Result can be found at ' +  dest)

def compile_inheritance(templates):
    """Compiles the inheritance chain of templates into a single
    template.

    PARAMETERS:
    templates -- a list of templates. The sub-template
                 should be first, and the super-templates (parents)
                 should be ordered after. In addition, each template
                 should be a single string.

    RETURNS:
    A single template (as a string). The template will be devoid of
    inheritance tags.

    DESCRIPTION:
    Compilation begins at the top of the template chain and works
    its way down to child templates. This allows child templates to
    inherit not just from parents, but from higher ancestors as well.

    If a sub-template decides not to inherit a tag in its
    super-template, that tag will be removed in the final result.

    >>> t = ['<% t1 %>\\nhello\\n<%/ t1 %>', '{% t1 %}']
    >>> compile_inheritance(t)
    'hello'
    >>> t = ['<% t2 %>\\nhello\\n<%/ t2 %>', '<% t1 %>\\n{% t2 %}\\n<%/ t1 %>', '{% t1 %}']
    >>> compile_inheritance(t)
    'hello'
    >>> t = ['<% t2 %>\\nhello\\n<%/ t2 %>', '<% t1 %>\\nbye\\n<%/ t1 %>', '{% t1 %}{% t2 %}']
    >>> compile_inheritance(t)
    'byehello'
    >>> t = ['<% t1 %>\\nbye\\n<%/ t1 %>', '{% t1 %}{{ hi }}{% t2 %}']
    >>> compile_inheritance(t)
    'bye{{ hi }}'
    """
    if len(templates) == 1:
        return re.sub('\{%\s.+?\s%\}', '', templates[0])
    super_temp, sub_temp = templates.pop(), templates.pop()
    supers = list_supers(sub_temp)
    for match in re.finditer(SUB_TAG, super_temp):
        tag = match.group(0)
        if tag not in supers:
            continue
        replace = '\n'.join(supers[tag])
        super_temp = re.sub('\{%\s' + tag + '\s%\}', replace, super_temp, count=1)
    templates.append(super_temp)
    return compile_inheritance(templates)

def list_supers(template):
    """Returns a dictionary where keys are tags inherited by the
    template, and values are lists of lines that correspond to each
    tag.

    PARAMETERS:
    template -- a single string. Inheritance tags should be on their
                own line. Inheritance tags cannot be nested -- if they
                are, the inner tags will be treated as plain text.

    RETURNS:
    A dictionary, where keys are tags and values are lists of lines
    associated with each tag. The lines do NOT end in newline
    characters.

    >>> t = '<% t1 %>\\nhello\\nthere dog\\n<%/ t1 %>'
    >>> list_supers(t)
    {'t1': ['hello', 'there dog']}
    >>> t = '<% t1 %>\\n<%/ t1 %>\\n<% t2 %>\\nhello\\n<%/ t2 %>'
    >>> list_supers(t)
    {'t2': ['hello'], 't1': []}
    >>> t = '<% t1 %>\\n<% t2 %>\\n<%/ t2 %>\\n<%/ t1 %>'
    >>> list_supers(t)
    {'t1': ['<% t2 %>', '<%/ t2 %>']}
    """
    supers = {}
    tag = None
    for line in template.split('\n'):
        open_match = re.search(SUPER_TAG_OPEN, line)
        close_match = re.search(SUPER_TAG_CLOSE, line)
        if open_match and tag is None:
            tag = open_match.group(0)
            supers[tag] = []
        elif close_match and close_match.group(0) == tag:
            tag = None
        elif tag:
            supers[tag].append(line)
    return supers

def parse_content(content):
    if content.endswith('.py'):
        content = content[:-3]
    content = os.path.join(os.path.split(os.getcwd())[1], content)
    content = content.split('/')
    content = '.'.join(content)
    thing= __import__(content, fromlist=['attrs'])
    return thing.attrs

def parse_dest(dest, content, template):
    return dest
    #return os.path.join(dest,
    #                    os.path.split(content)[0],
    #                    os.path.split(template)[1])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('template', help="The template's filename")
    parser.add_argument('content', help="The content's filename. Content should be a Python file")
    parser.add_argument('dest', help='The destination directory')
    args = parser.parse_args()

    templates = get_all_templates(args.template, [])
    dest = parse_dest(args.dest, args.content, args.template)
    tag_names = parse_content(args.content)
    compile(templates, tag_names, dest)

if __name__ == '__main__':
    main()
