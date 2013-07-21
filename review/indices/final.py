import sys
import os
sys.path.append(os.getcwd())

from indices.topics import final as contents
from indices.topics import publish

exam = 'Final'

notes = """
Don't forget about <b>Logic</b> and <b>Dynamic Scope</b>!
"""

contents = publish(contents)

attrs = globals()
