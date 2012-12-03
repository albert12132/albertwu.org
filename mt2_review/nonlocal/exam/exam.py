########################
# NONLOCAL EXAM-STYLE  #
########################

################
# CODE-WRITING #
################

#1
def make_sassy_function(f, msg):
    """Returns a version of f that only worrks every other function
    call.

    >>> f = lambda x: x ** 2
    >>> sassy_f = make_sassy_function(f, "Um, excuse me?")
    >>> sassy_f(4)
    16
    >>> sassy_f(5)
    'Um, excuse me?'
    >>> sassy_f(6)
    36
    >>> g = lambda x, y: x * y
    >>> sassy_g = make_sassy_function(g, "Don't tell me what to do!")
    >>> sassy_g(1, 2)
    2
    >>> sassy_g(5, 4)
    "Don't tell me what to do!"
    """
    "*** YOUR CODE HERE ***"


# Q2
def sentence_buffer():
    """Returns a function that will return entire sentences when it
    receives a string that ends in a period.

    >>> buffer = sentence_buffer()
    >>> buffer("This")
    >>> buffer("is")
    >>> buffer("Spot.")
    'This is Spot.'
    >>> buffer("See")
    >>> buffer("Spot")
    >>> buffer("run.")
    'See Spot run.'
    """
    "*** YOUR CODE HERE ***"

