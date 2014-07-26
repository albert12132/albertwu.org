import os
import re
# Import various utilities from utils
# import templar.utils.html
# import templar.utils.filters

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))

#################
# Substitutions #
#################

re_markdown_rule = re.compile(r"<(markdown|render)>\n(.*?)\n</\1>",
        re.S)
def markdown_rule_sub(match):
    return '<div class="{0}">{1}</div>'.format(match.group(1),
            match.group(2))

##################
# Configurations #
##################

configurations = {
    # List of directories in which to search for templates
    'TEMPLATE_DIRS': [
        FILEPATH,
        # Add directories that contain templates
        # os.path.join(FILEPATH, 'example'),
    ],

    # Variables that can be used in templates
    'VARIABLES': {
        # Add variables here, like the following
        # 'example': 'something here',
    },

    # Substitutions for the linker
    'SUBSTITUTIONS': [
        # Add substitutinos of the form
        # (regex, sub_function),
        (re_markdown_rule, markdown_rule_sub),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    # 'TOC_BUILDER': templar.utils.htmlHeaderParser,
}
