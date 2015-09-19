import os
import re
# Import various utilities from utils
# import templar.utils.html
# import templar.utils.filters
from templar.utils.html import HeaderParser

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))

#################
# Substitutions #
#################

style_guide_re = re.compile(r"<([NP])>")
def style_guide_sub(match):
    style = match.group(1)
    if style == 'N':
        return '<span class="style-non-ess">N</span>'
    elif style == 'P':
        return '<span class="style-python">P</span>'

style_guide_code_re = re.compile(r"""
<(good|bad)>\s*     # \1 is good/bad
<pre><code>
(.*?)                # \2 is codeblock content
</code></pre>\s*
</\1>
""", re.S | re.X)
def style_guide_code_sub(match):
    return '<pre class="style-{}"><code>{}</code></pre>'.format(
            match.group(1), match.group(2))

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
        (style_guide_re, style_guide_sub),
        (style_guide_code_re, style_guide_code_sub),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    'TOC_BUILDER': HeaderParser,
}
