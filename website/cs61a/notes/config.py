import re
from templar.api.rules.core import SubstitutionRule
from base_config import config as base_config

class StyleGuideTypeRule(SubstitutionRule):
    pattern = re.compile(r"<([NP])>")
    def substitute(self, match):
        style = match.group(1)
        if style == 'N':
            return '<span class="style-non-ess">N</span>'
        elif style == 'P':
            return '<span class="style-python">P</span>'

class StyleGuideCodeblockRule(SubstitutionRule):
    pattern = re.compile(r"""
    <(good|bad)>\s*     # \1 is good/bad
    <pre><code>
    (.*?)               # \2 is codeblock content
    </code></pre>\s*
    </\1>
    """, re.S | re.X)
    def substitute(self, match):
        return '<pre class="style-{}"><code>{}</code></pre>'.format(match.group(1), match.group(2))


config = base_config.to_builder().prepend_postprocess_rules(
    StyleGuideTypeRule(dst=r'\.html'),
    StyleGuideCodeblockRule(dst=r'\.html')
).build()

