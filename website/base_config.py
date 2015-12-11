import re

from templar.api.config import ConfigBuilder
from templar.api.rules.core import SubstitutionRule
from templar.api.rules.compiler_rules import MarkdownToHtmlRule
from templar.api.rules.table_of_contents import HtmlTableOfContents

class ImageRule(SubstitutionRule):
    pattern = re.compile(r'(<img.*?)>')
    def substitute(self, match):
        return match.group(1) + ' class="img-responsive">'

_config_builder = ConfigBuilder().add_template_dirs(
    'templates',
    'projects/templates',
    'cs61a/review/templates',
).add_variables({
    'MASTER_DIR': '',
    'CS61A_DIR': '/cs61a',
    'REVIEW_DIR': '/cs61a/review',
    'NOTES_DIR': '/cs61a/notes',
    'BLOG_DIR': '/blog',
    'PROJECTS_DIR': '/projects',
}).append_compiler_rules(
    MarkdownToHtmlRule()
).append_postprocess_rules(
    HtmlTableOfContents(),
    ImageRule(dst=r'\.html'),
)

config = _config_builder.build()

