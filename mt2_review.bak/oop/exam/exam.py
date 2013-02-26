##################
# OOP EXAM-STYLE #
##################

################
# CODE-WRITING #
################

# Q1
class Chef:
    """Doctests:

    >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
    >>> ramsey = Chef('steak', ['meat', 'bbq sauce', 'salt'])
    >>> ramsey.cook()
    'Not enough ingredients!'
    >>> ramsey.serve()
    'No food to serve!'
    >>> ramsey.fetch_ingredients()    # 1 salt remaining
    "Fetched: ['meat', 'bbq sauce', 'salt']"
    >>> ramsey.cook()
    'Cooked steak!'
    >>> ramsey.serve()
    >>> Chef.finished
    ['steak']
    >>> albert.fetch_ingredients()    # 0 salt remaining
    "Fetched: ['egg', 'cheese', 'cream', 'salt']"
    >>> albert.cook()
    'Cooked quiche!'
    >>> albert.serve()
    >>> Chef.finished
    ['steak', 'quiche']
    >>> ramsey.fetch_ingredients()
    'No more salt!'
    """
    "*** YOUR CODE HERE ***"

