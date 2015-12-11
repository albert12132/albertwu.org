import re
import html
from urllib.parse import quote_plus

from templar.api.rules.core import SubstitutionRule
from base_config import config as base_config

def make_counter():
    i = 0
    def count():
        nonlocal i
        ret = i
        i += 1
        return ret
    return count

class QuestionRule(SubstitutionRule):
    pattern = re.compile(r"""
    <\s*question(?:\s+(.+?))?\s*>
    """, re.X | re.S)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.counter = make_counter()

    def substitute(self, match):
        name = ': ' + match.group(1) if match.group(1) else ''
        return '<h3 class="question" id="q{0}">Question {0}{1}</h3>'.format(
                self.counter() + 1, name)

solution_counter = make_counter()
class SolutionRule(SubstitutionRule):

    pattern = re.compile(r"""
    <\s*solution\s*>
    (.*?)
    </\s*solution\s*>
    """, re.X | re.S)

    def substitute(self, match):
        text = """
        <button id='{0}' class='toggleButton'>
        Toggle Solution<noscript> (enable JavaScript)</noscript>
        </button>

        <div class="solution {0}">{1}</div>
        """.format(solution_counter(), match.group(1))
        return text

class PromptRule(SubstitutionRule):
    pattern = re.compile(r"<prompt>\s*<pre><code>(.*?)\s*</code></pre>\s*</prompt>", re.S)

    PROMPTS = r"&gt;|&gt;{3}|logic&gt;|scm&gt;|\.{3}"
    PROMPT_TOGGLE_PATTERN = re.compile(r"""
    (?:(?<=\n)|(?<=\A))
    (?!%s)
    (.*?)
    (?:(?=\n(?:%s))|\Z)
    """ % (PROMPTS, PROMPTS), re.X | re.S)

    def substitute(self, match):
        solution_num = solution_counter()
        prompts = '<pre><code>' + self.PROMPT_TOGGLE_PATTERN.sub(
            lambda m: """<span class="blank{0}">______</span><span class="hidden solution {0}">{1}</span>""".format(solution_num, m.group(1)),
            match.group(1)) + '</code></pre>'

        text = """
        {0}

        <button id='{1}' class='toggleButton'>
        Toggle Solution<noscript> (enable JavaScript)</noscript>
        </button>
        """.format(prompts, solution_num)
        return text

class EnvironmentRule(SubstitutionRule):
    pattern = re.compile(r"<env>\s*<pre><code>(.*?)\s*</code></pre>\s*</env>", re.S)
    def substitute(self, match):
        tutor_url = 'http://www.pythontutor.com/iframe-embed.html'
        tutor_url += '#mode=display&cumulative=true&py=3&code='
        tutor_url += quote_plus(html.unescape(match.group(1)))

        text = """<pre><code>{0}</code></pre>

        <button id='{1}' class='toggleButton'>
        Toggle Solution<noscript> (enable JavaScript)</noscript>
        </button>
        <div class="solution {1} iframe-container">
        <iframe width="900" height="500" frameborder="0" src="{2}">
        </iframe>
        </div>
        """.format(match.group(1), solution_counter(), tutor_url)
        return text


class TopicRule(SubstitutionRule):
    pattern = re.compile(r"<topic>(.*) :: (.*)</topic>")
    def substitute(self, match):
        return """
        <tr>
          <td>{0}</td>
          <td><a href="{1}/basic.html">Questions</td>
          <td><a href="{1}/exam.html">Questions</td>
        </tr>
        """.format(match.group(1), match.group(2))


config = base_config.to_builder().prepend_postprocess_rules(
    QuestionRule(dst=r'\.html'),
    SolutionRule(dst=r'\.html'),
    PromptRule(dst=r'\.html'),
    EnvironmentRule(dst=r'\.html'),
    TopicRule(dst=r'\.html'),
).build()

