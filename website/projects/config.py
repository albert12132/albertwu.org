import os
import re
from datetime import datetime
# Import various utilities from utils
from templar.utils.html import HeaderParser
# import templar.utils.filters

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))

item_re = re.compile(r"""
    <item\s+        # opening item tag
    (.+?)[ ]        # \1 is title
    (.+?)           # \2 is link
    >\n
    (.*?)           # \3 is description
    </item>         # closing tag
""", re.X | re.S)
item_template = """
  <div class='row'>
    <div class='col-md-3'>
      <div class='text-center'>
        <h2 class='item-title'><a href="{link}">{title}</a></h2>
      </div>
    </div>
    <div class='col-md-9'>
      {desc}
    </div>
  </div>
"""
def item_sub(match):
    title, link, description = match.group(1), match.group(2), match.group(3)
    return item_template.format(title=title, desc=description, link=link)

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
        'datetime': datetime,
    },

    # Substitutions for the linker
    'SUBSTITUTIONS': [
        (item_re, item_sub),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    'TOC_BUILDER': HeaderParser,
}
