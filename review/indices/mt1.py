from indices.topics import mt1 as contents
from indices.topics import publish

exam = 'Midterm 1'

notes = "Don't forget about <b>data abstraction</b> and <b>recursion</b>! The extra problems in Discussion 2a are very good for recursion practice."

contents = publish(contents)

attrs = globals()
