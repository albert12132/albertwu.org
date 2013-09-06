import sys
import os
sys.path.append(os.getcwd())

from indices.topics import mt1 as contents
from indices.topics import publish


exam = 'Midterm 1'

notes = ''

contents = publish(contents)

attrs = globals()
