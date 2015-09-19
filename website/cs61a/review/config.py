import os
import re
# Import various utilities from utils
# import templar.utils.html
# import templar.utils.filters
from templar.utils.html import HeaderParser
from templar.utils.html import unescape
from urllib.parse import quote_plus

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))

#################
# Substitutions #
#################

def make_counter():
    i = 0
    def count():
        nonlocal i
        ret = i
        i += 1
        return ret
    return count

question_re = re.compile(r"""
    <\s*question(?:\s+(.+?))?\s*>
""", re.X | re.S)
q_count = make_counter()
def question_sub(match):
    name = ': ' + match.group(1) if match.group(1) else ''
    return '<h3 class="question" id="q{0}">Question {0}{1}</h3>'.format(q_count() + 1, name)

solution_re = re.compile(r"""
    <\s*solution\s*>
    (.*?)
    </\s*solution\s*>
""", re.X | re.S)
s_count = make_counter()
def solution_sub(match):
    text = """
    <button id='{0}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>

    <div class="solution {0}">{1}</div>
    """.format(s_count(), match.group(1))
    return text

prompt_re = re.compile(r"<prompt>\s*<pre><code>(.*?)\s*</code></pre>\s*</prompt>", re.S)
prompts = r"&gt;|&gt;{3}|logic&gt;|scm&gt;|\.{3}"
prompt_toggle_re = re.compile(r"""
    (?:(?<=\n)|(?<=\A))
    (?!%s)
    (.*?)
    (?:(?=\n(?:%s))|\Z)
""" % (prompts, prompts), re.X | re.S)
def prompt_sub(match):
    s_num = s_count()
    prompts = '<pre><code>' + prompt_toggle_re.sub(
        lambda m: """<span class="blank{0}">______</span><span class="hidden solution {0}">{1}</span>""".format(s_num, m.group(1)),
        match.group(1)) + '</code></pre>'

    text = """
    {0}

    <button id='{1}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>
    """.format(prompts, s_num)
    return text

env_re = re.compile(r"<env>\s*<pre><code>(.*?)\s*</code></pre>\s*</env>", re.S)
def env_sub(match):
    tutor_url = 'http://www.pythontutor.com/iframe-embed.html'
    tutor_url += '#mode=display&cumulative=true&py=3&code='
    tutor_url += quote_plus(unescape(match.group(1)))

    text = """<pre><code>{0}</code></pre>

    <button id='{1}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>
    <div class="solution {1} iframe-container">
    <iframe width="900" height="500" frameborder="0" src="{2}">
    </iframe>
    </div>
    """.format(match.group(1), s_count(), tutor_url)
    return text


topic_re = re.compile(r"<topic>(.*) :: (.*)</topic>")
def topic_sub(match):
    return """
    <tr>
      <td>{0}</td>
      <td><a href="{1}/basic.html">Questions</td>
      <td><a href="{1}/exam.html">Questions</td>
    </tr>
    """.format(match.group(1), match.group(2))

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
        (question_re, question_sub),
        (solution_re, solution_sub),
        (prompt_re, prompt_sub),
        (env_re, env_sub),
        (topic_re, topic_sub),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    'TOC_BUILDER': HeaderParser,
}

