import sys
import os
sys.path.append(os.getcwd())

from indices.topics import mt2 as contents
from indices.topics import publish

exam = 'Midterm 2'

notes = ''

contents = publish(contents)

attrs = globals()
