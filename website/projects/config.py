import re
from templar.api.rules.core import SubstitutionRule
from base_config import config as base_config

class ItemRule(SubstitutionRule):
    pattern = re.compile(r"""
    <item\s+        # opening item tag
    (.+?)[ ]        # \1 is title
    (.+?)           # \2 is link
    >\n
    (.*?)           # \3 is description
    </item>         # closing tag
    """, re.X | re.S)

    template = """
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

    def substitute(self, match):
        title, link, description = match.group(1), match.group(2), match.group(3)
        return self.template.format(title=title, desc=description, link=link)

config = base_config.to_builder().prepend_postprocess_rules(
    ItemRule(dst=r'\.html')
).build()

