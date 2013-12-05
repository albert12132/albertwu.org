import sys
import os
sys.path.append(os.getcwd())

from indices.topics import final as contents
from indices.topics import publish

exam = 'Final'

notes = """
I've written some additional questions for my discussion section that can be found
<a href='http://inst.eecs.berkeley.edu/~cs61a-te/review/final_review/basic/index.html'>here</a>.
"""

contents = publish(contents)

attrs = globals()
